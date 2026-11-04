"""Run extracted production functions without invoking the installer entrypoints."""
import os
import re
import subprocess
import unittest

from audit import DOCKER, NATIVE, ROOT


def functions(name, *names):
    source = (ROOT / name).read_text(encoding="utf-8")
    snippets = []
    for function in names:
        match = re.search(rf"(?ms)^{function}\(\) ([{{(]).*?^[}})]$(?=\n(?:\n|#|$)|\Z)", source)
        if not match:
            raise ValueError((name, function))
        snippets.append(match.group())
    return "\n".join(snippets)


class Regression(unittest.TestCase):
    def bash(self, source, expected=0):
        result = subprocess.run(
            ["bash", "-ec", source], cwd=ROOT,
            capture_output=True, encoding="utf-8",
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result.stdout

    def test_local_qr_and_percent_encoding(self):
        for name in (*NATIVE, *DOCKER):
            with self.subTest(name=name):
                output = self.bash(functions(name, "urlEncode", "showLocalQR") + r'''
qrencode() { [[ "$*" == "-t ANSIUTF8" ]] && cat; }
encoded=$(urlEncode 'a&b#@/?%=中')
showLocalQR "vless://id@[2001:db8::1]:443?path=${encoded}#${encoded}"
''')
                value = "a%26b%23%40%2F%3F%25%3D%E4%B8%AD"
                self.assertEqual(output, f"vless://id@[2001:db8::1]:443?path={value}#{value}")

    def test_ip_controls(self):
        for name in (*NATIVE, *DOCKER):
            with self.subTest(name=name):
                self.bash(functions(name, "getPublicIP") + r'''
curl() { [[ "$*" == *https://www.cloudflare.com/cdn-cgi/trace ]] && printf 'colo=ABC\nip=192.0.2.1\n'; }
[[ "$(getPublicIP 4)" == 192.0.2.1 ]]
curl() { printf 'unexpected network request\n'; return 1; }
[[ -z "$(VASMA_DISABLE_IP_LOOKUP=1 getPublicIP 4)" ]]
[[ "$(VASMA_DISABLE_IP_LOOKUP=1 VASMA_PUBLIC_IPV6=2001:db8::2 getPublicIP)" == 2001:db8::2 ]]
''')

    def test_cron_preserves_other_jobs_and_reports_read_errors(self):
        for name in NATIVE:
            with self.subTest(name=name):
                self.bash(functions(name, "editAgentCron") + r'''
state=$(mktemp -d)
trap 'rm -rf -- "$state"' EXIT
printf '%s\n' '0 0 * * * /root/.acme.sh/acme.sh --cron' '5 0 * * * /opt/other UpdateGeo' >"$state/original"
cp "$state/original" "$state/current"
crontab() {
    if [[ "$1" == -l ]]; then
        if [[ -e "$state/denied" ]]; then
            echo "Permission denied" >&2
            return 1
        fi
        cat "$state/current"
    else
        cp "$1" "$state/current"
    fi
}
editAgentCron add RenewTLS
editAgentCron add RenewTLS
editAgentCron add UpdateGeo
[[ "$(grep -c '/etc/v2ray-agent/install.sh' "$state/current")" == 2 ]]
editAgentCron remove
cmp "$state/original" "$state/current"
touch "$state/denied"
if editAgentCron add RenewTLS; then exit 1; fi
cmp "$state/original" "$state/current"
''')

    def test_docker_refuses_system_and_unowned_directories(self):
        for name in DOCKER:
            with self.subTest(name=name):
                self.bash(functions(name, "validateDataDirPath", "ownsDockerDataDir", "removeDockerDataDir") + r'''
for dir in / /etc /etc/nginx /root /usr /usr/local /var /home /var/lib/docker /tmp/../etc; do
    if validateDataDirPath "$dir"; then exit 1; fi
done
tmp=$(mktemp -d)
trap 'rm -rf -- "$tmp"' EXIT
mkdir "$tmp/unowned"
touch "$tmp/unowned/keep"
if removeDockerDataDir "$tmp/unowned"; then exit 1; fi
test -f "$tmp/unowned/keep"
ln -s "$tmp/unowned" "$tmp/link"
if validateDataDirPath "$tmp/link/subdirectory"; then exit 1; fi
''')

    @unittest.skipUnless(os.name == "posix", "requires Linux ownership modes and mountinfo")
    def test_docker_owned_dir_install_uninstall_and_reinstall(self):
        for name in DOCKER:
            with self.subTest(name=name):
                self.bash(functions(name, "validateDataDirPath", "ownsDockerDataDir", "prepareDockerDataDir",
                                    "removeDockerDataDir") + r'''
tmp=$(mktemp -d)
trap 'rm -rf -- "$tmp"' EXIT
data="$tmp/data"
prepareDockerDataDir "$data"
[[ "$(stat -c %a "$data")" == 700 ]]
[[ "$(stat -c %a "$data/.vasmad-owned")" == 600 ]]
ownsDockerDataDir "$data"
mkdir "$tmp/unowned"
cp "$data/.vasmad-owned" "$tmp/unowned/"
if removeDockerDataDir "$tmp/unowned"; then exit 1; fi
removeDockerDataDir "$data"
[[ ! -e "$data" ]]
prepareDockerDataDir "$data"
ownsDockerDataDir "$data"
''')

    def test_unlabelled_legacy_firewall_is_preserved(self):
        for name in NATIVE:
            with self.subTest(name=name):
                self.bash(functions(name, "deleteLegacyPortHopping") + r'''
echoContent() { :; }
firewall-cmd() { exit 42; }
iptables() { exit 43; }
if deleteLegacyPortHopping hysteria2 legacy-firewalld; then exit 1; fi
''')

    def test_update_never_downloads_or_replaces(self):
        for name in NATIVE:
            with self.subTest(name=name):
                output = self.bash(functions(name, "updateV2RayAgent") + r'''
echoContent() { printf '%s\n' "$2"; }
curl() { exit 1; }
wget() { exit 1; }
mv() { exit 1; }
updateV2RayAgent 1
''')
                self.assertIn("clean.1", output)
                self.assertIn("jhlxlml/v2ray-agent/tree/clean-secure", output)

    def test_local_site_preserves_operator_content(self):
        for name in NATIVE:
            with self.subTest(name=name):
                self.bash(functions(name, "nginxBlog", "writeLocalCamouflagePage") + r'''
nginxStaticPath=$(mktemp -d)
trap 'rm -rf -- "$nginxStaticPath"' EXIT
printf 'custom\n' >"$nginxStaticPath/index.html"
nginxBlog
grep -Fxq custom "$nginxStaticPath/index.html"
if writeLocalCamouflagePage 1; then exit 1; fi
rm -- "$nginxStaticPath/index.html"
nginxBlog
grep -Fq '<title>Welcome</title>' "$nginxStaticPath/index.html"
writeLocalCamouflagePage 2
grep -Fq '<title>Field Notes</title>' "$nginxStaticPath/index.html"
''')

    def test_xhttp_and_docker_uri_fields(self):
        for name in NATIVE:
            with self.subTest(name=name):
                output = self.bash(functions(name, "urlEncode", "uriHost", "buildVLESSXHTTPTLSURI") + r'''
buildVLESSXHTTPTLSURI 2001:db8::1 443 id example.com '/a?x=y&z=中' auto 'user#1'
''')
                self.assertIn("id@[2001:db8::1]:443", output)
                self.assertIn("path=%2Fa%3Fx%3Dy%26z%3D%E4%B8%AD&mode=auto#user%231", output)
        for name in DOCKER:
            with self.subTest(name=name):
                output = self.bash(functions(name, "urlEncode", "buildXHTTPSubscriptionLink") + r'''
buildXHTTPSubscriptionLink 2001:db8::1 443 example.com pbk id 'user#1' sid '/a?x=y&z=中'
''')
                self.assertIn("id@[2001:db8::1]:443", output)
                self.assertIn("path=%2Fa%3Fx%3Dy%26z%3D%E4%B8%AD&pbk=pbk&sid=sid#user%231", output)

    def test_xray_json_generation(self):
        for name in NATIVE:
            with self.subTest(name=name):
                self.bash(functions(name, "buildXrayXHTTPTLSConfig") + r'''
buildXrayXHTTPTLSConfig 12000 example.com test '[{"id":"demo"}]' |
    jq -e '.inbounds[0].streamSettings.xhttpSettings.path == "/testxHTTP" and
           .inbounds[1].port == 12000 and .inbounds[0].settings.clients[0].id == "demo"'
''')


    def test_core_install_validates_digest_and_preserves_previous_binary(self):
        for name in NATIVE:
            with self.subTest(name=name):
                core = functions(name, "verifyReleaseAsset", "installCoreRelease")
                core = core.replace('/etc/v2ray-agent/${core}', '${testRoot}/${core}')
                self.bash(core + r'''
testRoot=$(mktemp -d)
trap 'rm -rf -- "$testRoot"' EXIT
echoContent() { :; }
xrayCoreCPUVendor=Xray-linux-64
singBoxCoreCPUVendor=-linux-amd64
mkdir -p "$testRoot/sing-box-1.2.3-linux-amd64"
printf 'new-sb\n' >"$testRoot/sing-box-1.2.3-linux-amd64/sing-box"
tar -czf "$testRoot/sb.tar.gz" -C "$testRoot" sing-box-1.2.3-linux-amd64/sing-box
python3 - "$testRoot/xr.zip" <<'PY'
import sys, zipfile
with zipfile.ZipFile(sys.argv[1], "w") as archive:
    archive.writestr("xray", "new-xr\n")
PY
curl() {
    local asset fixture output="" digest
    case "${*: -1}" in
        *sing-box*)
            asset=sing-box-1.2.3-linux-amd64.tar.gz
            fixture="$testRoot/sb.tar.gz"
            ;;
        *)
            asset=Xray-linux-64.zip
            fixture="$testRoot/xr.zip"
            ;;
    esac
    if [[ "${*: -1}" == https://api.github.com/* ]]; then
        digest=$(sha256sum "$fixture")
        printf '{"tag_name":"v1.2.3","draft":false,"assets":[{"state":"uploaded","name":"%s","digest":"sha256:%s"}]}\n' "$asset" "${digest%% *}"
    else
        if [[ "${downloadMode:-}" == failed ]]; then return 1; fi
        while [[ "$1" != -o ]]; do shift; done
        output=$2
        cp "$fixture" "$output"
        if [[ "${downloadMode:-}" == corrupt ]]; then printf corrupt >>"$output"; fi
    fi
}
installCoreRelease xray v1.2.3
installCoreRelease sing-box v1.2.3
grep -Fxq new-xr "$testRoot/xray/xray"
grep -Fxq new-sb "$testRoot/sing-box/sing-box"
for downloadMode in failed corrupt; do
    if installCoreRelease xray v1.2.3; then exit 1; fi
    grep -Fxq new-xr "$testRoot/xray/xray"
done
''')

    def test_docker_generates_private_vision_and_xhttp_json(self):
        for name in DOCKER:
            with self.subTest(name=name):
                source = functions(name, "validateDataDirPath", "ownsDockerDataDir", "prepareDockerDataDir",
                                   "installModeHasVision", "installModeHasXHTTP", "renderXHTTPPath",
                                   "_buildVisionInbounds", "_buildXHTTPInbound", "generateConfig")
                self.bash(source + r'''
umask 077
tmp=$(mktemp -d)
trap 'rm -rf -- "$tmp"' EXIT
echoContent() { :; }
initRandomSalt() { printf 'test-salt'; }
resolveValues() {
    resolvedInstallMode=all
    resolvedVisionPort=10443
    resolvedXHTTPPort=10444
    resolvedXHTTPPath=abc
    resolvedServerName=example.com
    resolvedTargetPort=443
    resolvedPrivateKey=private-fixture
    resolvedPublicKey=public-fixture
    resolvedUUID=uuid-fixture
    resolvedVisionEmail=vision-user
    resolvedXHTTPEmail=xhttp-user
    resolvedEmailBase=test-user
    resolvedSubscribePort=10445
}
dataDir="$tmp/data"
generateConfig
[[ "$(stat -c %a "$dataDir/config.json")" == 600 ]]
[[ "$(stat -c %a "$dataDir/client-summary.txt")" == 600 ]]
jq -e '[.inbounds[] | select(.protocol == "vless") | .streamSettings.network] | sort == ["tcp","xhttp"]' "$dataDir/config.json"
''')

    def test_existing_xray_user_delete_and_reload_rollback(self):
        for name in NATIVE:
            with self.subTest(name=name):
                source = functions(name, "restoreXrayUserConfigs", "deleteXrayUserByUUID")
                self.bash(source + r'''
tmp=$(mktemp -d)
trap 'rm -rf -- "$tmp"' EXIT
configPath="$tmp/"
ctlPath=true
echoContent() { :; }
reloadCore() { return 0; }
file="$tmp/02_inbounds.json"
printf '%s\n' '{"inbounds":[{"settings":{"clients":[{"id":"delete"},{"id":"keep"}]}}]}' >"$file"
cp "$file" "$tmp/original"
ctlPath=false
if deleteXrayUserByUUID delete; then exit 1; fi
cmp "$file" "$tmp/original"
ctlPath=true
deleteXrayUserByUUID delete
jq -e '.inbounds[0].settings.clients == [{"id":"keep"}]' "$file"
''')


if __name__ == "__main__":
    unittest.main(verbosity=2)
