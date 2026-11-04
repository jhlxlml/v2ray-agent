# 联网访问清单

覆盖安装入口、Docker、TLS 工具、续订任务及生成的客户端配置。下表所列 HTTP 请求一般会暴露出口 IP、请求时间、路径及客户端特征。仓库网页链接、命令帮助和注释中的示例域名仅在用户主动打开时访问。

| 分类 | 目的地与调用点 | 触发条件 | 可关闭或替代 | 额外暴露 |
| --- | --- | --- | --- | --- |
| 必要 | 系统配置的软件包镜像，由 apt、yum、apk 调用 | 裸机安装依赖、Nginx 和可选工具 | 使用系统配置的镜像。基础离线安装可预装依赖并设置 `VASMA_OFFLINE=1` | 发行版、架构、包名 |
| 必要 | `api.github.com` 的 XTLS/Xray-core 和 SagerNet/sing-box；`github.com` 和 GitHub 资产重定向主机 | 查询版本、安装或更新核心。Release API 返回资产 digest，归档下载完成后校验 | 离线安装预放经审核的核心文件 | 仓库、版本、资产名和架构 |
| 必要 | `api.github.com`、`github.com` 及资产 CDN，Loyalsoldier/v2ray-rules-dat | Xray 首装、规则菜单或显式启用 `UpdateGeo` cron | 使用预置规则，勿启用自动规则更新 | 规则版本 |
| 条件必要 | `github.com` 及资产 CDN，v2fly/domain-list-community | 选择相应域名规则功能 | 不启用相关规则 | 请求的规则集合 |
| 条件必要 | `raw.githubusercontent.com` 的 SagerNet sing-geoip、sing-geosite | sing-box 分流或 SOCKS5 路由选择了远程规则 | 使用本地规则或不启用该规则 | 规则名称 |
| 条件必要 | `raw.githubusercontent.com` 的 MetaCubeX、blackmatrix7、Loyalsoldier，`fastly.jsdelivr.net` 的 MetaCubeX 规则 | 生成的客户端启动后加载 Geo 或规则集 | 在客户端改用本地数据 | 客户端规则集名称 |
| 条件必要 | `github.com` 的 MetaCubeX/metacubexd 及重定向主机 | sing-box 客户端配置使用 Clash API 的外部管理界面 | 客户端可关闭或预置 UI | UI 版本或分支 |
| 条件必要 | `www.cloudflare.com/cdn-cgi/trace` | 取公网 IP、显式检测 WARP、显式测试 SOCKS5 出口 | IP 查询使用 `VASMA_DISABLE_IP_LOOKUP=1`；WARP 或 SOCKS5 测试分别由菜单触发 | WARP 或测试代理的出口 IP |
| 条件必要 | `1.1.1.1`、`8.8.8.8`、`2606:4700:4700::1111`，以及系统解析器 | TLS 域名 A/AAAA 核验，其他普通 DNS 解析 | 无域名 Reality 可避开 TLS DNS 校验 | 查询域名和记录类型 |
| 必要 | ACME CA 和对应账号服务。代码选择 Let's Encrypt、ZeroSSL 或其他受支持的 CA；具体端点由 acme.sh 与选择决定 | TLS 申请或续订 | Reality 或手工维护证书可免用 | 联系邮箱、域名、ACME 账户及挑战材料 |
| 条件必要 | Cloudflare DNS API、阿里云 DNS API，由 acme.sh DNS 插件调用 | 显式选择 DNS-01 认证 | 使用 HTTP-01 或自备证书 | DNS API Token 或密钥用于 API 认证，域名及挑战记录 |
| 条件必要 | `pkg.cloudflareclient.com` 等管理员配置的 WARP 软件包源，Cloudflare WARP 注册与隧道端点 | 管理员配置软件源后安装 WARP，或运行 `warp-cli`、预置 `warp-reg` | 不启用 WARP | 注册、设备和 WireGuard 协议信息。实际端点由 WARP 软件决定 |
| 必要 | `ghcr.io` 的 XTLS Xray 镜像；Docker Hub 的 Nginx 镜像及 Registry 认证/CDN | Docker 部署、配置验证或订阅服务启用 | 使用经审核的本地镜像及 `VASMA_OFFLINE=1` | 镜像、标签、架构和 Registry 认证元数据 |
| 条件必要 | 自有节点域名、Nginx 测试地址、Reality 目标域名 | `checkPortOpen`、`checkNginx302`、TLS 引导工具、Reality 目标检查 | 无域名部署可避免部分探测。Reality 目标由管理员选择 | 明文 HTTP 探测中可见路径及域名。Reality 目标可见连接元数据 |
| 条件必要 | 用户指定的远程订阅主机 | 显式更新或聚合远程订阅 | 不启用远程订阅 | 订阅访问路径含访问令牌。沿用原订阅协议，应优先配置 HTTPS |
| 条件必要 | `1.1.1.1`、`8.8.8.8`、`223.5.5.5`、`1.12.12.12`、`doh.pub`、`dns.alidns.com` 等客户端 DNS 服务；`cp.cloudflare.com`、`www.gstatic.com` | 客户端 DNS、代理可用性探测和测速 | 客户端配置可自行调整 | DNS 查询名称，或健康检查请求 |
| 条件必要 | 管理员选择的扫描范围和目标主机 | 确认后运行已预置的 RealiTLScanner | 不使用扫描工具 | 扫描源 IP、端口、TLS 握手 |
| 未知 | 九个隔离 ZIP 中的历史 CDN、远程脚本及打包资源 | 只在管理员另行部署旧模板时可能出现 | 默认页面全部为本地资产 | 取决于客户端执行，详见 ZIP 审计 |
| 不必要，已移除 | 第三方二维码、固定收件人邮件、推广和非必要中转域名 | 旧实现通过外部二维码链接携带节点或订阅数据。旧邮件脚本可发送公网 IP | 当前版二维码由本地 qrencode 或明文链接提供 | 节点密钥和订阅链接不再交给二维码服务 |

公网 IP 设置可通过 root 启动环境传入。使用 `VASMA_PUBLIC_IPV4` 或 `VASMA_PUBLIC_IPV6` 指定裸地址。传入 `VASMA_DISABLE_IP_LOOKUP=1` 后，域名工作流仍可使用已有域名，无域名 Reality 则应提供手动 IP。Nginx 的 IPv6 监听根据本地接口或手动 IPv6 设置判断。

续订和 Geo cron 只维护本项目的精确条目。acme.sh 自带的续订任务及已有其他 cron 保留。代理核心正常连接、出站路由、TUN、DNS 和客户端订阅访问属于代理功能。
