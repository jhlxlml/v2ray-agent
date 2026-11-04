"""Static policy checks on runtime sources and quarantined archives."""
import hashlib
import json
import re
import stat
import subprocess
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[2]
NATIVE = ("install.sh", "shell/install_en.sh")
DOCKER = ("shell/docker_reality.sh", "shell/docker_reality_en.sh")
SCRIPTS = (*NATIVE, *DOCKER, "shell/init_tls.sh", "scripts/security-audit.sh")


def main():
    banned = [
        r"api\.qrserver\.com",
        r"[?&]aff=\d+|推广区|Promotion area",
        r"\b(?:send_email|empty_login_history|ufw_remove)\.sh\b",
        r"\b(?:sendmail|mailx|smtp\.gmail\.com)\b",
        r"--no-check-certificate|--insecure\b|\bcurl\s+(?:-[a-zA-Z]+\s+)*-[a-zA-Z]*k[a-zA-Z]*(?:\s|$)",
        r"\b(?:curl|wget)\b[^\n]*\|\s*(?:sudo\s+)?(?:ba)?sh\b",
        r"raw\.githubusercontent\.com/mack-a/v2ray-agent/master/(?:shell/|install\.sh|fodder/)",
        r"\b(?:get\.docker\.com|get\.acme\.sh)\b",
        r"systemctl\s+(?:stop|disable)\s+(?:ufw|firewalld)|\bufw\s+(?:disable|reset)\b",
        r'rm\s+-rf\s+(?:--\s+)?(?:/etc/v2ray-agent(?=\s|$)|"\$\{nginxStaticPath\}[^"]*"|\$\{[^}]+\})',
        r"gh-proxy\.com",
    ]
    template = ROOT / "documents/sing-box.json"
    digest = hashlib.sha256(template.read_bytes()).hexdigest()
    assert json.loads(template.read_text(encoding="utf-8"))["outbounds"]
    for name in SCRIPTS:
        subprocess.run(["bash", "-n", str(ROOT / name)], check=True)
        source = (ROOT / name).read_text(encoding="utf-8")
        for pattern in banned:
            match = re.search(pattern, source, re.I | re.M)
            assert not match, (name, pattern, match.group() if match else None)
        if name in NATIVE:
            assert source.count(digest) == 2, f"{name}: template digest mismatch"

    for path in (ROOT / "README.md", ROOT / "documents/en/README_EN.md"):
        for pattern in banned:
            assert not re.search(pattern, path.read_text(encoding="utf-8"), re.I | re.M), (path, pattern)

    archives = sorted((ROOT / "fodder/blog/unable").glob("*.zip"))
    assert len(archives) == 9
    for path in archives:
        with zipfile.ZipFile(path) as archive:
            entries = archive.infolist()
            assert sum(entry.file_size for entry in entries) < 64 * 1024**2, path
            assert len({entry.filename.casefold() for entry in entries}) == len(entries), path
            for entry in entries:
                name = entry.filename.rstrip("/")
                parts = PurePosixPath(name).parts
                assert name and not name.startswith("/") and not set(parts) & {"..", "."}, (path, name)
                assert "\\" not in name and ":" not in name, (path, name)
                assert not stat.S_ISLNK(entry.external_attr >> 16), (path, name)
                assert entry.file_size <= 16 * 1024**2, (path, name)
                assert PurePosixPath(name).suffix.lower() not in {".zip", ".gz", ".7z", ".rar", ".tar"}, (path, name)
                if not entry.is_dir():
                    with archive.open(entry) as stream:
                        assert stream.read(4) not in {b"PK\x03\x04", b"7z\xbc\xaf", b"Rar!"}, (path, name)
            if path.stem == "html5":
                index = archive.read("index.html")
                assert b"ixarea-stats" not in index and b"window._paq" not in index
    print("Static policy, Bash syntax and archive checks passed")


if __name__ == "__main__":
    main()
