---
layout: default
title: "Horizon Summary: 2026-07-02 (ZH)"
date: 2026-07-02
lang: zh
---

> From 161 items, 26 important content pieces were selected

---

1. [弗吉尼亚州禁止出售地理位置数据](#item-1) ⭐️ 8.0/10
2. [Linux 6.9 中 LUKS 挂起未能清除加密密钥](#item-2) ⭐️ 8.0/10
3. [Podman v6.0.0 发布，带来重大网络改进](#item-3) ⭐️ 8.0/10
4. [Immich 3.0 重大发布引发社区热议](#item-4) ⭐️ 8.0/10
5. [人造细胞实现有限次数的分裂](#item-5) ⭐️ 8.0/10
6. [谷歌最终上诉失败，需支付欧盟 43 亿欧元反垄断罚款](#item-6) ⭐️ 8.0/10
7. [谷歌 AI 建设导致 2025 年用电量增长 37%](#item-7) ⭐️ 8.0/10
8. [PeerTube：去中心化视频平台获得关注](#item-8) ⭐️ 7.0/10
9. [如何有效向陌生人求助](#item-9) ⭐️ 7.0/10
10. [西班牙因国家安全将 Palantir 列入黑名单](#item-10) ⭐️ 7.0/10
11. [特斯拉司机因 FSD 事故致人死亡面临过失杀人指控](#item-11) ⭐️ 7.0/10
12. [PamStealer：新型 macOS 恶意软件通过 PAM 验证密码](#item-12) ⭐️ 7.0/10
13. [FAA 提议允许安静超音速飞机飞越美国城市](#item-13) ⭐️ 7.0/10
14. [隐私倡导者警告 FTC：马斯克的 X 平台存在风险](#item-14) ⭐️ 7.0/10
15. [社论：科学家必须发声反对政治化科学规则](#item-15) ⭐️ 7.0/10
16. [加州粪便甲烷计算不成立](#item-16) ⭐️ 7.0/10
17. [隐藏成本使燃气电厂价格上涨 30%](#item-17) ⭐️ 7.0/10
18. [加密货币转折点：从“为 Web3 而 Web3”走向现实金融](#item-18) ⭐️ 7.0/10
19. [前《使命召唤》开发者成立工作室，承诺游戏失败即开源](#item-19) ⭐️ 7.0/10
20. [谷歌因 GenAI 用电量激增](#item-20) ⭐️ 7.0/10
21. [Anthropic SDK Python v0.116.0 新增 Agent Memory Beta 标头](#item-21) ⭐️ 6.0/10
22. [Exapunks：回顾 Zachtronics 的编程解谜游戏](#item-22) ⭐️ 6.0/10
23. [AI 从聊天机器人转向关键工业基础设施](#item-23) ⭐️ 6.0/10
24. [初创公司 Springboards 用 Flint LLM 应对 AI 群体思维](#item-24) ⭐️ 6.0/10
25. [分析师预测清洁能源税收抵免到期将推高 PPA 价格](#item-25) ⭐️ 6.0/10
26. [工会工作者为被裁游戏开发者设立困难基金](#item-26) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [弗吉尼亚州禁止出售地理位置数据](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

2024 年 4 月 13 日，弗吉尼亚州州长 Abigail Spanberger 签署了 SB 338 法案，修订了《弗吉尼亚消费者数据保护法》，禁止出售精确地理位置数据，该禁令于 2024 年 7 月 1 日生效。 这项禁令为州级隐私保护树立了先例，限制了数据经纪商和科技公司未经同意将位置数据货币化的行为，并紧随马里兰州和俄勒冈州的类似行动。 该禁令将精确地理位置数据定义为识别个人位置在 1750 英尺以内的信息，并禁止出售或提供出售此类数据，由弗吉尼亚州总检察长负责执行。

hackernews · toomuchtodo · Jul 2, 21:03 · [社区讨论](https://news.ycombinator.com/item?id=48767347)

**背景**: 《弗吉尼亚消费者数据保护法》（VCDPA）于 2021 年颁布，2023 年 1 月 1 日生效，是美国继加州 CCPA 之后的第二部综合性州隐私法。地理位置数据越来越多地被应用程序和设备收集，其出售已被关联到滥用行为，例如追踪前往生殖健康诊所的访问。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cybereyeq.com/p/is-your-geolocation-data-ready-for-virginia-s-ban">Is Your Geolocation Data Ready for Virginia 's Ban?</a></li>
<li><a href="https://www.gblock.app/articles/virginia-geolocation-data-sale-ban">Virginia Banned the Sale of Your Location Data —Six More States...</a></li>
<li><a href="https://modernorange.io/item/48767347">US State of Virginia Bans Sale of Geolocation Data | Modern Orange</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该禁令，并引用了现实中的滥用案例，例如追踪 Planned Parenthood 就诊记录用于反堕胎广告。一些人提出了执法方面的担忧，例如如何处理州外公司或在弗吉尼亚数据中心处理的数据。

**标签**: `#privacy`, `#geolocation`, `#regulation`, `#data protection`, `#Virginia`

---

<a id="item-2"></a>
## [Linux 6.9 中 LUKS 挂起未能清除加密密钥](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 8.0/10

Linux 内核 6.9 中的一个回归导致 LUKS 挂起操作停止从内存中清除磁盘加密密钥，使其容易受到冷启动攻击。已提出修复方案。 此安全回归可能在挂起到内存期间暴露全盘加密密钥，削弱对敏感数据的保护。它凸显了测试安全关键内核功能的难度。 该错误影响 cryptsetup luksSuspend 命令，该命令用于在挂起前临时锁定 LUKS 设备。该问题在 Linux 6.9 中引入，并已在提议的补丁中修复。

hackernews · IngoBlechschmid · Jul 2, 15:25 · [社区讨论](https://news.ycombinator.com/item?id=48763035)

**背景**: LUKS（Linux 统一密钥设置）是一种磁盘加密规范，在操作期间将加密密钥存储在内核内存中。当挂起到内存时，系统通常会清除这些密钥以防止冷启动攻击，但回归破坏了这一行为。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48763035">Since Linux 6.9, LUKS suspend stopped wiping disk - encryption keys ...</a></li>
<li><a href="https://github.com/nailfarmer/debian-luks-suspend">GitHub - nailfarmer/debian- luks - suspend : Lock encrypted root volume...</a></li>
<li><a href="https://askubuntu.com/questions/95625/suspend-to-ram-and-encrypted-partitions">encryption - Suspend to RAM and encrypted partitions - Ask Ubuntu</a></li>

</ul>
</details>

**社区讨论**: 一些评论者指出 luksSuspend 并非官方支持，可能只影响 Debian，而另一些人则认为这类安全漏洞很容易被忽略，因为一切仍然正常。关于该风险对典型用户是否显著也存在争议。

**标签**: `#Linux`, `#security`, `#LUKS`, `#kernel`, `#encryption`

---

<a id="item-3"></a>
## [Podman v6.0.0 发布，带来重大网络改进](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0 作为无守护进程容器引擎的主要版本发布，引入了重大的网络改进，并继续作为 Docker 替代方案获得关注。 此版本巩固了 Podman 作为领先 Docker 替代方案的地位，增强了网络功能，有利于从 Docker 迁移或在生产环境中运行无根容器的用户。 该版本专注于网络改进，但摘要中未提供具体技术细节。用户报告与 docker-compose.yml 文件无缝兼容，从 Docker 切换无需任何更改。

hackernews · soheilpro · Jul 2, 14:23 · [社区讨论](https://news.ycombinator.com/item?id=48762098)

**背景**: Podman 是由 Red Hat 开发的无守护进程、无根、开源容器引擎。与 Docker 不同，它不需要中央守护进程，从而增强了安全性和系统集成。无根容器允许非 root 用户运行容器，降低了安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://podman.io/">Podman</a></li>
<li><a href="https://docs.podman.io/">What is Podman? — Podman documentation</a></li>
<li><a href="https://www.redhat.com/en/topics/containers/what-is-podman">What is Podman? - Red Hat</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户称赞从 Docker 迁移的简便性以及用于 systemd 集成的 Quadlet 功能。一些用户讨论了在 macOS 上与 OrbStack 的性能比较，并注意到轻微的 UI 对比度问题。

**标签**: `#Podman`, `#containers`, `#Docker alternative`, `#networking`, `#open source`

---

<a id="item-4"></a>
## [Immich 3.0 重大发布引发社区热议](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

开源自托管照片管理平台 Immich 发布了 3.0 重大更新，带来了显著改进并引发了社区讨论。 此次发布巩固了 Immich 作为 Google Photos 和 Apple Photos 领先开源替代品的地位，让用户完全掌控自己的数据和隐私。 该更新改进了 iOS 同步功能（此前是拥有大量照片库用户的一个痛点），并解决了与 Ente 等替代方案相比的加密权衡问题。

hackernews · hashier · Jul 2, 14:13 · [社区讨论](https://news.ycombinator.com/item?id=48761944)

**背景**: Immich 是一个高性能、自托管的照片和视频管理解决方案，提供人脸识别、地理定位和移动同步等功能。它常被拿来与 Google Photos 和 Apple Photos 比较，但优势在于完全的数据所有权和隐私。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/immich-app/immich">GitHub - immich-app/immich: High performance self-hosted photo and video management solution. · GitHub</a></li>
<li><a href="https://www.howtogeek.com/self-hosted-alternatives-to-google-photos/">3 Self-Hosted Alternatives to Google Photos - How-To Geek</a></li>
<li><a href="https://blog.elest.io/immich-free-open-source-photo-and-video-management-platform/">Immich: Free Open Source Photo and Video Management Platform</a></li>

</ul>
</details>

**社区讨论**: 社区成员称赞 Immich 结合 Tailscale 等 VPN 后是 Apple Photos 或 Google Photos 的“无需思考的替代品”。然而，一些用户报告了大型照片库的 iOS 同步问题，另一些用户则因端到端加密而选择 Ente，凸显了完善度与隐私之间的权衡。

**标签**: `#self-hosting`, `#photo management`, `#open-source`, `#privacy`, `#immich`

---

<a id="item-5"></a>
## [人造细胞实现有限次数的分裂](https://arstechnica.com/science/2026/07/artificial-cell-manages-a-few-rounds-of-cell-division/) ⭐️ 8.0/10

研究人员制造出能够进行几轮细胞分裂的人造细胞，这是合成生物学的一个里程碑，尽管该过程需要大量外部添加的材料。 这一成就使我们更接近创造自我复制的合成生命，可能彻底改变生物技术、药物递送以及我们对生命起源的理解。 人造细胞仅能进行几次分裂后便停止，并且它们依赖添加的膜组分和能量源等材料来分裂。

rss · Ars Technica · Jul 2, 16:21

**背景**: 细胞分裂是生命的基本过程，使生长和繁殖成为可能。合成生物学旨在从头构建最小细胞，以理解生命原理并创建有用的生物系统。之前的尝试实现了人造细胞的生长，但未能实现分裂。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/">For the First Time, a Cell Built From Scratch Grows and Divides | Quanta Magazine</a></li>
<li><a href="https://link.springer.com/article/10.1186/s12915-019-0665-1">Synthetic cell division via membrane-transforming molecular assemblies | BMC Biology | Springer Nature Link</a></li>

</ul>
</details>

**标签**: `#synthetic biology`, `#artificial cells`, `#cell division`, `#biotechnology`

---

<a id="item-6"></a>
## [谷歌最终上诉失败，需支付欧盟 43 亿欧元反垄断罚款](https://arstechnica.com/gadgets/2026/07/google-loses-long-running-appeal-of-record-eu-fine-will-have-to-cough-up-4-7-billion/) ⭐️ 8.0/10

欧洲法院维持了对谷歌 43 亿欧元的罚款，原因是谷歌通过将搜索和 Chrome 应用与 Android 捆绑，滥用市场支配地位，驳回了谷歌的最终上诉。 这一里程碑式的裁决确立了捆绑免费应用仍可能构成反垄断违规的先例，可能重塑全球科技巨头在移动平台上分发软件的方式。 该罚款最初于 2018 年开出，是欧盟有史以来最大的一笔。谷歌辩称 Android 是开源的，捆绑是平台盈利的必要手段。

rss · Ars Technica · Jul 2, 16:15

**背景**: 自 2010 年以来，欧盟委员会一直在调查谷歌的反垄断违规行为，共开出三项罚款，总额超过 80 亿欧元。Android 案的核心是谷歌要求制造商预装 Google 搜索和 Chrome，作为授权 Play Store 的条件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cryptobriefing.com/google-loses-eu-antitrust-fine-appeal/">Google loses appeal against €4B EU antitrust fine over Android bundling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Antitrust_cases_against_Google_by_the_European_Union">Antitrust cases against Google by the European Union - Wikipedia</a></li>
<li><a href="https://www.theverge.com/2018/10/18/17996640/google-eu-android-antitrust-ruling-app-unbundling-european-commission-chrome-search">Google is unbundling Android apps: all the news about the EU’s antitrust ruling | The Verge</a></li>

</ul>
</details>

**标签**: `#antitrust`, `#Google`, `#EU regulation`, `#Android`, `#tech policy`

---

<a id="item-7"></a>
## [谷歌 AI 建设导致 2025 年用电量增长 37%](https://arstechnica.com/ai/2026/07/googles-ai-buildout-drove-37-increase-in-electricity-use-in-2025/) ⭐️ 8.0/10

根据谷歌最新环境报告，其 2025 年总用电量增长了 37%，主要原因是 AI 数据中心的扩张。 这一激增凸显了 AI 基础设施扩张与企业清洁能源承诺之间日益加剧的矛盾，可能影响行业实践和能源政策。 谷歌的电力需求从 2020 年到 2024 年翻了一番多，尽管 2025 年签署了超过 12 吉瓦的新清洁能源协议，但其无碳能源目标仍面临挑战。

rss · Ars Technica · Jul 2, 11:15

**背景**: AI 模型的训练和部署需要大量计算资源，导致数据中心用电量快速增长。谷歌设定了到 2030 年实现全天候无碳能源运营的目标，但不断增长的 AI 需求使这一目标更难实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/">US data centers’ energy use amid the artificial intelligence ...</a></li>
<li><a href="https://www.technologyreview.com/2025/11/13/1127896/google-energy-goals/">Google is still aiming for its “moonshot” 2030 energy goals | MIT Technology Review</a></li>
<li><a href="https://blog.google/company-news/outreach-and-initiatives/sustainability/2026-environmental-report/">Read Google’s 2026 Environmental Report</a></li>

</ul>
</details>

**标签**: `#AI`, `#energy`, `#sustainability`, `#Google`, `#data centers`

---

<a id="item-8"></a>
## [PeerTube：去中心化视频平台获得关注](https://github.com/Chocobozzz/PeerTube) ⭐️ 7.0/10

PeerTube 是一个免费、开源、去中心化的视频平台，利用 ActivityPub 联邦协议和点对点技术将播放负载分散到观众之间，从而减轻热门视频对服务器的压力。 PeerTube 为 YouTube 等中心化平台提供了一个可行的替代方案，让内容创作者和社区更好地掌控自己的数据，并减少对大型科技基础设施的依赖。 PeerTube 主要处理播放（数据分发）和托管，但缺乏内置的变现和内容发现功能，这对专业创作者来说是主要挑战。

hackernews · doener · Jul 2, 11:17 · [社区讨论](https://news.ycombinator.com/item?id=48759634)

**背景**: PeerTube 基于 ActivityPub 协议构建，支持实例间的联邦互通，类似于 Mastodon。它使用 WebTorrent 进行点对点流媒体传输，当视频走红时，将负载分散到观众的浏览器上。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PeerTube">PeerTube - Wikipedia</a></li>
<li><a href="https://github.com/Chocobozzz/PeerTube">GitHub - Chocobozzz/PeerTube: ActivityPub-federated video streaming platform using P2P directly in your web browser · GitHub</a></li>
<li><a href="https://joinpeertube.org/">What is PeerTube? | JoinPeerTube</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，PeerTube 缺乏变现选项，使得专业 YouTuber 难以维持高质量制作。一些用户欣赏其联邦特性用于开源项目，但注意到内容发现和受众覆盖有限。

**标签**: `#decentralization`, `#video hosting`, `#federation`, `#open source`, `#PeerTube`

---

<a id="item-9"></a>
## [如何有效向陌生人求助](https://pradyuprasad.com/writings/how-to-ask-for-help/) ⭐️ 7.0/10

一篇关于如何向陌生人求助的实用指南被发布并引发广泛讨论，强调展示前期努力、简洁表达和理解对方视角。 这些建议解决了一个许多人感到困难的通用技能，社区的高度认可（344 分，53 条评论）表明其相关性和影响力。 关键点包括提前展示前期努力、保持请求简洁以及根据对方情况定制请求。文章标签为沟通、职业建议、软技能和社交网络。

hackernews · FigurativeVoid · Jul 2, 13:19 · [社区讨论](https://news.ycombinator.com/item?id=48761118)

**背景**: 向陌生人求助是职业和个人场景中常见但具有挑战性的任务。许多人因为不尊重对方的时间或未能展示自己的努力而失败。本指南总结了经验人士的最佳实践。

**社区讨论**: 评论者普遍赞同这些建议，并补充了个人经验和细微差别。一些人强调前期努力必须真实且深入，而非表面功夫，同时了解对方收到请求的频率至关重要。

**标签**: `#communication`, `#career-advice`, `#soft-skills`, `#networking`

---

<a id="item-10"></a>
## [西班牙因国家安全将 Palantir 列入黑名单](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv) ⭐️ 7.0/10

西班牙出于国家安全考虑，下令将美国数据分析巨头 Palantir 列入公共和私营公司的黑名单。 此举标志着欧洲对美国科技公司处理敏感数据的怀疑日益加深，可能重塑跨大西洋的数据主权和地缘政治信任。 该决定源于官方对与国家安全相关的机密信息可能被滥用的担忧，但具体担忧尚未详细说明。

hackernews · mgh2 · Jul 2, 15:02 · [社区讨论](https://news.ycombinator.com/item?id=48762725)

**背景**: Palantir 是一家美国公司，以其用于情报机构和军队的数据集成与分析软件而闻名。数据主权是指一国境内产生的数据受该国法律管辖的原则。西班牙的行动反映了欧洲保护数据主权、减少对外国技术供应商依赖的更广泛努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Palantir_Technologies">Palantir Technologies</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论意见分歧：一些人赞扬西班牙在数据主权方面的方向，而另一些人则怀疑该决定出于政治动机，指出西班牙最近与华为的类似公司签订了合同。批评者认为，鉴于中国的威权性质，信任中国公司而非 Palantir 是误导性的。

**标签**: `#Palantir`, `#Spain`, `#data sovereignty`, `#national security`, `#geopolitics`

---

<a id="item-11"></a>
## [特斯拉司机因 FSD 事故致人死亡面临过失杀人指控](https://www.theverge.com/transportation/961161/tesla-fsd-katy-tx-manslaughter-charges) ⭐️ 7.0/10

44 岁的迈克尔·巴特勒被捕并被指控过失杀人，此前他声称使用特斯拉全自动驾驶（FSD）的 Model 3 撞入得克萨斯州一处住宅，导致屋内一名女性死亡。 此案可能为使用高级驾驶辅助系统时追究驾驶员责任树立法律先例，从而影响相关法规和公众对自动驾驶技术的信任。 事故发生在上个月得克萨斯州凯蒂市，巴特勒声称当时车辆处于 FSD 模式。特斯拉的 FSD 是 L2 级驾驶辅助系统，需要驾驶员主动监督。

rss · The Verge · Jul 2, 22:09

**背景**: 特斯拉的全自动驾驶（FSD）是一种高级驾驶辅助系统（ADAS），可自动完成转向、加速和制动，但仍要求驾驶员保持注意力并随时准备接管控制。尽管名为“全自动驾驶”，FSD 并非完全自主，在 SAE 自动化等级中属于 L2 级。这起事件凸显了围绕此类系统安全性和法律责任的持续争议。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.com/en-us/autos/self-driving-cars/tesla-driver-charged-with-manslaughter-after-woman-killed-in-crash-sheriff/ar-AA274Thv">Tesla driver charged with manslaughter after woman killed in ...</a></li>
<li><a href="https://www.tesla.com/fsd">Full Self - Driving (Supervised) | Tesla</a></li>

</ul>
</details>

**标签**: `#Tesla`, `#autonomous driving`, `#legal`, `#FSD`, `#crash`

---

<a id="item-12"></a>
## [PamStealer：新型 macOS 恶意软件通过 PAM 验证密码](https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/) ⭐️ 7.0/10

Jamf Threat Labs 的研究人员发现了 PamStealer，这是一种基于 Rust 的 macOS 信息窃取器，它利用可插拔认证模块（PAM）接口在窃取敏感数据前本地验证窃取的登录密码。 这一发现凸显了 macOS 信息窃取器日益复杂化，PamStealer 的密码验证技术减少了误报并使检测更加困难，标志着 Mac 安全领域令人担忧的趋势。 PamStealer 使用自包含的 JXA 投放器和基于 Rust 的第二阶段，在窃取凭证前通过 PAM 本地验证，这使其区别于盲目窃取数据的典型信息窃取器。

rss · Ars Technica · Jul 2, 19:38

**背景**: macOS 信息窃取器是一种旨在从 Mac 系统窃取密码和凭证等敏感数据的恶意软件。最近的攻击活动使用社会工程策略，如 ClickFix 提示和恶意 DMG 安装程序，来部署 AMOS、MacSync 和 DigitStealer 等窃取器。PamStealer 代表了进化，它增加了密码验证功能，确保在窃取前窃取的凭证是正确的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/">Newly discovered PamStealer isn’t your typical macOS malware</a></li>
<li><a href="https://www.idropnews.com/news/pamstealer-macos-malware-password-verification/265878/">New PamStealer Mac Malware Pre-verifies Stolen Passwords</a></li>
<li><a href="https://appleworld.today/2026/07/pamstealer-is-a-rust-based-macos-infostealer-that-validates-credentials-through-pam/">PamStealer is a Rust-based macOS infostealer that validates ...</a></li>

</ul>
</details>

**标签**: `#macOS`, `#malware`, `#security`, `#infostealer`

---

<a id="item-13"></a>
## [FAA 提议允许安静超音速飞机飞越美国城市](https://arstechnica.com/gadgets/2026/07/faa-proposal-supersonic-airliners-can-fly-over-us-cities-if-theyre-quiet/) ⭐️ 7.0/10

美国联邦航空管理局（FAA）提出新规，允许安静的、不产生扰人音爆的超音速飞机飞越美国城市。这一监管变化可能使新一代超音速客机能够在陆地上空运营。 该提案可能通过取消长期以来对陆上超音速飞行的禁令来重振超音速航空旅行，而这一禁令曾是协和式飞机退役的主要原因之一。如果通过，它将为超音速飞机开辟利润丰厚的跨大陆航线，可能大幅缩短飞行时间。 该提案基于安静超音速技术的进步，例如 NASA 的 X-59 Quesst，其设计目标是产生低至 75 EPNdB 的砰声，而不是响亮的音爆。该规则将设定一个噪声标准，超音速飞机必须达到该标准才能获准在陆地上空飞行。

rss · Ars Technica · Jul 2, 17:29

**背景**: 自 1973 年以来，美国一直禁止在陆地上空进行超音速飞行，因为飞机超过 1 马赫时会产生扰人的音爆。最著名的超音速客机协和式飞机仅限于水上航线，这导致了其商业失败。NASA 和洛克希德·马丁公司一直在开发 X-59 Quesst，以证明超音速飞机可以设计成产生更安静的声音，从而可能为监管变革铺平道路。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quiet_Supersonic_Technology">Quiet Supersonic Technology</a></li>
<li><a href="https://www.nasa.gov/centers-and-facilities/armstrong/nasa-prepares-to-go-public-with-quiet-supersonic-tech/">NASA Prepares to Go Public with Quiet Supersonic Tech</a></li>
<li><a href="https://www.nasa.gov/centers-and-facilities/armstrong/supersonic-technologies/">Supersonic Technologies - NASA</a></li>

</ul>
</details>

**标签**: `#aviation`, `#regulation`, `#supersonic`, `#technology`, `#FAA`

---

<a id="item-14"></a>
## [隐私倡导者警告 FTC：马斯克的 X 平台存在风险](https://arstechnica.com/tech-policy/2026/07/musks-x-poses-serious-risk-to-americans-privacy-advocates-warn-ftc/) ⭐️ 7.0/10

隐私倡导者敦促美国联邦贸易委员会（FTC）拒绝埃隆·马斯克终止该机构对 X（前身为 Twitter）监控的企图，警告该平台对美国人的隐私和人工智能相关担忧构成严重风险。 此事意义重大，因为 X 是一个拥有数亿用户的主要社交媒体平台，终止 FTC 的监督可能导致数据保护松懈，并增加由人工智能驱动的隐私侵犯，为科技监管树立危险先例。 FTC 的同意令目前要求 X 维持一个数据治理团队并监控出站流量以防止数据泄露；倡导者声称，在马斯克的领导下，该团队已被解散，违反了该命令。

rss · Ars Technica · Jul 2, 14:39

**背景**: X（前身为 Twitter）自 2022 年起因先前的隐私违规行为而受到 FTC 同意令的约束。该命令要求对平台的数据实践进行独立监控。埃隆·马斯克于 2022 年收购了 Twitter，此后进行了重大变革，包括据报道影响了合规团队的裁员。隐私倡导者担心，终止该命令将使 X 能够在没有充分保障措施的情况下滥用用户数据进行人工智能训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.citizen.org/article/twitters-potential-violations-of-the-ftc-consent-decree/">Twitter's Potential Violations of the FTC Consent Decree - Public Citizen</a></li>
<li><a href="https://www.hoganlovells.com/en/publications/ftc-consent-decree-requires-monitoring-and-filtering-of-outbound-computer-traffic-to-block-export-of-sensitive-information">FTC Consent Decree Requires Monitoring and Filtering of Outbound...</a></li>

</ul>
</details>

**标签**: `#privacy`, `#AI`, `#regulation`, `#social media`, `#Elon Musk`

---

<a id="item-15"></a>
## [社论：科学家必须发声反对政治化科学规则](https://arstechnica.com/science/2026/07/editorial-the-most-important-thing-you-can-do-to-protect-science/) ⭐️ 7.0/10

Ars Technica 的一篇社论敦促科学家就一项拟议规则提交公众意见，该规则将允许政治任命人员推翻科学决策。 该规则威胁基于科学的决策的完整性，公众评论是科学家捍卫循证治理的关键途径。 社论强调，个人评论可以产生影响，因为机构在最终确定规则前必须考虑公众反馈。

rss · Ars Technica · Jul 2, 10:00

**背景**: 在美国，联邦机构经常就拟议法规征求公众意见。这项特定规则将赋予政治官员修改或拒绝科学发现的权力，引发了对科学政治干预的担忧。

**标签**: `#science policy`, `#editorial`, `#advocacy`

---

<a id="item-16"></a>
## [加州粪便甲烷计算不成立](https://www.technologyreview.com/2026/07/02/1139981/why-californias-carbon-manure-math-doesnt-add-up/) ⭐️ 7.0/10

一项调查揭示，加州激励捕获牛粪甲烷的项目因碳核算存在缺陷，可能适得其反。 这暴露了加州气候政策的关键缺陷，可能削弱可再生能源激励和碳抵消市场的有效性。 该计划向农民支付费用，将粪便甲烷转化为天然气，但核算可能高估减排量，导致温室气体净增加。

rss · MIT Technology Review · Jul 2, 09:00

**背景**: 加州的低碳燃料标准（LCFS）激励低碳交通燃料，包括来自粪便的生物甲烷。但批评者认为，碳强度计算方法未能考虑泄漏和其他间接影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.ucs.org/jeremy-martin/something-stinks-california-must-end-manure-biomethane-accounting-gimmicks-in-its-low-carbon-fuel-standard/">Something Stinks: California Must End Manure Biomethane...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0013935124021765">Methodological study on carbon sequestration accounting for ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-025-27609-2">Reduced life cycle climate impact from manure through ...</a></li>

</ul>
</details>

**标签**: `#climate policy`, `#methane`, `#carbon accounting`, `#renewable energy`, `#agriculture`

---

<a id="item-17"></a>
## [隐藏成本使燃气电厂价格上涨 30%](https://www.utilitydive.com/news/sticker-shock-gas-power-plants-pipeline-gridlab/824061/) ⭐️ 7.0/10

GridLab 和 Current Energy Group 发布报告指出，管道、燃料和储存成本使新建燃气电厂的总成本增加约 30%，而这些成本常被监管机构忽略。 该分析挑战了燃气电厂相对于清洁能源的经济竞争力，可能影响能源政策和基础设施规划决策。 隐藏成本包括强制性长期合同，用于固定管道运输、天然气储存和天然气处理设备，这些会显著改变项目对消费者的真实成本。

rss · Utility Dive · Jul 2, 13:04

**背景**: 当公用事业公司提议新建燃气电厂时，监管机构通常只审查前期建设成本。然而，燃气电厂需要广泛的支持基础设施——管道、储存和燃料供应合同——这些会增加大量持续成本。GridLab 的报告量化了这些被忽视的费用，显示它们可能使项目总成本增加约 30%。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gridlab.org/the-hidden-costs-of-gas-press-release/">The Hidden Costs of Gas Press Release - GridLab</a></li>
<li><a href="https://gridlab.org/hidden-cost-of-gas/">Beyond the Power Plant: The Hidden Costs of Gas-Fired ...</a></li>
<li><a href="https://www.utilitydive.com/news/sticker-shock-gas-power-plants-pipeline-gridlab/824061/">Why the true cost of new gas plants is much higher than the sticker price | Utility Dive</a></li>

</ul>
</details>

**标签**: `#energy`, `#infrastructure`, `#policy`, `#gas plants`, `#cost analysis`

---

<a id="item-18"></a>
## [加密货币转折点：从“为 Web3 而 Web3”走向现实金融](https://www.4gamer.net/games/991/G999104/20260702015/) ⭐️ 7.0/10

在 IVS2026 大会上，IVC 合伙人 J.T. Law 和 Ann Chien 宣布“为 Web3 而 Web3”的时代已经结束，加密货币正转向实用的金融基础设施，并引用了比特币周期、机构入场、稳定币类型以及日本监管对风投投资的影响。 这标志着加密货币行业走向成熟，从投机炒作转向实际应用，可能吸引更多机构资本和监管明确性，最终惠及更广泛的金融生态系统。 主题演讲区分了收益型稳定币和实用型稳定币，并指出日本的监管框架已改变了风投的投资标准。讨论还涵盖了比特币的四年周期和机构投资者参与。

rss · 4Gamer.net · Jul 2, 06:32

**背景**: Web3 指的是基于区块链技术构建的去中心化互联网，但许多项目专注于投机而非实际应用。稳定币是与美元等稳定资产挂钩的加密货币，分为收益型（赚取利息）和实用型（用于交易）。日本一直是加密货币监管的先驱，影响着全球投资模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chain.link/article/yield-bearing-stablecoins-explained">Yield-Bearing Stablecoins: Generating Onchain Yield | Chainlink</a></li>
<li><a href="https://www.bitgo.com/resources/blog/stablecoin-yield-explained/">Understanding Stablecoin Yield Sources and Variability | BitGo</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#Web3`, `#financial infrastructure`, `#regulation`, `#institutional investment`

---

<a id="item-19"></a>
## [前《使命召唤》开发者成立工作室，承诺游戏失败即开源](https://www.pcgamer.com/gaming-industry/former-call-of-duty-frontman-launches-new-studio-with-a-stop-killing-games-style-mission-statement-if-the-game-bombs-it-goes-open-source/) ⭐️ 7.0/10

前《使命召唤》开发者 Robert Bowling 成立了一家新游戏工作室，承诺如果游戏商业失败，将把游戏开源，这与“停止杀死游戏”运动的主张一致。 这一举措直接回应了日益增长的游戏保存问题——发行商经常放弃仅限在线的游戏，使其无法游玩。如果成功，可能为其他工作室采用类似的开源后备计划树立先例。 该工作室的使命声明明确表示，如果游戏“失败”，它将开源，让社区能够继续维持其运行。此前，Bowling 之前的工作室 Midnight Society 因联合创始人 Dr Disrespect 的争议于 2025 年 1 月关闭。

rss · PC Gamer · Jul 2, 17:19

**背景**: “停止杀死游戏”运动由 YouTuber Ross Scott 于 2024 年发起，旨在反对发行商在关闭服务器时不提供离线模式，从而永久销毁游戏。该运动在育碧关闭《飙酷车神》后获得关注，这是一款主要单人游戏却需要持续联网。将失败的游戏开源可以让玩家自行托管服务器并继续游玩。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stop_Killing_Games">Stop Killing Games - Wikipedia</a></li>
<li><a href="https://www.stopkillinggames.com/en">Stop Killing Games — They Kill Games. We Fight Back.</a></li>
<li><a href="https://www.ign.com/articles/midnight-society-dr-disrepsect-game-studio-closes-cancels-game-deadrop">Midnight Society, Game Studio Co-Founded by Dr Disrespect, Closes Shop, Cancels Game - IGN</a></li>

</ul>
</details>

**标签**: `#game preservation`, `#open source`, `#gaming industry`, `#software engineering`

---

<a id="item-20"></a>
## [谷歌因 GenAI 用电量激增](https://www.pcgamer.com/software/ai/a-wild-testament-to-the-obscene-bloat-and-waste-of-genai-googles-electricity-consumption-is-exponentially-increasing/) ⭐️ 7.0/10

谷歌的电力消耗呈指数级增长，超过了斯洛伐克、厄瓜多尔、爱尔兰和尼日利亚等国家的全年总用电量，这主要归因于生成式 AI（GenAI）的能源需求。 这凸显了 GenAI 的严重环境代价，随着 AI 应用加速，引发了关于科技行业可持续性和资源分配的紧迫问题。 训练像 GPT-4 这样的大型 GenAI 模型是主要的能源消耗点，谷歌的电力需求现已超过多个国家，凸显了问题的规模。

rss · PC Gamer · Jul 2, 12:15

**背景**: 生成式 AI（GenAI）是一种能够创建文本、图像或代码等新内容的人工智能。训练这些模型需要大量的计算资源，导致高电力消耗。谷歌对 GenAI 服务的日益使用显著增加了其能源足迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/software/ai/a-wild-testament-to-the-obscene-bloat-and-waste-of-genai-googles-electricity-consumption-is-exponentially-increasing/">'A wild testament to the obscene bloat and waste of GenAI ... | PC Gamer</a></li>
<li><a href="https://www.ohio.edu/news/2024/11/ais-increasing-energy-appetite">AI’s increasing energy appetite | OHIO Today</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_AI">Generative AI - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GenAI`, `#energy consumption`, `#sustainability`, `#environmental impact`

---

<a id="item-21"></a>
## [Anthropic SDK Python v0.116.0 新增 Agent Memory Beta 标头](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.116.0) ⭐️ 6.0/10

Anthropic 发布了其 Python SDK 的 0.116.0 版本，新增了用于 Agent Memory API 的 Beta 标头，具体为 'agent-memory-2026-07-22'。 此更新使开发者能够访问实验性的 Agent Memory 功能，使代理能够跨对话保留信息，这对于构建更具上下文感知和持久性的 AI 应用至关重要。 使用 Agent Memory API 需要此 Beta 标头，该 API 目前处于 Beta 阶段，可能会发生变化。Memory 工具在 Claude 4 及更高版本上无需 Beta 标头即可使用，但用于更高级内存管理的 Agent Memory API 则需要此标头。

github · stainless-app[bot] · Jul 2, 19:07

**背景**: Anthropic API 中的 Beta 标头允许开发者在功能成为标准 API 之前访问实验性功能。Agent Memory API 旨在为 AI 代理提供跨会话的持久内存，提高其处理长时间运行任务和保持上下文的能力。这是 Anthropic 在 2025 年 10 月推出 Claude Skills 后，增强代理能力的更广泛努力的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/api/beta-headers">Beta headers - Claude Platform Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool">Memory tool - Claude Platform Docs</a></li>
<li><a href="https://aiwiki.ai/wiki/anthropic_api">Anthropic API | AI Wiki</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SDK`, `#Python`, `#API`

---

<a id="item-22"></a>
## [Exapunks：回顾 Zachtronics 的编程解谜游戏](https://www.zachtronics.com/exapunks/) ⭐️ 6.0/10

一篇 Hacker News 帖子讨论了 2018 年的编程解谜游戏 Exapunks，强调了其设计和社区赞赏，同时更新了创作者的新工作室 Coincidence Games 及其最新游戏 UVS Nirmana 的信息。 Exapunks 是编程解谜爱好者钟爱的作品，讨论反映了 Zachtronics 游戏对学习底层编程概念的持久影响。提及创作者的新项目表明该类型游戏仍在持续创新。 Exapunks 于 2018 年 8 月 9 日进入抢先体验，2018 年 10 月 22 日完整发布。游戏包含一个名为 Axiom VirtualNetwork+的自定义谜题创建工具，使用 JavaScript 定义主机、文件和寄存器。

hackernews · yu3zhou4 · Jul 2, 18:41 · [社区讨论](https://news.ycombinator.com/item?id=48765663)

**背景**: Exapunks 是 Zachtronics 开发的一款编程解谜游戏，该工作室以 TIS-100 和 Shenzhen I/O 等工程类解谜游戏闻名。玩家编写类似汇编的代码来入侵虚拟网络，通过控制 EXA（可执行代理）解决谜题。游戏设定在赛博朋克世界中，玩家通过阅读虚构杂志获取教程和背景故事。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exapunks">Exapunks - Wikipedia</a></li>
<li><a href="https://www.zachtronics.com/exapunks/">EXAPUNKS - Zachtronics</a></li>
<li><a href="https://store.steampowered.com/app/716490/EXAPUNKS/">Save 50% on EXAPUNKS on Steam Exapunks - Wikipedia EXAPUNKS - Zachtronics EXAPUNKS by Zachtronics Steam Community :: Guide :: Dan's Exapunks Solutions -50% EXAPUNKS on GOG.com Exapunks Review - by Felix Roth - Corerunner</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Exapunks 和 Shenzhen I/O 捕捉到了编程的乐趣，其中一位指出预先优化解决方案是徒劳的。另一位用户分享说 Exapunks 和 TIS-100 通过揭开汇编语言的神秘面纱影响了他们的职业发展。还有评论指出 Zachtronics 创始人 Zach Barth 现在在 Coincidence Games，该公司发布了航天器工程解谜游戏 UVS Nirmana。

**标签**: `#gaming`, `#programming`, `#puzzle`, `#zachtronics`

---

<a id="item-23"></a>
## [AI 从聊天机器人转向关键工业基础设施](https://www.technologyreview.com/2026/07/02/1138433/teaching-ai-to-run-with-the-turbines/) ⭐️ 6.0/10

《麻省理工科技评论》的一篇文章指出，AI 正越来越多地部署在工业环境中，用于保障运营连续性和安全性，其应用已超越聊天机器人和图像生成器等消费级场景。 这一转变表明 AI 在关键基础设施中的作用日益增强——此类设施的故障可能造成严重后果，同时也标志着 AI 正从炒作走向高风险运营技术领域的成熟应用。 文章讨论了 AI 如何在拥有庞大物理系统的行业中成为核心运营层，但未提供具体技术细节或案例研究。

rss · MIT Technology Review · Jul 2, 12:51

**背景**: 运营技术（OT）是指用于监控和控制能源、制造、交通等行业物理设备与流程的硬件和软件。将 AI 集成到 OT 中旨在提高效率、实现预测性维护并增强安全性，但同时也带来了新的网络安全挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/02/1140045/achieving-operational-excellence-with-ai/">Achieving operational excellence with AI - MIT Technology Review</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-cybersecurity-operational-technology-industrial-control-systems/">NVIDIA Brings AI-Powered Cybersecurity to World’s Critical Infrastructure | NVIDIA Blog</a></li>

</ul>
</details>

**标签**: `#AI`, `#industrial AI`, `#infrastructure`, `#operational technology`

---

<a id="item-24"></a>
## [初创公司 Springboards 用 Flint LLM 应对 AI 群体思维](https://www.technologyreview.com/2026/07/02/1140027/the-download-ai-groupthink-llms/) ⭐️ 6.0/10

澳大利亚初创公司 Springboards 开发了一款名为 Flint 的大语言模型，该模型经过训练，能够对开放式问题产生更多样化的回答，以解决主流大语言模型（如 ChatGPT、Claude 和 Gemini）给出惊人相似答案的群体思维问题。 这很重要，因为 AI 群体思维限制了在头脑风暴、旅行规划和创意写作等应用中的创造性和实用性，而解决方案可以恢复输出的多样性并增强用户对 LLM 的信任。 Flint 经过专门训练，能够对诸如“我应该去欧洲哪里？”和“给我一个 1 到 10 之间的随机数”等开放式提示产生更多样化的回答，而主流 LLM 通常默认给出相同的答案（例如“7”）。

rss · MIT Technology Review · Jul 2, 12:10

**背景**: 大语言模型（如 GPT-4、Claude 和 Gemini）在海量互联网数据上训练，由于共同的训练数据和基于人类反馈的强化学习（RLHF），可能导致回答趋同。这种“群体思维”效应降低了输出的多样性，尤其是在开放式问题上。初创公司 Springboards 旨在通过训练 Flint 优先考虑多样性来打破这种模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/01/1140003/llms-are-stuck-in-a-groupthink-rut-this-startup-is-trying-to-get-them-out/">LLMs are stuck in a groupthink groove. This startup is trying ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#LLMs`, `#startup`, `#groupthink`

---

<a id="item-25"></a>
## [分析师预测清洁能源税收抵免到期将推高 PPA 价格](https://www.utilitydive.com/news/rising-ppa-prices-anticipated-as-clean-energy-tax-credits-phase-out/824386/) ⭐️ 6.0/10

据 Utility Dive 报道，分析师预计随着清洁能源税收抵免逐步取消，购电协议（PPA）价格将上涨。Crux 的 Josh Price 指出，缺失的税收抵免收入可能会通过更高的 PPA 价格来弥补。 这一变化可能会增加可再生能源的企业和公用事业买家的成本，可能减缓清洁能源的采用。这凸显了政策变化对可再生能源市场的经济影响。 逐步取消包括 2024 年后清洁电力投资税收抵免取代能源投资税收抵免，住宅抵免从 2033 年开始逐步取消。PPA 是发电方与客户之间通常持续 10-25 年的长期合同。

rss · Utility Dive · Jul 2, 17:17

**背景**: 购电协议（PPA）是发电方与客户（如公用事业公司或企业）之间以预先协商价格购买电力的长期合同。清洁能源税收抵免（如投资税收抵免）历来降低了项目成本，其逐步取消将移除这一财务激励，可能推高 PPA 价格。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Power_purchase_agreement">Power purchase agreement - Wikipedia</a></li>
<li><a href="https://www.irs.gov/credits-deductions/residential-clean-energy-credit">Residential Clean Energy Credit | Internal Revenue Service</a></li>

</ul>
</details>

**标签**: `#clean energy`, `#PPA`, `#tax credits`, `#renewable energy`

---

<a id="item-26"></a>
## [工会工作者为被裁游戏开发者设立困难基金](https://www.gamedeveloper.com/business/union-workers-establish-hardship-fund-to-support-devs-impacted-by-layoffs) ⭐️ 6.0/10

工会工作者设立了一项困难基金，为美国和加拿大受裁员影响的游戏开发者提供高达 5000 美元的资助。 这一举措为面临失业的游戏开发者提供了直接的经济援助，回应了受大规模裁员冲击的行业中的迫切需求。 该基金面向美国和加拿大的游戏开发者，每位符合条件的个人可申请高达 5000 美元。

rss · Game Developer (Gamasutra) · Jul 2, 10:20

**背景**: 近年来，游戏开发行业经历了大规模裁员，许多工作者缺乏经济支持。工会组织的困难基金是在危机期间向成员提供紧急援助的常见方式。

**标签**: `#game development`, `#layoffs`, `#union`, `#hardship fund`

---