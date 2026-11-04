# Clean Secure 安全策略

Clean Secure Edition clean.1 源自 mack-a/v2ray-agent v3.5.37。审计基准为 `140b1659f1874aaefb1cdde412c6baefaf196198`。保留 AGPL-3.0 和原作者署名。

## 安装及更新

1. 从 Fork 取得完整源码，核对提交 ID、提交签名或在独立可信渠道获取的归档 SHA-256，再审阅变更。使用同一提交的脚本与 `documents/sing-box.json`。
2. 在受信任的 Linux 主机上执行 `sudo bash install.sh` 或 `sudo bash shell/install_en.sh`。Docker 版使用 `sudo bash shell/docker_reality.sh` 或英文对应脚本。Docker 需要预装并启动。使用 ACME 的 TLS 配置需要预装经审核的 acme.sh。
3. 脚本菜单「查看脚本更新」显示版本与 Fork 地址。当前没有可信的自动发布渠道，自动下载和替换已关闭。核心组件的独立版本菜单依然可用。
4. 手动更新前以 root 权限备份脚本、客户端模板、服务配置和凭据到权限为 700 的独立目录。先在隔离环境校验新版本。用 `bash -n` 检查已审核的脚本，用 `install -m 700` 写到目标同一目录内的新文件，再用 `mv -fT` 原子替换目标。裸机安装的两个目标为 `/etc/v2ray-agent/install.sh` 和 `/etc/v2ray-agent/sing-box-client.json`。模板使用 600 权限。Docker 启动脚本的目标为 `/etc/v2ray-agent/docker_reality.sh`。运行新脚本前完成对应脚本与模板的替换。若启动失败，使用备份通过同样方式恢复。
5. 确认 `vasma` 或 `vasmad` 实际指向上述安装路径。已有脚本和同名入口须由管理员审核后迁移。

## 离线准备

在联网构建机上审核并打包同一提交的源码、发行版签名软件包、选定架构的核心和规则文件，或经核验的 Docker 镜像。通过可信介质传输，核验包、归档和镜像清单后再安装。

- 裸机 Reality 可以预装依赖和核心，再以 `sudo env VASMA_OFFLINE=1 VASMA_PUBLIC_IPV4=203.0.113.10 bash install.sh` 运行。将示例 IP 换为实际地址。按所选核心将经核验的二进制放在 `/etc/v2ray-agent/xray/xray` 或 `/etc/v2ray-agent/sing-box/sing-box`，为 Xray 同时准备同目录的 `geoip.dat` 与 `geosite.dat`。预装 Nginx、curl、dig、jq、lsof、OpenSSL、sha256sum 和相应服务管理工具。
- Docker 可通过 `docker load` 导入已核验的镜像，然后以 `VASMA_OFFLINE=1` 运行启动器。需要 `ghcr.io/xtls/xray-core:26.5.9`，启用订阅 HTTP 服务时还需要 `nginx:alpine`。本地标签应指向审核过的镜像。无缓存时启动会失败。
- 离线变量控制基础安装中的下载及 IP 查询。ACME 签发和续订、显式规则更新、WARP、远程订阅和代理流量仍各有网络前提。隔离环境应通过出站策略落实离线约束。

## 权限和迁移

裸机默认 umask 077。私有配置、TLS、WARP 和订阅源目录限制访问，Nginx 发布目录和已发布订阅由专用的 Web 路径读取。已发布订阅包含客户端凭据，访问链接需要作为密码保管。Docker Xray 只挂载配置文件，Docker Nginx 单独挂载发布目录。

Docker `--data-dir` 需使用专用绝对路径。新安装只接管空目录，归属标记绑定目录路径、设备和 inode。卸载同时检查目录、挂载点与容器标签。迁移旧安装时先备份，将旧目录移至旁边留存，人工核对并移除占用项目名称的旧容器。让新版初始化空目录后再按需恢复经审核的配置和客户端摘要，设置 600 权限，然后用 `--start-only` 启动。不要手工给旧目录伪造标记。

systemd 单元仍以 root 启动。Xray 与 sing-box 使用 `NoNewPrivileges` 和 `ProtectSystem=full`，能力上限保留网络管理、低端口绑定和原始套接字。Alpine/OpenRC 的服务权限仍需单独评估。隔离系统中的 TUN、WARP、端口跳跃和面板兼容性仍需验收。

## 信任边界和已知限制

- 核心归档验证所选仓库、版本、资产和 SHA-256。信任 GitHub Release 元数据及对应上游仓库，尚未验证独立的签名或透明日志。缺少 digest 时安装中止。
- Docker 镜像版本仍由标签解析，OCI 内容校验依赖 Docker。联网部署尚未绑定经审核的镜像 digest。旧的预置核心和外部工具由管理员验证。
- 防火墙保留现有服务状态。项目 SOCKS5 和端口跳跃规则已有各自状态记录。旧 firewalld 端口跳跃规则无法通过标签识别，迁移前应导出并审核规则。裸机历史安装路径与旧系统服务的归属校验仍不完整。
- 裸机 HTTP 订阅、Docker HTTP 订阅及部分兼容性探测仍支持明文 HTTP。按需在受信任网络使用，或部署 TLS 终止。规则文件和用户指定订阅服务器仍是独立信任边界。
- GitHub Actions 只运行静态与 Mock 测试。真正部署请使用一次性 Linux 虚拟机或隔离测试环境。

报告漏洞时请避免在公开 Issue 中粘贴节点、证书、API Token 或订阅链接。通过 Fork 的私密漏洞报告功能提交复现步骤和脱敏样本。
