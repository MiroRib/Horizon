---
layout: default
title: "Horizon Summary: 2026-08-02 (ZH)"
date: 2026-08-02
lang: zh
---

> From 39 items, 10 important content pieces were selected

---

1. [Kakehashi：在 Linux ARM 上运行 macOS 二进制文件](#item-1) ⭐️ 8.0/10
2. [Fuse：一种采用 GRIN 后端的新静态类型函数式语言](#item-2) ⭐️ 8.0/10
3. [Karpathy 的 Pelican 基准引发关于 AI 物理世界理解的讨论](#item-3) ⭐️ 7.0/10
4. [F*：面向验证软件的证据导向编程语言](#item-4) ⭐️ 7.0/10
5. [eBay 骚扰活动导致 5600 万美元赔偿及监禁判决](#item-5) ⭐️ 7.0/10
6. [自 1953 年以来，英语学习者核心词汇的变迁](#item-6) ⭐️ 7.0/10
7. [Bor 0.8：开源 Linux 桌面策略管理，支持实时流式传输](#item-7) ⭐️ 7.0/10
8. [RISC OS Open 庆祝小众操作系统开发 20 周年](#item-8) ⭐️ 6.0/10
9. [Meshdiff：浏览器中的客户端 STL 比较工具](#item-9) ⭐️ 6.0/10
10. [仅靠版税无法说服艺术家接受 AI 训练](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Kakehashi：在 Linux ARM 上运行 macOS 二进制文件](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Kakehashi 是一个用 Rust 编写的实验性用户空间翻译层，成功在 Linux ARM64 上运行 macOS 命令行二进制文件。可用的原型包括 7-Zip、curl 和 Xcode Tools Git，其中 7-Zip 通过了多线程压缩测试，curl 通过了 200 多个命令。 该项目解决了重大的技术挑战，并可能通过使 macOS 二进制文件在更便宜的 Linux ARM 运行器上运行来降低 CI/CD 成本。它还为在 Linux 上运行 macOS 应用程序开辟了可能性，类似于 Windows 的 Wine/Proton。 该项目处于早期阶段；7-Zip 目前比原生 Linux 执行慢约 5.2 倍，但作者已有优化计划。它专注于命令行二进制文件，并采用用户空间方法，无需完整的硬件模拟。

hackernews · vlad_kalinkin · Aug 2, 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49145937)

**背景**: macOS 二进制文件使用 Mach-O 格式，与 Linux 的 ELF 格式不同，并且它们依赖 macOS 系统库。在 Linux 上运行它们通常需要模拟或兼容层。Kakehashi 旨在用户空间翻译系统调用和库调用，类似于 Darling，后者是一个在 Linux 上实现 macOS 兼容性的长期项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>
<li><a href="https://news.mcan.sh/item/49145937">Show HN: Kakehashi – Experimental userspace to run macOS ...</a></li>
<li><a href="https://ecosistemastartup.com/kakehashi-reduce-costos-ci-cd-con-binarios-macos-en-linux/">Kakehashi reduce costos CI/CD con binarios macOS en Linux</a></li>

</ul>
</details>

**社区讨论**: 社区表现出浓厚兴趣，用户提到 Darling 项目并建议潜在合作。一些人持谨慎乐观态度，指出项目仍处于早期阶段，而另一些人则设想通过类似 yabridge 的桥接在 Linux 上运行 Audio Unit 插件等应用。

**标签**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#userspace`

---

<a id="item-2"></a>
## [Fuse：一种采用 GRIN 后端的新静态类型函数式语言](https://fuselang.org/) ⭐️ 8.0/10

Fuse 是一种由独立开发者历时五年开发的静态类型纯函数式编程语言，已在 Hacker News 上展示。它通过 GRIN 全程序优化器编译为 LLVM 原生代码，支持高阶类型、特设多态、代数数据类型、特质和模式匹配。 Fuse 是对函数式编程生态的重要贡献，提供了一种结合 Rust 类似特性与纯函数语义的现代语言。其使用 GRIN 作为后端，可能激励更多函数式语言编译器采用全程序优化技术。 该语言使用 Scala 实现，从 TAPL 中描述的 System F 出发，并扩展了双向类型检查和高阶多态。标准库中的字符串类型不支持 Unicode，这是社区指出的一个限制。

hackernews · the_unproven · Aug 2, 11:23 · [社区讨论](https://news.ycombinator.com/item?id=49143412)

**背景**: GRIN（图归约中间表示）是一个用于惰性和严格函数式语言的编译器框架和中间表示，支持全程序优化。高阶类型允许对类型构造器进行抽象，而特设多态允许基于类型的函数重载。Fuse 旨在提供一种具有 Rust、Haskell 和 Scala 熟悉特性的纯函数式语言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grin-compiler.github.io/">GRIN Compiler - Overview</a></li>
<li><a href="https://github.com/grin-compiler/grin">GitHub - grin-compiler/grin: GRIN is a compiler back-end for ... A Modern Look at GRIN, an Optimizing Functional Language Back ... A modern look at GRIN, an optimizing functional language back ... A modern look at GRIN, an optimizing functional language back ... [PDF] A Modern Look at GRIN, an Optimizing Functional ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Higher-kinded_type">Higher-kinded type</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ad_hoc_polymorphism">Ad hoc polymorphism</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区反应积极，称赞了 GRIN 的使用和语言设计。评论包括关于非类型依赖成员的特质语法问题、建议添加性能基准和编译器指标，以及指出标准库中的 Unicode 支持问题。

**标签**: `#programming language`, `#functional programming`, `#type theory`, `#GRIN`, `#LLVM`

---

<a id="item-3"></a>
## [Karpathy 的 Pelican 基准引发关于 AI 物理世界理解的讨论](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy 将'Pelican'作为评估 AI 模型物理世界理解的新基准，具体通过生成骑自行车的鹈鹕的 SVG 来实现。这在 Hacker News 上引发了 280 条评论的辩论，讨论此类基准的有效性和影响。 这很重要，因为它将焦点从图像生成质量转移到更深入的物理世界理解，这对具身 AI 和机器人技术至关重要。随着模型超越简单的生成任务，这场辩论凸显了更好评估方法的需求。 该基准涉及生成骑自行车的鹈鹕的 SVG，包含 18 个轨迹和 4 个视角，如 GitHub 仓库所示。一些人认为像 Anthropic 这样的模型可能专门训练生成 three.js 代码，质疑该基准的指示价值。Dylan Castillo 进行的一项统计研究测试了 7 个模型在 48 种动物-车辆 SVG 组合上的表现，未发现'pelicanmaxxing'（专门针对基准训练）的显著证据。

hackernews · delichon · Aug 2, 04:05 · [社区讨论](https://news.ycombinator.com/item?id=49140998)

**背景**: Pelican 是一个基准，通过要求 AI 模型生成骑自行车的鹈鹕的 SVG 来评估其对物理世界的理解。该任务需要空间推理、物体交互和物理合理性，超越了简单的图像生成。该基准是 AI 评估中更广泛趋势的一部分，旨在测试模型的具身智能和世界模型，相关项目如 Pelican-VL 和 Pelican-Unified 也体现了这一点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/jlebensold/pelican-benchmark">GitHub - jlebensold/ pelican - benchmark : Pelican -on-Bicycle SVG...</a></li>
<li><a href="https://explainx.ai/blog/are-ai-labs-pelicanmaxxing-study-july-2026">Are AI Labs Pelicanmaxxing? A Statistical Study | explainx.ai</a></li>
<li><a href="https://simonwillison.net/2026/Jun/9/andrej-karpathy/">A quote from Andrej Karpathy | Simon Willison’s Weblog</a></li>

</ul>
</details>

**社区讨论**: 社区讨论表现出复杂情绪。像 YmiYugy 这样的用户担心作者暗示'骑自行车的鹈鹕'问题已解决，同时指出 AI 内容提高了对速度的期望但降低了质量。其他人如 jmugan 则认为该基准的目的是揭示物理世界理解，而不仅仅是产生精美的输出。一些评论者分享了实践经验，如 bredren 使用 LLM 进行 3D 动画，其他人如 HarHarVeryFunny 质疑模型是否专门训练生成 three.js 代码。

**标签**: `#AI`, `#benchmarking`, `#Karpathy`, `#physical world understanding`, `#model evaluation`

---

<a id="item-4"></a>
## [F*：面向验证软件的证据导向编程语言](https://fstar-lang.org/) ⭐️ 7.0/10

F* 是一种通用的面向证明的编程语言，它将依赖类型与基于 SMT 的证明自动化相结合，并因其能够将现有 C 代码库增量迁移到验证环境而在社区中受到关注。该语言默认编译为 OCaml，并支持提取到 F#、C 或 Wasm。 F* 之所以重要，是因为它使开发者能够正式验证软件属性，如功能正确性，这对高保证系统至关重要。其增量 C 迁移能力为在现有代码库中采用形式验证提供了一条实用路径，可能提高各行业软件的可靠性。 F* 支持纯函数式和带效果编程，其证明自动化依赖于 SMT 求解和基于策略的交互式定理证明。该语言在 GitHub 上积极开发，有在线书籍《Proof-Oriented Programming in F*》和教程，但社区反馈指出主页上缺乏易于访问的语法示例。

hackernews · ducktective · Aug 2, 12:31 · [社区讨论](https://news.ycombinator.com/item?id=49143925)

**背景**: F*（读作 F star）是一种受 ML、Caml 和 OCaml 启发的高级多范式编程语言，旨在进行程序验证。它是一种依赖类型语言和证明助手，能够表达精确的规范并证明程序的性质。该语言是形式验证更广泛趋势的一部分，Frama-C 和基于 Rust 的方法等工具也用于验证和迁移遗留代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language) - Wikipedia</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>
<li><a href="https://github.com/FStarLang/FStar">GitHub - FStarLang/FStar: A Proof-oriented Programming ... F* (programming language) - Wikipedia Proof-oriented Programming in F* - fstar-lang.org F*: A Proof-oriented Programming Language - GitHub Proof-Oriented Programming in F* - mtzguido.github.io Internships on the F proof-oriented programming language</a></li>

</ul>
</details>

**社区讨论**: 社区评论反应不一：一些人称赞 F* 在增量迁移 C 代码库方面的坚实支持，而另一些人则批评主页缺乏易于访问的语法示例，使新手难以快速理解该语言。还有人对它的行业使用情况表示好奇，并有人对响应式样式表中的副作用发表了幽默评论。

**标签**: `#formal verification`, `#programming language`, `#proof-oriented`, `#functional programming`, `#software verification`

---

<a id="item-5"></a>
## [eBay 骚扰活动导致 5600 万美元赔偿及监禁判决](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10

eBay 已同意向大卫和伊娜·施泰纳夫妇支付 5600 万美元，这对夫妇曾是 eBay 前安全高管策划的骚扰活动的目标。包括前高级总监吉姆·鲍在内的多名前员工因参与恐吓计划而被判监禁。 此案凸显了企业不当行为和安全人员滥用权力的严重后果，强化了最高层问责的重要性。它警示企业，对批评者进行报复将面临法律和财务风险。 骚扰活动包括发送令人不安的包裹、监视和威胁，针对施泰纳夫妇，因为他们发表了批评 eBay 的文章。eBay 安全团队的七名成员（包括前警察队长）参与其中；吉姆·鲍被判处 57 个月监禁，而布莱恩·吉尔伯特则被判已服刑时间并罚款 2 万美元。

hackernews · JumpCrisscross · Aug 2, 19:19 · [社区讨论](https://news.ycombinator.com/item?id=49147435)

**背景**: eBay 是一个主要的在线市场，用户可以在其中买卖商品。施泰纳夫妇经营一份批评 eBay 商业实践的通讯，促使公司安全团队进行报复。此案凸显了企业安全部门在针对被视为威胁的对象时，可能超越道德和法律界限。

**社区讨论**: 评论者表示怀疑骚扰活动仅限于施泰纳夫妇，质疑是否还有其他批评者成为目标。一些人注意到前警察队长的参与，并呼吁进行更广泛的调查，而另一些人则将其与其他企业不当行为案例相提并论，并讨论了 eBay 高昂的卖家费用。

**标签**: `#corporate accountability`, `#legal`, `#harassment`, `#eBay`, `#security`

---

<a id="item-6"></a>
## [自 1953 年以来，英语学习者核心词汇的变迁](https://pudding.cool/2026/07/essential-words/) ⭐️ 7.0/10

The Pudding 发布了一项数据驱动分析，展示了从 1953 年到 2023 年英语学习者所学核心词汇的变化，从“humble”、“loyalty”等人际词汇转向“community”、“identity”等与身份和社区相关的词汇。 这一分析揭示了 70 年来文化和社会变迁如何反映在语言教育中，影响学习者的优先选择以及他们与英语社区的联系方式。同时，它也引发了关于教学重点和词汇在塑造社会身份中作用的讨论。 “社交-交际”类别的词汇量大小基本不变，但 1953 年的词汇中近四分之一被替换，2023 年的词汇中有 39%是新词。这一转变表明，词汇从描述亲密人际关系的词转向描述更广泛归属感和身份的词。

hackernews · c-oreills · Aug 2, 15:41 · [社区讨论](https://news.ycombinator.com/item?id=49145590)

**背景**: 该分析基于对 1953 年和 2023 年英语学习者核心词汇表的比较，可能使用了语料库或教材中的频率数据。词汇表是语言教学的基础，指导课程设计和学习重点。观察到的变化反映了公共话语中强调身份和社区的更广泛社会趋势。

**社区讨论**: 评论者讨论了创建此类词汇表的难度，有人指出根据学习目标的不同，没有“正确”的答案。另有人将词汇变化与不平等加剧和部落化联系起来。一些人批评文章的呈现方式为“滚动劫持”，而其他人则分享了关于语言变化的个人经历。

**标签**: `#linguistics`, `#education`, `#data-analysis`, `#language-learning`, `#societal-change`

---

<a id="item-7"></a>
## [Bor 0.8：开源 Linux 桌面策略管理，支持实时流式传输](https://getbor.dev/blog/2026-08-02-bor-v080-release/) ⭐️ 7.0/10

开源集中式 Linux 桌面管理系统 Bor 发布了 0.8 版本，新增了对 Thunderbird、Microsoft Edge for Business 和 FirewallD 区域的新策略类型。该系统使用 Go 代理和服务器，通过 mTLS/gRPC 实时流式传输策略，无需轮询。 这填补了 Linux 桌面管理领域的重大空白，为手动配置或现有工具提供了现代替代方案。其实时流式架构可以提高管理 Linux 工作站的组织在策略执行方面的效率和响应速度。 0.8 版本引入了针对 Thunderbird、Microsoft Edge for Business 和 FirewallD 区域的新策略类型，并包含改进和修复。架构使用 mTLS 进行安全认证，gRPC 进行双向流式传输，确保策略实时推送而无需轮询。

hackernews · eniac111 · Aug 2, 09:06 · [社区讨论](https://news.ycombinator.com/item?id=49142569)

**背景**: Linux 桌面管理通常依赖手动配置或 Ansible 等基于拉取模型的工具。Bor 采用基于推送的方法，通过 mTLS/gRPC 流式传输，提供了一种新颖的替代方案，可能减少配置漂移并提高可扩展性。该项目面向需要集中控制 Firefox、Chrome、KDE、dconf、polkit 和包管理的组织。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://firewalld.org/documentation/zone/">Documentation - Zone | firewalld</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dconf">dconf - Wikipedia</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-08-grpc-mtls-mutual-tls/view">How to Add mTLS (Mutual TLS) to gRPC Services</a></li>

</ul>
</details>

**社区讨论**: 社区成员表现出浓厚兴趣，一位用户表示这非常符合他们管理非营利组织笔记本电脑的需求。问题集中在架构选择（mTLS 与 SSH）、与现有工具的比较、自定义脚本执行、用户映射以及无轮询情况下如何处理配置漂移等方面。

**标签**: `#Linux`, `#desktop management`, `#policy`, `#open-source`, `#gRPC`

---

<a id="item-8"></a>
## [RISC OS Open 庆祝小众操作系统开发 20 周年](https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open) ⭐️ 6.0/10

RISC OS Open（ROOL）于 2026 年 6 月 20 日庆祝其成立 20 周年，标志着该项目管理 RISC OS 开源发布和持续开发已有二十年。这一里程碑凸显了该项目在维护这一最初由 Acorn Computers 创建的小众操作系统方面的坚持。 这一周年纪念凸显了在主流平台主导的生态系统中，社区驱动的开源操作系统仍能持续生存。这对复古计算爱好者和开源倡导者具有重要意义，展示了在原始供应商停止运营后，一个专注的社区如何能够长期维持一个遗留系统。 RISC OS Open 由前 Pace 员工创立，Pace 在 Acorn 倒闭后收购了 RISC OS，该项目负责监督 RISC OS 源代码的发布。RISC OS 5.0 于 2018 年开源，该操作系统以在树莓派等硬件上启动速度快而闻名。

hackernews · AlexeyBrin · Aug 2, 12:36 · [社区讨论](https://news.ycombinator.com/item?id=49143967)

**背景**: RISC OS 是一款模块化操作系统，最初由 Acorn Computers 为其基于 ARM 的机器（如 Archimedes 和 Risc PC）开发。尽管 Acorn 倒闭，该操作系统通过社区努力得以延续，RISC OS Open 负责管理其开源开发。该系统轻量高效，专为 RISC 架构设计，并继续由一个虽小但活跃的社区进行更新。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS">RISC OS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS_Open">RISC OS Open - Wikipedia</a></li>
<li><a href="https://www.riscosopen.org/content/">RISC OS Open: Welcome</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人轶事和技术见解，有人回忆曾为 RISC OS 开发软件，也有人对该项目的坚持表示惊讶。一些人强调了该系统在树莓派上启动速度快，另一些人则指出 Sibelius 等著名应用程序起源于 RISC OS。

**标签**: `#RISC OS`, `#Open Source`, `#Retro Computing`, `#Operating Systems`

---

<a id="item-9"></a>
## [Meshdiff：浏览器中的客户端 STL 比较工具](https://meshdiff.com/) ⭐️ 6.0/10

Meshdiff 是一款新的基于浏览器的工具，允许用户完全在客户端视觉比较两个 STL 文件版本，无需将文件上传到服务器。它提供三个视口进行并排和叠加比较，社区建议添加同步视图旋转和 GitHub 集成等功能。 该工具解决了 3D 打印和 CAD 工作流程中常见的文件版本比较需求。其客户端方法增强了隐私性和速度，社区的积极反应表明它可能成为设计师和工程师的有用工具。 Meshdiff 完全在浏览器中运行，可能使用 WebGL 或 Three.js 进行渲染，并支持 3D 打印中常见的 STL 文件。该工具目前提供三个视口，社区成员已请求同步相机控制和与 GitHub 集成，以便在拉取请求中进行自动比较。

hackernews · projscope · Aug 2, 11:34 · [社区讨论](https://news.ycombinator.com/item?id=49143479)

**背景**: STL 是一种用于 3D 打印和 CAD 的文件格式，将表面几何表示为三角网格，不包含颜色或纹理。客户端处理意味着文件在浏览器本地处理，提高了隐私性并减少了服务器负载。像 Meshdiff 这样的工具利用 WebGL 和 WebAssembly 等现代 Web 技术，在浏览器中实现复杂的 3D 可视化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/STL_(file_format)">STL (file format)</a></li>
<li><a href="https://www.adobe.com/creativecloud/file-types/image/vector/stl-file.html">STL files explained | Learn about the STL file format | Adobe</a></li>

</ul>
</details>

**社区讨论**: 社区反应积极，用户称赞该工具的实用性和对客户端的重视。建议包括同步视口旋转、锁定视图以及作为 GitHub PR 触发器嵌入 3D 文件。一位用户最初将 STL 与 C++ 标准模板库混淆，但其他人澄清了上下文。

**标签**: `#3D`, `#STL`, `#browser-tool`, `#visualization`, `#CAD`

---

<a id="item-10"></a>
## [仅靠版税无法说服艺术家接受 AI 训练](https://www.theverge.com/ai-artificial-intelligence/974018/pippa-seedance-artist-royalties) ⭐️ 6.0/10

《The Verge》文章探讨了向艺术家支付版税是否足以解决他们对生成式 AI 模型未经许可使用其作品进行训练的反对意见。文章指出，尽管有补偿提议，许多艺术家仍不买账，认为这种做法本质上是剥削性的。 这场争论对生成式 AI 和版权法的未来至关重要，影响艺术家、AI 公司和政策制定者。其结果可能为 AI 训练数据的获取和补偿方式树立先例，影响行业的伦理和法律格局。 文章提及正在进行的法律斗争和艺术家抗议，例如 2024 年 10 月超过 10,500 名创意人士签署声明谴责未经授权的 AI 训练。文章还指出，一些提案如印度的强制版税制度正在出现，但面临实际挑战。

rss · The Verge · Aug 2, 13:00

**背景**: 像 GPT-4 和 Stable Diffusion 这样的生成式 AI 模型是在从互联网抓取的海量数据集上训练的，这些数据通常包含受版权保护的作品。艺术家认为这构成盗窃，而 AI 公司则主张合理使用或文本与数据挖掘例外。法律框架因司法管辖区而异，美国依赖合理使用，欧洲则依赖 TDM 例外。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf">Copyright and Artificial Intelligence, Part 3: Generative AI ...</a></li>
<li><a href="https://arxiv.org/pdf/2502.15858">Generative AI Training and Copyright Law</a></li>
<li><a href="https://www.technologyreview.com/2023/10/23/1082189/data-poisoning-artists-fight-generative-ai/">This new data poisoning tool lets artists fight back against ... Artists Fight Back Against Unethical AI Training The Ethics of Using Artists' Work Without Consent to Train AI ... AI Training and Copyright: The Fight for Creative Consent</a></li>

</ul>
</details>

**社区讨论**: 此新闻条目未提供社区评论。

**标签**: `#AI ethics`, `#generative AI`, `#copyright`, `#artists`, `#compensation`

---