---
layout: default
title: "Horizon Summary: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
---

> From 137 items, 27 important content pieces were selected

---

1. [微软画图和照片应用对 AI 编辑图片隐形添加 GUID 水印](#item-1) ⭐️ 8.0/10
2. [IPFS 维护团队在 Shipyard 逐步收尾，项目继续](#item-2) ⭐️ 8.0/10
3. [seL4 在 AArch64 上的安全证明完成](#item-3) ⭐️ 8.0/10
4. [AI 编码工具可能削弱人类编码专业知识](#item-4) ⭐️ 8.0/10
5. [将可执行文件作为 SQLite 数据库：一种新颖方法](#item-5) ⭐️ 8.0/10
6. [FDA 批准阿尔茨海默病血液检测](#item-6) ⭐️ 8.0/10
7. [儿童在语言学习上胜过 AI，原因成谜](#item-7) ⭐️ 8.0/10
8. [小米新 CPU 单核追平苹果，多核性能超越](#item-8) ⭐️ 7.0/10
9. [整个旧金山被重制为可玩的网页游戏](#item-9) ⭐️ 7.0/10
10. [欧盟法规威胁创客与微型企业家](#item-10) ⭐️ 7.0/10
11. [海洋温度创历史新高，预示气候变化加速](#item-11) ⭐️ 7.0/10
12. [XMPP 庆祝数字独立 25 周年](#item-12) ⭐️ 7.0/10
13. [OpenAI 暂时下调 GPT-5.6 Sol 价格](#item-13) ⭐️ 7.0/10
14. [单文件 HTML 电子音乐机，渲染可验证](#item-14) ⭐️ 7.0/10
15. [自动驾驶出租车扩张，但监管阻力增大](#item-15) ⭐️ 7.0/10
16. [AliExpress 被曝使用听不见的超声波进行浏览器指纹识别](#item-16) ⭐️ 7.0/10
17. [英伟达经理因向中国走私 AI 服务器被起诉](#item-17) ⭐️ 7.0/10
18. [联邦聚变系统获 10 亿美元资金以完成 SPARC 反应堆](#item-18) ⭐️ 7.0/10
19. [Twitch 因未经同意使用用户数据训练亚马逊 AI 面临集体诉讼](#item-19) ⭐️ 7.0/10
20. [3D 打印枪械创作者声称已找到绕过屏蔽软件的方法](#item-20) ⭐️ 6.0/10
21. [Netflix 或向 Peacock 和 Fox One 等竞争对手开放应用](#item-21) ⭐️ 6.0/10
22. [GrapheneOS 明年将支持摩托罗拉手机，包括折叠屏](#item-22) ⭐️ 6.0/10
23. [微软与 PowerHouse Hillwood 就数据中心协议与公用事业公司发生纠纷](#item-23) ⭐️ 6.0/10
24. [亚利桑那州电网电池热潮能否持续？](#item-24) ⭐️ 6.0/10
25. [PJM 批准清洁能源项目但面临建设挑战](#item-25) ⭐️ 6.0/10
26. [GPU 供应危机迫在眉睫，价格预计上涨](#item-26) ⭐️ 6.0/10
27. [Nightdive 的《神偷》重制版发现过时的代码仓库](#item-27) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [微软画图和照片应用对 AI 编辑图片隐形添加 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软画图和照片应用现在会在经过 AI 处理的图片中嵌入不可见的 GUID 水印，即使 AI 处理是在设备本地进行的。该水印在后台静默添加，用户无法察觉，也无法关闭。 这种隐藏水印引发了重大的隐私和匿名性担忧，因为它使微软能够将任何 AI 编辑过的图片追溯到用户账户，可能通过法律请求泄露个人信息。这也影响了依赖在线匿名分享图片的内容创作者和用户。 即使在 Copilot+ PC 上使用本地 AI 模型，水印也会被嵌入，但提示词审核仍然在远程进行。目前尚不清楚水印是适用于所有 AI 辅助编辑（如背景移除），还是仅适用于图像生成等特定功能。

hackernews · ComputerGuru · Aug 24, 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: 水印是一种将元数据或标识符嵌入数字内容以确立所有权或来源的技术。隐形水印设计为人类不可感知，但可以通过软件检测。微软一直在将 AI 功能集成到其内置应用中，这一发现揭示了它还在添加隐藏的追踪机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs ... :: Xusheng Li</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了震惊和担忧，一些人认为 AI 方面是转移注意力的，真正的问题是隐藏的唯一标识符可能被用来去匿名化用户。其他人指出微软在实施上的草率历史，例如错误地为 Azure DevOps 提交添加水印，并建议在使用此类应用时保持谨慎。

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#security`

---

<a id="item-2"></a>
## [IPFS 维护团队在 Shipyard 逐步收尾，项目继续](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 8.0/10

Shipyard 的 IPFS 维护团队宣布逐步收尾，从集中的实现支持转向个人维护者资助。这标志着 IPFS 开发资金和组织方式的转变。 这一变化标志着去中心化存储生态系统的重大转变，因为一个关键的维护团队退出。这引发了对 IPFS 长期可持续性和治理的质疑，影响依赖该协议的开发者和项目。 IPFS 项目本身并未关闭，只是 Shipyard 团队在收尾。个人维护者资助将取代集中支持，IPFS 资助平台正用于资助集成和新实现。

hackernews · iand · Aug 24, 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49421489)

**背景**: IPFS（星际文件系统）是一种用于去中心化文件存储和共享的点对点超媒体协议。Shipyard 是一个独立的工程集体，曾担任 IPFS 和 libp2p 实现的核心维护者。向个人资助的转变反映了开源治理中向去中心化资金模式发展的更广泛趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ipshipyard.com/">We are the core maintainers of IPFS , libp2p, and other foundational...</a></li>
<li><a href="https://blog.ipfs.tech/shipyard-hello-world/">IPFS & libp2p Devs Go Independent: Meet Interplanetary Shipyard</a></li>
<li><a href="https://github.com/ipfs/devgrants">GitHub - ipfs/devgrants: The IPFS Grant platform connects funding organizations with builders and researchers in the IPFS community. · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论澄清该公告是关于 Shipyard 而非 IPFS 本身，并表达了复杂情绪。一些人建议替代方案如 Iroh，另一些人则批评项目方向，如对 IPNS 的重视以及使用 Google 表单收集反馈。

**标签**: `#IPFS`, `#decentralized storage`, `#open source`, `#maintenance`, `#community`

---

<a id="item-3"></a>
## [seL4 在 AArch64 上的安全证明完成](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核的安全证明现已针对 AArch64 架构完成，标志着形式化验证操作系统领域的一个重要里程碑。这一成就将 seL4 已验证的安全属性扩展到了广泛使用的 64 位 ARM 架构上。 这一成果意义重大，因为 AArch64 是现代移动和嵌入式设备的基础，在此架构上拥有经过形式化验证的内核可增强关键系统的安全保障。它可能影响汽车、航空航天等高度重视形式化验证的安全关键行业的采用。 根据细则，这些证明仅限于非 MCS（混合关键性系统）和单核配置。这意味着已验证的安全属性尚未涵盖多核或混合关键性场景，而这些在现实部署中很常见。

hackernews · snvzz · Aug 24, 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**背景**: seL4 是一个以形式化验证著称的微内核，其正确性通过数学方式对照规范得到证明。操作系统内核的形式化验证涉及证明实现与高层规范相匹配，通常细化到 C 代码级别，并假定编译器、汇编代码和硬件是正确的。AArch64，也称为 ARM64，是 ARM 架构的 64 位执行状态，随 ARMv8-A 引入，广泛用于移动和嵌入式系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dl.acm.org/doi/10.1145/1629575.1629596">seL4 | Proceedings of the ACM SIGOPS 22nd symposium on Operating systems principles</a></li>
<li><a href="https://sel4.systems/Research/pdfs/comprehensive-formal-verification-os-microkernel.pdf">Comprehensive Formal Verification of an OS Microkernel</a></li>
<li><a href="https://en.wikipedia.org/wiki/AArch64">AArch64 - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区评论对实际影响表示怀疑，一位用户开玩笑说侧信道定时攻击很快就会使该结果失效，另一位则指出了其局限性（非 MCS、单核）。其他人讨论了 seL4 的采用情况，提到其在 GenodeOS、LionsOS 以及一家中国汽车制造商作为虚拟机监控程序的使用，同时质疑如果没有原生 seL4/Linux，它能否真正提高安全性。

**标签**: `#seL4`, `#formal verification`, `#AArch64`, `#security`, `#operating systems`

---

<a id="item-4"></a>
## [AI 编码工具可能削弱人类编码专业知识](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) ⭐️ 8.0/10

一篇文章认为，对 AI 编码工具的依赖将导致人类编码专业知识的崩溃，并在 Hacker News 上引发了 392 条评论的讨论。作者认为，在没有深入理解的情况下无节制地生成代码，会对软件质量和开发者的技能发展构成风险。 这很重要，因为它凸显了现代软件工程中的一个关键矛盾：AI 编码工具带来的生产力提升可能以牺牲开发者的长期专业知识和代码质量为代价。随着 AI 生成代码的普及，行业必须解决技能可能退化以及代码审查负担加重的问题。 文章和评论强调了刻意练习对技能形成的重要性，与 AI 带来的无摩擦编码形成对比。社区成员指出，工程师生成代码的速度超过了人类审查的能力，而且 AI 生成的代码往往缺乏安全最佳实践，这一点得到了近期研究的支持。

hackernews · larsfaye · Aug 24, 15:52 · [社区讨论](https://news.ycombinator.com/item?id=49421554)

**背景**: AI 编码工具，如 GitHub Copilot 和 ChatGPT，使用大型语言模型（LLM）从自然语言提示生成代码。虽然这些工具提高了生产力，但也带来了风险：研究表明，LLM 生成的代码可能不安全，过度依赖可能阻碍深层专业知识的培养。刻意练习是心理学中的一个概念，对于掌握软件工程等复杂技能至关重要，但 AI 工具可能减少了驱动这种练习的摩擦。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.20612">[2504.20612] The Hidden Risks of LLM-Generated Web Application Code: A Security-Centric Evaluation of Code Generation Capabilities in Large Language Models</a></li>
<li><a href="https://www.darkreading.com/application-security/llms-ai-generated-code-wildly-insecure">LLMs' AI-Generated Code Remains Wildly Insecure</a></li>
<li><a href="https://medium.com/@yotammanor/deliberate-practice-for-software-engineers-e7f1f65bbf2b">Deliberate Practice For Software Engineers | by Yotam Manor | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区讨论强烈赞同文章的观点，用户们分享了对企业强制使用 AI 的担忧、审查 AI 生成代码的困难以及开发者技能可能退化的忧虑。一些评论者建议使用 AI 来提问以确保理解，而另一些人则担心当前趋势的可持续性。

**标签**: `#AI coding`, `#software engineering`, `#expertise`, `#LLM`, `#code review`

---

<a id="item-5"></a>
## [将可执行文件作为 SQLite 数据库：一种新颖方法](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) ⭐️ 8.0/10

文章提出将 SQLite 数据库嵌入可执行文件中，使二进制文件具有自描述性和可内省性。这样可以通过 SQL 查询和操作可执行文件，利用 SQLite 的虚拟表机制。 这一概念可能改变软件分发和二进制分析，通过实现对可执行文件的强大内省和修改能力。它可能带来更高效的打包格式以及新的调试和逆向工程能力，可能影响开发者和安全研究人员与二进制文件的交互方式。 该方法利用 SQLite 的虚拟表功能，将可执行文件的结构“挂载”为可查询的数据库。它还强调了 SQLite 动态链接与 ELF 动态链接之间的兼容性，暗示有可能用更高效的格式取代 AppImage。

hackernews · setheron · Aug 24, 04:48 · [社区讨论](https://news.ycombinator.com/item?id=49415271)

**背景**: ELF（可执行和可链接格式）是类 Unix 系统上可执行文件和共享库的标准文件格式。它将数据组织成节和段，但缺乏自描述模式。SQLite 是一个轻量级的嵌入式 SQL 数据库引擎，支持虚拟表，允许将外部数据源作为表进行查询。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Executable_and_Linkable_Format">Executable and Linkable Format - Wikipedia</a></li>
<li><a href="https://sqlite.org/forum/forumpost/c37eaeff51">SQLite User Forum: Thoughts on Compiling SQLite Database into Executable?</a></li>
<li><a href="https://mysticmind.dev/how-to-use-sqlite-db-as-an-embedded-resource-in-net/">How to use SQLite db as an embedded resource in .NET | MysticMind.dev</a></li>

</ul>
</details>

**社区讨论**: 社区反应热烈，评论称赞这一想法并指出其潜力。一些人讨论更广泛的概念，即所有数据都是数据库，而另一些人则指出实际应用，如自修改的 Lisp 镜像和取代 AppImage。作者指出学术界的反馈不太友好，但 Hacker News 的受众更为接受。

**标签**: `#SQLite`, `#Executables`, `#ELF`, `#Software Engineering`, `#Innovation`

---

<a id="item-6"></a>
## [FDA 批准阿尔茨海默病血液检测](https://medicine.washu.edu/news/fda-clears-blood-test-to-aid-evaluation-for-alzheimers-disease/) ⭐️ 8.0/10

FDA 已批准基于 p-tau217 生物标志物的血液检测 PrecivityAD2，用于辅助阿尔茨海默病的评估。这一批准标志着血液生物标志物在常规临床诊断中的应用迈出了重要一步。 这一批准可能改变诊断模式，使阿尔茨海默病的评估创伤更小、更易获得。它可能促进早期发现和更好的疾病管理，并可能减少对昂贵的 PET 扫描或腰椎穿刺的需求。 PrecivityAD2 的定价约为 1400-1500 美元，高于其他价格在 200-300 美元的 p-tau217 检测。该测试适用于轻度认知障碍或痴呆患者，据报道其准确率约为 90%。

hackernews · dabinat · Aug 24, 06:30 · [社区讨论](https://news.ycombinator.com/item?id=49415893)

**背景**: 阿尔茨海默病是一种进行性神经退行性疾病，其特征是大脑中的淀粉样斑块和 tau 蛋白缠结。传统上，诊断依赖于临床评估、认知测试和影像学检查，但像 p-tau217 这样的血液生物标志物提供了一种创伤更小、更可扩展的替代方案。p-tau217 是磷酸化 tau 蛋白片段，与淀粉样病理和认知衰退相关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11351463/">P - tau 217 as a Reliable Blood-Based Marker of Alzheimer ’ s Disease ...</a></li>
<li><a href="https://www.qml.com.au/tests/precivityad2">Alzheimer’s disease and PrecivityAD 2 ™ blood test | QML Pathology</a></li>
<li><a href="https://www.mayocliniclabs.com/api/sitecore/TestCatalog/DownloadTestCatalog?testId=621652">Test Definition: C2AD2</a></li>

</ul>
</details>

**社区讨论**: 社区评论既表达了热情也提出了担忧。一些人指出 PrecivityAD2 与其他 p-tau217 检测相比价格较高，质疑其作为筛查工具的成本效益。其他人询问检测阳性者的干预策略，还有一位从业者表示愿意回答关于数字认知测试与 p-tau 血液检测结合使用的问题。

**标签**: `#Alzheimer's`, `#biomarker`, `#FDA`, `#diagnostics`, `#health tech`

---

<a id="item-7"></a>
## [儿童在语言学习上胜过 AI，原因成谜](https://www.technologyreview.com/2026/08/24/1141740/kids-machines-language-learning/) ⭐️ 8.0/10

文章指出，尽管像 ChatGPT 这样的大型语言模型发展迅速，儿童在语言学习上仍然胜过 AI，而原因尚不清楚。文章强调，只有人类儿童和现在的 AI 模型能够流利掌握人类语言，但两者的机制差异显著。 这很重要，因为理解儿童为何比 AI 更高效地学习语言，可能会在 AI 发展和认知科学领域带来突破。它挑战了当前通过增加数据来扩展模型的范式，并表明需要探索学习机制的根本差异。 文章指出，ChatGPT 发布仅四年，AI 已经达到了与人类相当的语言流利度，但儿童仍然用更少的数据、更高效地学习。文章提出了一个问题：联想学习或其他机制是否在人类语言习得中扮演更重要的角色，正如最近的研究所暗示的那样。

rss · MIT Technology Review · Aug 24, 09:00

**背景**: 语言习得一直是认知科学的核心话题，先天论和经验论之间存在争论。大型语言模型（LLM）从海量文本数据中学习，而儿童则从有限的互动经验中学习。最近的研究，如 Neuroscience News 和 ACL 的研究，探讨了如何将 AI 学习与儿童式体验对齐以提高效率，但根本差距仍然存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://plato.stanford.edu/entries/innateness-language/llms.html">Innateness and Language > A. Innateness and ( Large ) Language ...</a></li>
<li><a href="https://neurosciencenews.com/ai-child-language-25551/">AI Learns Language Like a Child - Neuroscience News</a></li>
<li><a href="https://aclanthology.org/2026.acl-long.895/">Language Acquisition Device in Large Language Models</a></li>

</ul>
</details>

**标签**: `#AI`, `#language learning`, `#cognitive science`, `#LLMs`, `#child development`

---

<a id="item-8"></a>
## [小米新 CPU 单核追平苹果，多核性能超越](https://twitter.com/lemire/status/2091894299289874926) ⭐️ 7.0/10

据泄露的 Geekbench 分数，小米新款 CPU XRing O3 在单线程性能上追平苹果最新核心，并在多线程负载上显著超越。 这标志着小米进军高端智能手机芯片市场，可能打破高通和联发科的垄断地位。作为全球第三大智能手机制造商，小米的自研芯片可能重塑竞争格局，给现有供应商带来压力。 XRing O3 据称是基于 ARM 的芯片，可能与联发科天玑 9500 中的 C1-Ultra 有关。然而，由于智能手机中的散热和功耗限制，实际性能可能较低，类似芯片已出现这种情况。

hackernews · tosh · Aug 24, 15:08 · [社区讨论](https://news.ycombinator.com/item?id=49420873)

**背景**: 单线程性能衡量 CPU 处理单个任务的速度，而多线程性能利用多个核心。苹果自研的 ARM 芯片长期以来在效率和性能上领先。小米进入芯片设计领域可能减少对外部供应商的依赖，并获得成本优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nanoreview.net/en/soc/xiaomi-xring-o1">Xiaomi Xring O1: specs and benchmarks</a></li>
<li><a href="https://www.cpubenchmark.net/singleThread.html">cpubenchmark.net/singleThread.html</a></li>
<li><a href="https://en.wikipedia.org/wiki/Multithreading_(computer_architecture)">Multithreading ( computer architecture) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者强调功耗效率是最关键但缺失的指标，指出没有效率的高性能在手机中毫无用处。有人指出该芯片可能与联发科类似，实际结果往往低于实验室测试。其他人则认为这对高通和联发科构成威胁。

**标签**: `#CPU`, `#Xiaomi`, `#Apple`, `#ARM`, `#semiconductors`

---

<a id="item-9"></a>
## [整个旧金山被重制为可玩的网页游戏](https://sf.thijs.gg/) ⭐️ 7.0/10

一个基于网页的游戏已发布，它利用 GIS 数据和程序化生成技术，将整个旧金山重建为可玩的 3D 环境。该项目托管在 sf.thijs.gg，允许用户在浏览器中探索这座城市。 该项目展示了利用公开数据和现代网络技术创建大规模、逼真城市模拟的可行性。它可能激发其他城市的类似项目，并推动程序化城市生成领域的发展，在游戏、城市规划和教育等方面具有潜在应用。 该游戏基于 GIS 数据构建，并使用程序化生成来填充建筑物和其他特征。它完全在浏览器中运行，虽然包含一些交互元素如驾驶和收集硬币，但主要是一种探索体验。该项目在新闻聚合器上引起了广泛关注，获得了 92 条评论和 272 个点赞。

hackernews · centrosphere · Aug 24, 17:05 · [社区讨论](https://news.ycombinator.com/item?id=49422784)

**背景**: 程序化城市生成是计算机图形学和游戏设计中用于通过算法自动创建城市环境的一种计算技术。基于网页的 3D 城市渲染已利用 OpenStreetMap 等数据源进行过探索，如学术研究所示。该项目利用了类似的概念，但将其应用于真实城市，为用户创造了沉浸式且情感共鸣的体验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://proceduralworldlab.com/procedural-city-generator/">Procedural City Generator | Procedural World Lab | Premium...</a></li>
<li><a href="https://www.semanticscholar.org/paper/Generating-web-based-3D-City-Models-from-The-in-Over-Schilling/ffdf3f958fe09db96e7562c14d4202e7021726d7">Generating web - based 3 D City Models from... | Semantic Scholar</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映出强烈的热情和个人情感联系，一位在旧金山生活了 20 年的用户表示这让他很感动。另一位用户分享了费城的类似项目，其他人则讨论了技术方面，如使用街景数据和潜在改进，例如添加街道名称或 MMO 模式。一些用户还质疑页面底部的 Apple 版权和服务条款。

**标签**: `#GIS`, `#procedural generation`, `#web game`, `#3D rendering`, `#city modeling`

---

<a id="item-10"></a>
## [欧盟法规威胁创客与微型企业家](https://lectronz.com/u/lectronz/articles/how-europe-is-killing-makers-and-micro-entrepreneurs) ⭐️ 7.0/10

一篇观点文章认为，欧盟最近关于产品包装和标签的法规对小型创客和微型企业家造成了不成比例的伤害，可能迫使许多人停业。这篇文章在 Hacker News 上引发了大量讨论，获得了 954 分和 605 条评论。 这很重要，因为旨在针对大公司的欧盟法规可能无意中扼杀小企业和个人创作者，减少创新和经济多样性。讨论凸显了欧洲监管合规与创客运动之间日益紧张的矛盾。 文章特别批评了欧盟的《包装和包装废弃物法规》（PPWR）和《通用产品安全法规》（GPSR），这些法规要求详细的标签和注册。评论者指出，微型企业和通用包装有豁免，但各成员国实施不一致且复杂性仍然是个问题。

hackernews · l-one-lone · Aug 24, 13:05 · [社区讨论](https://news.ycombinator.com/item?id=49419237)

**背景**: 欧盟一直在更新产品安全和包装法规，以减少浪费并保护消费者，但这些规则通常假设是大规模生产者。销售手工或小批量商品的小型创客和微型企业家可能缺乏资源来满足复杂的行政要求。这场辩论反映了关于监管对数字时代小企业影响的更广泛担忧。

**社区讨论**: 社区讨论意见不一：一些评论者捍卫欧盟法规，指出微型企业和通用包装有豁免，而另一些人则批评各成员国实施不一致以及给小企业带来的负担。一位评论者指出，欧盟委员会曾希望建立中央登记处，但成员国阻止了，欧盟现在建议在修正完成前不要执行。

**标签**: `#EU regulation`, `#makers`, `#micro-entrepreneurs`, `#e-commerce`, `#policy`

---

<a id="item-11"></a>
## [海洋温度创历史新高，预示气候变化加速](https://www.bbc.com/news/articles/c62m4gpnp78o) ⭐️ 7.0/10

据最新报告，全球海洋温度已达到有记录以来的最高值。这一里程碑事件凸显了气候变化对海洋环境日益加剧的影响。 这一纪录是全球变暖的关键指标，对海洋生态系统、天气模式以及全球沿海社区具有深远影响。它凸显了采取政策行动减缓气候变化的紧迫性。 2024 年观测到的海洋温度创下纪录，海洋热含量达到前所未有的水平。科学家指出，持续的厄尔尼诺现象可能在未来几个月进一步推高温度。

hackernews · tcp_handshaker · Aug 24, 19:19 · [社区讨论](https://news.ycombinator.com/item?id=49424606)

**背景**: 海洋温度是气候变化的关键指标，因为海洋吸收了温室气体排放产生的 90%以上的多余热量。海洋温度上升可能导致珊瑚白化、海平面上升和更强烈的风暴。最近的纪录是人类活动导致的长期变暖趋势的一部分。

**社区讨论**: 社区评论表达了对政府不作为的担忧，并强调了海洋升温的科学细节，如融冰的作用。一些用户分享了更深入理解的额外资源，而另一些用户则强调即使是小幅升温的严重性。

**标签**: `#climate change`, `#ocean temperature`, `#environment`, `#science`, `#policy`

---

<a id="item-12"></a>
## [XMPP 庆祝数字独立 25 周年](https://gultsch.de/posts/25-years-of-digital-independence/) ⭐️ 7.0/10

Daniel Gultsch 发表了一篇关于 XMPP 25 年遗产的反思文章，强调其在数字独立和当前生态系统中的作用。该文章引发了社区关于 XMPP 与 Matrix 比较的讨论。 这一里程碑凸显了 XMPP 在去中心化通信中的持久相关性，与集中式平台形成对比。讨论凸显了社区对开放标准的持续兴趣，以及 XMPP 与 Matrix 等新协议之间的权衡。 文章提到了 XMPP 的历史及其当前生态系统，包括 Movim 和 Fluux 等项目。社区评论提到了 jmp.chat、Dino、Cheogram 和 Prosody，表明其活跃的使用和开发。

hackernews · inputmice · Aug 24, 15:51 · [社区讨论](https://news.ycombinator.com/item?id=49421536)

**背景**: XMPP（可扩展消息与存在协议）是一种用于实时消息和存在的开放标准，用于即时通讯和 VoIP。25 年来，它一直是去中心化通信的基础，拥有 Prosody 等服务器和 Dino 等客户端。Matrix 是一种较新的联合协议，已获得普及，但经常与 XMPP 在复杂性和供应商锁定方面进行比较。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gultsch.de/posts/25-years-of-digital-independence/">Daniel Gultsch | Jabber/ XMPP : 25 Years of Digital Independence</a></li>
<li><a href="https://lukesmith.xyz/articles/matrix-vs-xmpp/">Matrix vs . XMPP | Luke Smith</a></li>
<li><a href="https://selfhosting.sh/compare/matrix-vs-xmpp/">Matrix vs XMPP : Federated Chat Protocols Compared | selfhosting.sh</a></li>

</ul>
</details>

**社区讨论**: 社区对 XMPP 的情绪总体积极，用户对其未来表示希望，并对 Matrix 的分道扬镳表示遗憾。一些用户指出客户端质量与 Telegram 相比存在问题，而另一些用户则分享了成功迁移到基于 XMPP 服务的经验。还有人对仍然使用 XMPP 的大型社区感到好奇。

**标签**: `#XMPP`, `#decentralization`, `#messaging`, `#open standards`, `#community`

---

<a id="item-13"></a>
## [OpenAI 暂时下调 GPT-5.6 Sol 价格](https://developers.openai.com/api/docs/pricing) ⭐️ 7.0/10

OpenAI 宣布暂时下调其 GPT-5.6 Sol 模型的价格，输入价格降低 20%，输出价格降低 33%，有效期至少到 2026 年 11 月 21 日。新价格为每 100 万输入 token 4.00 美元，每 100 万输出 token 20.00 美元。 此次降价标志着 AI 模型市场竞争加剧，各提供商竞相提供更实惠的智能服务。这可能加速 AI 模型的商品化，使依赖 API 访问的开发者与企业受益。 修订后的定价还包括其他模型的降价：GPT-5.6 Terra 降至每 100 万输入 token 2.00 美元、输出 12.00 美元；GPT-5.6 Luna 降至每 100 万输入 token 0.20 美元、输出 1.20 美元。折扣同样适用于缓存输入和缓存写入，并且通过 OpenRouter 等第三方提供商可能还有额外折扣。

hackernews · tosh · Aug 24, 15:22 · [社区讨论](https://news.ycombinator.com/item?id=49421074)

**背景**: GPT-5.6 Sol 是 OpenAI 的前沿模型之一，以在知识基准测试中的强劲表现著称，拥有 100 万 token 的上下文窗口，并支持文本和图像输入。AI 模型市场正经历快速商品化，开源模型和各家提供商的竞争性定价使得原始模型性能不再成为显著差异化因素。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://benchlm.ai/compare/gemma-4-31b-vs-gpt-5-6-sol">Gemma 4 31B vs GPT - 5 . 6 Sol : Benchmarks, Pricing... | BenchLM.ai</a></li>
<li><a href="https://www.mextalearn.com/blog/chatgpt-5-6-sol">ChatGPT 5 . 6 Sol : Benchmarks, API Pricing, Tools & Review · Mexta</a></li>
<li><a href="https://artificialanalysis.ai/models/gpt-5-6-sol">GPT - 5 . 6 Sol (max) - Intelligence, Performance... | Artificial Analysis</a></li>

</ul>
</details>

**社区讨论**: 社区评论对价格战表示热情，一些人称赞价格的实惠性，并指出开源模型从这种竞争中受益。其他人则强调通过 OpenRouter 还可享受额外 50% 的折扣，使实际成本降至每 100 万 token 2/10 美元，并认为 AI 智能可能演变为一场逐底竞争。一些用户将 OpenAI 的产品与 Anthropic 的产品进行比较，表示更倾向于 OpenAI 的消费者优先策略。

**标签**: `#OpenAI`, `#pricing`, `#AI models`, `#market dynamics`

---

<a id="item-14"></a>
## [单文件 HTML 电子音乐机，渲染可验证](https://ssx360.github.io/rack-02/?src=hn) ⭐️ 7.0/10

一位开发者发布了一款单文件 HTML 电子音乐机，具有可验证的渲染功能，完全离线运行，无需外部依赖。该项目在 Hacker News 上展示并获得高度关注。 这展示了自包含 Web 应用的潜力，提供了便携性和无需安装的易用性。它突显了向极简、无依赖软件发展的趋势，这类软件可在任何地方运行，吸引开发者和音乐爱好者。 该 HTML 文件作为单页应用在本地运行，无外部库、字体或图标，确保功能不会因外部因素而失效。'可验证渲染'可能指可复现的确定性视听输出，但摘要中未提供具体技术细节。

hackernews · ssx360 · Aug 24, 13:17 · [社区讨论](https://news.ycombinator.com/item?id=49419351)

**背景**: 基于 Web 的音乐工具通常依赖外部库和资源，导致脆弱且依赖网络连接。该项目利用 Web Audio API 和 canvas/WebGL 直接在浏览器中生成声音和视觉效果，实现完全自包含的体验。'可验证渲染'的概念可能与产生一致输出的确定性算法有关，这对于创意编码中的可复现性很有价值。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49419351">Show HN: A techno machine in one HTML file , with... | Hacker News</a></li>
<li><a href="https://vk.ru/wall-238001904_3787">Show HN: A techno machine in one HTML file , with verifiable renders...</a></li>
<li><a href="https://github.com/FlashGalatine/timbre-visualizer">FlashGalatine/timbre-visualizer: Streamer.bot-native microphone audio ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论绝大多数是正面的，称赞软件的美观、便携性和完美执行。一些用户表达了功能请求，如更高的 BPM 以用于鼓和贝斯，而一位评论者批评它缺乏原创性，与 ReBirth 等工具相比。

**标签**: `#music`, `#web`, `#creative-coding`, `#html`, `#demo`

---

<a id="item-15"></a>
## [自动驾驶出租车扩张，但监管阻力增大](https://www.theverge.com/transportation/983765/robotaxi-waymo-zoox-tesla-rules-pushback-nhtsa) ⭐️ 7.0/10

自动驾驶出租车服务在美国各地扩张，但监管阻力正在加剧。在纽约，州长凯西·霍楚尔在出租车司机、工会和州议员反对后，撤回了允许在纽约市以外地区运营无人驾驶出租车的提案。 部署与监管之间的这种紧张关系将塑造自动驾驶汽车的未来，影响 Waymo、Zoox 和特斯拉等公司。结果可能决定自动驾驶出租车成为主流的速度，以及它们如何与现有交通系统整合。 提案撤回六个月后，商业无人驾驶服务在纽约仍然是非法的。与此同时，尽管劳工团体试图减缓更广泛的推广，美国自动驾驶出行里程已达到 3.6 亿英里，自动驾驶出租车出行次数达到 2100 万次。

rss · The Verge · Aug 24, 16:42

**背景**: 自动驾驶出租车是在没有人类驾驶员的情况下运营的自动驾驶汽车，提供叫车服务。它们依靠传感器、摄像头和人工智能来导航道路。监管框架仍在演变，联邦和州政府正在就安全标准和责任问题进行辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/transportation/983765/robotaxi-waymo-zoox-tesla-rules-pushback-nhtsa">Robotaxis are real now — so is the pushback | The Verge</a></li>
<li><a href="https://www.thecooldown.com/green-business/autonomous-vehicles-resistance-in-us/">Driverless vehicles hit major milestone as labor groups fight to slow...</a></li>
<li><a href="https://autos.yahoo.com/policy-and-environment/articles/trumps-dot-proposes-rules-driverless-010713359.html">Trump's DOT proposes new rules for driverless vehicles</a></li>

</ul>
</details>

**标签**: `#autonomous vehicles`, `#robotaxis`, `#regulation`, `#transportation`, `#policy`

---

<a id="item-16"></a>
## [AliExpress 被曝使用听不见的超声波进行浏览器指纹识别](https://arstechnica.com/security/2026/08/aliexpress-caught-fingerprinting-visitors-after-sending-inaudible-sounds-to-browsers/) ⭐️ 7.0/10

AliExpress 被发现使用听不见的超声波对访客的浏览器进行指纹识别，这一技术是由研究员 Matthew Callaghan 在加载 AliExpress 首页后，其手机音频在多点连接耳机上停止播放时偶然发现的。 这一事件凸显了一种侵犯隐私的追踪技术，尽管该技术已过时，但仍在大型电商平台中使用，引发了对用户同意以及数字广告生态系统中隐蔽追踪方法持续存在的担忧。 该技术涉及发出人类听不见但附近设备可接收的超声波频率，可能用于跨设备追踪。文章指出，尽管这种方法被认为已过时，但像 AliExpress 这样的大型平台使用它，凸显了监管此类做法的持续挑战。

rss · Ars Technica · Aug 24, 19:19

**背景**: 浏览器指纹识别是一种通过收集浏览器和设备的独特属性（如屏幕分辨率、安装的字体和插件）来识别和跟踪用户的技术。超声波指纹识别是一种更隐蔽的变体，利用听不见的声音来关联附近的设备，从而在用户不知情的情况下实现跨设备追踪。这种方法在 2015 年曾被报道，但其持续使用表明此类侵犯隐私的技术仍然存在。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/08/aliexpress-caught-fingerprinting-visitors-after-sending-inaudible-sounds-to-browsers/">Inaudible sounds used to fingerprint browsers catch... - Ars Technica</a></li>
<li><a href="https://fingerprint.com/blog/browser-fingerprinting-techniques/">Browser Fingerprinting Techniques: 6 Top Methods Explained</a></li>
<li><a href="https://yro.slashdot.org/story/15/11/14/027252/ad-networks-using-inaudible-sound-to-link-phones-tablets-and-other-devices">Ad Networks Using Inaudible Sound To Link Phones... - Slashdot</a></li>

</ul>
</details>

**社区讨论**: 文章的评论表明了一种复杂的情绪：虽然该技术被认为已过时，但其仍在被使用这一事实令人毛骨悚然且担忧。没有提供具体的社区评论，但语气暗示了对隐私侵犯的普遍不安。

**标签**: `#privacy`, `#browser fingerprinting`, `#security`, `#tracking`, `#AliExpress`

---

<a id="item-17"></a>
## [英伟达经理因向中国走私 AI 服务器被起诉](https://arstechnica.com/tech-policy/2026/08/nvidia-senior-manager-linked-to-supermicro-scheme-smuggling-ai-servers-to-china/) ⭐️ 7.0/10

台湾已起诉一名英伟达高级经理，其涉嫌通过超微（Supermicro）向中国走私高端 AI 服务器，此前英伟达 CEO 黄仁勋曾对此表示斥责。此次起诉共涉及九人，其中包括英伟达和超微的员工，他们涉嫌伪造文件以规避美国出口管制。 此案凸显了在放松限制的情况下，美国对先进 AI 技术出口管制执行仍面临挑战。它强调了大型科技公司及其员工在全球 AI 硬件市场中运营时所面临的法律和地缘政治风险。 超微已确认进行了整改，并解雇了与此次事件相关的数名员工。据报道，此次起诉发生在黄仁勋斥责之后，台湾已加强出口管制，以防止先进技术流入中国。

rss · Ars Technica · Aug 24, 16:41

**背景**: 美国出口管制限制向中国出售先进 AI 芯片和服务器，以限制其获得高性能计算能力。尽管这些限制有所放松，但非法出口仍在继续，导致法律行动。台湾（其政府声称独立于中国）也实施了出口管制，以防止先进技术流入中国大陆。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/08/nvidia-senior-manager-linked-to-supermicro-scheme-smuggling-ai-servers-to-china/">Nvidia senior manager linked to Supermicro scheme smuggling AI ...</a></li>
<li><a href="https://www.engadget.com/2242415/taiwan-reportedly-indicted-nvidia-employees-for-exporting-prohibited-ai-servers-to-china/?zsource=yahoo">Taiwan Reportedly Indicted NVIDIA Employees For Exporting ...</a></li>
<li><a href="https://english.aawsat.com/technology/5310438-taiwan-indicts-nine-over-alleged-illegal-export-ai-servers-china">Taiwan Indicts Nine Over Alleged Illegal Export of AI Servers to China</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI hardware`, `#export controls`, `#legal`, `#China`

---

<a id="item-18"></a>
## [联邦聚变系统获 10 亿美元资金以完成 SPARC 反应堆](https://www.utilitydive.com/news/what-a-billion-dollar-funding-means-for-commonwealth-fusion-systems-and-its/828515/) ⭐️ 7.0/10

联邦聚变系统公司已筹集 10 亿美元资金，用于完成其 SPARC 示范反应堆，首席执行官 Bob Mumgaard 表示该反应堆现已完成约 80%。 这一融资里程碑表明投资者对商业聚变能信心十足，可能加速实现净能量聚变装置的进程，开启清洁发电的新时代。 SPARC 是一种紧凑型托卡马克装置，旨在产生比消耗更多的能量，这在聚变装置中尚属首次。该公司正与麻省理工学院等离子体科学与聚变中心合作，反应堆正在马萨诸塞州德文斯建造。

rss · Utility Dive · Aug 24, 15:40

**背景**: 聚变能复制了太阳供能的过程，有望提供几乎无限且清洁的能源。联邦聚变系统公司于 2018 年从麻省理工学院分拆出来，旨在基于 ARC 托卡马克设计建造小型聚变电站，SPARC 是关键示范步骤。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Commonwealth_Fusion_Systems">Commonwealth Fusion Systems - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/SPARC_(tokamak)">SPARC (tokamak) - Wikipedia</a></li>
<li><a href="https://cfs.energy/technology/sparc/">SPARC : Proving commercial fusion energy is possible</a></li>

</ul>
</details>

**标签**: `#fusion energy`, `#funding`, `#clean energy`, `#technology`

---

<a id="item-19"></a>
## [Twitch 因未经同意使用用户数据训练亚马逊 AI 面临集体诉讼](https://www.pcgamer.com/software/ai/twitch-hit-with-class-action-lawsuit-over-amazon-ai-training-twitch-sent-no-email-displayed-no-pop-up-notification-and-made-no-announcement/) ⭐️ 7.0/10

Twitch 因未经明确同意使用用户数据训练亚马逊 AI 而面临集体诉讼，且据透露，该公司选择退出机制是因为“没有人会主动选择加入”。 这起诉讼凸显了业界一个有争议的做法，即公司依赖退出机制来获取 AI 训练数据，这可能侵犯用户隐私和信任。它可能开创法律先例，影响科技巨头如何处理用户数据以进行 AI 开发。 Twitch 的首席产品官承认，选择退出机制是因为“没有人会主动选择加入”，且公司未发送任何电子邮件、弹窗通知或公告。诉讼认为这违反了用户同意要求。

rss · PC Gamer · Aug 24, 11:08

**背景**: 在数据隐私领域，选择加入和选择退出是两种同意机制。选择加入要求在使用数据前获得用户明确同意，而选择退出则默认用户同意，除非用户主动反对。许多公司倾向于选择退出，因为这样可以获得更多数据，但这可能被批评为削弱用户自主权。此案是更广泛的 AI 训练数据伦理讨论的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.termsfeed.com/blog/what-is-opt-out-policy/">Opt - Out Policies Explained: Why They Matter and How... - TermsFeed</a></li>
<li><a href="https://www.robometricsagi.com/blog/ai-policy/the-problem-with-opt-out-consent-mechanisms">ROBOMETRICS® MACHINES - The Problem with Opt - Out Consent ...</a></li>
<li><a href="https://www.newsminimalist.com/articles/twitch-faces-backlash-over-amazon-ai-training-using-user-data-by-default-07c43875">Twitch faces backlash over Amazon AI training using user data by...</a></li>

</ul>
</details>

**社区讨论**: 此新闻未提供社区评论。

**标签**: `#AI`, `#privacy`, `#legal`, `#Twitch`, `#Amazon`

---

<a id="item-20"></a>
## [3D 打印枪械创作者声称已找到绕过屏蔽软件的方法](https://www.theverge.com/tech/983244/3d-printed-guns-hashes-hochul) ⭐️ 6.0/10

首个 3D 打印枪械的创作者科迪·威尔逊声称，他已开发出一种方法，可以绕过政府强制要求安装在 3D 打印机上、用于阻止制造枪械的软件。这标志着监管机构与试图规避此类限制的个人之间猫鼠游戏的开始。 这一进展凸显了执行幽灵枪法规所面临的持续挑战，因为技术变通手段可能削弱法律措施的效果。它强调了在公共安全关切与技术革新及个人权利之间取得平衡的困难。 该变通方法专门针对一些州要求 3D 打印机制造商安装的强制性文件屏蔽软件。尽管许多州对幽灵枪进行监管，但执法难度众所周知，这种新方法旨在打印开始前就阻止，但威尔逊的说法表明此类措施可以被规避。

rss · The Verge · Aug 24, 19:50

**背景**: 幽灵枪是指没有序列号的枪械，通常由零件组装或 3D 打印而成，因此无法追踪，且无需背景调查即可获得。作为回应，一些司法管辖区已要求 3D 打印机制造商在软件中加入阻止打印枪支部件的功能。然而，威尔逊声称的变通方法现在对这一软件的有效性提出了挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/983244/3d-printed-guns-hashes-hochul">The cat-and-mouse game over 3 D - printed guns has begun | The Verge</a></li>
<li><a href="https://www.nytimes.com/2021/04/09/us/politics/ghost-guns-explainer.html">Ghost Guns : What They Are, and Why They Are an Issue Now - The...</a></li>
<li><a href="https://www.npr.org/2018/08/14/638629404/some-3d-printing-companies-are-taking-action-against-gun-blueprints">Some 3 D Printing Companies Are Taking Action Against Gun ... : NPR</a></li>

</ul>
</details>

**标签**: `#3D printing`, `#firearms`, `#regulation`, `#technology policy`, `#security`

---

<a id="item-21"></a>
## [Netflix 或向 Peacock 和 Fox One 等竞争对手开放应用](https://www.theverge.com/streaming/983741/netflix-open-app-peacock-fox-one) ⭐️ 6.0/10

据《纽约时报》报道，Netflix 高管已讨论将 Peacock 和 Fox One 等第三方流媒体服务整合到其应用中的可能性。此举可能允许用户直接在 Netflix 内访问其他提供商的内容，但订阅模式等细节尚不明确。 如果实现，这将标志着流媒体行业的重大转变，使 Netflix 从独立平台转变为聚合平台。这可能重塑消费者的选择和竞争格局，可能导致更整合的流媒体体验，并影响其他服务的内容分发方式。 据报道，讨论主要集中在将 Peacock 和 Fox One 引入 Netflix，但尚不清楚 Netflix 是否会销售这些服务的订阅，或只是将其内容添加到应用中。这遵循了流媒体平台探索捆绑和聚合以减少用户流失并提高参与度的更广泛趋势。

rss · The Verge · Aug 24, 13:47

**背景**: Peacock 是 NBCUniversal 的流媒体服务，提供经典电视节目、电影、当前剧集和原创内容的组合，高级订阅用户可观看超过 20,000 小时的内容。Fox One 是 Fox Corporation 推出的直播电视流媒体服务，提供体育、新闻和娱乐内容，包括直播线性频道。这两个服务都是竞争激烈的流媒体市场中的新进入者，该市场由 Netflix、Disney+ 和 HBO Max 等巨头主导。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.androidauthority.com/what-is-peacock-1030392/">What is Peacock ? Pricing, content, and more - Android Authority</a></li>
<li><a href="https://www.cabletv.com/fox-one">FOX One Streaming Guide: Price, Channels, and How To Watch</a></li>
<li><a href="https://thestreamable.com/fox-one-details-price-programming-sports-free-trial-launch-date">Everything you need to know about Fox One ; price, programming...</a></li>

</ul>
</details>

**社区讨论**: 此新闻未提供社区评论。

**标签**: `#streaming`, `#Netflix`, `#media`, `#business`

---

<a id="item-22"></a>
## [GrapheneOS 明年将支持摩托罗拉手机，包括折叠屏](https://www.theverge.com/tech/983714/grapheneos-motorola-razr-fold-ultra-support-pixel-11) ⭐️ 6.0/10

注重隐私的基于安卓的操作系统 GrapheneOS 宣布计划从明年开始正式支持摩托罗拉智能手机，首先支持传统旗舰机型，随后扩展到折叠屏机型，并可能覆盖更便宜的设备。 这一扩展将 GrapheneOS 的适用范围扩大到谷歌 Pixel 设备之外，为注重隐私的用户提供更多硬件选择，尤其是在不断增长的折叠屏市场。这也可能促使其他安卓制造商考虑支持替代操作系统。 该公告由 GrapheneOS 基金会在 Mastodon 帖子中发布。推广将首先从传统的摩托罗拉旗舰机型开始，然后扩展到折叠屏机型，并可能覆盖廉价机型，但未提供具体型号或日期。

rss · The Verge · Aug 24, 11:37

**背景**: GrapheneOS 是一个基于安卓开源项目（AOSP）的开源移动操作系统，通过加固和减少攻击面来提升安全性和隐私保护。目前它可用于谷歌 Pixel 设备，截至 2026 年 4 月约有 40 万活跃用户。摩托罗拉的折叠屏手机，如 Razr 系列，是流行的翻盖式安卓设备。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/GrapheneOS">GrapheneOS</a></li>
<li><a href="https://grapheneos.org/">GrapheneOS : the private and secure mobile OS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Motorola_Razr">Motorola Razr - Wikipedia</a></li>

</ul>
</details>

**标签**: `#GrapheneOS`, `#Android`, `#privacy`, `#security`, `#Motorola`

---

<a id="item-23"></a>
## [微软与 PowerHouse Hillwood 就数据中心协议与公用事业公司发生纠纷](https://www.utilitydive.com/news/microsoft-powerhouse-hillwood-data-center-service-ferc/828566/) ⭐️ 6.0/10

微软和 PowerHouse Hillwood 在威斯康星州和伊利诺伊州与公用事业公司就数据中心服务协议发生纠纷，微软声称协议未能保护纳税人，而 PowerHouse Hillwood 则指责 Exelon 旗下的 ComEd 利用垄断权力扼杀协议。 这些纠纷凸显了大型科技公司与公用事业公司之间在数据中心能源合同上的紧张关系，引发了对纳税人保护和公用事业市场力量的担忧。其结果可能为数据中心服务协议的制定和监管树立先例，影响科技和能源行业。 纠纷涉及威斯康星州和伊利诺伊州的具体协议，微软认为协议未能充分保护纳税人，而 PowerHouse Hillwood 声称 ComEd 利用其垄断地位阻止数据中心协议。这些案件可能由监管机构审查，可能涉及联邦能源监管委员会（FERC）。

rss · Utility Dive · Aug 24, 13:05

**背景**: 数据中心服务协议是数据中心运营商与公用事业公司之间的合同，规定了电力供应条款，包括定价、可靠性和电网互联。随着 AI 和云计算导致数据中心需求激增，公用事业公司正在谈判这些协议以管理负荷和成本回收，但人们担心纳税人是否免受成本转移的影响，以及公用事业公司是否滥用垄断权力。FERC 等监管机构负责监督州际电力事务，州监管机构则批准公用事业费率和合同。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.utilityeducation.com/developing-data-center-rates">Developing Data Center Rates — UtilityEducation.com</a></li>
<li><a href="https://linknky.com/news/2026/06/15/kentucky-data-centers-electricity-rates-ratepayer-protections/">Utilities say their rules protect ratepayers against big data... - LINK nky</a></li>
<li><a href="https://www.aixenergy.io/beyond-the-prompt-washingtons-ai-power-pledge-tests-who-pays-for-the-grid/">AI’s Grid Problem Is Not the Prompt. It Is the Commitment</a></li>

</ul>
</details>

**标签**: `#data centers`, `#energy`, `#utilities`, `#Microsoft`, `#regulation`

---

<a id="item-24"></a>
## [亚利桑那州电网电池热潮能否持续？](https://www.canarymedia.com/articles/batteries/arizona-grid-battery-growth) ⭐️ 6.0/10

根据 Canary Media 对美国能源信息管理局数据的分析，2026 年上半年，亚利桑那州的电网电池装机容量超过了除得克萨斯州以外的所有州，成为电池装机量第三大的州。 这一增长表明电网电池革命正从加利福尼亚州和得克萨斯州向外扩展，可能增强西南地区的电网可靠性和可再生能源整合能力。这也可能促使其他州加快其电池储能部署。 文章指出，亚利桑那州的电池容量增长显著，但对其可持续性提出疑问。该分析基于 2026 年上半年的数据，该州的快速扩张可能面临市场饱和或政策变化等挑战。

rss · Latitude Media (Canary Media) · Aug 24, 07:30

**背景**: 电网电池是大型储能系统，有助于平衡电网供需，尤其是在太阳能和风能等可变可再生能源并网时。加利福尼亚州和得克萨斯州在美国电池部署方面处于领先地位，亚利桑那州近期的增长反映了全国电池储能容量增加的大趋势，其总容量已超过抽水蓄能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.canarymedia.com/articles/energy-storage/grid-batteries-have-never-been-more-abundant-or-more-useful">Grid batteries have never been more abundant — or... | Canary Media</a></li>
<li><a href="https://www.wired.com/story/grid-scale-battery-storage-is-quietly-revolutionizing-the-energy-system/">Grid -Scale Battery Storage Is Quietly Revolutionizing the... | WIRED</a></li>

</ul>
</details>

**标签**: `#grid batteries`, `#energy storage`, `#renewable energy`, `#Arizona`, `#electric grid`

---

<a id="item-25"></a>
## [PJM 批准清洁能源项目但面临建设挑战](https://www.canarymedia.com/articles/energy-markets/pjm-greenlit-new-clean-power) ⭐️ 6.0/10

美国最大的能源市场 PJM 互联已批准大量新的清洁能源项目，但该地区难以快速建设这些项目以满足不断增长的电力需求。这导致其覆盖 13 个州的 6700 万客户的电费上涨。 这一情况凸显了清洁能源批准与实际部署之间的关键差距，可能损害电网可靠性和气候目标。其结果将影响能源价格、政策决策以及美国清洁能源转型的步伐。 PJM 计划于 2026 年 4 月重新开放互联队列，采用基于集群的“先准备好先服务”流程，旨在将研究时间缩短至一到两年。批评者将容量价格上涨归咎于 PJM 的规划缺陷和市场设计失误。

rss · Latitude Media (Canary Media) · Aug 24, 07:30

**背景**: PJM 互联是一个区域输电组织（RTO），为 13 个州及哥伦比亚特区部分地区运营电网。其容量市场“可靠性定价模型”提前三年向发电商支付承诺供电的费用。互联队列是新电厂（尤其是可再生能源）接入电网的研究和连接流程，目前面临严重积压。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PJM_Interconnection">PJM Interconnection - Wikipedia</a></li>
<li><a href="https://www.nrdc.org/bio/dana-ammann/breaking-through-pjm-interconnection-queue-crisis">Breaking Through the PJM Interconnection Queue Crisis</a></li>
<li><a href="https://advancedenergyunited.org/blog/pjm-stalled-the-clean-energy-transition-affordability-and-reliability-depends-on-getting-it-back-on-track/">PJM Stalled the Clean Energy Transition: Affordability and Reliability...</a></li>

</ul>
</details>

**标签**: `#energy`, `#grid`, `#clean power`, `#PJM`, `#infrastructure`

---

<a id="item-26"></a>
## [GPU 供应危机迫在眉睫，价格预计上涨](https://www.pcgamer.com/hardware/graphics-cards/theres-a-looming-gpu-supply-crisis-which-means-prices-are-likely-to-get-a-whole-lot-worse-and-its-not-just-because-of-memory/) ⭐️ 6.0/10

一家主要的 GPU 制造商在其财务业绩中警告称，今年下半年将出现严重的 GPU 供应危机，可能导致价格进一步上涨。这一警告是在持续的存储短缺和成本上升的背景下发出的。 这场供应危机可能严重影响依赖 GPU 的游戏玩家、PC 组装者和 AI 开发者，导致成本上升和供应受限。它反映了更广泛的行业趋势，即 AI 需求正在给存储和 GPU 生产带来压力，影响整个硬件生态系统。 这场危机不仅归因于存储短缺，还归因于其他因素，如 AI 需求的爆炸性增长和 DRAM 价格上涨。例如，据报道 AMD 计划将 8GB GPU 价格提高 20 美元，16GB GPU 提高 40 美元，并预计 2026 年全年还会有进一步上涨。

rss · PC Gamer · Aug 24, 12:17

**背景**: GPU 对于游戏、专业图形和 AI 工作负载至关重要。供应危机源于多种因素，包括 2024 年开始的全球存储短缺（由 AI 需求驱动），以及为现代 GPU 制造高密度 GDDR7 存储的复杂性。这些问题导致 DRAM 价格出现两位数上涨，现在正影响 GPU 的供应和定价。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.szwecent.com/why-no-rtx-gaming-gpus-in-2026/">Global memory crises have crippled consumer GPU timelines…</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2ktMjhDTEVCRThzSjRrd3dZR2x5Z0FQAQ?hl=en-US&gl=US&ceid=US:en">Google News - AMD GPU price hike rumors - Overview</a></li>
<li><a href="https://www.pcgamer.com/gpu-supply-problems-easing/">As the GPU supply crisis eases it's budget PC gamers... | PC Gamer</a></li>

</ul>
</details>

**标签**: `#GPU`, `#supply chain`, `#hardware`, `#pricing`

---

<a id="item-27"></a>
## [Nightdive 的《神偷》重制版发现过时的代码仓库](https://www.pcgamer.com/games/sim/nightdives-thief-remaster-unearths-a-very-very-out-of-date-version-control-repository-with-the-wildest-things-to-say-about-the-code/) ⭐️ 6.0/10

Nightdive Studios 在重制《神偷：暗黑计划》时，发现了一个“非常非常过时”的版本控制仓库，其中包含原始的 Dark Engine 代码。Josh Dowell 指出，光照代码“与 Quake 完全相同”，揭示了意想不到的技术相似性。 这一发现为经典游戏及其引擎的开发历史提供了罕见的见解，对游戏历史学家和模组社区很有价值。它也展示了现代重制版如何成为考古发掘，揭示被遗忘的技术细节，为保存和未来开发提供参考。 该仓库包含 Dowell 描述为“对代码有最疯狂评论”的内容，暗示了开发者直白的注释。与 Quake 的光照比较值得注意，因为《神偷》使用软件渲染，而 Quake 也是软件渲染，但光照方法的完全复制出乎意料。

rss · PC Gamer · Aug 24, 04:23

**背景**: 《神偷：暗黑计划》于 1998 年由 Looking Glass Studios 发行，是一款开创性的潜行游戏，使用了 Dark Engine，这是一个在硬件加速过渡期间开发的软件渲染引擎。Nightdive Studios 专注于重制经典游戏，经常使用原始源代码。此类版本控制仓库包含历史代码和开发者注释，为开发过程提供了见解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/games/sim/nightdives-thief-remaster-unearths-a-very-very-out-of-date-version-control-repository-with-the-wildest-things-to-say-about-the-code/">Nightdive 's Thief remaster unearths a 'very very out of date version .....</a></li>
<li><a href="https://everythingedinburgh.com/games/news/nightdive-thief-dark-engine-code-secrets/">Nightdive Dev Reveals What Hides Inside Thief 's Dark Engine</a></li>
<li><a href="https://thegeek.games/2026/08/24/nightdive-thief-remaster-secrets-video/">Nightdive Stumbled Upon Interesting Stuff While Developing the Thief ...</a></li>

</ul>
</details>

**标签**: `#game development`, `#reverse engineering`, `#Thief`, `#Nightdive`, `#version control`

---