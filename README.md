# v2ray-agent Clean Secure Edition



[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Telegram Channel](https://img.shields.io/badge/Telegram-Channel-blue)](https://t.me/v2rayAgentChannel)
[![Telegram Group](https://img.shields.io/badge/Telegram-Group-blue)](https://t.me/technologyshare)
[![Official Website](https://img.shields.io/badge/Website-v2ray--agent.com-blue)](https://www.v2ray-agent.com/)
[![English Version](https://img.shields.io/badge/English-Version-blue)](documents/en/README_EN.md)

基于 Bash 的 Xray-core / sing-box 安装与管理脚本，支持普通主机部署和 Docker Reality 独立部署。

## 功能

*   **多核心支持:** 支持 Xray-core 和 sing-box，可按需安装单核心或组合使用.
*   **多协议支持:** 支持 VLESS（TLS、Reality、XHTTP）、VMess、Trojan、Hysteria2、Tuic、NaiveProxy、AnyTLS，以及独立 SOCKS5 入站.
*   **TLS 与 Reality:** TLS 协议可通过 acme.sh 自动申请和续订证书；Reality 支持无域名部署.
*   **易于管理:** 提供菜单管理用户、端口、配置、核心版本、日志和证书，并支持二维码及客户端节点信息输出.
*   **订阅支持:** 生成和管理订阅链接，支持远程订阅配置.
*   **分流管理:** 提供 WARP/WireGuard（IPv4/IPv6）、IPv6、SOCKS5、DNS、VMess+WS、SNI 反向代理等分流能力，可用于流媒体等场景.
*   **网络策略管理:** 支持 Hysteria2 端口跳跃、域名黑名单和 BT/P2P 下载限制.
*   **Docker Reality:** 无需域名即可通过 Docker 部署 VLESS-Reality，支持 Vision、XHTTP 或同时启用两种模式，并提供交互式和命令行参数模式.
*   **更多内容请访问[官方网站](https://www.v2ray-agent.com/categories/jiao-cheng)、[备用](https://www.592083.com/categories/jiao-cheng)、[X](https://x.com/v2rayagent)**

## 环境要求

*   **脚本版:** Linux、root 权限，支持 CentOS、Debian、Ubuntu 和 Alpine；支持 amd64/x86_64、arm64/aarch64.
* **Docker Reality:** Linux、root 或 sudo 权限，预装并启动 Docker。

## 快速开始


从 [当前 Fork](https://github.com/jhlxlml/v2ray-agent) 获取完整源码，在本地检出已审核的固定提交后执行。TLS 安装还需要预先安装经审核的 acme.sh。

### 安装脚本版

```
sudo bash install.sh
```

### 使用

安装后，运行以下命令可再次打开管理菜单:

```
vasma
```

### 安装Docker版
```
sudo bash shell/docker_reality.sh
```

### 使用 

* [Docker Reality 使用说明](https://www.v2ray-agent.com/archives/019e1b57-92b3-70ab-8919-cdf8c0bb4fe9)
 
安装后，运行以下命令可再次打开管理菜单:

```
vasmad
```

## 文档和指南

*   [八合一脚本从入门到精通](https://www.v2ray-agent.com/archives/1710141233)
*   [脚本快速搭建教程](https://www.v2ray-agent.com/archives/1682491479771)
*   [脚本使用注意事项](https://www.v2ray-agent.com/archives/1679931532764)
*   [脚本异常处理](https://www.v2ray-agent.com/archives/1684115970026)   
*   [VPS选购攻略](https://www.v2ray-agent.com/archives/1679975663984)
*   [垃圾VPS大救星，hysteria2最新协议一键搭建](https://www.v2ray-agent.com/archives/1697162969693)
*   [RackNerd低价 联通AS4837套餐，年付10美起](https://www.v2ray-agent.com/archives/racknerdtao-can-zheng-li-nian-fu-10mei-yuan)
*   [搬瓦工优质套餐推荐](https://www.v2ray-agent.com/archives/2023nian-ban-wa-gong-ji-fang-tui-jian)
*   [DMIT优质套餐推荐](https://www.v2ray-agent.com/archives/1679159868033)

## 社区与支持

*   **Telegram:** [频道](https://t.me/v2rayAgentChannel) | [群组](https://t.me/technologyshare)
*   **网站:** [官网](https://www.v2ray-agent.com/) | [备用](https://www.592083.xyz/)
*   **反馈:** [提交 issue](https://github.com/mack-a/v2ray-agent/issues)
*   **X:** [链接](https://x.com/v2rayagent)

## 安全、离线安装和更新

Clean Secure Edition `clean.1` 源自 mack-a/v2ray-agent v3.5.37。更新菜单提供 Fork 地址供手工审核。安装使用经审核的完整源码，手动替换脚本前先备份。离线 Reality 可预置经核验的软件包、核心和规则，或导入 Docker 镜像后设置 `VASMA_OFFLINE=1`。

详见[安全策略与迁移](docs/SECURITY.md)、[联网访问清单](docs/NETWORK_ACCESS.md)、[伪装站 ZIP 审计](docs/CAMOUFLAGE_AUDIT.md)和[上游同步](docs/UPSTREAM_SYNC.md)。

## 许可证

本项根据 [AGPL-3.0 许可证](LICENSE) 授权.
