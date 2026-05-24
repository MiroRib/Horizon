---
layout: default
title: "Horizon Summary: 2026-05-24 (ZH)"
date: 2026-05-24
lang: zh
---

> From 72 items, 16 important content pieces were selected

---

1. [16 字节 Windows 可执行文件突破演示极限](#item-1) ⭐️ 9.0/10
2. [内存成本占 AI 芯片组件成本 63%](#item-2) ⭐️ 8.0/10
3. [约束衰减：LLM 代理在后端代码规则上失败](#item-3) ⭐️ 8.0/10
4. [微软开源已知最早的 DOS 源代码](#item-4) ⭐️ 8.0/10
5. [Usborne 1980 年代计算机书籍现已在线提供](#item-5) ⭐️ 8.0/10
6. [DeepSeek 永久降价旗舰 AI 模型 75%](#item-6) ⭐️ 8.0/10
7. [AMD 取消免费 Vivado 版本的 Linux 支持](#item-7) ⭐️ 8.0/10
8. [澳大利亚四天工作制研究显示生产力提升](#item-8) ⭐️ 7.0/10
9. [从 Go 迁移到 Rust 的指南引发热议](#item-9) ⭐️ 7.0/10
10. [Greg Brockman 访谈因肤浅而受批评](#item-10) ⭐️ 7.0/10
11. [骗子滥用微软内部账户发送垃圾邮件](#item-11) ⭐️ 7.0/10
12. [以交互式 Jupyter Notebook 形式掌握 Dyalog APL](#item-12) ⭐️ 6.0/10
13. [Ruby for Good：维护者齐聚社会公益](#item-13) ⭐️ 6.0/10
14. [黑客从简单提示注入进化到利用聊天机器人个性](#item-14) ⭐️ 6.0/10
15. [白鲸通过镜子测试](#item-15) ⭐️ 6.0/10
16. [Godot 在体积、速度和加载时间测试中击败 Unity](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [16 字节 Windows 可执行文件突破演示极限](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 9.0/10

一个名为“Wake up! 16b”的 16 字节 Windows 可执行文件，生成了包含视觉和声音的全屏演示，在演示场景中创下了代码大小优化的新纪录。 这一成就展示了算法密度的极限，激励演示场景和底层编程社区探索在最小二进制大小内能实现什么。 该可执行文件在实模式 DOS 兼容性下运行，利用视频内存作为计算空间绘制谢尔宾斯基分形，同时通过 PC 扬声器操作生成声音。

hackernews · MaximilianEmel · May 24, 00:30 · [社区讨论](https://news.ycombinator.com/item?id=48253060)

**背景**: 演示场景是一个专注于创建小型自包含程序（称为“演示”）的社区，这些程序生成视听演示。代码高尔夫是编写尽可能小的程序以完成给定任务的实践。这个 16 字节的演示是两者的极端例子，超越了典型的 4K 或 64K 介绍大小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene - Wikipedia SizeCoding Exploring the algorithmic density in 16 bytes of x86 assembly Home - Assembly X Demoscene - 30 years of Demoscene by Assembly. Deconstruction of a 16 byte demo - jsalter.tech</a></li>
<li><a href="https://board.flatassembler.net/topic.php?t=24270">flat assembler - 16 byte demo with graphics and sound</a></li>
<li><a href="https://blog.adafruit.com/2026/05/18/explorating-the-algorithmic-density-in-16-bytes-of-x86-assembly/">Exploring the algorithmic density in 16 bytes of x86 assembly</a></li>

</ul>
</details>

**社区讨论**: 社区表达了敬畏和钦佩，一位评论者指出，之前一个没有声音的 32 字节演示被认为是极限。其他人分享了相关工作和深入探索，例如用递归 PowerPoint 演示构建的谢尔宾斯基三角形。

**标签**: `#demoscene`, `#code golf`, `#low-level programming`, `#executable compression`, `#x86 assembly`

---

<a id="item-2"></a>
## [内存成本占 AI 芯片组件成本 63%](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

根据 Epoch AI 的数据，高带宽内存（HBM）目前占 AI 芯片组件成本的 63%，高于 2024 年第一季度的 52%。 这一成本变化凸显了 DRAM 供需失衡加剧，推高价格，可能减缓 AI 硬件成本下降的速度。 截至 2025 年第三季度，DRAM 合约价格同比飙升 171.8%，部分内存模组价格涨幅高达 619%。

hackernews · intelkishan · May 24, 16:31 · [社区讨论](https://news.ycombinator.com/item?id=48258684)

**背景**: AI 芯片在训练和推理过程中严重依赖高带宽内存（HBM）实现快速数据访问。DRAM 制造产能难以跟上 AI 需求的激增，导致价格飙升。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://epoch.ai/data-insights/ai-chip-component-cost-shares">AI Chip Component Costs: Memory at 63% | Epoch AI</a></li>
<li><a href="https://www.tomshardware.com/pc-components/dram/dram-prices-surge-171-percent-year-over-year-ai-demand-drives-a-higher-yoy-price-increase-than-gold">DRAM prices skyrocket 171% year-over-year, outpacing the rate of gold ...</a></li>
<li><a href="https://www.glukhov.org/hardware/memory/ram-price-increase/">RAM Price Surge: Up to 619% in 2025 - glukhov.org</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到价格大幅上涨（例如 96GB 内存从 250 美元涨到 1200 美元），并对消费者承受能力表示担忧。有人认为等待供应赶上需求，无需技术创新即可实现约 3 倍的硬件成本降低。

**标签**: `#AI hardware`, `#memory costs`, `#DRAM`, `#semiconductors`, `#supply chain`

---

<a id="item-3"></a>
## [约束衰减：LLM 代理在后端代码规则上失败](https://arxiv.org/abs/2605.06445) ⭐️ 8.0/10

一项系统性研究揭示，基于 LLM 的编码代理存在约束衰减现象：在无约束代码生成中表现良好，但在后端开发中需要遵循架构、ORM 和框架约束时，断言通过率显著下降。 这一发现凸显了 LLM 代理在生产级后端开发中的关键可靠性差距——遵循结构规则至关重要，并表明当前代理仅适用于快速原型设计，不适合生产级代码生成。 研究发现，在多文件后端生成中，随着约束累积，LLM 代理的断言通过率下降约 30 个百分点，且损失集中在约定密集型框架上。由于成本限制，该研究未全面测试前沿模型。

hackernews · wek · May 24, 12:55 · [社区讨论](https://news.ycombinator.com/item?id=48256912)

**背景**: 基于 LLM 的编码代理是从自然语言提示生成代码的 AI 系统。在后端开发中，代码必须同时满足功能需求（正确输出）和结构需求（例如架构模式、ORM 约定、框架规则）。约束衰减是指随着更多规则引入，代理在保持功能正确性的同时，越来越无法满足结构约束的现象。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.06445">[2605.06445] Constraint Decay: The Fragility of LLM Agents in Backend Code Generation</a></li>
<li><a href="https://arxiv.org/html/2605.06445">Constraint decay: The Fragility of LLM Agents in Backend Code Generation</a></li>
<li><a href="https://agentpatterns.ai/verification/constraint-decay-backend-agents/">Constraint Decay in Backend Code Generation - AgentPatterns.ai</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，业界已通过技能、规则、测试和代理循环等生态系统来应对这一问题，但一致认为随着代码库增长，LLM 会越来越吃力。一位评论者引入了“钙化”概念，即代码库中的模式会随时间推移降低代理性能。

**标签**: `#LLM agents`, `#code generation`, `#software engineering`, `#AI reliability`, `#backend development`

---

<a id="item-4"></a>
## [微软开源已知最早的 DOS 源代码](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 8.0/10

微软开源了已知最早的 MS-DOS 源代码版本，这些代码由 DOS 反汇编小组通过 OCR 技术从纸质打印件中艰难恢复。 此次发布保存了计算史上关键的一页，并为微软早期操作系统开发提供了罕见视角，该系统为 PC 革命奠定了基础。 源代码是从原始开发者 Tim Paterson 提供的纸质打印件中恢复的，现代 OCR 软件难以处理几十年前的打印质量。

hackernews · DamnInteresting · May 24, 01:21 · [社区讨论](https://news.ycombinator.com/item?id=48253386)

**背景**: MS-DOS 是微软在 1981 年授权给 IBM 用于原始 IBM PC 的操作系统，后来成为 PC 时代的主导操作系统。该代码主要用汇编语言编写，当时并未以数字形式存储。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/zacharywhitley/awesome-ocr">GitHub - zacharywhitley/awesome-ocr</a></li>
<li><a href="https://www.ocr4all.org/">OCR4all | Setup guide, user guide, developer documentation and more.</a></li>
<li><a href="https://stackoverflow.com/questions/1888587/need-good-ocr-for-printed-source-code-listing-any-ideas">Need good OCR for printed source code listing, any ideas?</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软的发布表示感谢，有人指出同时开源的 BASIC 源代码也具有历史意义。还有人感叹几千行汇编代码就能催生一家成功的软件公司。

**标签**: `#open source`, `#history`, `#DOS`, `#Microsoft`, `#preservation`

---

<a id="item-5"></a>
## [Usborne 1980 年代计算机书籍现已在线提供](https://usborne.com/us/books/computer-and-coding-books) ⭐️ 8.0/10

Usborne 出版社已将其 1980 年代的计算机书籍合集免费在线提供，让新一代读者能够接触到这些曾激励许多早期程序员的经典读物。 这些书籍在教导一代儿童编程方面发挥了关键作用，其在线发布不仅保存了计算史上的重要篇章，也让现代学习者能够轻松获取。 该合集包括《练习你的 BASIC》和《编写你自己的冒险程序》等书籍，通过动手项目和插图教授编程概念。

hackernews · ngram · May 24, 15:43 · [社区讨论](https://news.ycombinator.com/item?id=48258194)

**背景**: 在 1980 年代，Commodore 64 和 ZX Spectrum 等家用电脑非常流行，Usborne 的书籍提供了 BASIC 编程的入门指南。这些书籍以其彩色插图和分步指导而闻名，使复杂主题对儿童来说易于理解。

**社区讨论**: 评论者分享了这些书籍如何启发他们编程生涯的个人故事，一位用户回忆起 1989 年从学校图书馆的副本学习 BASIC，另一位则在 2000 年代初将 BASIC 代码移植到 JavaScript。整体情绪充满怀旧和感激，突显了这些书籍的持久影响。

**标签**: `#retro computing`, `#programming education`, `#nostalgia`, `#BASIC`

---

<a id="item-6"></a>
## [DeepSeek 永久降价旗舰 AI 模型 75%](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model) ⭐️ 8.0/10

DeepSeek 宣布对其旗舰 AI 模型 V4 Pro 实施永久性降价 75%，该折扣此前为临时促销，现已转为永久定价。 这一激进定价策略加剧了 AI 模型市场的竞争，可能迫使 OpenAI 和 Anthropic 等竞争对手降价。同时，它使更多开发者和企业能够负担得起先进 AI，加速技术普及。 该折扣适用于 DeepSeek 的 V4 Pro 模型，这是一个 671B 参数的混合专家模型，每个 token 激活 37B 参数。此次降价是永久性的，而非限时促销。

hackernews · moh_maya · May 24, 14:09 · [社区讨论](https://news.ycombinator.com/item?id=48257410)

**背景**: DeepSeek 是一家成立于 2023 年的中国 AI 公司，以开发高性价比的大语言模型而闻名。其 V3 模型训练成本仅为 600 万美元，远低于 GPT-4 等竞争对手。该公司开源权重模型和高效训练方式颠覆了 AI 行业，常被称为美国的“斯普特尼克时刻”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3">deepseek-ai/DeepSeek-V3 · Hugging Face</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3">GitHub - deepseek-ai/DeepSeek-V3</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区在相关讨论中提及该折扣，一些用户注意到 DeepSeek 缓存系统的高效性。一位评论者分享称，通过桥接使用 DeepSeek V4 Pro 实现了超过 95% 的缓存命中率，进一步降低了成本。

**标签**: `#AI`, `#pricing`, `#DeepSeek`, `#industry news`

---

<a id="item-7"></a>
## [AMD 取消免费 Vivado 版本的 Linux 支持](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 8.0/10

从 Vivado 2026.1 版本开始，AMD 将取消其 Vivado Design Suite 免费 Basic 版本的 Linux 支持，而 Windows 支持仍将保留。 这一决定疏远了依赖 Linux 进行 FPGA 开发的学生、爱好者和开发者，可能缩小 AMD FPGA 生态系统，并促使用户转向 Lattice 等竞争对手。 Basic 版本仍然免费，但仅限 Windows；需要 Linux 的用户必须升级到付费版本。尽管社区强烈反对，AMD 尚未提供明确的变更理由。

hackernews · zdw · May 24, 04:14 · [社区讨论](https://news.ycombinator.com/item?id=48254309)

**背景**: Vivado 是 AMD 主要的 FPGA 设计套件，用于在 Xilinx FPGA 上综合和实现设计。免费的 Basic 版本历来支持 Windows 和 Linux，为教育和爱好者使用提供了广泛访问。Linux 在学术和专业环境中因其自动化和交叉编译工作流而受到青睐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html">AMD Vivado™ Design Suite: Standard & Enterprise Edition</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html">AMD Vivado™ Design Suite</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-licensing-options.html">AMD Vivado™ Licensing Options | Flexible Subscription & Perpetual Tiers</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了强烈不满，用户批评 AMD 忽视真正关切并损害生态系统。一些人建议转向 Lattice 或 Cologne Chip 作为替代方案，而长期用户指出自收购以来 AMD 工程重点的下降。

**标签**: `#FPGA`, `#AMD`, `#Vivado`, `#Linux`, `#hardware design`

---

<a id="item-8"></a>
## [澳大利亚四天工作制研究显示生产力提升](https://scienceaim.com/australia-just-proved-the-four-day-work-week-works-here-is-what-the-data-actually-says/) ⭐️ 7.0/10

一项关于澳大利亚四天工作制试验的研究报告显示生产力提升，重新引发了关于工作文化和企业动机的讨论。 这很重要，因为它为缩短工作时间提供了实证依据，挑战了传统的五天工作制，并影响全球职场政策讨论。 该研究基于调查数据而非对照实验，导致一些人批评其科学严谨性。澳大利亚还处于 60 年来的生产力低点，这可能影响研究结果的普适性。

hackernews · randycupertino · May 24, 18:56 · [社区讨论](https://news.ycombinator.com/item?id=48259990)

**背景**: 四天工作制是一种员工以相同薪酬减少工作天数的安排，旨在改善工作与生活的平衡并提高生产力。支持者认为，技术进步应允许在不牺牲产出的情况下减少工作时间。

**社区讨论**: 评论者对企业的动机表示怀疑，一些人认为历史上生产力提升并未导致工时减少或工资增加。其他人质疑研究方法，称其为意见调查而非严谨科学。少数人主张进一步缩短工作周，例如一天或三天。

**标签**: `#work-life balance`, `#productivity`, `#workplace culture`, `#four-day work week`, `#labor economics`

---

<a id="item-9"></a>
## [从 Go 迁移到 Rust 的指南引发热议](https://corrode.dev/learn/migration-guides/go-to-rust/) ⭐️ 7.0/10

一篇从 Go 迁移到 Rust 的详细指南在 corrode.dev 上发布，引发了关于两种语言在 Web 后端开发中实际权衡的讨论。 这场讨论凸显了 Go 的简单性和托管运行时与 Rust 的性能和安全性之间的持续张力，帮助开发者为后端系统做出明智的语言选择。 该指南涵盖了错误处理、包管理和借用检查器，而社区评论指出 Go 的标准库覆盖了许多 Rust 需要外部 crate 才能满足的需求。

hackernews · jabits · May 24, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48259808)

**背景**: Go 和 Rust 都是现代系统编程语言，但理念不同：Go 优先考虑简单性和带有垃圾回收的托管运行时，而 Rust 提供零成本抽象和无垃圾回收的内存安全。选择通常取决于目标领域是否接受托管运行时。

**社区讨论**: Animats 和 tptacek 等评论者认为，对于 Web 后端工作，Go 的托管运行时通常更可取，而其他人则指出 Rust 的包管理复杂性。还有用户指出该文档包含典型的 LLM 生成文本风格模式。

**标签**: `#Go`, `#Rust`, `#migration`, `#web back-end`, `#programming languages`

---

<a id="item-10"></a>
## [Greg Brockman 访谈因肤浅而受批评](https://fs.blog/knowledge-project-podcast/greg-brockman/) ⭐️ 7.0/10

OpenAI 联合创始人 Greg Brockman 在 The Knowledge Project 播客中接受采访，谈及 OpenAI 的发展历程和争议，但讨论因缺乏深度、回避关键内部冲突而受到广泛批评。 作为 OpenAI 的关键人物，Brockman 的访谈本可提供关于该组织治理和内部动态的宝贵见解，但其肤浅性令 AI 社区许多人失望，凸显了公众对 OpenAI 挑战的理解存在缺口。 该访谈评分为 7.0/10，社区评论指出它轻描淡写了 Sam Altman 被解雇和复职等重大事件，以及 Ilya Sutskever 的角色。批评者还提到，Musk 诉讼中披露的 Brockman 个人日记显示了财务动机。

hackernews · prakashqwerty · May 24, 08:29 · [社区讨论](https://news.ycombinator.com/item?id=48255593)

**背景**: OpenAI 最初是作为非营利性 AI 研究组织成立的，但后来创建了一个利润上限的子公司以吸引投资。这种结构一直存在争议，批评者认为它削弱了非营利使命。访谈触及了这些问题，但没有深入探讨细节。

**社区讨论**: 社区评论大多持批评态度，用户对访谈缺乏深度表示失望。一位评论者质疑为何无人问及 Ilya Sutskever 在 Altman 解雇事件中的角色，另一位批评非营利组织向营利性转变树立了不良先例。还有用户引用了 Musk 诉讼中 Brockman 的个人日记，暗示其财务动机。

**标签**: `#OpenAI`, `#interview`, `#AI governance`, `#non-profit controversy`

---

<a id="item-11"></a>
## [骗子滥用微软内部账户发送垃圾邮件](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 7.0/10

骗子利用微软基础设施中的一个漏洞，从一个通常用于发送合法账户警报的内部微软电子邮件地址发送垃圾邮件和钓鱼邮件。 这种滥用行为削弱了用户对微软域名管理和电子邮件安全的信任，可能导致针对微软用户的钓鱼攻击更加成功。 该问题已持续数月，骗子利用一个内部微软账户发送垃圾邮件链接和虚假警报，引发了对微软保护自身域名能力的担忧。

hackernews · spike021 · May 24, 00:51 · [社区讨论](https://news.ycombinator.com/item?id=48253186)

**背景**: SPF、DKIM 和 DMARC 等电子邮件认证协议旨在防止域名欺骗和滥用。然而，如果内部账户被入侵或滥用，这些保护措施可能被绕过，使收件人难以区分合法邮件和垃圾邮件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/">Scammers are abusing an internal Microsoft account to send spam links | TechCrunch</a></li>
<li><a href="https://techplanet.today/post/microsofts-internal-account-abuse-a-critical-security-failure-that-undermines-user-trust">Microsoft's Internal Account Abuse: A Critical Security Failure That Undermines User Trust | TechPlanet</a></li>
<li><a href="https://powerdmarc.com/what-is-domain-abuse/">What Is Domain Abuse ?</a></li>

</ul>
</details>

**社区讨论**: 评论者对微软的域名管理表示不满，指出该公司拥有众多域名造成混乱，难以识别合法邮件。一些人分享了个人遭遇的微软安全问题，另一些人建议使用 internal.microsoft.com 等子域名来简化域名管理。

**标签**: `#security`, `#phishing`, `#Microsoft`, `#spam`, `#domain abuse`

---

<a id="item-12"></a>
## [以交互式 Jupyter Notebook 形式掌握 Dyalog APL](https://mastering.dyalog.com/README.html) ⭐️ 6.0/10

经典书籍《Mastering Dyalog APL》已重新发布为一组交互式 Jupyter Notebook，读者可以直接在浏览器中运行和修改 APL 代码。 这种现代格式降低了学习 APL（一种强大但小众的面向数组的语言）的门槛，无需复杂设置即可进行动手实践。它可能有助于重燃人们对 APL 在数据分析和算法问题解决中的兴趣。 这些 Notebook 托管在 GitHub 上，可以本地运行或通过 Binder 等云服务运行。它们涵盖从基本数组操作到高级惯用法的主题，与原书结构一致。

hackernews · tosh · May 24, 11:42 · [社区讨论](https://news.ycombinator.com/item?id=48256475)

**背景**: APL 是一种起源于 20 世纪 60 年代的编程语言，以其简洁的符号语法和强大的数组操作而闻名。Dyalog APL 是最广泛使用的现代实现，但它是专有软件，采用企业许可证。Jupyter Notebook 提供了一种结合代码、文本和可视化的交互式环境，非常适合学习像 APL 这样的语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dyalog_APL">Dyalog APL</a></li>
<li><a href="https://github.com/Dyalog/dyalog-jupyter-notebooks">Jupyter notebooks for Dyalog APL - GitHub</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍欢迎这种交互式格式，指出动手实践对于 APL 这种符号密集的语法至关重要。一些人表达了对 Dyalog 专有许可证的担忧，而另一些人则推荐了其他学习资源，如 xpqz 的《Learn APL》。

**标签**: `#APL`, `#programming languages`, `#education`, `#Jupyter`

---

<a id="item-13"></a>
## [Ruby for Good：维护者齐聚社会公益](https://ti.to/codeforgood/rubyforgood) ⭐️ 6.0/10

Ruby for Good 宣布举办一场线下聚会，邀请开源维护者共同致力于现有社会公益项目，由于社区关注，早鸟注册已提前开放。 该活动标志着从黑客松式创建转向对社会公益项目的持续维护，在开源社区中促进长期影响。 该活动明确不是黑客松；它专注于维护现有项目，其中一些已运行超过 10 年，由 Ruby for Good 创始人 Sean Marcia 组织。

hackernews · mooreds · May 24, 15:49 · [社区讨论](https://news.ycombinator.com/item?id=48258254)

**背景**: Ruby for Good 是一个社区倡议，汇聚 Ruby 开发者致力于有益社会事业的项目。与产生新原型的黑客松不同，本次聚会强调对非营利组织使用的成熟开源工具进行持续维护和支持。

**社区讨论**: 社区评论积极，创始人 Sean Marcia 澄清这不是黑客松。用户对赞助商表示兴趣，并希望看到后续关于所建项目的报道。

**标签**: `#Ruby`, `#Open Source`, `#Community`, `#Social Good`

---

<a id="item-14"></a>
## [黑客从简单提示注入进化到利用聊天机器人个性](https://www.theverge.com/column/935545/hackers-ai-chatbots) ⭐️ 6.0/10

一份新闻通讯报道，黑客正从简单的提示注入转向利用 AI 聊天机器人的“个性”，通过操纵聊天机器人的角色和语气来绕过安全防护，实施更复杂的攻击。 这一转变凸显了 AI 安全威胁日益复杂，攻击者正瞄准使聊天机器人具有吸引力的特性，可能导致更有效的社会工程攻击和数据泄露。 早期的提示注入攻击非常简单，但现在黑客会精心设计与聊天机器人被赋予的个性相符的输入，以引发非预期的响应，这种技术利用了模型无法区分开发者指令和用户输入的弱点。

rss · The Verge · May 24, 12:00

**背景**: 提示注入是一种网络安全漏洞，恶意输入会导致大型语言模型（LLM）产生非预期行为，绕过安全过滤器。随着聊天机器人被赋予不同个性以改善用户体验，攻击者可以利用这些角色来设计更具说服力和有效的攻击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://xeber.world/en/article/cybercriminals-exploit-ai-chatbot-personalities-in-new-wave-of-jailbreak-attacks-182634">AI Chatbot Jailbreak Attacks: How Hackers Exploit Personalities</a></li>

</ul>
</details>

**标签**: `#AI security`, `#chatbots`, `#prompt injection`, `#hacking`

---

<a id="item-15"></a>
## [白鲸通过镜子测试](https://arstechnica.com/science/2026/05/belugas-may-pass-the-mirror-test-but-does-the-mirror-test-still-pass/) ⭐️ 6.0/10

研究人员重新审视了旧录像带，确认白鲸表现出通过镜子自我认知测试的行为，加入了包括类人猿、海豚和大象在内的少数动物行列。 这一发现加剧了关于动物自我意识以及镜子测试本身有效性的争论，该测试因在评估跨物种认知时存在潜在偏见和局限性而受到批评。 镜子测试由 Gordon Gallup Jr.于 1970 年开发，包括在动物身上放置标记，并观察它是否在照镜子时触摸标记，从而表明自我认知。白鲸是高度智能的北极鲸类，拥有大型大脑和先进的沟通能力。

rss · Ars Technica · May 24, 11:15

**背景**: 镜子测试是一种行为技术，用于确定动物是否能在镜子中认出自己，这被认为是自我意识的标志。只有少数物种持续通过了测试，包括黑猩猩、海豚和大象。然而，该测试因依赖视觉线索而受到批评，这可能不适用于更依赖其他感官的动物。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mirror_test">Mirror test - Wikipedia</a></li>
<li><a href="https://www.animalcognition.org/2015/04/15/list-of-animals-that-have-passed-the-mirror-test/">List of Animals That Have Passed the Mirror Test - Animal ...</a></li>
<li><a href="https://arstechnica.com/science/2026/05/belugas-may-pass-the-mirror-test-but-does-the-mirror-test-still-pass/">Whatever the mirror test tells us, beluga whales pass it - Ars Technica</a></li>

</ul>
</details>

**标签**: `#animal cognition`, `#mirror test`, `#beluga whales`, `#science`

---

<a id="item-16"></a>
## [Godot 在体积、速度和加载时间测试中击败 Unity](https://www.pcgamer.com/gaming-industry/game-development/a-game-developer-compared-godot-and-unity-by-making-the-same-game-in-both-engines-and-hes-found-a-clear-winner/) ⭐️ 6.0/10

游戏设计师 Thomas Grové在 Godot 和 Unity 中制作了相同的游戏，发现 Godot 更小、更快、加载更迅速。 这次实际操作对比为在两种流行引擎之间选择的开发者提供了实际证据，可能影响独立开发者和小团队的决策。 测试涉及在两个引擎中复制相同的游戏逻辑和资源，Godot 在构建体积、运行时性能和启动时间方面表现出优势。

rss · PC Gamer · May 24, 13:00

**背景**: Godot 是一款基于 MIT 许可证的免费开源游戏引擎，而 Unity 是一款专有引擎，广泛用于独立和移动游戏开发。两者都支持跨平台的 2D 和 3D 开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unity_(game_engine)">Unity (game engine)</a></li>

</ul>
</details>

**标签**: `#game development`, `#Godot`, `#Unity`, `#engine comparison`

---