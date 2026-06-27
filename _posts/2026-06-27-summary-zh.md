---
layout: default
title: "Horizon Summary: 2026-06-27 (ZH)"
date: 2026-06-27
lang: zh
---

> From 48 items, 13 important content pieces were selected

---

1. [DeepSeek DSpark：投机解码加速大模型推理](#item-1) ⭐️ 9.0/10
2. [IP Crawl：公开网络摄像头实时地图引发隐私担忧](#item-2) ⭐️ 8.0/10
3. [Meta 因对前高管进行 12 个月监控被起诉](#item-3) ⭐️ 8.0/10
4. [分布不连续性揭示人类行为怪癖](#item-4) ⭐️ 8.0/10
5. [物理媒介所有权的辩护](#item-5) ⭐️ 7.0/10
6. [后 Mythos 时代的网络安全：保持冷静，继续前行](#item-6) ⭐️ 7.0/10
7. [苹果寻求豁免，从被制裁的中国供应商 CXMT 购买内存](#item-7) ⭐️ 7.0/10
8. [OpenRA 以现代特性重振经典即时战略游戏](#item-8) ⭐️ 6.0/10
9. [TownSquare 为网站添加短暂在场感](#item-9) ⭐️ 6.0/10
10. [金融科技工程手册因建议浅薄遭批评](#item-10) ⭐️ 6.0/10
11. [智能家居行业仍押注 Matter 标准](#item-11) ⭐️ 6.0/10
12. [PUBG 的 AI 队友 Ella：聊天自然，操作拉胯](#item-12) ⭐️ 6.0/10
13. [通过 WebAssembly 实现《半条命 2》和《传送门》的浏览器移植](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek DSpark：投机解码加速大模型推理](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) ⭐️ 9.0/10

DeepSeek 发布了论文和开源模型（DeepSeek-V4-Flash-DSpark 和 DeepSeek-V4-Pro-DSpark），实现了投机解码，在生产流量中推理速度提升 60% 到 85%。 这一突破显著降低了 LLM 推理延迟和成本，使先进 AI 更易获取。DeepSeek 的开源方式与闭源的美国实验室形成对比，促进了社区创新。 DSpark 报告吞吐量提升 51% 到 400%（取决于并发度），并已在 DeepSeek-V4 Flash 和 Pro 模型的真实在线流量中部署。Hugging Face 上的模型已内置投机解码模块。

hackernews · aurenvale · Jun 27, 09:18 · [社区讨论](https://news.ycombinator.com/item?id=48696585)

**背景**: 投机解码是一种推理时优化技术，通过同时预测和验证多个 token 来加速 LLM 的 token 生成，且不降低输出质量。该技术由 Google 于 2022 年提出，并经过 NVIDIA 等机构改进。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bentoml.com/llm/inference-optimization/speculative-decoding">Speculative decoding | LLM Inference Handbook</a></li>
<li><a href="https://cryptobriefing.com/deepseek-dspark-faster-inference/">DeepSeek unveils DSpark for 60% to 85% faster inference optimization</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark">deepseek -ai/ DeepSeek -V4-Pro- DSpark · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区称赞 DeepSeek 的开源创新，与不再发布此类细节的美国实验室形成对比。用户报告了 DeepSeek V4 Pro 的积极实际体验，称其快速、可靠且成本低廉。有人猜测其将集成到本地推理工具（如 DwarfStar）中。

**标签**: `#LLM inference`, `#speculative decoding`, `#DeepSeek`, `#AI acceleration`, `#open source`

---

<a id="item-2"></a>
## [IP Crawl：公开网络摄像头实时地图引发隐私担忧](https://ipcrawl.com/) ⭐️ 8.0/10

IP Crawl（ipcrawl.com）推出了一个可公开访问的地图集，展示了在公共互联网上发现的数千个开放网络摄像头，任何人都可以观看全球未受保护摄像头的实时画面。 该网站揭示了未受保护的物联网设备的巨大规模，暴露了个人和组织面临的严重隐私风险。它重新引发了关于互联网扫描伦理以及设备制造商和用户责任的讨论。 该地图集通过扫描公共互联网，寻找使用默认凭据或无需认证的摄像头构建而成。许多画面显示私人空间，如家庭、办公室甚至非法活动，引发了法律和伦理问题。

hackernews · arm32 · Jun 27, 19:09 · [社区讨论](https://news.ycombinator.com/item?id=48700834)

**背景**: 像 Shodan 这样的互联网扫描工具早已索引了暴露的设备，但 IP Crawl 以用户友好的地图形式呈现它们。许多廉价 IP 摄像头带有默认密码且无防火墙，使其成为易攻击目标。扫描并发布此类数据的做法介于安全研究和隐私侵犯之间的灰色地带。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Internet_Scamming">Internet Scamming</a></li>
<li><a href="https://cyberstreams.com/post/unsecured-webcams-are-wide-open-on-the-internet">Unsecured Webcams Are Wide Open On The Internet</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/iot-device-vulnerabilities">Top IoT Device Vulnerabilities: How To Secure IoT Devices - Fortinet</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了不安，将该网站比作用望远镜窥视他人公寓。一些人指出这个问题至少从 2012 年就存在，而另一些人建议该网站应提醒摄像头所有者其设备已暴露。少数人指出了显示潜在非法活动的特定画面。

**标签**: `#privacy`, `#security`, `#IoT`, `#webcams`, `#internet scanning`

---

<a id="item-3"></a>
## [Meta 因对前高管进行 12 个月监控被起诉](https://fortune.com/2026/06/26/meta-wynn-williams-surveillance-gag-order-lawsuit-2026/) ⭐️ 8.0/10

前 Meta 高管 Wynn-Williams 提起诉讼，声称 Meta 对她进行了 12 个月的监控，并施加禁言令，以阻止她谈论其著作《Careless People》。 这起诉讼引发了对企业监控以及利用保密协议和禁言令压制举报人的严重担忧，可能影响科技伦理和企业问责制。 诉讼指控 Meta 在一年内追踪了她的通信和行踪，禁言令阻止她讨论自己的经历。社区评论提供了法庭案卷和投诉存档的链接。

hackernews · 1vuio0pswjnm7 · Jun 27, 21:14 · [社区讨论](https://news.ycombinator.com/item?id=48701822)

**背景**: Meta 此前曾因员工监控问题引发争议，包括一项通过笔记本电脑追踪员工的计划。保密协议和禁言令在企业中常用于保护机密信息，但用于压制批评者已引起法律审查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.the-independent.com/tech/meta-staff-surveillance-mci-privacy-ai-b3001251.html">Meta pauses controversial staff surveillance program after massive data leak | The Independent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Non-disclosure_agreement">Non-disclosure agreement - Wikipedia</a></li>
<li><a href="https://shegerianconniff.com/use-of-ndas-gag-orders-in-harassment-claims-whats-legal-and-whats-not/">Use of NDAs & Gag Orders in Harassment Claims: What’s Legal and What’s Not - Shegerian Conniff</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Meta 的行为表示怀疑，一些人认为监控行为表明这些指控可能是真的。其他人则强调了斯特赖桑德效应，并呼吁提供法庭案卷等主要来源的链接。

**标签**: `#Meta`, `#surveillance`, `#lawsuit`, `#tech ethics`, `#corporate accountability`

---

<a id="item-4"></a>
## [分布不连续性揭示人类行为怪癖](https://danluu.com/discontinuities/) ⭐️ 8.0/10

Dan Luu 在 2020 年的文章中分析了统计分布中的不连续性如何揭示系统性的行为偏差，例如马拉松完赛时间集中在整数附近，以及考试成绩避开刚好不及格的分数段。 该分析揭示了人类目标设定和阈值效应如何扭曲数据，对行为经济学、数据科学和政策设计等领域具有启示意义，因为这些领域中指标可能被操纵或行为在边界附近发生变化。 例子包括马拉松跑者集中在整数时间目标附近、波兰语考试成绩在及格线 30%处出现巨大扭曲，以及 Lichess 上的国际象棋等级分在 100 的倍数处聚集。

hackernews · tosh · Jun 27, 13:32 · [社区讨论](https://news.ycombinator.com/item?id=48698151)

**背景**: 当人类行为在特定阈值（如及格分数或整数）处发生突变时，分布就会出现不连续性。这些人为痕迹在汇总统计中往往不可见，但在绘制完整分布图时会变得清晰。理解它们有助于避免数据误读，并揭示激励如何塑造行为。

**社区讨论**: 评论者分享了现实世界的例子：英国税收悬崖导致超过 60%的边际税率、AWS 工程师操纵 P90 延迟目标、以及国际象棋棋手避免掉到整数等级分以下。这些讨论用来自不同领域的具体案例验证了文章的观点。

**标签**: `#statistics`, `#behavioral economics`, `#data analysis`, `#human behavior`

---

<a id="item-5"></a>
## [物理媒介所有权的辩护](https://dervis.de/physical/) ⭐️ 7.0/10

一篇文章主张，真正的媒体所有权需要物理占有，引发了关于数字许可和 DRM 的讨论。讨论中提到了数字所有权的脆弱性，例如 Ultraviolet 的关闭和索尼移除已购买内容的事件。 这很重要，因为消费者越来越依赖可能被撤销的数字购买，引发了对长期访问和保存的担忧。这场辩论影响着人们在便利性和真正所有权之间的选择，进而影响游戏、电影和音乐等行业。 文章和评论提到了已停用的数字权利存储服务 Ultraviolet，以及索尼 2026 年从 PlayStation 库中移除 Studio Canal 内容的通知。一些评论者主张将盗版作为永久访问的实用解决方案。

hackernews · cemdervis · Jun 27, 11:32 · [社区讨论](https://news.ycombinator.com/item?id=48697335)

**背景**: 数字版权管理（DRM）限制了消费者使用已购买数字内容的方式，通常将其绑定到特定平台或账户。物理媒介（如蓝光和 DVD）提供离线、可转让的所有权，但由于流媒体和数字下载的便利性，其受欢迎程度正在下降。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://jacobin.com/2025/01/digital-ownership-physical-media-control">Digital Ownership and the End of Physical Media - Jacobin</a></li>
<li><a href="https://libertyproject.com/digital-vs-physical-media">Digital Media May Be Convenient, But Is It Yours ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为数字所有权是脆弱的，一些人主张将盗版作为可靠的备份。其他人则强调物理媒介并非实现真正所有权的唯一途径，并指出了像 GOG 和 Bandcamp 这样的无 DRM 数字商店。

**标签**: `#digital rights`, `#DRM`, `#media ownership`, `#piracy`, `#consumer rights`

---

<a id="item-6"></a>
## [后 Mythos 时代的网络安全：保持冷静，继续前行](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/) ⭐️ 7.0/10

一篇反思性博客文章指出，尽管 Anthropic 的 Mythos AI 模型发布并引发争议，核心网络安全问题并未改变，而社区评论则强调了 LLM 在漏洞研究中日益重要的作用。 这篇分析戳破了供应商的炒作，提醒业界即使像 Mythos 这样的 LLM 展示了强大的新能力，配置错误和人为错误等基础问题仍然是主要安全风险。 Anthropic 的 AI 模型 Mythos 能够识别并利用主流操作系统和浏览器中的零日漏洞，但博客认为大多数安全问题源于糟糕的配置和实践，而非高级漏洞利用。

hackernews · Versipelle · Jun 27, 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48698559)

**背景**: Mythos 是 Anthropic 于 2026 年 4 月发布的 AI 模型，能够自主发现并利用零日漏洞。其发布引发了关于 AI 在网络安全中作用的辩论，供应商迅速推销解决方案。LLM 越来越多地用于漏洞检测，但其对日常安全运营的实际影响仍在演变中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/apr/22/what-is-anthropic-mythos-ai-threat-global-cybersecurity">What is Mythos AI and why could it be a threat to global cybersecurity? | AI (artificial intelligence) | The Guardian</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Assessing Claude Mythos Preview’s cybersecurity capabilities \ Anthropic</a></li>
<li><a href="https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection">GitHub - huhusmang/Awesome-LLMs-for-Vulnerability-Detection: The community's most comprehensive, continuously-updated index of research on Large Language Models for software vulnerability detection — papers across function-level, repository-level, agentic, and smart-contract detection, plus datasets, benchmarks, and surveys.</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了不同观点：一些人指出 LLM 已经能有效发现漏洞（例如 Deepseek V4 Flash），而另一些人则批评供应商的恐慌营销，并强调大多数安全问题源于配置错误和人为失误。一位评论者强调了发现 BSD 漏洞所需的工作量，从而客观看待 LLM 的能力。

**标签**: `#cybersecurity`, `#Mythos`, `#LLM`, `#vulnerability research`, `#AI security`

---

<a id="item-7"></a>
## [苹果寻求豁免，从被制裁的中国供应商 CXMT 购买内存](https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt) ⭐️ 7.0/10

苹果已向美国政府申请豁免，允许其从长鑫存储（CXMT）购买 DRAM 芯片。CXMT 是一家中国内存制造商，因被指与中国人民解放军有关联而被美国国防部列入黑名单。 此举凸显了苹果在内存价格上涨和地缘政治紧张局势下的供应链脆弱性，并可能为其他寻求绕过黑名单限制的科技公司开创先例。 CXMT 仅生产普通 DRAM，而非先进的高带宽内存（HBM），因此该请求对美国主要内存制造商美光构成威胁较小。苹果提出请求之际，RAM 和存储价格飙升，给其供应链带来压力。

rss · The Verge · Jun 27, 17:28

**背景**: 美国国防部根据《国防授权法》第 1260H 条维护一份中国军事公司名单，限制美国实体在未获得特别许可的情况下与其开展业务。CXMT 因被指与中国人民解放军有关联而被列入该名单。苹果请求豁免，以便从 CXMT 购买内存，缓解供应链压力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://247wallst.com/investing/2026/06/27/apple-wants-to-buy-blacklisted-chinese-memory-micron-has-nothing-to-worry-about/">Apple Wants to Buy Blacklisted Chinese Memory. - 24/7 Wall St.</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2024-03-09/us-mulls-blacklisting-cxmt-to-further-curb-china-s-chip-advance">US Mulls Blacklisting CXMT to Further Curb... - Bloomberg</a></li>

</ul>
</details>

**标签**: `#Apple`, `#supply chain`, `#memory`, `#geopolitics`, `#CXMT`

---

<a id="item-8"></a>
## [OpenRA 以现代特性重振经典即时战略游戏](https://www.openra.net/) ⭐️ 6.0/10

OpenRA 是一个开源项目，重新实现了《红色警戒》、《命令与征服》和《沙丘 2000》等经典即时战略游戏，提供了改进的平衡性、现代特性以及跨平台支持。 该项目让备受喜爱的经典游戏在现代系统上得以延续和运行，拥有活跃的社区和持续的开发，提升了游戏体验和平衡性。 OpenRA 使用 C# 和 SDL 编写，支持 Windows、macOS、Linux 和 *BSD，并能自动下载原始游戏文件或从光盘安装。项目的下一个主要目标是增加对《泰伯利亚之日》等第二代 C&C 游戏的支持。

hackernews · tosh · Jun 27, 12:10 · [社区讨论](https://news.ycombinator.com/item?id=48697560)

**背景**: 《命令与征服：红色警戒》由 Westwood Studios 于 1996 年发布，是一款里程碑式的即时战略游戏，背景设定在盟军与苏联作战的架空历史中。EA 于 2008 年将该游戏转为免费软件。OpenRA 是多个开源引擎重制项目之一，旨在现代化经典游戏的同时保留其原始体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenRA">OpenRA</a></li>
<li><a href="https://www.openra.net/">OpenRA - Classic strategy games rebuilt for the modern era</a></li>
<li><a href="https://cnc.fandom.com/wiki/OpenRA">OpenRA - Command & Conquer Wiki - covering Tiberium, Red ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍非常积极，称赞 OpenRA 改进的平衡性和现代特性。一位用户指出玩家基数仍然强劲，而另一位则提到在线游戏中偶尔存在不友好行为。该项目已在 Hacker News 上被多次讨论，显示出持续的兴趣。

**标签**: `#open-source`, `#gaming`, `#RTS`, `#game-development`

---

<a id="item-9"></a>
## [TownSquare 为网站添加短暂在场感](https://cauenapier.com/blog/townsquare_release/) ⭐️ 6.0/10

TownSquare 是一个轻量级的短暂在场层，让网站访客无需账户或永久记录即可实时看到彼此并聊天。 它复兴了早期网络中的共在感，提供了一种非企业化的社交媒体替代方案，优先考虑偶然互动而非数据收集。 该工具刻意小巧且健忘：没有账户、个人资料、关注者数量或永久聊天记录；消息仅当人们在场时存在。

hackernews · eustoria · Jun 27, 17:11 · [社区讨论](https://news.ycombinator.com/item?id=48699928)

**背景**: IndieWeb 运动倡导个人网站和去中心化社交互动，常使用 Webmention 等工具。TownSquare 通过提供不依赖中心化平台的轻量级短暂社交层，与这一理念相符。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IndieWeb">IndieWeb</a></li>
<li><a href="https://indieweb.org/">IndieWeb</a></li>

</ul>
</details>

**社区讨论**: 评论褒贬不一：一些人称赞其怀旧感和与 IndieWeb 的契合，而另一些人则认为界面令人困惑，或质疑没有永久记录的短暂互动的价值。

**标签**: `#web development`, `#social software`, `#real-time`, `#indieweb`, `#ephemeral`

---

<a id="item-10"></a>
## [金融科技工程手册因建议浅薄遭批评](https://w.pitula.me/fintech-engineering-handbook/) ⭐️ 6.0/10

一本金融科技工程手册发布，涵盖货币数据处理和外汇兑换等主题，但社区批评其内容浅薄，并提供可疑建议，例如将货币值存储为浮点数。 该手册旨在指导金融科技工程师，但其褒贬不一的评价凸显了金融软件中需要经过严格验证的最佳实践，因为错误可能带来严重的财务后果。 该手册在线发布，已产生 147 条评论，用户指出其缺陷，如应使用整数表示货币值以及外汇汇率处理的复杂性，而有些人则认为它是有用的现有知识汇编。

hackernews · signa11 · Jun 27, 10:28 · [社区讨论](https://news.ycombinator.com/item?id=48696982)

**背景**: 金融软件必须精确处理货币值以避免舍入误差。最佳实践建议使用整数（如分）或定点运算，而非浮点数。外汇处理需要仔细考虑汇率和时机。

**社区讨论**: 社区意见分歧：一些人批评手册内容浅薄，在货币存储和外汇方面提供糟糕建议；另一些人则认为它是已知最佳实践的实用汇编。争议焦点在于货币值应使用整数还是浮点数。

**标签**: `#fintech`, `#software engineering`, `#monetary data`, `#best practices`

---

<a id="item-11"></a>
## [智能家居行业仍押注 Matter 标准](https://www.theverge.com/tech/958008/matter-unify-conference-csa-apple-google-amazon-samsung-smart-home-interoperability) ⭐️ 6.0/10

The Verge 在阿姆斯特丹的 Matter Unify 会议上报道，包括苹果、谷歌、亚马逊和三星在内的智能家居行业，尽管消费者采用缓慢，仍继续投资于 Matter 互操作性标准。 Matter 旨在通过使不同品牌的设备无缝协作来解决智能家居碎片化问题，这可以简化用户体验并加速物联网的采用。 Matter 四年前作为基于现有技术的开放标准推出，但由于复杂性和认证延迟，采用速度缓慢。会议突显了行业持续的承诺和渐进式进展。

rss · The Verge · Jun 27, 13:00

**背景**: Matter 是智能家居和物联网设备的技术标准，旨在提高互操作性和安全性，同时允许本地控制。它于 2019 年由亚马逊、苹果、谷歌等公司发起，最初名为 Project Connected Home over IP（CHIP），第一个版本于 2022 年发布。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matter_(standard)">Matter (standard) - Wikipedia matter-handbook | This is the repository for the Matter ... Top Stories Welcome to Matter’s documentation — Matter documentation What Is Matter? We Explain the Smart Home Standard (2025 ... Matter: IoT Interoperability for Smart Homes - arXiv.org Matter Protocol in 2026: The Smart Home Interoperability ...</a></li>
<li><a href="https://matter-smarthome.de/en/">All about the Matter standard | FAQ | News | Product overview</a></li>
<li><a href="https://csa-iot.org/all-solutions/matter/">Build With Matter | Smart Home Device Solution - CSA-IOT</a></li>

</ul>
</details>

**标签**: `#smart home`, `#Matter`, `#interoperability`, `#IoT`

---

<a id="item-12"></a>
## [PUBG 的 AI 队友 Ella：聊天自然，操作拉胯](https://www.4gamer.net/games/348/G034868/20260626019/) ⭐️ 6.0/10

《PUBG: Battlegrounds》限时推出了 AI 队友 Ella，她基于大语言模型和 NVIDIA ACE 技术，支持自然对话和语音指令，在 Ally Duo 模式中可用，持续至 6 月 30 日。 这标志着大语言模型在主流多人游戏中的重要整合，展示了 AI 如何增强合作玩法，并可能重塑玩家对 NPC 互动的期望。 Ella 能理解地图标记、物品名称，并执行“找车”或“掩护我”等指令，但报告指出她操作不佳，经常很快阵亡且缺乏闲聊，类似一个野人外国队友。

rss · 4Gamer.net · Jun 27, 02:00

**背景**: 《PUBG》是一款大逃杀游戏，玩家通常与真人组队。此前游戏中已有 AI 队友，但 Ella 使用大语言模型（LLM）实现更自然的交流，并由 NVIDIA ACE 技术支持实时 AI 交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamesn.com/playerunknowns-battlegrounds/ai-teammate">PUBG's new AI teammate is somehow more useless than my friends - PCGamesN</a></li>
<li><a href="https://www.tweaktown.com/news/112250/pubgs-new-ally-duo-game-mode-pairs-you-with-an-ai-teammate-powered-by-nvidia-ace/index.html">PUBG's new Ally Duo game mode pairs you with an AI teammate powered by NVIDIA ACE</a></li>
<li><a href="https://www.gamermarkt.com/blog/pubg-ally-duo-ai-teammate-beta-mode-ella/">PUBG Ally Duo Beta: AI Teammate Ella Explained (2026)</a></li>

</ul>
</details>

**标签**: `#AI`, `#gaming`, `#LLM`, `#PUBG`

---

<a id="item-13"></a>
## [通过 WebAssembly 实现《半条命 2》和《传送门》的浏览器移植](https://www.pcgamer.com/games/fps/web-port-wizards-produce-browser-versions-of-half-life-2-and-portal/) ⭐️ 6.0/10

开发者利用 WebAssembly 创建了《半条命 2》和《传送门》的浏览器版本，使这些经典游戏无需插件即可直接在网页浏览器中运行。 这展示了 WebAssembly 处理复杂高性能应用（如 AAA 级游戏）的能力日益增强，可能将游戏覆盖范围扩展到无需本地安装的平台。 这些移植利用 Emscripten 将原始 C++代码编译为 WebAssembly，在现代浏览器中实现了可玩的帧率。但性能可能因硬件和浏览器优化而异。

rss · PC Gamer · Jun 27, 16:28

**背景**: WebAssembly 是一种二进制指令格式，允许用 C++等语言编写的代码以接近原生的速度在网页浏览器中运行。Emscripten 是一个工具链，可将 C/C++代码编译为 WebAssembly，从而将现有应用移植到网页上。该项目延续了将经典游戏（如《毁灭战士》和《雷神之锤》）移植到浏览器的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/genizy/web-ports">GitHub - genizy/web-ports: a huge collection of games that ...</a></li>
<li><a href="https://markaicode.com/webassembly-games-cpp-engines-browser/">WebAssembly 4.0 for Games: Porting C++ Engines to the Browser</a></li>

</ul>
</details>

**标签**: `#WebAssembly`, `#game ports`, `#browser technology`, `#Half-Life 2`, `#Portal`

---