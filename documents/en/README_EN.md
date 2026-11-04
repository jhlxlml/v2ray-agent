# v2ray-agent Clean Secure Edition



[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-blue)](https://t.me/v2rayAgentChannel)
[![Telegram Group](https://img.shields.io/badge/Telegram-Group-blue)](https://t.me/technologyshare)
[![Official Website](https://img.shields.io/badge/Website-v2ray--agent.com-blue)](https://www.v2ray-agent.com/)
[![English Version](https://img.shields.io/badge/English-Version-blue)](README_EN.md)

An installation and management script for Xray-core and sing-box, with regular host deployment and standalone Docker Reality deployment.

## Features

*   **Multi-core Support:** Supports Xray-core and sing-box, either separately or in combination.
*   **Multi-protocol Support:** Supports VLESS (TLS, Reality, XHTTP), VMess, Trojan, Hysteria2, Tuic, NaiveProxy, AnyTLS, and standalone SOCKS5 inbound.
*   **TLS and Reality:** TLS protocols can use acme.sh for automatic certificate issuance and renewal; Reality supports deployment without a domain.
*   **Easy Management:** Provides menus for users, ports, configurations, core versions, logs, and certificates, with QR codes and client node output.
*   **Subscription Support:** Generates and manages subscription links, including remote subscription configuration.
*   **Traffic Routing:** Provides WARP/WireGuard (IPv4/IPv6), IPv6, SOCKS5, DNS, VMess+WS, and SNI reverse-proxy routing.
*   **Network Policy Management:** Supports Hysteria2 port hopping, domain blacklists, and BT/P2P download restrictions.
*   **Docker Reality:** Runs VLESS-Reality in Docker without a domain, with Vision, XHTTP, or combined modes and both interactive and CLI operation.
*   **For more content, please visit the [Official Website](https://www.v2ray-agent.com/categories/jiao-cheng), [Backup](https://www.592083.com/categories/jiao-cheng)**

## Requirements

*   **Regular installation:** Linux with root privileges; CentOS, Debian, Ubuntu, and Alpine are supported on amd64/x86_64 and arm64/aarch64.
*   **Docker Reality:** Linux with root or sudo privileges and a running Docker daemon.

## Quick Start


Use a complete source checkout from the [fork](https://github.com/jhlxlml/v2ray-agent) at a reviewed commit. Install a reviewed acme.sh release first for TLS.

### One-command online installation

Paste this command on Linux with Bash, Git, and sudo installed. It fetches the full source tree from the fork, verifies the pinned commit, and starts the English installer. The pinned commit must be available on GitHub.

```bash
bash -c 'set -eu; rev=7c95c9fd75ee74e062ba328b56ed05ba28991adb; tmp=$(mktemp -d); trap "rm -rf -- \"\$tmp\"" EXIT; git -C "$tmp" init -q; git -C "$tmp" fetch -q --depth=1 https://github.com/jhlxlml/v2ray-agent.git "$rev"; test "$(git -C "$tmp" rev-parse FETCH_HEAD)" = "$rev"; git -C "$tmp" checkout -q --detach "$rev"; cd "$tmp"; sudo bash shell/install_en.sh'
```

For Docker Reality, install and start Docker first, then replace `shell/install_en.sh` at the end of the command with `shell/docker_reality_en.sh`.

### Installation

```
sudo bash shell/install_en.sh
```

### Usage

After installation, run the following command to open the management menu again:

```
vasma
```

### Docker Reality

```
sudo bash shell/docker_reality_en.sh
```

The Docker launcher supports Reality Vision, Reality XHTTP, or both modes. After installation, run `vasmad` to reopen its menu. See the [Docker Reality guide](https://www.v2ray-agent.com/archives/019e1b57-92b3-70ab-8919-cdf8c0bb4fe9).

## Documentation and Guides

*   [From Beginner to Master with the 8-in-1 Script](https://www.v2ray-agent.com/archives/1710141233)
*   [Quick Script Setup Tutorial](https://www.v2ray-agent.com/archives/1682491479771)
*   [Script Usage Precautions](https://www.v2ray-agent.com/archives/1679931532764)
*   [Script Exception Handling](https://www.v2ray-agent.com/archives/1684115970026)   
*   [VPS Purchasing Guide](https://www.v2ray-agent.com/archives/1679975663984)
*   [Junk VPS Savior, one-click setup of the latest hysteria2 protocol](https://www.v2ray-agent.com/archives/1697162969693)
*   [RackNerd Low-cost Unicom AS4837 Package, starting from $10/year](https://www.v2ray-agent.com/archives/racknerdtao-can-zheng-li-nian-fu-10mei-yuan)
*   [Recommended High-Quality Bandwagon Host Packages](https://www.v2ray-agent.com/archives/2023nian-ban-wa-gong-ji-fang-tui-jian)
*   [Recommended High-Quality DMIT Packages](https://www.v2ray-agent.com/archives/1679159868033)

## Community & Support

*   **Telegram:** [Channel](https://t.me/v2rayAgentChannel) | [Group](https://t.me/technologyshare)
*   **Website:** [Official](https://www.v2ray-agent.com/) | [Backup](https://www.592083.xyz/)
*   **Feedback:** [Submit an issue](https://github.com/mack-a/v2ray-agent/issues)
*   **X:** [Link](https://x.com/v2rayagent)

## Security, offline setup and updates

Clean Secure Edition `clean.1` is based on mack-a/v2ray-agent v3.5.37. The update menu links to the fork for review. Use the full source tree from a reviewed commit for installation, and make a private backup before manually replacing an installed script. For offline Reality setup, stage verified dependencies, cores and rules or Docker images, then use `VASMA_OFFLINE=1`.

See [security and migration](../../docs/SECURITY.md), [network access](../../docs/NETWORK_ACCESS.md), [camouflage template audit](../../docs/CAMOUFLAGE_AUDIT.md) and [upstream sync](../../docs/UPSTREAM_SYNC.md).

## License

This project is licensed under the [AGPL-3.0 License](../../LICENSE).
