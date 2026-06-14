---
layout: default
title: "Horizon Summary: 2026-06-14 (ZH)"
date: 2026-06-14
lang: zh
---

> From 36 items, 10 important content pieces were selected

---

1. [里约自称自研的大语言模型被发现是现有模型的合并](#item-1) ⭐️ 8.0/10
2. [Jane Street 谈形式化方法与 AI 代码验证](#item-2) ⭐️ 8.0/10
3. [2014 年演讲预言 JavaScript 的兴衰](#item-3) ⭐️ 8.0/10
4. [Kage：将网站归档为单个离线二进制文件](#item-4) ⭐️ 7.0/10
5. [AI 采用率不如炒作所示](#item-5) ⭐️ 7.0/10
6. [FBI 建造模拟小镇用于网络攻击训练](#item-6) ⭐️ 7.0/10
7. [中国可能已接触 Anthropic 的 Mythos AI 模型](#item-7) ⭐️ 7.0/10
8. [Zeroserve 提升 Caddy 兼容性，吞吐量达 3 倍](#item-8) ⭐️ 6.0/10
9. [保罗·格雷厄姆谈打造十亿美元初创公司](#item-9) ⭐️ 6.0/10
10. [资深开发者：主题公园 MMO 已不再可行](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [里约自称自研的大语言模型被发现是现有模型的合并](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

一项调查显示，里约热内卢声称自研的大语言模型 Rio-3.5-Open-397B 实际上是约 60% Nex-N2 Pro 和 40% Qwen3.5-397B-A17B 的加权合并，没有证据表明进行了额外训练。 这引发了对 AI 开发透明度和归属问题的严重担忧，因为市政府将一个合并模型作为自研创新呈现，可能误导公众和 AI 社区。 权重张量分析显示，Rio 模型中的每个权重张量在所有 60 层和组件中，以数千个标准差的程度，都是 Nex 和 Qwen 的 0.6/0.4 混合，这种模式在典型的微调中并不存在。

hackernews · unrvl22 · Jun 14, 15:37 · [社区讨论](https://news.ycombinator.com/item?id=48528371)

**背景**: 模型合并是一种将多个训练好的模型的权重组合成一个模型的技术，无需额外训练，通常使用线性插值。它已成为大语言模型开发的主流方法，但在开源实践中，对基础模型的适当归属是预期的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/arcee-ai/mergekit">GitHub - arcee-ai/mergekit: Tools for merging pretrained large language ...</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs - NVIDIA Developer</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：一些人辩护称上传的模型可能缺少蒸馏步骤，而另一些人则批评缺乏归属。一位评论者指出深度学习模型的鲁棒性，简单的线性组合就能提升性能。

**标签**: `#LLM`, `#AI ethics`, `#model merging`, `#open source`, `#transparency`

---

<a id="item-2"></a>
## [Jane Street 谈形式化方法与 AI 代码验证](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street 发表了一篇博客文章，讨论形式化方法在编程中的实际应用及其验证 AI 生成代码的潜力，引发了社区讨论，获得 165 个点赞和 52 条评论。 随着 AI 生成更多代码，形式化方法可以将人类价值从编写代码转向验证代码，从而提高软件工程的可靠性和安全性。 该文章指出，形式化方法已从早期的 Boyer-Moore 定理证明器发展到 Scala 3 中的现代类型系统，并且可以帮助防止 AI 生成代码中的“名词堆积”等问题。

hackernews · eatonphil · Jun 14, 12:35 · [社区讨论](https://news.ycombinator.com/item?id=48526633)

**背景**: 形式化方法是用于规范和验证软件与硬件系统的数学严格技术，包括定理证明、模型检测和类型系统。历史上，它们需要大量人力引导证明，但现代工具和 AI 正使其更加实用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_methods">Formal methods - Wikipedia</a></li>
<li><a href="https://web.mit.edu/16.35/www/lecturenotes/FormalMethods.pdf">Introducing Formal Methods - MIT</a></li>
<li><a href="https://formal.epfl.ch/">Formal Methods Portal</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了不同观点：有人回忆了早期使用 SAT 求解器的证明自动化，有人称赞 Scala 3 中用于编译时证明的表达类型，还有人质疑形式化规范是否只是“以不同方式编写的测试”，并可能遭受相同的错误。

**标签**: `#formal methods`, `#programming`, `#verification`, `#AI`, `#software engineering`

---

<a id="item-3"></a>
## [2014 年演讲预言 JavaScript 的兴衰](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

Gary Bernhardt 在 2014 年的一次演讲中幽默地预言了 JavaScript 作为编译目标的统治地位及其最终被取代，这一预言随着 WebAssembly 和 TypeScript 的兴起已被证实具有先见之明。 该演讲对 JavaScript 演变以及 WebAssembly 等编译目标出现的准确预见至今仍极具相关性，影响着开发者对 Web 技术未来的思考。 演讲特别提到了 asm.js 作为编译目标，该技术后来被 WebAssembly 取代，并正确预言了 JavaScript 将成为一种通用的中间语言。

hackernews · subset · Jun 14, 12:38 · [社区讨论](https://news.ycombinator.com/item?id=48526661)

**背景**: 编译目标是指其他语言被编译成的语言，例如机器码或字节码。JavaScript 最初是浏览器的脚本语言，现已通过 WebAssembly 成为 TypeScript 和 C++等语言的流行编译目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://softwareengineering.stackexchange.com/questions/344599/what-exactly-is-a-compile-target">compiler - What exactly is a compile target? - Software ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compiler">Compiler - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者指出该演讲惊人地准确，有人开玩笑说它预言了 2020-2025 年间的全球灾难但类型错了。其他人讨论了 WebAssembly 的局限性，如无法直接操作 DOM，以及 JavaScript 作为胶水代码的持续依赖。

**标签**: `#JavaScript`, `#WebAssembly`, `#compilation target`, `#programming languages`, `#tech talk`

---

<a id="item-4"></a>
## [Kage：将网站归档为单个离线二进制文件](https://github.com/tamnd/kage) ⭐️ 7.0/10

Kage 是一款新的开源工具，可将任何网站克隆到文件夹中供离线浏览，去除所有脚本，并可选择将归档文件附加到自身副本上，生成一个可离线提供网站服务的单一可执行文件。 该工具简化了网站的离线访问，使得将整个站点作为单个无依赖的二进制文件分发变得容易，特别适用于文档、维基或任何需要在无网络区域使用的内容。 该工具使用 `--format binary` 标志创建一个单一可执行文件，将归档站点与内置服务器捆绑在一起；生成的二进制文件可通过 `kage serve` 运行以提供静态内容。

hackernews · tamnd · Jun 14, 17:25 · [社区讨论](https://news.ycombinator.com/item?id=48529990)

**背景**: 像 HTTrack 和 SingleFile 这样的网站归档工具早已存在，但它们通常生成文件夹或单个 HTML 文件。Kage 将整个站点打包成带有内置服务器的单个二进制文件的方法很新颖，利用了 Go 语言创建独立可执行文件的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/tamnd/kage">GitHub - tamnd/ kage : Shadow any website for offline viewing, with the...</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到该工具在离线维基和文档方面的潜力，但有人质疑既然静态 HTML 文件就足够，为何还需要服务器；其他人则指出 SingleFile 或 HTTrack 等替代方案在某些用例中更强大。

**标签**: `#offline`, `#archiving`, `#static-site`, `#tool`, `#open-source`

---

<a id="item-5"></a>
## [AI 采用率不如炒作所示](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they) ⭐️ 7.0/10

Gabriel Weinberg 认为，尽管 AI 炒作火热，仍有相当一部分人很少使用 AI，真正的采用将来自将 AI 嵌入现有软件，而非独立的聊天界面。 这挑战了“人人都在使用 AI”的主流说法，揭示了认知与现实之间的差距，可能影响 AI 行业的投资和产品策略。 文章引用了一项研究，显示超过 50%的人每周使用 AI 不到一次，并指出 AI 采用将通过集成到现有工具中增长，而非通过专用聊天界面。

hackernews · yegg · Jun 14, 14:44 · [社区讨论](https://news.ycombinator.com/item?id=48527700)

**背景**: 自 2022 年底 ChatGPT 推出以来，媒体广泛报道 AI 在各行各业迅速普及。然而，实际使用数据显示情况更为复杂，许多人尝试过 AI 但并未将其融入日常生活。

**社区讨论**: 评论者讨论了在求职面试中回答 AI 使用问题的挑战，一些人指出 AI 代码生成仍需大量人工监督。其他人同意将 AI 嵌入现有软件是更广泛采用的关键，而少数人表示根本没有使用 AI。

**标签**: `#AI adoption`, `#LLMs`, `#software engineering`, `#technology trends`, `#community discussion`

---

<a id="item-6"></a>
## [FBI 建造模拟小镇用于网络攻击训练](https://www.theverge.com/tech/949648/fbi-fake-town-cyberattacks-kinetic-cyber-range) ⭐️ 7.0/10

FBI 在阿拉巴马州亨茨维尔开设了一个占地 22000 平方英尺的网络靶场，物理复制了一个小镇，包括便利店、加油站和医院等建筑，用于模拟网络攻击训练。 该设施为 FBI 特工提供了独特的沉浸式环境，使其能够在真实场景中练习应对网络威胁，弥合了数字与物理安全训练之间的差距。 该靶场被称为“动能网络靶场”，位于 FBI 在红石兵工厂的北校区，由该局的操作技术部门运营。

rss · The Verge · Jun 14, 20:35

**背景**: FBI 长期以来一直使用像 Hogan's Alley 这样的物理模拟城镇进行战术训练。动能网络靶场将这一概念扩展到网络安全领域，使特工能够针对影响物理基础设施的网络攻击进行训练。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.fbi.gov/news/stories/inside-the-fbis-kinetic-cyber-range">Inside the FBI's Kinetic Cyber Range — FBI</a></li>
<li><a href="https://www.hstoday.us/subject-matter-areas/law-enforcement-and-public-safety/inside-the-fbis-massive-kinetic-cyber-range-in-huntsville/">Inside the FBI's Massive Kinetic Cyber Range in Huntsville</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#FBI`, `#training`, `#simulation`

---

<a id="item-7"></a>
## [中国可能已接触 Anthropic 的 Mythos AI 模型](https://www.theverge.com/ai-artificial-intelligence/949644/china-white-house-anthropic-mythos) ⭐️ 7.0/10

据 Semafor 报道，白宫对 Anthropic 的 Mythos AI 模型实施出口限制的部分原因是担心一个与中国有关的组织已接触该模型。 如果属实，这种接触可能使中国获得先进的 AI 能力，构成严重的国家安全风险，并加速中美之间的 AI 军备竞赛。 报告特别提到 Mythos 5 或 Fable 5，这是 Anthropic 最先进的模型；Fable 5 是 Mythos 5 的安全调优版本，而 Mythos 5 仅通过 Project Glasswing 有限发布。

rss · The Verge · Jun 14, 18:27

**背景**: Anthropic 是一家 AI 安全公司，开发了 Claude 等大语言模型。Mythos 是其最强大的模型，因在网络安全等敏感领域的高级能力被认为过于危险而无法公开发布。出口限制旨在防止对手获得此类技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs</a></li>

</ul>
</details>

**标签**: `#AI`, `#national security`, `#export controls`, `#Anthropic`

---

<a id="item-8"></a>
## [Zeroserve 提升 Caddy 兼容性，吞吐量达 3 倍](https://su3.io/posts/zeroserve-caddy-compat) ⭐️ 6.0/10

基于 io_uring 的 HTTPS 服务器 Zeroserve 现已声称兼容 Caddy，相比标准 Caddy 实现了 3 倍吞吐量和 70% 的延迟降低。 这一性能飞跃可能吸引追求高速 Web 服务的用户，但缺乏 ACME 和插件支持限制了其在生产环境中的实际采用。 兼容性是部分的：zeroserve 可以编译并提供 Caddy 配置，但不支持 ACME 自动 HTTPS 或 Caddy 插件，而这些是许多用户的核心功能。

hackernews · losfair · Jun 14, 13:43 · [社区讨论](https://news.ycombinator.com/item?id=48527145)

**背景**: Caddy 是一款流行的 Web 服务器，以其通过 ACME 实现的自动 HTTPS 和丰富的插件生态系统而闻名。Zeroserve 是一款较新的高性能服务器，基于 Linux 的 io_uring 异步 I/O 接口构建，旨在实现零配置和 eBPF 脚本。io_uring 提供低开销、零拷贝的 I/O 操作，可显著提升吞吐量并降低延迟。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/losfair/zeroserve">GitHub - losfair/zeroserve: Zero-config, fast `io_uring`-based HTTPS server. · GitHub</a></li>
<li><a href="https://su3.io/posts/introducing-zeroserve">zeroserve: a zero-config web server you can script with eBPF</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户认为缺少 ACME 和插件支持是不可接受的，而另一些用户则对性能数据印象深刻。此外，还有关于使用 io_uring 构建 Web 服务器安全性的技术讨论，涉及网络安全方面的担忧。

**标签**: `#web server`, `#performance`, `#Caddy`, `#io_uring`, `#Rust`

---

<a id="item-9"></a>
## [保罗·格雷厄姆谈打造十亿美元初创公司](https://paulgraham.com/earn.html) ⭐️ 6.0/10

保罗·格雷厄姆发表了一篇题为《如何赚十亿美元》的文章，概述了打造十亿美元初创公司的策略，强调创造和获取价值。 这篇文章提供了一个财富创造框架，可能影响有抱负的企业家和投资者，并引发关于极端财富积累伦理的辩论。 文章认为十亿美元财富来自创造新价值而非攫取，但评论中的批评者以 Uber 颠覆出租车司机为例提出异议。

hackernews · kingstoned · Jun 14, 11:50 · [社区讨论](https://news.ycombinator.com/item?id=48526360)

**背景**: 保罗·格雷厄姆是知名风险投资家和创业加速器 Y Combinator 的联合创始人。他关于初创公司和创业的文章在科技界广为流传。

**社区讨论**: 评论褒贬不一：有人称赞文章的见解，也有人批评其为财富攫取辩护，并忽视了创造性破坏等负面外部性。

**标签**: `#startups`, `#wealth`, `#entrepreneurship`, `#Paul Graham`

---

<a id="item-10"></a>
## [资深开发者：主题公园 MMO 已不再可行](https://www.pcgamer.com/games/mmo/ultima-online-and-star-wars-galaxies-vet-tells-me-the-theme-park-assembly-line-mmo-just-isnt-viable-anymore-especially-as-dev-costs-spike-we-hit-the-wall/) ⭐️ 6.0/10

一位《网络创世纪》和《星球大战：星系》的资深开发者认为，由于开发成本飙升以及玩家对盈利模式的不满，传统的主题公园 MMO 已不再可行。 这一评论凸显了 MMO 行业的关键转变：不断上升的成本和玩家期望的变化使经典的主题公园模式难以为继，可能影响未来的游戏设计和商业策略。 该开发者指出，MMO 玩家感到‘服务不足且过度收费’，行业在主题公园流水线模式上已经‘撞墙’。MMO 的开发成本已飙升，例如亚马逊的《新世界》耗资数亿美元。

rss · PC Gamer · Jun 14, 15:00

**背景**: 主题公园 MMO 是引导玩家通过一系列预设景点或任务的游戏，类似于现实中的主题公园。这与提供更多自由和涌现式玩法的沙盒 MMO 形成对比。该类型面临开发成本上升和其他娱乐形式的竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/amazon-axes-mmos-pivots-to-ai-party-games-in-gaming-shakeup">Amazon axes MMOs, pivots to AI party games in... | The Tech Buzz</a></li>
<li><a href="https://forums.mmorpg.com/discussion/315163/sandbox-vs-theme-park-style-mmos">Sandbox vs Theme Park style MMOs — MMORPG.com Forums</a></li>

</ul>
</details>

**标签**: `#MMO`, `#game development`, `#industry trends`, `#monetization`

---