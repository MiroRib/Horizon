---
layout: default
title: "Horizon Summary: 2026-06-15 (ZH)"
date: 2026-06-15
lang: zh
---

> From 169 items, 32 important content pieces were selected

---

1. [LinkedIn 求职陷阱：npm 脚本隐藏后门](#item-1) ⭐️ 9.0/10
2. [福克斯以 220 亿美元收购 Roku](#item-2) ⭐️ 9.0/10
3. [渐冻症患者成为首个长期使用脑植入设备说话的重度用户](#item-3) ⭐️ 9.0/10
4. [Iroh 1.0：用拨号键，不用 IP 地址](#item-4) ⭐️ 8.0/10
5. [TimescaleDB Hypercore 压缩技术减少 98%存储空间](#item-5) ⭐️ 8.0/10
6. [Typst 0.15.0 新增多参考文献功能](#item-6) ⭐️ 8.0/10
7. [美国关闭 Anthropic 模型推动主权 AI 发展](#item-7) ⭐️ 8.0/10
8. [AMD 悄然移除消费级 CPU 内存加密功能](#item-8) ⭐️ 8.0/10
9. [微软可能关闭 Double Fine 和 Ninja Theory 工作室](#item-9) ⭐️ 8.0/10
10. [美国电池制造业产量创历史新高](#item-10) ⭐️ 7.0/10
11. [Hacker News 用户分享本地 LLM 编程设置](#item-11) ⭐️ 7.0/10
12. [Hetzner 宣布大幅上调云服务器价格](#item-12) ⭐️ 7.0/10
13. [《指挥官基恩》白皮书详解平滑滚动技术](#item-13) ⭐️ 7.0/10
14. [铜转运药物恢复阿尔茨海默病小鼠记忆](#item-14) ⭐️ 7.0/10
15. [Chrome 150 和 151 版本将彻底封杀旧广告拦截器](#item-15) ⭐️ 7.0/10
16. [科技巨头推动联邦 AI 优先立法](#item-16) ⭐️ 7.0/10
17. [英国拟禁止 16 岁以下儿童使用社交媒体，并可能实施夜间宵禁](#item-17) ⭐️ 7.0/10
18. [中国计划 2030 年新能源重卡销量占比达 40%](#item-18) ⭐️ 7.0/10
19. [加州大学圣地亚哥分校计划用 2000 部 Pixel 手机打造低碳数据中心](#item-19) ⭐️ 7.0/10
20. [关于热爱计算机的个人反思](#item-20) ⭐️ 6.0/10
21. [家庭实验室 AI 开发平台引发社区讨论](#item-21) ⭐️ 6.0/10
22. [研究确认新冠疫苗仍保护心脏](#item-22) ⭐️ 6.0/10
23. [中国火箭在星链附近解体产生太空碎片](#item-23) ⭐️ 6.0/10
24. [Intel Mac 二十年：苹果的两次重大转型](#item-24) ⭐️ 6.0/10
25. [俄罗斯将解决国际空间站长期裂缝问题](#item-25) ⭐️ 6.0/10
26. [韩国人为何如此热衷 AI](#item-26) ⭐️ 6.0/10
27. [固态空调：前景光明，科学存疑](#item-27) ⭐️ 6.0/10
28. [AI 负载增长重塑公用事业商业模式](#item-28) ⭐️ 6.0/10
29. [美国清洁能源今春屡破纪录](#item-29) ⭐️ 6.0/10
30. [EA 推出游戏内广告平台](#item-30) ⭐️ 6.0/10
31. [谷歌地球网页版新增飞行模拟器](#item-31) ⭐️ 6.0/10
32. [SteamOS 测试版扩展至 MSI Claw 等 Intel 掌机](#item-32) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [LinkedIn 求职陷阱：npm 脚本隐藏后门](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

一名求职者在 LinkedIn 面试过程中，发现招聘方发送的 GitHub 仓库中隐藏了一个后门，该后门利用 npm 的 prepare 脚本在运行 npm install 时执行任意代码。 这种攻击手段极其危险，因为它模仿了常见的面试任务——审查一个损坏的仓库——可能危及大量开发者的机器，导致供应链攻击或凭证窃取。 后门隐藏在注释掉的测试代码中，通过 npm 的 prepare 生命周期脚本执行，该脚本在 npm install 后自动运行。有效载荷可以从远程服务器接收命令。

hackernews · lwhsiao · Jun 15, 20:00 · [社区讨论](https://news.ycombinator.com/item?id=48546294)

**背景**: npm 的 prepare 脚本是一个生命周期钩子，在发布前和 npm install 后运行，常用于构建步骤。通过 npm 进行的供应链攻击日益常见，近期如 Sha1-Hulud 攻击事件就入侵了流行软件包。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/44499912/why-is-npm-running-prepare-script-after-npm-install-and-how-can-i-stop-it">node.js - Why is npm running prepare script after npm install, and how ...</a></li>
<li><a href="https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html">GitHub to Disable npm Install Scripts by Default to Stop Supply Chain ...</a></li>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/?v=true">scripts - npm Docs</a></li>

</ul>
</details>

**社区讨论**: 评论者表示担忧，认为这种攻击与正常的面试任务过于相似，并呼吁建立更好的网络犯罪举报机制。有人批评 npm 默认不阻止脚本，也有人指出了法律层面的影响。

**标签**: `#security`, `#supply chain attack`, `#npm`, `#cybercrime`, `#hiring`

---

<a id="item-2"></a>
## [福克斯以 220 亿美元收购 Roku](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 9.0/10

福克斯公司宣布以 220 亿美元收购领先的流媒体平台 Roku，该交易将使福克斯掌控全球数千万家庭使用的操作系统。 此次收购引发了重大的反垄断担忧，因为它将一家大型内容生产商与一个占主导地位的硬件平台结合在一起，可能威胁到 Roku 历史上保持的平台中立性，并赋予福克斯对流媒体格局不当的影响力。 该交易价值 220 亿美元，预计将在获得监管批准后完成。Roku 熟悉的紫色界面可能保持不变，但收购可能导致福克斯自有内容获得优先待遇，并增加广告整合。

hackernews · thm · Jun 15, 12:50 · [社区讨论](https://news.ycombinator.com/item?id=48540499)

**背景**: Roku 是一家流媒体设备和平台公司，以其简单、以应用为先的用户体验和平台中立性而闻名，深受消费者和流媒体服务商的欢迎。媒体整合日益引发担忧，最近的 Tegna-Nexstar 合并使一家公司覆盖了 80%的美国电视家庭，引发了反垄断诉讼。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Concentration_of_media_ownership">Concentration of media ownership - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户对 Roku 失去其服务中立性、成为福克斯内容的载体表示悲观。许多评论者认为，福克斯不应被允许购买如此大比例美国家庭的直接访问权，一些人已经开始迁移到 Nvidia Shield 等替代平台。

**标签**: `#acquisition`, `#streaming`, `#antitrust`, `#media`, `#Roku`

---

<a id="item-3"></a>
## [渐冻症患者成为首个长期使用脑植入设备说话的重度用户](https://www.technologyreview.com/2026/06/15/1138953/man-als-first-power-user-brain-implant-speak-bci/) ⭐️ 9.0/10

患有渐冻症（ALS）的 Casey Harrell 使用脑机接口（BCI）近三年，累计数千小时，实时说出句子。他被认为是此类语音 BCI 的首个长期“重度用户”。 这一里程碑表明 BCI 可以在现实环境中多年可靠运行，超越了短期实验室演示。它为瘫痪患者恢复沟通带来希望，并加速了商用神经假体的进程。 Harrell 于 2023 年首次使用 BCI 说话，该系统经过数千小时的使用不断优化。植入物将电极放置在语言皮层，将神经信号解码为合成语音。

rss · MIT Technology Review · Jun 15, 15:12

**背景**: 脑机接口（BCI）在大脑活动与外部设备之间建立直接通信链路。对于语音，BCI 记录参与语言产生区域的神经信号，并将其转换为单词或声音。渐冻症会逐渐麻痹包括语言肌肉在内的全身肌肉，因此 BCI 成为一种有前景的辅助技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11053081/">Online speech synthesis using a chronically implanted...</a></li>
<li><a href="https://spectrum.ieee.org/bci-speech-synthesis">BCI Speech Synthesis Using Voice-Cloning AI Model - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#brain-computer interface`, `#ALS`, `#neuroprosthetics`, `#speech synthesis`, `#medical technology`

---

<a id="item-4"></a>
## [Iroh 1.0：用拨号键，不用 IP 地址](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 作为一个点对点网络库发布，使用加密拨号键而非 IP 地址实现应用间连接。 这简化了开发者的安全直连过程，类似于 Tailscale 但在应用层，使应用中的点对点通信更简单，无需用户管理网络配置。 Iroh 原生支持 IPv4、IPv6 和中继传输，现在通过插件系统允许自定义传输实现。

hackernews · chadfowler · Jun 15, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48542480)

**背景**: 传统网络依赖 IP 地址，但 IP 地址可能变化或被封锁。Iroh 使用加密键作为稳定标识符，即使在 NAT 或防火墙后也能建立直连，类似于 Tailscale 在网络层创建安全网状网络。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/v1">Iroh 1.0 - Dial Keys, not IPs - Iroh</a></li>
<li><a href="https://github.com/n0-computer/iroh">GitHub - n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. · GitHub</a></li>
<li><a href="https://tailscale.com/kb/1456/osi">Learn how Tailscale relates to the OSI model layers .</a></li>

</ul>
</details>

**社区讨论**: 评论者将 Iroh 比作应用层的 Tailscale，开发者澄清可以通过新插件系统添加 WebRTC 或 BLE 等自定义传输。一些用户对 Iroh 解决的问题感到困惑，而另一些则称赞其在 P2P 工具中的潜力。

**标签**: `#networking`, `#peer-to-peer`, `#rust`, `#open-source`, `#p2p`

---

<a id="item-5"></a>
## [TimescaleDB Hypercore 压缩技术减少 98%存储空间](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

TimescaleDB 推出了 Hypercore 压缩技术，通过列式存储和类型感知编码，对时序数据实现了高达 98%的存储空间缩减。 该压缩技术大幅降低了存储成本，并能加速时序数据的分析查询，使 TimescaleDB 在与专用时序数据库的竞争中更具优势。 Hypercore 采用了增量编码、游程编码和字典压缩等方法，但社区讨论指出存在查询性能上的权衡。

hackernews · lkanwoqwp · Jun 15, 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48544451)

**背景**: TimescaleDB 是一个用于时序数据的 PostgreSQL 扩展。传统的行式存储对于扫描多行但仅需少数列的分析查询效率低下。列式存储按列组织数据，能够实现更好的压缩和更快的扫描速度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.tigerdata.com/use-timescale/latest/hypercore/compression-methods/">Tiger Data Documentation | About compression methods</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/compression/">Timescale Documentation | Compression</a></li>
<li><a href="https://www.linkedin.com/pulse/row-vs-columnar-storage-secret-behind-blazing-fast-analytics-rashid-wawec">Row vs . Columnar Storage : The Secret Behind Blazing-Fast Analytics!</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了权衡：压缩可能因解压缩开销而减慢某些查询。讨论了 deltaX 和摆动门算法等替代方案，并提出了许可问题，因为压缩功能需要非 Apache 许可证。

**标签**: `#TimescaleDB`, `#compression`, `#time-series`, `#PostgreSQL`, `#database`

---

<a id="item-6"></a>
## [Typst 0.15.0 新增多参考文献功能](https://typst.app/docs/changelog/0.15.0/) ⭐️ 8.0/10

Typst 0.15.0 引入了在单个文档中支持多个参考文献的功能，并改进了 HTML 导出，包括自动将数学公式转换为 MathML。 此版本解决了一个长期存在的用户需求，使 Typst 更适合需要分类参考文献的复杂学术文档，如学位论文和书籍。 多参考文献功能允许用户使用带有 'title' 参数的新 'bibliography' 函数将参考文献分成多个部分（例如书籍、期刊）。此外，HTML 导出现在自动将数学公式转换为 MathML，以提高网页可访问性。

hackernews · schu · Jun 15, 17:24 · [社区讨论](https://news.ycombinator.com/item?id=48544396)

**背景**: Typst 是一种现代的基于标记的排版系统，旨在替代 LaTeX 和 Word，提供更简单的语法和更快的编译速度。它在科学和学术社区中特别受欢迎，用于文档准备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/typst/typst/issues/1097">Multiple bibliographies · Issue #1097 · typst/typst</a></li>
<li><a href="https://github.com/typst/typst">GitHub - typst / typst : A markup-based typesetting system that is...</a></li>

</ul>
</details>

**社区讨论**: 社区反馈总体积极，用户称赞多参考文献功能和改进的 HTML 支持。但一些用户指出脚注仍存在问题，特别是包含参考文献引用的长篇脚注，可能导致布局问题。

**标签**: `#typesetting`, `#open source`, `#software release`, `#typst`, `#document processing`

---

<a id="item-7"></a>
## [美国关闭 Anthropic 模型推动主权 AI 发展](https://www.theverge.com/ai-artificial-intelligence/949986/anthropic-fable-mythos-shutdown-sovereign-ai) ⭐️ 8.0/10

美国政府要求 Anthropic 关闭其最新 AI 模型 Fable 5 和 Mythos 5，禁止所有外国公民（包括 Anthropic 在国外的员工）访问。 这一事件凸显了依赖美国控制的 AI 基础设施的风险，加速了全球发展独立于美国技术的主权 AI 能力的努力。 Fable 5 和 Mythos 5 于 6 月 9 日发布，是最强大的 AI 模型之一，其中 Fable 5 能够仅凭截图重建 Web 应用源代码。此次关闭是在白宫要求下进行的，且正值 Anthropic 与五角大楼的争端期间。

rss · The Verge · Jun 15, 18:10

**背景**: Anthropic 是美国领先的 AI 公司，旗下有 Claude 系列模型。主权 AI 是指国家建立独立 AI 基础设施和模型、减少对外国供应商依赖的战略。例如，英国于 2026 年设立了 5 亿英镑的主权 AI 基金以支持本土 AI 公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c932g3v3e13o">Anthropic's Claude Fable 5 and Mythos 5 AI suspended over security fears</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI_Fund">Sovereign AI Fund</a></li>

</ul>
</details>

**标签**: `#AI`, `#geopolitics`, `#Anthropic`, `#AI regulation`, `#sovereign AI`

---

<a id="item-8"></a>
## [AMD 悄然移除消费级 CPU 内存加密功能](https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/) ⭐️ 8.0/10

AMD 悄然从其消费级 Ryzen CPU 中移除了透明安全内存加密（TSME）功能，该功能可加密所有系统内存，以防范冷启动攻击等物理攻击。 这一移除使消费级系统面临冷启动等物理内存攻击的风险，可能危及敏感数据。同时，此举未经公开宣布，削弱了用户对 AMD 安全承诺的信任。 TSME 是一种 BIOS 级功能，使用 AMD 安全处理器在启动时生成的单一密钥加密所有内存。此前该选项可在 BIOS 设置的 AMD CBS 下找到，但 AMD 现已未经警告在消费级 CPU 固件中禁用了它。

rss · Ars Technica · Jun 15, 17:55

**背景**: 透明安全内存加密（TSME）是一种基于硬件的内存加密技术，可加密系统内存的全部内容，使物理接触机器的攻击者无法访问数据。它与标准安全内存加密（SME）不同，后者需要操作系统或虚拟机监控程序支持。TSME 此前作为 BIOS 选项存在于 AMD Ryzen CPU 中，但 AMD 现已将其从消费级芯片中移除，可能是为了区分产品线或降低成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/developer/sev.html">AMD Secure Encrypted Virtualization (SEV) | AMD</a></li>
<li><a href="https://mricher.fr/post/amd-memory-encryption/">Memory encryption: AMD SME , TSME and SEV</a></li>
<li><a href="https://xeber.world/en/article/amd-removes-tsme-security-from-consumer-ryzen-cpus-without-warning-09496c">AMD Removes TSME from Consumer Ryzen CPUs Without Warning</a></li>

</ul>
</details>

**社区讨论**: 论坛和社交媒体上的用户表达了愤怒，指责 AMD 暗中破坏安全。许多人呼吁 AMD 恢复该功能或给出明确解释，而一些人猜测这可能是削减成本的手段或推动企业级芯片销售的措施。

**标签**: `#AMD`, `#CPU security`, `#TSME`, `#hardware`, `#controversy`

---

<a id="item-9"></a>
## [微软可能关闭 Double Fine 和 Ninja Theory 工作室](https://www.pcgamer.com/gaming-industry/double-fine-ninja-theory-and-more-xbox-studios-reportedly-at-risk-of-closure/) ⭐️ 8.0/10

据 The Verge 报道，微软计划关闭多个 Xbox 游戏工作室，包括 Ninja Theory（《地狱之刃》系列）和 Double Fine（《脑航员》系列），作为重大重组的一部分。员工在周一的一次电话会议上被告知，不过部分工作室可能会寻找买家。 这些关闭将消除备受好评且拥有忠实粉丝的工作室，可能削弱 Xbox 第一方作品的多样性。这表明微软转向优先考虑盈利能力而非创意实验，可能重塑游戏行业格局。 这些关闭发生在 Xbox 大规模裁员报道之后不久，是更广泛的“Xbox 重置”的一部分，可能还涉及 Compulsion Games。Ninja Theory 于 2018 年被微软收购，Double Fine 于 2019 年加入。

rss · PC Gamer · Jun 15, 21:43

**背景**: 微软一直在重组其游戏部门，专注于高潜力项目和长期增长，最近的裁员和工作室评估就体现了这一点。Ninja Theory 以《地狱之刃》等叙事驱动游戏闻名，而 Double Fine 则以《脑航员》等古怪作品著称。尽管获得好评，但两家工作室历史上都面临财务挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/07/02/microsoft-laying-off-about-9000-employees-in-latest-round-of-cuts.html">cnbc.com/ 2025 /07/02/microsoft-laying-off-about-9000-employees-in...</a></li>
<li><a href="https://www.geeky-gadgets.com/project-helix-next-gen-hardware/">Why Xbox is Returning to Exclusives for Major... - Geeky Gadgets</a></li>
<li><a href="https://www.doublefine.com/about">About Double Fine Productions | Double Fine Productions</a></li>

</ul>
</details>

**标签**: `#gaming`, `#Microsoft`, `#Xbox`, `#studio closures`, `#industry news`

---

<a id="item-10"></a>
## [美国电池制造业产量创历史新高](https://fred.stlouisfed.org/series/IPG33591S) ⭐️ 7.0/10

根据美联储电池工业生产指数（IPG33591S），美国电池制造业产量持续刷新纪录。 这一增长表明国内储能供应链正在加强，对国家安全和清洁能源转型至关重要，尽管全球竞争依然激烈。 尽管美国产量创纪录，但中国 2025 年的电池产能预计为 1,755 GWh，远超美国的 70 GWh 和欧洲的 252 GWh。

hackernews · epistasis · Jun 15, 20:28 · [社区讨论](https://news.ycombinator.com/item?id=48546616)

**背景**: 电池制造是电动汽车和电网储能的关键产业。美国一直在投资国内生产，以减少对进口（尤其是来自中国的进口）的依赖。

**社区讨论**: 评论者注意到美国与中国产能之间的巨大差距，有人建议允许中国公司在美建厂然后国有化等策略。其他人则强调了比亚迪刀片电池 2.0 的先进规格。

**标签**: `#battery manufacturing`, `#energy storage`, `#US economy`, `#industrial policy`, `#global competition`

---

<a id="item-11"></a>
## [Hacker News 用户分享本地 LLM 编程设置](https://news.ycombinator.com/item?id=48542100) ⭐️ 7.0/10

Hacker News 用户正在积极分享他们用本地模型（如 Qwen3.6 35B 和 Gemma）替代基于云的编程助手（如 Claude 和 GPT）的经验，使用的工具包括 Pi coding harness、llama.cpp 和 Continue 扩展。 这一转变凸显了在 AI 辅助编程中对数据隐私、成本节约和离线能力的日益增长的需求，可能减少对昂贵云订阅的依赖，并使更多开发者能够在本地使用强大的模型。 用户报告在双 RTX 3090 设置上使用 Qwen3.6 35B 达到约 150 tokens/秒，而其他人指出本地模型不如前沿模型智能，但足以完成大多数日常编程任务。一些用户仍会在复杂任务时回退到云模型。

hackernews · cloudking · Jun 15, 14:46

**背景**: 本地 LLM 是在用户自己的硬件上运行的大型语言模型，而不是在云服务器上。Ollama、llama.cpp 和 Continue 等工具使开发者能够将这些模型集成到他们的编程工作流中。Qwen3.6 35B 模型是一种混合专家（MoE）模型，平衡了性能和资源使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/data-science-collective/how-to-build-your-own-llm-coding-assistant-with-qwen2-5-coder-b26aaadf071d">How to Build Your Own LLM Coding Assistant With... | Medium</a></li>
<li><a href="https://vasilkoff.com/blog/vscodium-and-ollama">VSCodium + Ollama: Local LLM Coding Setup Guide</a></li>
<li><a href="https://www.packetswitch.co.uk/using-the-continue-vscode-extension-and-local-llms-for-improved-coding/">How to Use Continue and Local LLMs for Better Coding in VSCode?</a></li>

</ul>
</details>

**社区讨论**: 社区对本地设置充满热情，许多人分享了详细的配置和性能指标。一些用户提醒说，本地模型在能力上仍落后于云模型，但总体情绪是积极的，尤其是对于注重隐私的开发者。少数评论者质疑这种权衡是否对所有用户都值得。

**标签**: `#local LLM`, `#coding assistant`, `#Qwen`, `#data privacy`, `#self-hosted`

---

<a id="item-12"></a>
## [Hetzner 宣布大幅上调云服务器价格](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 7.0/10

Hetzner 宣布大幅上调云服务器价格，部分配置涨幅高达 3 倍，现有服务器自 2025 年 2 月 1 日起生效，专用服务器自 2026 年 6 月 15 日起生效。 此次涨价反映了 AI 热潮对硬件成本的广泛影响，将冲击依赖 Hetzner 廉价云服务的开发者和企业，可能迫使用户寻找替代方案或调整基础设施预算。 涨价适用于云服务器和负载均衡器，新价格已公布。Hetzner 将原因归咎于硬件成本上升和产品标准化，并引入了供应受限的“限量”类别。

hackernews · tuhtah · Jun 15, 13:19 · [社区讨论](https://news.ycombinator.com/item?id=48540844)

**背景**: Hetzner 是一家德国托管服务商，以性价比高的专用服务器和云服务著称，深受开发者和中小企业欢迎。AI 热潮推高了 GPU 和内存的需求，导致整个行业的硬件成本上升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lowendtalk.com/discussion/200033/hetzner-black-friday-price-increase-surprise">Hetzner Black Friday Price Increase Surprise — LowEndTalk</a></li>
<li><a href="https://cloudnews.tech/hetzner-will-increase-prices-on-june-15-and-simplify-its-server-catalog/">Hetzner Will Increase Prices on June 15 and Simplify Its Server Catalog</a></li>

</ul>
</details>

**社区讨论**: 社区对涨价幅度感到震惊，许多人质疑 3 倍涨幅的合理性。部分用户指出硬件成本确实飙升，而另一些用户则批评 Hetzner 多年来未更新硬件产品线。

**标签**: `#cloud`, `#pricing`, `#Hetzner`, `#hardware costs`, `#AI boom`

---

<a id="item-13"></a>
## [《指挥官基恩》白皮书详解平滑滚动技术](https://forgottenbytes.net/commander_keen.html) ⭐️ 7.0/10

ForgottenBytes.net 发布了白皮书，详细介绍了《指挥官基恩》在早期 PC 硬件上实现平滑滚动的技术创新，包括自适应瓦片刷新技术。 这份文档保存了游戏引擎历史上的一个关键时刻，展示了 id Software 如何克服严重的硬件限制，在 PC 上创建了第一款平滑滚动的平台游戏，这直接导致了《德军总部 3D》和《毁灭战士》的开发。 自适应瓦片刷新技术在 VRAM 中构建虚拟屏幕，并利用 EGA CRTC 并行读取四个字节的能力，尽管 PC 在精灵渲染能力上不如 SNES 等游戏机，仍实现了平滑滚动。

hackernews · mfiguiere · Jun 15, 17:52 · [社区讨论](https://news.ycombinator.com/item?id=48544781)

**背景**: 在 20 世纪 80 年代末，PC 硬件缺乏专用的精灵硬件，使得平滑的横向卷轴游戏难以实现。1990 年发布的《指挥官基恩》是一个突破，证明了 PC 可以运行色彩丰富的平台游戏。该游戏的引擎后来被称为 idTech 1，由约翰·卡马克和约翰·罗梅罗开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Commander_Keen">Commander Keen - Wikipedia</a></li>
<li><a href="https://ohtldr.com/summary/commander-keens-adaptive-tile-refresh/">Commander Keen ’s adaptive tile refresh – Oh TL;DR</a></li>
<li><a href="https://www.neogaf.com/threads/i-do-not-understand-why-people-consider-commander-keen-important-and-a-technical-achievement-in-the-industry.1655244/">I do not understand why people consider Commander Keen ... | NeoGAF</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这些白皮书，并推荐了《毁灭战士大师》一书作为背景资料。一位用户指出，解释为什么 PC 在精灵渲染方面比 SNES 等当代游戏机更困难很重要，另一位用户则提到该网站与 Fabien Sanglard 的作品相似。

**标签**: `#game development`, `#retro computing`, `#id Software`, `#game engines`, `#technical history`

---

<a id="item-14"></a>
## [铜转运药物恢复阿尔茨海默病小鼠记忆](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins) ⭐️ 7.0/10

莫纳什大学的研究人员发现，一种已在其他疾病中经过安全性评估的铜转运药物，在阿尔茨海默病小鼠模型中恢复了记忆并清除了有毒的β-淀粉样蛋白。 这可能推动该药物快速进入阿尔茨海默病的人体试验，提供一种针对铜失调而非有争议的淀粉样蛋白假说的新疗法。 该药物是一种铜转运化合物，可纠正大脑中异常的铜分布，减少淀粉样斑块并改善小鼠的认知功能。

hackernews · bookofjoe · Jun 15, 14:48 · [社区讨论](https://news.ycombinator.com/item?id=48542132)

**背景**: 阿尔茨海默病的特征是大脑中β-淀粉样蛋白斑块的积累和铜分布异常。由于针对淀粉样蛋白的疗法在临床试验中屡屡失败，淀粉样蛋白假说一直受到质疑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48542132">Copper transport drug restores memory and clears... | Hacker News</a></li>
<li><a href="https://colab.ws/articles/10.1007/s00249-007-0235-2">Copper transport and Alzheimer ’ s disease | CoLab</a></li>
<li><a href="https://www.academia.edu/115715222/In_vivo_reduction_of_amyloid_β_by_a_mutant_copper_transporter">(PDF) In vivo reduction of amyloid-β by a mutant copper transporter</a></li>

</ul>
</details>

**社区讨论**: 社区评论对淀粉样蛋白假说表示怀疑，并指出许多阿尔茨海默病疗法在老鼠身上有效，但在人类身上失败。一些评论者赞赏将铜失调作为潜在替代机制的研究方向。

**标签**: `#Alzheimer's`, `#drug discovery`, `#neuroscience`, `#amyloid-beta`, `#copper`

---

<a id="item-15"></a>
## [Chrome 150 和 151 版本将彻底封杀旧广告拦截器](https://www.theverge.com/tech/950005/google-chrome-removing-ad-blocker-loopholes) ⭐️ 7.0/10

预计于 2025 年 6 月底和 7 月发布的 Chrome 150 和 151 版本将移除允许 uBlock Origin 等旧版 Manifest V2 广告拦截器继续运行的最后变通方法。 这标志着向 Manifest V3 的完全过渡，后者限制了广告拦截功能，将影响数百万依赖 uBlock Origin 等强大拦截器的 Chrome 用户。 这些更改将禁用允许 Manifest V2 扩展运行的企业策略和实验标志。希望获得完整广告拦截功能的用户需要切换到 uBlock Origin Lite 等 Manifest V3 替代方案。

rss · The Verge · Jun 15, 18:06

**背景**: Manifest V3 是 Google 推出的新扩展平台，旨在提升隐私、安全性和性能。它取代了允许 uBlock Origin 等扩展使用强大的 webRequest API 拦截网络请求的 Manifest V2。在 Manifest V3 下，扩展被限制使用 declarativeNetRequest API，这降低了广告拦截器的灵活性。Google 于 2024 年开始逐步淘汰 Manifest V2，但一些变通方法使旧扩展得以继续运行至今。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh">uBlock Origin Lite - Chrome Web Store</a></li>

</ul>
</details>

**标签**: `#Chrome`, `#ad blocking`, `#Manifest V3`, `#privacy`, `#browser extensions`

---

<a id="item-16"></a>
## [科技巨头推动联邦 AI 优先立法](https://www.theverge.com/policy/949970/ai-regulation-child-safety-kosa-congress) ⭐️ 7.0/10

大型科技公司的游说者正在积极推动国会通过一项联邦人工智能法律，以优先于各州法规，建立统一的国家人工智能治理框架。 如果成功，这将推翻像科罗拉多州人工智能法案这样的州法律，可能削弱消费者保护，并将监管权力集中在华盛顿，影响全国范围内人工智能的开发和部署方式。 拟议的优先权将冻结各州人工智能法律三年，但各州保留对人工智能部署和使用的权力，而非开发。儿童安全是联邦框架唯一对人工智能开发者施加义务的领域。

rss · The Verge · Jun 15, 17:44

**背景**: 目前，美国缺乏全面的联邦人工智能监管，导致科罗拉多州等州自行立法。优先权将用单一的联邦标准取代这种零散局面，但批评者认为这可能会阻碍更严格的州级保护措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.imperiochaos.com/insights/federal-ai-preemption-power-consolidation">Federal AI Preemption Is a Power Consolidation... — Imperio Chaos</a></li>
<li><a href="https://www.justsecurity.org/134693/beware-ai-preemption-trap/">Beware the AI Preemption Trap</a></li>
<li><a href="https://www.stateside.com/blog/trumps-national-framework-vs-state-ai-laws">Trump’s “National Framework” vs . State AI Laws | Stateside Associates</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#Big Tech`, `#lobbying`, `#policy`, `#preemption`

---

<a id="item-17"></a>
## [英国拟禁止 16 岁以下儿童使用社交媒体，并可能实施夜间宵禁](https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/) ⭐️ 7.0/10

英国政府宣布计划禁止 16 岁以下儿童使用社交媒体，并考虑对 18 岁以下青少年实施夜间宵禁和暂停无限滚动功能，具体细节将于 2026 年 7 月公布。 这标志着全球范围内保护儿童在线安全的最激进监管举措之一，但批评者警告称，这可能会将儿童推向不受监管的替代平台，并且可以通过 VPN 轻易绕过。 该禁令不适用于 WhatsApp 和 Signal 等即时通讯服务。政府还在就注册年龄限制和 AI 聊天机器人访问的新限制进行咨询。

rss · Ars Technica · Jun 15, 20:14

**背景**: 社交媒体平台利用算法和无限滚动功能最大化用户参与度，这可能对年轻用户产生成瘾性和危害。VPN 允许用户加密流量并显示为不同位置，从而可能绕过地理限制或年龄验证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/">UK to ban social media for kids under 16, may impose overnight ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/VPN">VPN</a></li>
<li><a href="https://completeaitraining.com/news/uk-ministers-consider-overnight-social-media-curfew-and-ai/">UK ministers consider overnight social media curfew and AI chatbot...</a></li>

</ul>
</details>

**社区讨论**: 提供的内容不包含社区评论，因此无法总结讨论内容。

**标签**: `#tech policy`, `#social media`, `#child safety`, `#regulation`, `#UK`

---

<a id="item-18"></a>
## [中国计划 2030 年新能源重卡销量占比达 40%](https://www.energyintel.com/0000019e-cbe0-d720-af9f-fbe662f40000) ⭐️ 7.0/10

中国中央政府通过 11 部委联合发布计划，设定到 2030 年新能源重卡销量占比达 40%的目标，车队规模预计超过 160 万辆。 该政策标志着中国交通运输领域的重大转变，将大幅减少柴油需求，推动本土卡车和电池制造商发展，同时助力全球碳减排。 2025 年新能源重卡渗透率约为 29%，表明正快速接近 2030 年目标。该计划涵盖电动、氢燃料电池及其他清洁燃料等多种新能源类型。

rss · Energy Intelligence · Jun 15, 20:03

**背景**: 重卡是中国柴油消耗和碳排放的主要来源之一。由于高能耗、长续航和重载需求，该领域的电动化颇具挑战。中国多年来一直推广新能源汽车，但重卡电动化落后于乘用车。该政策通过设定约束性目标并协调多部委，加速了这一转型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cnevpost.com/2026/06/13/china-targets-40-penetration-new-energy-heavy-trucks-2030/">China targets 40% penetration for new - energy heavy trucks by 2030</a></li>
<li><a href="https://auto.economictimes.indiatimes.com/news/commercial-vehicle/china-sets-sights-on-heavy-truck-electrification-in-blow-to-diesel-demand/131740375">China sets sights on heavy truck electrification in blow to diesel...</a></li>
<li><a href="https://www.automotiveworld.com/news/china-maps-out-heavy-truck-electrification-with-40-2030-goal/">China maps out heavy - truck electrification with 40% 2030 goal</a></li>

</ul>
</details>

**标签**: `#energy`, `#transportation`, `#policy`, `#electrification`

---

<a id="item-19"></a>
## [加州大学圣地亚哥分校计划用 2000 部 Pixel 手机打造低碳数据中心](https://www.pcgamer.com/hardware/uni-researchers-plan-to-build-a-low-carbon-data-center-hivemind-from-2-000-pixel-smartphones-with-googles-help-no-less/) ⭐️ 7.0/10

加州大学圣地亚哥分校的研究人员在谷歌的支持下，计划部署一个由 2000 部退役 Pixel 智能手机构建的数据中心，打造一个低成本、低碳的云计算平台。 该项目展示了一种通过将旧智能手机重新用作计算节点来减少电子垃圾和碳排放的新方法，可能为传统数据中心提供一种可持续的替代方案。 该集群预计将在新学年之前投入使用，能够同时支持一百门计算机科学课程。现代智能手机处理器的单核性能高于同类多核服务器，使其适用于某些工作负载。

rss · PC Gamer · Jun 15, 16:34

**背景**: 传统数据中心消耗大量能源并需要不断升级硬件，导致电子垃圾增加。研究人员此前曾尝试将旧手机集群用于计算，但这是计划中规模最大、且有行业支持的部署。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/">A low - carbon computing platform from your retired phones</a></li>
<li><a href="https://www.tomshardware.com/desktops/servers/researchers-recycle-old-phones-and-cluster-them-into-computing-platforms-says-processors-on-modern-smartphones-deliver-higher-single-core-performance-than-comparable-multicore-servers">Researchers recycle old phones and cluster them... | Tom's Hardware</a></li>
<li><a href="https://www.pcgamer.com/hardware/uni-researchers-plan-to-build-a-low-carbon-data-center-hivemind-from-2-000-pixel-smartphones-with-googles-help-no-less/">Uni researchers plan to build a low - carbon data center ... | PC Gamer</a></li>

</ul>
</details>

**标签**: `#green computing`, `#data center`, `#smartphone cluster`, `#sustainability`, `#research`

---

<a id="item-20"></a>
## [关于热爱计算机的个人反思](https://michaelenger.com/blog/i-love-the-computer/) ⭐️ 6.0/10

Michael Enger 发表了一篇题为《我爱计算机》的个人随笔，反思了他对计算机的深厚感情，以及对现代科技行业聚焦于 AI 和守门行为的不适。 这篇文章引发了社区关于对计算机的怀旧热爱与当前行业趋势之间张力的讨论，包括 AI 的角色以及谁有权定义什么是“真正的”计算。 这篇文章是个人反思而非技术分析，获得了高参与度和多样化的观点。评论者讨论了 LLM 等 AI 工具的价值以及计算社区中的守门心态。

hackernews · speckx · Jun 15, 20:14 · [社区讨论](https://news.ycombinator.com/item?id=48546441)

**背景**: 这篇文章触及了对早期、小众计算体验的怀旧，与现代商业化科技行业之间的对比。术语“守门”指的是一种态度，即只有那些在底层编程中挣扎过的人才配称自己为计算机爱好者。

**社区讨论**: 像 fasterik 这样的评论者为 AI 工具辩护，认为它们确实有用，而 tptacek 则批评文章中的守门意味。Yhippa 对作者的怀旧感同身受，但承认这是一种自私的观点。

**标签**: `#computing`, `#nostalgia`, `#AI`, `#industry`, `#programming`

---

<a id="item-21"></a>
## [家庭实验室 AI 开发平台引发社区讨论](https://rsgm.dev/post/ai-dev-platform/) ⭐️ 6.0/10

一位开发者分享了他的家庭实验室 AI 开发平台设置，详细介绍了使用 OpenCode、Forgejo 和 Docker 管理 AI 辅助编码任务的工作流程。该帖子在社区获得了 208 个点赞和 42 条评论。 这次讨论突显了自托管 AI 开发工具的增长趋势，能够实现隐私保护、定制化和成本节约。它与许多独立探索类似工作流程的开发者产生了共鸣。 该设置使用 OpenCode 作为 AI 编码代理，Forgejo 用于 Git 托管，以及 Docker 容器来运行服务。一些评论者指出了资源限制，并建议在本地机器上运行代理以加快迭代速度。

hackernews · rsgm · Jun 15, 15:09 · [社区讨论](https://news.ycombinator.com/item?id=48542433)

**背景**: 家庭实验室是用于实验和自托管服务的个人服务器环境。家庭实验室中的 AI 开发平台通常结合了 OpenCode（AI 编码助手）、Forgejo（自托管 Git 服务）和 Docker 容器化等开源工具。这种设置使开发者能够在不依赖外部云服务的情况下利用 AI。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rsgm.dev/post/ai-dev-platform/">My Homelab AI Dev Platform • Rsgm's Blog</a></li>
<li><a href="https://github.com/hoangriki/homelab-ai-platform">GitHub - hoangriki/ homelab - ai - platform : Mixed-architecture homelab ...</a></li>
<li><a href="https://llmengg.com/homelab-ai-assistant-setup/">Homelab AI Assistant Setup — Build With OpenClaw and Docker April...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了类似的设置和工作流程，其中一位提到了将 OpenCode 集成到 Forgejo 的 action runner 中。另一位指出许多开发者独立地想到了类似的想法，还有少数人提出了域名过滤和资源需求的担忧。

**标签**: `#homelab`, `#AI`, `#dev platform`, `#self-hosting`, `#open-source`

---

<a id="item-22"></a>
## [研究确认新冠疫苗仍保护心脏](https://arstechnica.com/health/2026/06/covid-vaccines-still-protect-against-heart-problems-large-study-finds/) ⭐️ 6.0/10

一项大型研究发现，尽管反疫苗言论导致接种率下降，但新冠疫苗仍能持续预防心脏问题。 这再次证实了新冠疫苗对心血管的长期益处，反驳了疫苗会导致心脏损伤的错误信息。 该研究未给出具体效应量或人群细节，但这一发现在疫苗更新和公众信任下降的背景下仍然成立。

rss · Ars Technica · Jun 15, 21:04

**背景**: 新冠疫苗最初旨在预防重症和死亡。mRNA 疫苗接种后曾报告罕见心脏炎症（心肌炎）病例，引发担忧。本研究提供了证据表明整体心脏保护作用大于风险。

**标签**: `#COVID-19`, `#vaccines`, `#public health`, `#heart protection`

---

<a id="item-23"></a>
## [中国火箭在星链附近解体产生太空碎片](https://arstechnica.com/space/2026/06/a-chinese-rocket-breaks-apart-dangerously-close-to-the-starlink-constellation/) ⭐️ 6.0/10

一枚中国火箭在距离星链星座极近的位置解体，产生了约 100 至 150 块新的太空碎片。 这一事件凸显了太空碎片对星链等运行中卫星星座日益增长的威胁——星链已有近 6500 颗在轨卫星。它强调了加强碎片减缓措施和国际空间交通管理的必要性。 解体可能涉及火箭的末级，类似于此前长征六号甲火箭的多次碎片化事件。碎片云对星链及其他低地球轨道航天器构成碰撞风险。

rss · Ars Technica · Jun 15, 18:55

**背景**: 太空碎片是指地球轨道上已失效的人造物体，包括火箭解体和卫星碰撞产生的碎片。SpaceX 运营的星链星座由数千颗活跃卫星组成，提供全球互联网覆盖。随着巨型星座的扩张，产生碎片的事件概率增加，威胁空间活动的可持续性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/space/2024/08/us-military-tracks-more-than-300-pieces-of-debris-from-chinese-launch/">China’s Long March 6A rocket is making a mess in... - Ars Technica</a></li>
<li><a href="https://www.wikiwand.com/en/Space_debris">Space debris - Wikiwand</a></li>
<li><a href="https://www.linkedin.com/posts/phantom-space_mega-constellations-are-a-megatrend-starlink-activity-7260648579038347266-cGvN">Mega constellations are a megatrend. Starlink has led the way...</a></li>

</ul>
</details>

**标签**: `#space debris`, `#Starlink`, `#rocket breakup`, `#space safety`

---

<a id="item-24"></a>
## [Intel Mac 二十年：苹果的两次重大转型](https://arstechnica.com/gadgets/2026/06/20-years-of-intel-macs-why-apple-switched-and-why-it-switched-again/) ⭐️ 6.0/10

Ars Technica 发表了一篇回顾性文章，梳理了基于 Intel 的 Mac 的 20 年历史，分析了苹果为何在 2006 年从 PowerPC 转向 Intel，以及从 2020 年起又从 Intel 转向自研 Apple Silicon 的原因。 这篇回顾有助于理解苹果的战略硬件决策，这些决策塑造了现代 Mac 生态系统，并推动了整个计算行业向定制 ARM 处理器转型。 Intel Mac 时代始于 2006 年 1 月，首款基于 Intel 的 iMac 和 MacBook Pro 发布，并于 2023 年 6 月随着苹果完成全系 Mac 向 Apple Silicon 的迁移而正式结束。

rss · Ars Technica · Jun 15, 16:32

**背景**: 苹果已两次转换 Mac 处理器架构：2006 年从 IBM PowerPC 转向 Intel x86，以及 2020 年起从 Intel 转向自研的基于 ARM 的 Apple Silicon。第一次转型源于 PowerPC 的性能和散热限制，而第二次则出于苹果对更紧密软硬件集成、更高能效比以及统一设备架构的追求。Apple Silicon 芯片（如 M1）由苹果自主设计、台积电代工，相比 Intel 处理器在性能和能效上均有显著提升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mac_transition_to_Intel_processors">Mac transition to Intel processors - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_silicon">Apple silicon</a></li>
<li><a href="https://support.apple.com/en-us/116943">Mac computers with Apple silicon - Apple Support</a></li>

</ul>
</details>

**标签**: `#Apple`, `#Intel Macs`, `#Apple Silicon`, `#history`

---

<a id="item-25"></a>
## [俄罗斯将解决国际空间站长期裂缝问题](https://arstechnica.com/space/2026/06/russia-appears-set-to-finally-address-long-term-serious-space-station-cracks/) ⭐️ 6.0/10

俄罗斯似乎终于要解决国际空间站上长期存在的严重裂缝问题，从而结束与 NASA 在责任和修复计划上的争端。 这一进展对国际空间站的持续安全运行至关重要，因为未解决的裂缝可能导致灾难性故障，危及空间站的使用寿命。 裂缝发现于俄罗斯建造的曙光号功能货舱，俄罗斯联邦航天局与 NASA 之间的争端已在幕后持续了一段时间。

rss · Ars Technica · Jun 15, 13:54

**背景**: 国际空间站是一个位于近地轨道的模块化空间站，由 NASA、俄罗斯联邦航天局及其他航天机构共同运营。曙光号功能货舱于 1998 年发射，是国际空间站的第一个组件，提供推进和存储功能。如此关键模块上的裂缝会带来空气泄漏和结构失效的风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.space.com/international-space-station-cracks-found-zarya-module">Small cracks found in International Space Station module... | Space</a></li>
<li><a href="https://www.independent.co.uk/tech/international-space-station-iss-cracks-b1912379.html">The ISS is cracked and facing ‘irreparable’ failures... | The Independent</a></li>
<li><a href="https://www.newsy-today.com/russia-moves-to-repair-long-term-iss-cracks/">Russia Moves to Repair Long-Term ISS Cracks - Newsy Today</a></li>

</ul>
</details>

**标签**: `#space`, `#ISS`, `#engineering`

---

<a id="item-26"></a>
## [韩国人为何如此热衷 AI](https://www.technologyreview.com/2026/06/15/1138983/why-do-south-koreans-love-ai-so-much/) ⭐️ 6.0/10

一篇通讯文章探讨了推动韩国广泛采用 AI 的文化和社会因素，举例说明了使用面部识别的无人化入境检查站。 理解韩国对 AI 的热情有助于洞察文化态度如何加速技术采用，可能影响全球 AI 部署策略。 该文章是 MIT Technology Review 的《算法》通讯的一部分，缺乏技术深度，而是聚焦于作者旅行经历中的文化观察。

rss · MIT Technology Review · Jun 15, 18:46

**背景**: 韩国是一个高度数字化的社会，政府大力支持 AI 和机器人技术。文化因素如对技术的高度信任和集体主义社会取向可能促进了 AI 的接受度。

**标签**: `#AI`, `#South Korea`, `#culture`, `#technology adoption`

---

<a id="item-27"></a>
## [固态空调：前景光明，科学存疑](https://www.technologyreview.com/2026/06/15/1138552/solid-state-acs-promise-cool-future/) ⭐️ 6.0/10

《麻省理工科技评论》的一篇文章探讨了固态空调作为气候友好型替代方案的潜力，但指出科学家对其效率和可扩展性仍持怀疑态度。 随着全球空调使用量预计到 2050 年将增长两倍，固态冷却技术有望降低能耗并消除有害制冷剂，但当前的质疑可能减缓其应用和投资。 固态空调利用电卡效应，即电场引起材料温度变化，但现有设备效率低下，难以实际应用；文章强调了前景与现实之间的差距。

rss · MIT Technology Review · Jun 15, 09:00

**背景**: 传统空调依赖蒸汽压缩循环，使用具有高全球变暖潜值的制冷剂。固态冷却技术，如电卡器件，提供了一种无制冷剂的替代方案，可能更高效且环保，但仍处于早期开发阶段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://northnjhvac.com/solid-state-air-conditioner/">Solid State Air Conditioners : The Future Of Energy-Efficient Cooling...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Electrocaloric_effect">Electrocaloric effect - Wikipedia</a></li>
<li><a href="https://www.cibsejournal.com/technical/electrocaloric-cooling-making-a-difference/">Electrocaloric cooling – making a difference - CIBSE Journal</a></li>

</ul>
</details>

**标签**: `#climate tech`, `#air conditioning`, `#solid-state`, `#energy`, `#environment`

---

<a id="item-28"></a>
## [AI 负载增长重塑公用事业商业模式](https://www.utilitydive.com/spons/ai-load-growth-is-changing-the-utility-business-model/822321/) ⭐️ 6.0/10

一篇在 Utility Dive 上的赞助文章指出，人工智能驱动的大负载需求正在改变公用事业的战略、监管和投资。 这一转变可能从根本上改变公用事业规划容量、制定电价和投资基础设施的方式，从而影响所有客户的能源成本和可靠性。 该文章是赞助内容，缺乏具体的技术细节或案例研究，但表明行业对人工智能对能源需求影响的关注日益增加。

rss · Utility Dive · Jun 15, 09:00

**背景**: 公用事业传统上以可预测的负载增长运行，但 AI 数据中心和计算集群引入了大量且可变的负载，给电网带来压力，需要新的规划方法。这一趋势正促使监管机构和公用事业重新思考电价结构和投资策略。

**标签**: `#AI`, `#energy`, `#utilities`, `#business model`

---

<a id="item-29"></a>
## [美国清洁能源今春屡破纪录](https://www.canarymedia.com/articles/clean-energy/clean-energy-us-set-records) ⭐️ 6.0/10

在春季过渡季节，美国清洁能源发电量屡创新高，包括太阳能和风能发电量达到历史最高水平。 这些纪录表明可再生能源部署正在加速，这对实现气候目标和减少化石燃料依赖至关重要。 文章强调，太阳能和风能等可再生能源在春季月份创下了新的发电纪录，为更清洁的电网做出了贡献。

rss · Latitude Media (Canary Media) · Jun 15, 07:30

**背景**: 过渡季节指冬季和夏季之间能源需求适中的时期，通常允许可再生能源实现更高渗透率。这一时期清洁能源产出创纪录，表明可再生能源装机容量强劲增长且条件有利。

**标签**: `#clean energy`, `#renewable energy`, `#US energy`, `#climate`

---

<a id="item-30"></a>
## [EA 推出游戏内广告平台](https://www.gamedeveloper.com/marketing/ea-announces-advertising-platform-to-launch-ads-directly-into-gameplay-) ⭐️ 6.0/10

电子艺界（EA）宣布推出 EA Advertising 新平台，该平台将动态实时广告直接植入游戏玩法中，首批品牌合作伙伴包括 Visa、红牛、Xfinity、Lowe's、Peacock 和 Mountain Dew。 此举标志着游戏变现方式的重大转变，可能为 EA 带来可观收入，同时也引发了对玩家体验和隐私的担忧。这可能会为其他发行商树立先例。 这些广告设计为非侵入式，以体育场标牌或自定义游戏内容形式出现，并动态实时投放。该平台旨在将品牌与高度参与的游戏受众联系起来。

rss · Game Developer (Gamasutra) · Jun 15, 19:05

**背景**: 游戏内广告（IGA）是指在电子游戏中投放广告，区别于专门为推广而制作的广告游戏。动态 IGA 允许广告根据上下文或用户数据变化，Anzu 等公司已率先采用该技术。EA 以专用平台进入这一领域，标志着行业的重要发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ea.com/news/introducing-ea-advertising">Introducing EA Advertising</a></li>
<li><a href="https://www.gamedeveloper.com/marketing/ea-announces-advertising-platform-to-launch-ads-directly-into-gameplay-">EA unveils new platform to insert ads 'directly into gameplay'</a></li>
<li><a href="https://en.wikipedia.org/wiki/In-game_advertising">In - game advertising - Wikipedia</a></li>

</ul>
</details>

**标签**: `#gaming`, `#advertising`, `#monetization`, `#EA`

---

<a id="item-31"></a>
## [谷歌地球网页版新增飞行模拟器](https://www.4gamer.net/games/042/G004283/20260615001/) ⭐️ 6.0/10

2026 年 6 月 12 日，谷歌在网页版谷歌地球中增加了飞行模拟器功能，用户无需注册账号或下载即可直接在浏览器中飞越全球景观。 这使得之前隐藏的桌面功能变得广泛可用，可能以更具吸引力的方式吸引更多用户探索谷歌地球，并展示了 WebGL 在浏览器中进行 3D 渲染的能力。 该飞行模拟器此前是谷歌地球专业版桌面应用中的隐藏功能；网页版现在将其带到浏览器中，无需安装，使用 WebGL 技术进行实时 3D 渲染。

rss · 4Gamer.net · Jun 15, 01:53

**背景**: 谷歌地球是基于卫星图像的地球 3D 表示，有桌面程序和网页应用两种形式。桌面版谷歌地球专业版长期以来包含一个隐藏的飞行模拟器，用户可激活使用。网页版现在使用 WebGL（一种用于 3D 图形的网络标准）复制了这一功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Earth">Google Earth - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Google Earth`, `#flight simulator`, `#web application`, `#mapping`

---

<a id="item-32"></a>
## [SteamOS 测试版扩展至 MSI Claw 等 Intel 掌机](https://www.pcgamer.com/hardware/handheld-gaming-pcs/it-looks-like-more-handhelds-will-soon-be-able-to-run-steamos-if-this-msi-claw-gameplay-test-is-anything-to-go-by/) ⭐️ 6.0/10

Valve 的 SteamOS 3.8.7 测试版增加了对基于 Intel 的掌上游戏 PC 的官方支持，包括 MSI Claw 8 AI+，并提供了手柄映射和固件准备。 这一扩展打破了 SteamOS 此前仅支持 AMD 的限制，可能让更多掌上设备运行 SteamOS，并挑战 Windows 在便携游戏领域的主导地位。 该测试版包含针对即将推出的 Intel 掌机的初始固件，以及对 MSI Claw 8 AI+ 等设备的手柄支持，但 Intel 硬件上的性能预计将在未来更新中提升。

rss · PC Gamer · Jun 15, 16:10

**背景**: SteamOS 是 Valve 基于 Linux 的游戏操作系统，最初仅用于搭载 AMD 处理器的 Steam Deck。MSI Claw 是一款搭载 Intel Core Ultra 7 155H 处理器和 Intel Arc 显卡的掌上游戏 PC，标志着便携游戏领域从 AMD 主导的转变。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techradar.com/computing/gaming-pcs/valves-latest-steamos-beta-provides-better-intel-hardware-compatibility-and-thats-great-news-for-upcoming-handhelds">Valve's latest SteamOS beta provides better Intel ... | TechRadar</a></li>
<li><a href="https://otontechnology.com/steamos-3-8-7-beta-intel-handheld-support/">SteamOS 3.8.7 Beta : Intel Handhelds Get Official Support</a></li>
<li><a href="https://www.tweaktown.com/news/112145/youtuber-tests-steamos-on-an-intel-based-msi-claw-8-ai-plus-handheld-steamos-now-supports-intel-handheld-gaming-pcs-in-new-beta/index.html">YouTuber tests SteamOS on an Intel -based MSI Claw 8 AI+ handheld ...</a></li>

</ul>
</details>

**标签**: `#SteamOS`, `#handheld gaming`, `#Intel`, `#beta`

---