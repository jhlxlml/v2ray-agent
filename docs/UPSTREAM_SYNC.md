# 上游同步

以 `clean-secure` 为发布分支，以 `master` 保留原版。初始审计基准是 `140b1659f1874aaefb1cdde412c6baefaf196198`。

1. 从 `upstream` 获取 `master`，记录拟合并的固定 SHA、更新范围和上次审核点。创建以 `clean-secure` 为起点的临时分支或 worktree。
2. 比对上次审核点与候选提交。优先逐个 cherry-pick 有价值的修复。需要批量同步时在临时分支合并并保留冲突处理记录。分别审阅中文、英文、Docker、订阅模板和工作流。
3. 对每个新增联网调用补充网络访问清单。重点复核下载与执行、密钥输出、安装器覆盖、归属标记、cron、防火墙、广告及 ZIP 资源。修改订阅 JSON 时，在两个裸机安装器中同步更新固定 SHA-256。
4. 运行 `bash scripts/security-audit.sh`。ShellCheck 与最初审计提交对比，定位新增诊断；待消化历史警告后再经 PR 更新基线。检查 CI 和发行工作流仍符合分支限制。
5. 在隔离 Linux 环境完成协议和服务生命周期验收。记录镜像/包版本、系统、架构、失败项和未执行项。通过 PR 进入 `clean-secure`。
6. 只有在维护者明确授权并建立可验证发布流程后才创建 Clean Secure Release。当前在菜单中查看 Fork 后按固定提交手工安装或回滚。发行标签、校验值和签名应通过受保护且独立的信任渠道验证。

PR 审核需要验证许可证和作者署名、记录 upstream SHA，并附隔离测试结果。详见 [安全策略](SECURITY.md) 与 [联网访问清单](NETWORK_ACCESS.md)。
