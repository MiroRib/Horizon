---
layout: default
title: "Horizon Summary: 2026-08-01 (ZH)"
date: 2026-08-01
lang: zh
---

> From 54 items, 11 important content pieces were selected

---

1. [Ripgrep musl 二进制在大规模搜索中因 mallocng 分配器缺陷而段错误](#item-1) ⭐️ 8.0/10
2. [加拿大签署联合国网络犯罪公约引发监控担忧](#item-2) ⭐️ 8.0/10
3. [谷歌在 RSS 订阅衰落中的作用](#item-3) ⭐️ 7.0/10
4. [800 页 64 位汇编综合书籍引发讨论](#item-4) ⭐️ 7.0/10
5. [NetBSD 11.0 发布，引入 MICROVM 内核和防火墙改进](#item-5) ⭐️ 7.0/10
6. [微软 Flint：面向 AI 代理的新型可视化语言](#item-6) ⭐️ 7.0/10
7. [硅谷创始人的财务破产：一个警示故事](#item-7) ⭐️ 7.0/10
8. [Cursor 意外从使用页面和 CSV 导出中移除成本数据](#item-8) ⭐️ 6.0/10
9. [Reddit 股价下跌，CEO 质疑 Google AI 概览价值](#item-9) ⭐️ 6.0/10
10. [Defcon 徽章兼作开源安全密钥](#item-10) ⭐️ 6.0/10
11. [果蝇如何利用记忆和方向感在湍流气味羽流中导航](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Ripgrep musl 二进制在大规模搜索中因 mallocng 分配器缺陷而段错误](https://github.com/BurntSushi/ripgrep/issues/3494) ⭐️ 8.0/10

Ripgrep 的 musl 二进制在大规模搜索中偶尔发生段错误，如 issue #3494 所报告。根本原因追溯到 musl 的 mallocng 分配器，该分配器在高内存竞争下存在触发缺陷。 该缺陷影响依赖 ripgrep 静态 musl 构建进行大规模性能关键搜索的用户，可能导致崩溃和数据丢失。它凸显了多线程应用中分配器选择的重要性，并引发了对内核级内存管理问题的讨论。 该问题涉及 ripgrep 15.2.0，使用 x86_64-unknown-linux-musl 静态链接，jemalloc 作为 Rust 全局分配器，而 musl 1.2.5 服务 C 分配器调用（特别是 opendir 中的 calloc）。分析表明 Linux 7.0 中存在疑似内存管理竞争，详细分析见 ripgrep-3494-analysis 仓库。

hackernews · throwaway2037 · Aug 1, 12:34 · [社区讨论](https://news.ycombinator.com/item?id=49133889)

**背景**: musl 是一种轻量级 libc 实现，常用于静态二进制，其 mallocng 分配器（在 v1.2.1 引入）专注于强化内存错误防护。然而，它在多线程竞争下存在已知性能问题。Ripgrep 是一个流行的快速搜索工具，提供 musl 构建以增强可移植性，但此缺陷揭示了性能与稳定性之间的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/dfoxfranke/ripgrep-3494-analysis">dfoxfranke/ ripgrep -3494-analysis: Analysis of one crazy segfault in...</a></li>
<li><a href="https://elsolitario.org/en/2026/08/01/ripgrep-musl-segfault-mallocng-heap-en/">Musl Segfault : mallocng Bug Hits Ripgrep 15.2</a></li>
<li><a href="https://sourcefeed.dev/a/that-ripgrep-segfault-is-probably-a-kernel-bug">That ripgrep Segfault Is Probably a Kernel Bug — SourceFeed</a></li>

</ul>
</details>

**社区讨论**: 社区讨论包括专家对分配器性能的评论，一位用户指出 mallocng 在处理多线程竞争方面表现不佳，并建议替换它。另一位用户指出内核补丁可能是真正原因，并链接到详细分析。还有评论提到在集群文件系统上运行 ripgrep 的 HPC 工作流因高小 I/O 而不合适。

**标签**: `#ripgrep`, `#musl`, `#allocator`, `#bug`, `#performance`

---

<a id="item-2"></a>
## [加拿大签署联合国网络犯罪公约引发监控担忧](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/) ⭐️ 8.0/10

加拿大于 2026 年悄然签署了《联合国网络犯罪公约》（又称河内公约），尽管此前曾反对该条约。此次签署遭到隐私倡导者的批评，他们认为该条约实为变相的监控条约。 此举可能扩大政府监控权力，并削弱加拿大及全球的隐私和公民自由。这也标志着加拿大在国际网络犯罪合作立场上的转变，可能为其他国家树立先例。 该条约由俄罗斯于 2017 年提出，并于 2024 年 12 月由联合国大会通过，旨在加强打击网络犯罪的国际合作和电子证据共享。截至 2026 年 5 月，已有 76 个参与方签署，但需批准才能完全生效；加拿大尚未批准。

hackernews · iamnothere · Aug 1, 14:19 · [社区讨论](https://news.ycombinator.com/item?id=49134694)

**背景**: 《联合国网络犯罪公约》是首个关于网络犯罪的全球性全面条约，提供了预防和打击措施以及国际合作。人权组织因担心监控和潜在滥用而反对该条约。加拿大最初反对该条约，并在谈判中强调其对人权的威胁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Convention_against_Cybercrime">United Nations Convention against Cybercrime - Wikipedia</a></li>
<li><a href="https://www.unodc.org/unodc/en/cybercrime/convention/home.html">United Nations Convention against Cybercrime</a></li>
<li><a href="https://ccla.org/privacy/ccla-distrubed-as-canada-signs-global-surveillance-treaty/">CCLA distrubed as Canada signs global surveillance treaty - CCLA</a></li>

</ul>
</details>

**社区讨论**: 评论者意见不一：有人称赞 Michael Geist 在隐私问题上的长期工作，也有人指出签署对加拿大很常见，批准才是关键步骤。一位评论者强调了国际政治的表演性质，质疑此类承诺的严肃性。

**标签**: `#surveillance`, `#cybercrime`, `#privacy`, `#Canada`, `#UN treaty`

---

<a id="item-3"></a>
## [谷歌在 RSS 订阅衰落中的作用](https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds) ⭐️ 7.0/10

Open RSS 上发布的一篇文章指出，谷歌在 2013 年关闭 Google Reader 的决定对 RSS 订阅的衰落起到了重要作用。文章强调，这一行动以及其他科技公司的举措，侵蚀了开放网络生态系统。 这很重要，因为 RSS 是一个基本的开放标准，赋予用户控制内容消费的能力，而它的衰落导致了更加集中化、以广告驱动的网络，被围墙花园所主导。理解谷歌的角色有助于理解开放网络原则的丧失，并为关于维护数字开放性的讨论提供背景。 文章特别批评了谷歌以“使用率下降”为由关闭 Reader，并指出这恰逢谷歌推广使用率很低的 Google+。文章还提到 Mozilla 在 Firefox 64 中移除 RSS 功能（如 Live Bookmarks）是另一个促成因素。

hackernews · pudgywalsh · Aug 1, 18:07 · [社区讨论](https://news.ycombinator.com/item?id=49136821)

**背景**: RSS（简易信息聚合）是一种网络订阅格式，允许用户订阅网站的内容更新。在 21 世纪初，RSS 被广泛使用，Google Reader 成为最受欢迎的 RSS 阅读器，但其在 2013 年的关闭留下了一个空白，许多人认为这加速了 RSS 的衰落。像 Twitter 和 Facebook 这样的社交媒体平台提供了自己的信息流，也减少或移除了对 RSS 的支持，进一步边缘化了这项技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds">How Google helped destroy adoption of RSS feeds - Open RSS</a></li>
<li><a href="https://news.ycombinator.com/item?id=16722260">> When did RSS go out of style anyway? It went away when Google killed Reader. R... | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSS">RSS - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了对早期互联网的怀念和对谷歌决定的不满，有人指出谷歌的借口“显然是假的”，因为他们当时在推广 Google+。还有人提到 Mozilla 移除 RSS 功能，另一些人则感叹 Google Reader 的关闭感觉像是他们认知中互联网“终结的开始”。

**标签**: `#RSS`, `#Google`, `#Web History`, `#Open Standards`, `#Internet Culture`

---

<a id="item-4"></a>
## [800 页 64 位汇编综合书籍引发讨论](https://nostarch.com/art-64-bit-assembly-v2) ⭐️ 7.0/10

No Starch Press 发布了《64 位汇编的艺术》，这是一本 800 页的书籍，专注于使用 MASM 在 Windows 上进行 x86-64 汇编编程。该书旨在为底层程序员提供全面的资源。 这本书意义重大，因为它提供了对汇编语言的全面、现代的处理，而汇编语言在当代开发中常被忽视。对于对底层编程、性能优化和理解计算机体系结构感兴趣的人来说，它是一个宝贵的资源。 这本书近 800 页，专门针对 x86-64 架构，使用 Windows 上的 Microsoft 宏汇编器（MASM）。它涵盖了宏语言特性，如循环、算术和字符串处理，这些是 MASM 相对于 GAS 等其他汇编器的优势。

hackernews · 0x54MUR41 · Aug 1, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=49134599)

**背景**: 汇编语言是一种与处理器机器代码紧密相关的低级编程语言，允许对硬件进行精确控制。它常用于实时嵌入式系统、操作系统内核和设备驱动程序中，这些领域对性能和效率要求极高。x86-64 架构在现代计算机中广泛使用，而 MASM 是一种成熟的汇编器，自 1981 年就已存在，Visual Studio 中包含其 64 位版本（ml64.exe）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/X86_assembly_language">x86 assembly language - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Macro_Assembler">Microsoft Macro Assembler - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/assembler/masm/masm-for-x64-ml64-exe?view=msvc-170">MASM for x64 (ml64.exe) | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论很活跃，有 76 条评论。一些用户对这本书的深度以及汇编语言的持续相关性表示赞赏，而另一些人则批评营销文案和使用 AI 生成的文本。还有关于选择 MASM 和 Windows 的评论，有些人询问是否有 Linux 等效书籍。

**标签**: `#assembly`, `#low-level programming`, `#book`, `#x86-64`, `#MASM`

---

<a id="item-5"></a>
## [NetBSD 11.0 发布，引入 MICROVM 内核和防火墙改进](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 7.0/10

NetBSD 11.0 正式发布，为 x86 引入了新的 MICROVM 内核，可在约 10 毫秒内启动，并改进了 npf(7) 防火墙，包括二层和用户/组过滤功能。 此版本展示了 NetBSD 在虚拟化和安全方面的持续演进，可能吸引对轻量级、快速启动系统感兴趣的用户。MICROVM 内核为微服务和边缘计算开辟了可能性，而防火墙改进则增强了现有用户的安全性。 MICROVM 内核利用 PVH 引导和 VirtIO MMIO，支持 i386 和 amd64 架构。npf 防火墙现在支持二层过滤以及基于用户和组 ID 的过滤，这些是网络安全管理的显著新增功能。

hackernews · jaypatelani · Aug 1, 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49136736)

**背景**: NetBSD 是一个免费、开源的类 Unix 操作系统，以其可移植性和简洁设计而闻名。它是主要的 BSD 变体之一，与 FreeBSD 和 OpenBSD 并列。MICROVM 内核专为极快的虚拟机启动而设计，适用于微服务等需要快速启动的场景。npf 防火墙是 NetBSD 的数据包过滤器，此次增强提供了更细粒度的控制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.netbsd.org/releases/formal-11/NetBSD-11.0.html">Announcing NetBSD 11.0 RC7 (July 21, 2026)</a></li>
<li><a href="https://www.phoronix.com/news/smolBSD">smolBSD Builds On The NetBSD-MicroVM Kernel For Booting To Service VMs In Milliseconds - Phoronix</a></li>
<li><a href="https://wiki.netbsd.org/users/imil/microvm/">microvm</a></li>

</ul>
</details>

**社区讨论**: 社区评论反映了对 BSD 相关性和软件兼容性的好奇。一位用户询问 NetBSD 上 Wine 的支持情况，以运行仅限 Windows 的软件；另一位则思考 BSD 与 Linux 相比的现状和使用情况。其他人则强调了防火墙改进和 MICROVM 内核快速启动时间的价值，并指出发布公告提供了更多细节。

**标签**: `#NetBSD`, `#BSD`, `#operating systems`, `#release`, `#virtualization`

---

<a id="item-6"></a>
## [微软 Flint：面向 AI 代理的新型可视化语言](https://microsoft.github.io/flint-chart/) ⭐️ 7.0/10

微软推出了 Flint，这是一种开源的中间可视化语言，旨在让 AI 代理能够从紧凑、可人工编辑的规范中创建富有表现力且精美的图表。该项目已在 GitHub 上发布，并通过微软研究院的博客进行了公告。 Flint 解决了 AI 驱动应用中高效、可靠生成图表的需求，可能简化大型语言模型生成可视化的方式。它通过在低级绘图库和高级语法之间提供中间方案，可能影响整个生态系统，但其采用取决于社区的接受度以及与现有方法相比的明显优势。 Flint 是一种中间语言，可以渲染到多个图表后端，旨在为 LLM 节省 token。然而，社区反馈表明，直接生成 Vega-Lite 规范可能为复杂定制提供更多灵活性，并且当 LLM 已经能够编写后端代码时，新语言的必要性受到质疑。

hackernews · vinhnx · Aug 1, 02:45 · [社区讨论](https://news.ycombinator.com/item?id=49130604)

**背景**: 像 Vega-Lite 和 ggplot2 这样的可视化语言为统计图形提供了高级语法，允许用户以声明方式指定图表。在 AI 时代，大型语言模型越来越多地被用于从自然语言生成可视化，但它们常常难以处理现有规范的冗长和复杂性。Flint 旨在通过提供一种紧凑、可人工编辑的中间表示来弥合这一差距，使 AI 代理能够高效地生成和编辑。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/flint-a-visualization-language-for-the-ai-era/">Flint : A visualization language for the AI era - Microsoft Research</a></li>
<li><a href="https://github.com/microsoft/flint-chart">GitHub - microsoft / flint -chart: 🪄 Flint is a visualization language ...</a></li>
<li><a href="https://vega.github.io/vega-lite/examples/">Example Gallery | Vega-Lite</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了复杂的情绪：一些人称赞这一概念，但质疑其相对于直接生成 Vega-Lite 的优势，指出在自定义可视化方面存在灵活性问题。其他人则想知道为什么不直接让 AI 编写后端代码，还有人指出像 ggplot2 这样的现有 API 仍然很强大。总体而言，讨论反映了对该项目价值主张的深思熟虑的批评和参与。

**标签**: `#visualization`, `#AI`, `#Microsoft`, `#charting`, `#LLM`

---

<a id="item-7"></a>
## [硅谷创始人的财务破产：一个警示故事](https://zaksa.zip/blog/silicon-valley-founder-meat-grinder/) ⭐️ 7.0/10

一篇个人故事详细描述了一位创始人（化名 Jim）追求创业财富和冒险，最终导致财务破产的经历。文章用他的经历来批评硅谷以金钱为导向的文化。 这个故事引起了许多科技界人士的共鸣，凸显了将财富置于真正热情之上以及创业结果高方差的风险。它引发了对硅谷文化从创造事物转向追逐金钱的反思。 文章提到 Jim 的财务鲁莽行为，包括一个进入家庭酿酒的例子，一位评论者指出这其实是一种廉价的爱好。故事强调了想要成为“创始人”而非实际做事的心理陷阱。

hackernews · Kaizeras · Aug 1, 20:20 · [社区讨论](https://news.ycombinator.com/item?id=49138045)

**背景**: 创业文化常常美化冒险和财富，但这可能导致个人财务灾难。旧金山湾区的科技圈多年来发生了变化，一些观察者指出，重点从构建产品转向赚钱，尤其是在比特币兴起之后。

**社区讨论**: 评论者对创始人的故事表示同情，并批评了以金钱为导向的文化。一些人分享了个人经历，说明坚持可以带来成功，而另一些人则指出想成为创始人和实际做事的区别。一位评论者指出家庭酿酒是一种廉价的爱好，质疑作者举的例子。

**标签**: `#startup culture`, `#entrepreneurship`, `#financial risk`, `#tech industry`, `#personal story`

---

<a id="item-8"></a>
## [Cursor 意外从使用页面和 CSV 导出中移除成本数据](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153) ⭐️ 6.0/10

Cursor 从其使用页面和 CSV 导出中移除了成本信息，但一位 Cursor 员工澄清这是意外操作，CSV 导出已修复。移除原因是清理了一个旧功能标志，该标志曾向部分自助用户显示美元使用量图表。 这一变化影响了依赖 Cursor 使用页面和 CSV 导出进行成本跟踪和内部费用分摊的用户，尤其是团队用户。它凸显了 token 使用和计费透明性的重要性，以及社区对成本可见性变化的敏感性。 Cursor 员工表示 CSV 导出已修复，但美元使用量图表是故意移除的，因为它将包含的计划使用量显示为美元，可能与实际支出混淆。支出页面仍显示账单信息。一些用户报告了仪表盘 UI、CSV 导出和 API 成本总额之间的差异。

hackernews · EugeneOZ · Aug 1, 15:25 · [社区讨论](https://news.ycombinator.com/item?id=49135257)

**背景**: Cursor 是一款 AI 驱动的代码编辑器，使用 token 计费，按需使用与包含的计划使用分开计费。用户通常通过仪表盘和 CSV 导出跟踪 token 使用量和成本，用于预算和费用分摊。社区讨论还涉及 AI 编码代理之间 token 效率的差异，以及切换回 VS Code 的容易程度。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://forum.cursor.com/t/dashboard-export-usage-events-csv-no-longer-exports-cost/167193">Dashboard export-usage-events-csv no longer exports cost! - Bug Reports - Cursor - Community Forum</a></li>
<li><a href="https://forum.cursor.com/t/question-about-discrepancies-between-dashboard-ui-csv-export-and-teams-filtered-usage-events-cost-totals/157091">Question about discrepancies between Dashboard UI, CSV export, and /teams/filtered-usage-events cost totals - Help - Cursor - Community Forum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区成员表达了不同的情绪：一些人建议测量不同 harness 的 token 效率，而另一些人质疑 Cursor 在 2026 年的价值，更倾向于 Claude Code 和 Codex 等 CLI 工具。一位 Cursor 员工澄清了意外移除和修复，一位用户开玩笑说未来将采用基于 token 的定价。另一位指出 Cursor 从 VS Code 迁移容易是双刃剑。

**标签**: `#Cursor`, `#AI coding tools`, `#usage tracking`, `#token efficiency`, `#product update`

---

<a id="item-9"></a>
## [Reddit 股价下跌，CEO 质疑 Google AI 概览价值](https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/) ⭐️ 6.0/10

Reddit 首席执行官公开质疑 Google AI 概览功能的价值，暗示随着 Reddit 股价下跌，公司可能重新考虑与 Google 的授权协议。 这一事件凸显了内容提供商与可能减少原始来源流量的 AI 搜索功能之间日益紧张的关系。它可能影响 Reddit 及其他平台未来如何谈判 AI 数据授权协议。 Reddit 于 2024 年 2 月与 Google 签署了一项授权协议，据报道每年价值约 6000 万美元，允许 Google 访问 Reddit 数据用于 AI 训练和基础支持。CEO 的评论表明，在股价下跌的情况下，该协议的价值正在被重新评估。

rss · Ars Technica · Aug 1, 12:30

**背景**: Google AI 概览是集成在 Google 搜索中的 AI 功能，在搜索结果顶部生成 AI 回答。该功能因不准确、产生幻觉以及减少原始来源的网页流量而受到批评，这可能影响像 Reddit 这样的内容提供商。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Overviews">Google AI Overviews</a></li>
<li><a href="https://mentionova.com/research/why-reddit-runs-the-ai-answer">Why Reddit Runs the AI Answer — How One Forum... — Mentionova</a></li>
<li><a href="https://marketvantage.com/blog/the-google-reddit-deal-nine-months-in/">The Google - Reddit Deal Nine Months In | Market Vantage</a></li>

</ul>
</details>

**标签**: `#AI`, `#Reddit`, `#Google`, `#business`, `#licensing`

---

<a id="item-10"></a>
## [Defcon 徽章兼作开源安全密钥](https://arstechnica.com/security/2026/08/defcons-new-badge-is-a-security-key-you-can-see-inside/) ⭐️ 6.0/10

由 Andrew 'bunnie' Huang 设计的 2026 年 Defcon 徽章包含一个可拆卸的透明核心模块 Baochip-1x，可作为开源硬件安全令牌使用。与会者可以检查芯片设计，并在会议结束后继续将其用作安全密钥。 这款徽章推动了硬件安全和透明度的边界，展示了开源设计如何建立对加密硬件的信任。它可能激励更广泛地在消费设备和安全会议中采用可验证的安全密钥。 Baochip-1x 是一款开源芯片，其安全性可验证，并可用作硬件安全令牌。徽章的可拆卸核心模块是透明的，允许黑客物理检查芯片及其连接。

rss · Ars Technica · Aug 1, 10:05

**背景**: Defcon 是世界上最大、最著名的黑客大会之一，以其独特的电子徽章而闻名，这些徽章通常包含挑战和收藏设计。硬件安全令牌（如 YubiKey）提供加密认证，但其内部设计通常是专有的。通过使芯片开源，Defcon 旨在展示安全性可以是透明且可验证的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/">The New Defcon Badges Pack a Unique Open Source Chip That Doubles as a Security Key | WIRED</a></li>
<li><a href="https://iplogger.org/blog/the-new-defcon-badges-pack-a-unique-open-source-chip-that-doubles-as-a-security-key/">Defcon's Open-Source Badge: A Hardware Root of Trust ...</a></li>
<li><a href="https://www.techmeme.com/260801/p10">Techmeme: This year's Defcon badges include Baochip-1x, an ...</a></li>

</ul>
</details>

**标签**: `#security`, `#hardware`, `#Defcon`, `#badge`, `#hacking`

---

<a id="item-11"></a>
## [果蝇如何利用记忆和方向感在湍流气味羽流中导航](https://arstechnica.com/science/2026/08/how-fruit-flies-chase-invisible-ribbons-of-smell-to-get-to-their-source/) ⭐️ 6.0/10

文章解释了果蝇如何通过结合对过去气味的记忆和方向感，在湍流空气中追踪看不见的气味带，而不是依赖浓度梯度。这项研究为生物嗅觉和导航策略提供了新的见解。 理解果蝇如何导航气味羽流，可能启发更高效的机器人嗅觉系统，并改进自主代理搜索化学源的算法。这也加深了我们对简单神经系统中的感觉处理和记忆的理解。 文章可能讨论了在受控风洞中追踪果蝇在湍流气味羽流中的行为实验，揭示果蝇结合逆风冲刺和侧风扫掠，并受近期气味记忆的调节。研究还可能涉及计算模型或神经成像来识别潜在机制。

rss · Ars Technica · Aug 1, 10:00

**背景**: 自然环境中的气味羽流是湍流的，会破碎成不规则的细丝，因此不能提供平滑的浓度梯度用于导航。果蝇等昆虫必须利用间歇性的气味接触和风向定位来源。这项研究建立在先前昆虫导航研究的基础上，对机器人和人工嗅觉有启示。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.21329">Smart strategies to navigate turbulent odor plumes ...</a></li>
<li><a href="https://arxiv.org/html/2605.21329v2">Smart strategies to navigate turbulent odor plumes ...</a></li>
<li><a href="https://elifesciences.org/articles/72196">Learning to predict target location with turbulent odor plumes</a></li>

</ul>
</details>

**标签**: `#biology`, `#olfaction`, `#fruit flies`, `#neuroscience`, `#robotics`

---