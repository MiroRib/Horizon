---
layout: default
title: "Horizon Summary: 2026-07-12 (ZH)"
date: 2026-07-12
lang: zh
---

> From 46 items, 12 important content pieces were selected

---

1. [Claude Code 与 OpenCode 的 Token 开销对比](#item-1) ⭐️ 8.0/10
2. [菲尔兹奖得主陶哲轩用 LLM 编码代理做可视化](#item-2) ⭐️ 8.0/10
3. [LLM 炒作与现实：价值捕获与开源转向](#item-3) ⭐️ 8.0/10
4. [电影 CGI 与编程 LLM：劳动力类比](#item-4) ⭐️ 8.0/10
5. [Chromium 148 的 Math.tanh 可实现操作系统指纹识别](#item-5) ⭐️ 7.0/10
6. [爱尔兰数据中心耗电量已达全国 23%](#item-6) ⭐️ 7.0/10
7. [带状疱疹疫苗或可降低痴呆风险](#item-7) ⭐️ 7.0/10
8. [Ghostel.el：基于 libghostty 的快速 Emacs 终端](#item-8) ⭐️ 7.0/10
9. [苹果失败的汽车项目催生了强大的 AI 芯片](#item-9) ⭐️ 7.0/10
10. [LARP 网站讽刺创业公司收入基础设施](#item-10) ⭐️ 6.0/10
11. [反对 AI 数据中心的斗争才刚刚开始](#item-11) ⭐️ 6.0/10
12. [荷兰消费者组织起诉索尼数字游戏控制权](#item-12) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Claude Code 与 OpenCode 的 Token 开销对比](https://systima.ai/blog/claude-code-vs-opencode-token-overhead) ⭐️ 8.0/10

一项实证研究发现，Claude Code 在读取用户提示前发送约 33,000 个 token，而 OpenCode 仅发送约 7,000 个 token，相差 4.7 倍，原因是缓存策略低效和工具框架开销大。 这种 token 低效直接增加了使用 Claude Code 的开发者的成本，尤其是在涉及子代理的复杂任务中，并引发了对专有编码工具透明度和盈利动机的担忧。 该研究在编码工具与 Anthropic 端点之间的 API 边界测量了 token 使用量，捕获了所有请求和使用块。Claude Code 的基础系统提示本身超过 10,000 个 token，子代理编排可能额外增加数万个 token。

hackernews · systima · Jul 12, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48883275)

**背景**: 像 Claude Code 和 OpenCode 这样的智能编码工具使用大语言模型来辅助软件开发任务。它们在用户实际请求之前向模型发送系统提示、工具定义和上下文，这会消耗 token 并产生成本。Token 效率对于成本管理和性能至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://systima.ai/blog/claude-code-vs-opencode-token-overhead">Claude Code Sends 4.7x More Tokens Than... | Systima Blog</a></li>
<li><a href="https://github.com/anthropics/claude-code/issues/14963">Prompt Caching Inefficiency - Dynamic Variables Placed Before...</a></li>
<li><a href="https://prowe214.medium.com/agentic-coding-harnesses-a-comparison-4db34b87fd5c">Agentic Coding Harnesses: A Comparison | by Paul Cullen Rowe | Medium</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，子代理是 token 浪费的主要来源，有用户报告单个任务启动了 7 个子代理。其他人怀疑 Anthropic 故意夸大 token 使用量以推动订阅收入，并指出 Claude Code 自二月以来变得更加不透明。研究作者计划添加定性比较并复现输入/输出。

**标签**: `#AI coding tools`, `#token efficiency`, `#Claude Code`, `#OpenCode`, `#cost analysis`

---

<a id="item-2"></a>
## [菲尔兹奖得主陶哲轩用 LLM 编码代理做可视化](https://terrytao.wordpress.com/2026/07/11/old-and-new-apps-via-modern-coding-agents/) ⭐️ 8.0/10

菲尔兹奖得主陶哲轩展示了使用基于 LLM 的编码代理为学术论文构建交互式可视化，展现了 AI 辅助软件开发的变革潜力。 陶哲轩指出，由于这些可视化并非论文核心的关键任务，使用 LLM 代理的下行风险是可以接受的，这反映了对 AI 可靠性的平衡看法。

hackernews · subset · Jul 12, 11:09 · [社区讨论](https://news.ycombinator.com/item?id=48880170)

**背景**: LLM 编码代理是使用大型语言模型辅助软件开发任务的 AI 系统，如代码生成、调试和可视化。截至 2026 年 7 月，像 Claude Fable 5 这样的模型在编码基准测试中领先，能力日益增强。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://benchlm.ai/coding">Best LLMs for Coding — July 2026 Leaderboard | BenchLM.ai</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI-assisted_software_development">AI-assisted software development</a></li>
<li><a href="https://github.com/kaushikb11/awesome-llm-agents">GitHub - kaushikb11/awesome-llm-agents: A curated list of ... Best AI Coding Agents (June 2026): Scored Leaderboard Best Open-Source LLM Models in 2026: Coding, Local, Agentic ... 20 Best AI Coding Agents in 2026 — Agentic.ai Release: llm-coding-agent 0.1a0 - simonwillison.net</a></li>

</ul>
</details>

**社区讨论**: 评论者对实际影响表示兴奋，有人指出 LLM 使他们能够构建一直想要但没时间做的可视化。其他人幽默地将陶哲轩使用编码代理比作米其林星级厨师发现微波炉晚餐，既突出了新颖性也指出了工具的局限性。

**标签**: `#LLM`, `#coding agents`, `#AI-assisted development`, `#education`, `#visualization`

---

<a id="item-3"></a>
## [LLM 炒作与现实：价值捕获与开源转向](https://geohot.github.io//blog/jekyll/update/2026/07/12/i-love-llms.html) ⭐️ 8.0/10

一篇批判性博客文章指出，前沿 AI 实验室可能无法捕获它们创造的巨大价值，并注意到向使用 LLM 构建个性化开源软件的转变。 这挑战了前沿实验室的高估值，并凸显了 AI 价值可能重新分配给最终用户和开源社区，重塑 AI 行业的经济格局。 文章强调，虽然 LLM 提高了生产力，但由此产生的软件通常保持私有或高度定制化，不公开可见。它还警告说，轻松分叉可能会分裂开源项目。

hackernews · therepanic · Jul 12, 18:31 · [社区讨论](https://news.ycombinator.com/item?id=48883343)

**背景**: 前沿 AI 实验室是开发最强大 AI 系统的组织，如 OpenAI、Google DeepMind 和 Anthropic。价值捕获指的是 AI 创造的经济价值中有多少被开发者保留，而非用户或其他实体。文章认为，尽管生产力大幅提升，但随着用户越来越依赖开源替代品和定制解决方案，前沿实验室可能难以将其模型货币化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.longtermwiki.com/wiki/E820">Frontier AI Labs (Overview) | Longterm Wiki</a></li>
<li><a href="https://newsletter.semianalysis.com/p/ai-value-capture-the-shift-to-model">AI Value Capture - The Shift To Model Labs</a></li>

</ul>
</details>

**社区讨论**: 评论者基本同意价值捕获的论点，指出前沿实验室的订阅价格对于重度用户来说是明智之选。一些人担心，借助 LLM 轻松分叉可能会分裂开源社区，减少向上游贡献的动力。

**标签**: `#LLM`, `#AI hype`, `#open source`, `#value capture`, `#software engineering`

---

<a id="item-4"></a>
## [电影 CGI 与编程 LLM：劳动力类比](https://fabiensanglard.net/extinct/index.html) ⭐️ 8.0/10

Fabien Sanglard 发表了一篇文章，将电影中 CGI 的兴起与软件开发中 LLM 的采用进行类比，认为这两种趋势都贬低了熟练劳动力的价值，并可能最终面临反弹。 这一类比引发了关于 LLM 对软件工程职业长期影响的批判性讨论，呼应了 CGI 如何通过贬低实际特效来改变电影行业，并导致对传统工艺的回归。 文章指出，虽然 LLM 提高了生产力，但它们可能降低手写代码的感知价值，类似于 CGI 使实际特效贬值。社区评论强调，非工会化的 VFX 工作室剥削了 CGI 艺术家，类似的情况可能在科技行业出现。

hackernews · zdw · Jul 12, 15:17 · [社区讨论](https://news.ycombinator.com/item?id=48881830)

**背景**: CGI（计算机生成图像）从 1990 年代开始彻底改变了电影制作，实现了壮观的视觉效果，但往往以贬低实际特效和熟练工匠为代价。类似地，像 GPT-4 这样的大型语言模型（LLM）越来越多地用于代码生成，引发了对编程技能贬值和就业保障的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Computer-generated_imagery">Computer-generated imagery - Wikipedia</a></li>
<li><a href="https://benchlm.ai/coding">Best LLMs for Coding — July 2026 Leaderboard | BenchLM.ai</a></li>
<li><a href="https://huggingface.co/blog/daya-shankar/open-source-llms">Best Open-Source LLM Models in 2026: Coding, Local, Agentic ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多同意这一类比，ChiperSoft 指出非工会化的 VFX 工作室剥削了 CGI 艺术家，类似的情况可能在科技行业出现。一些人不同意拒绝 LLM 会导致落后的说法，认为数量不是唯一的衡量标准。其他人指出，LLM 生成的测试可能无法测试正确的行为。

**标签**: `#LLMs`, `#software engineering`, `#CGI`, `#analogy`, `#labor`

---

<a id="item-5"></a>
## [Chromium 148 的 Math.tanh 可实现操作系统指纹识别](https://scrapfly.dev/posts/browser-math-os-fingerprint/) ⭐️ 7.0/10

自 Chromium 148 起，Math.tanh 的实现因操作系统而异，网站可通过特定输入调用 tanh 来识别底层操作系统。 这种新颖的指纹识别技术绕过了传统的用户代理伪装，可与其他信号结合形成更强大的设备指纹，引发用户隐私担忧。 该指纹识别之所以有效，是因为不同操作系统使用不同的数学库（如 glibc 与 macOS 数学库），对相同输入产生略有差异的 tanh 结果。最近的 glibc 版本使用了 CORE-MATH 的正确舍入 tanh，从而改变了指纹。

hackernews · joahnn_s · Jul 12, 21:12 · [社区讨论](https://news.ycombinator.com/item?id=48884853)

**背景**: 浏览器指纹识别通过收集设备和浏览器的各种属性来识别用户，无需使用 Cookie。Math.tanh 是 JavaScript 中的双曲正切函数，其浮点实现因不同平台的数学库和舍入模式而异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Browser_fingerprinting">Browser fingerprinting</a></li>
<li><a href="https://www.emmtrix.com/wiki/tanh_Software_Implementation">tanh Software Implementation - emmtrix Wiki</a></li>
<li><a href="https://learn.microsoft.com/en-us/dotnet/api/system.math.tanh?view=net-10.0">Math.Tanh (Double) Method (System) | Microsoft Learn</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，该技术还可识别浏览器版本范围，而正确舍入的超越函数（如 tanh）可减少此类指纹识别。一些人批评文章由 AI 生成，以及背后抓取公司的动机。

**标签**: `#browser fingerprinting`, `#privacy`, `#Chromium`, `#JavaScript`, `#security`

---

<a id="item-6"></a>
## [爱尔兰数据中心耗电量已达全国 23%](https://www.theregister.com/on-prem/2026/07/11/irish-datacenters-now-guzzle-23-of-the-countrys-electricity/5270013) ⭐️ 7.0/10

据一份报告显示，爱尔兰数据中心目前消耗了该国总电力的 23%，较往年大幅增长。 这一趋势引发了对能源可持续性和国家电网压力的担忧，可能影响数据中心扩张和可再生能源目标的政策决策。 23%这一数据基于爱尔兰中央统计局的最新数据，凸显了在云计算和人工智能热潮下数据中心能源需求的快速增长。

hackernews · Bender · Jul 12, 20:16 · [社区讨论](https://news.ycombinator.com/item?id=48884322)

**背景**: 数据中心是容纳计算机系统及相关组件的设施，需要大量电力用于服务器和冷却。由于优惠的企业税率和熟练的劳动力，爱尔兰已成为大型科技公司的枢纽，导致数据中心建设激增。

**社区讨论**: 评论将爱尔兰的情况与其他地区进行比较，指出加州绝对用量更高但占比更低。一些人批评使用“狂饮”等情绪化语言，而另一些人则建议核能可以抵消需求。

**标签**: `#datacenters`, `#energy`, `#infrastructure`, `#Ireland`, `#sustainability`

---

<a id="item-7"></a>
## [带状疱疹疫苗或可降低痴呆风险](https://www.economist.com/leaders/2026/07/09/a-no-brainer-for-protecting-your-brain) ⭐️ 7.0/10

一项利用带状疱疹疫苗年龄资格截止点的英国研究发现，接种疫苗的人在七年内患痴呆症的可能性比未接种者低约 20%。 这一发现表明，一种简单、广泛可用的干预措施可能有助于预防或延缓痴呆症——一种尚无治愈方法的重大公共卫生挑战。它还为了解免疫系统在神经退行性疾病中的作用开辟了新途径。 该研究利用了一个自然实验：年龄刚好低于截止点的人有资格接种疫苗，而刚好高于截止点的人则没有，从而实现了清晰的比较。这种效应是在活带状疱疹疫苗（Zostavax）中观察到的，可能也适用于较新的重组疫苗（Shingrix）。

hackernews · saikatsg · Jul 12, 15:23 · [社区讨论](https://news.ycombinator.com/item?id=48881874)

**背景**: 带状疱疹是由水痘-带状疱疹病毒（该病毒也引起水痘）再激活引起的疼痛性皮疹。痴呆症（包括阿尔茨海默病）影响全球数百万人，且尚无有效的疾病修饰疗法。先前的研究已提示感染与痴呆风险之间存在联系，但因果证据有限。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cidrap.umn.edu/varicella/shingles-vaccine-may-prevent-delay-or-slow-dementia-process">Shingles vaccine may prevent, delay, or slow dementia process | CIDRAP</a></li>
<li><a href="https://www.aarp.org/health/conditions-treatments/shingles-vaccine-lowers-dementia-risk/">Shingles Vaccine May Reduce Dementia Risk, Slow Decline</a></li>
<li><a href="https://hsph.harvard.edu/news/link-between-shingles-vaccine-and-slowed-dementia-is-promising-says-expert/">Link between shingles vaccine and slowed dementia is ‘promising,’ says expert | Harvard T.H. Chan School of Public Health</a></li>

</ul>
</details>

**社区讨论**: 评论者既表达了热情也表达了怀疑。一些人分享了个人经历，称为了降低痴呆风险而提前接种疫苗；另一些人则警告这一发现可能是虚假的，认为接种疫苗的人住院次数更少，因此偶然诊断出痴呆症的机会也更少。一位评论者指出，痴呆症有许多风险因素，而疫苗只针对其中一个。

**标签**: `#dementia`, `#vaccine`, `#public health`, `#epidemiology`, `#aging`

---

<a id="item-8"></a>
## [Ghostel.el：基于 libghostty 的快速 Emacs 终端](https://dakra.github.io/ghostel/) ⭐️ 7.0/10

Ghostel.el 是一款由 libghostty-vt 驱动的新型 Emacs 终端模拟器，在性能上优于 vterm 和 eat 等现有方案。 这为 Emacs 用户提供了更快、更可靠的终端体验，尤其适用于需要流畅渲染的 TUI 应用，并可能成为 Emacs 终端集成的新标准。 Ghostel 基于 libghostty 构建，这是一个跨平台、零依赖的 C 和 Zig 库，用于构建终端模拟器。它具备多种输入模式，以处理终端与编辑器按键所有权之间的固有冲突。

hackernews · signa11 · Jul 12, 08:52 · [社区讨论](https://news.ycombinator.com/item?id=48879504)

**背景**: Emacs 长期以来支持 vterm（基于 libvterm）和 eat 等终端模拟器，但它们在处理现代 TUI 应用时可能存在性能问题。libghostty 是 Ghostty 项目开发的新一代高性能终端核心库，旨在嵌入到各种应用中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ghostty-org/ghostty">GitHub - ghostty-org/ghostty: Ghostty is a fast, feature-rich, and...</a></li>
<li><a href="https://github.com/akermu/emacs-libvterm">GitHub - akermu/emacs-libvterm: Emacs libvterm integration · GitHub</a></li>
<li><a href="https://codeberg.org/akib/emacs-eat">akib/ emacs - eat : Emulate A Terminal, in a region, in... - Codeberg.org</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极，用户报告称与 vterm 相比，性能明显更快，输入处理更可靠。部分用户指出存在偶尔的屏幕清除问题或冻结等小瑕疵，但总体情绪热烈，维护者积极参与并提供功能对比。

**标签**: `#emacs`, `#terminal-emulator`, `#libghostty`, `#open-source`, `#productivity`

---

<a id="item-9"></a>
## [苹果失败的汽车项目催生了强大的 AI 芯片](https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra) ⭐️ 7.0/10

苹果放弃的自动驾驶汽车项目间接促成了神经引擎及其他强大 AI 芯片的开发，这些芯片现在用于其设备中，而即将推出的 M7 Ultra 芯片支持高达 1.5TB 的内存。 这揭示了一个重大技术成功可能源于一个失败的项目，凸显了苹果在设备端 AI 处理上的战略投资，如今这一技术驱动着其整个产品线，并使苹果在 AI 硬件领域占据竞争地位。 汽车处理器从未完成，但对 AI 处理的需求推动了神经引擎的创建，该引擎首次出现在 2017 年的 A11 仿生芯片中。预计将加速 AI 工作负载的 M7 Ultra 芯片正是这一努力的直接产物。

rss · The Verge · Jul 12, 16:27

**背景**: 苹果的自动驾驶汽车项目（代号 Project Titan）是一项历时多年的努力，旨在打造一款自动驾驶电动汽车，但该项目于 2024 年被取消。在开发过程中，苹果意识到需要强大的设备端 AI 芯片进行实时处理，从而催生了神经引擎和 Apple Silicon。Apple Silicon 指的是苹果自研的基于 ARM 架构的芯片，以其集成度和能效而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/964519/apple-silicon-self-driving-car-ai-m7-ultra">Apple’s self-driving car program left a legacy of powerful AI ...</a></li>
<li><a href="https://www.technobezz.com/news/apples-canceled-self-driving-car-program-left-a-legacy-of-powerful-ai-chips">Apple’s canceled self-driving car program left a legacy of ...</a></li>

</ul>
</details>

**标签**: `#Apple`, `#AI chips`, `#self-driving cars`, `#Apple Silicon`, `#hardware`

---

<a id="item-10"></a>
## [LARP 网站讽刺创业公司收入基础设施](https://www.larp.website/) ⭐️ 6.0/10

一个名为 LARP（larp.website）的讽刺网站上线，嘲讽创业文化中普遍存在的收入基础设施和 Y Combinator 批次动态。 这一讽刺揭示了创业融资和收入声明中的荒谬之处，与那些认识到夸大指标和跨批次客户列表的创始人和投资者产生共鸣。 该网站通过提供“战略合作伙伴关系”和虚高估值等功能来模仿收入基础设施工具，其语气模糊了真实与虚假的界限，直到最后一段才揭示真相。

hackernews · BerislavLopac · Jul 12, 16:56 · [社区讨论](https://news.ycombinator.com/item?id=48882569)

**背景**: 创业公司收入基础设施指帮助企业管理计费、订阅和财务指标的工具和服务。Y Combinator 批次中的初创公司经常将其他批次公司列为客户，夸大表面吸引力。该讽刺针对这些做法。

**社区讨论**: 评论者欣赏其幽默，有人表示直到最后才确定这是玩笑。另一人指出近期 YC 批次中跨批次客户列表的普遍性，还有人称该讽刺可能对其目标对象来说过于隐晦。

**标签**: `#satire`, `#startup culture`, `#YC`, `#revenue infrastructure`

---

<a id="item-11"></a>
## [反对 AI 数据中心的斗争才刚刚开始](https://www.theverge.com/column/963346/ai-data-centers-fight) ⭐️ 6.0/10

一份新闻简报预告强调了围绕 AI 数据中心及其对当地电网影响的新兴冲突。 这表明公众和监管机构对能源密集型 AI 基础设施的快速扩张日益抵制，可能重塑科技行业的增长格局。 该文章是一份深度有限的新闻简报引言，但提及了当地社区因电力和环境问题反对数据中心建设的更广泛趋势。

rss · The Verge · Jul 12, 12:00

**背景**: AI 数据中心需要大量电力来运行和冷却服务器，给当地电网带来压力并引发环境担忧。随着 AI 应用的激增，科技公司正在建设更多数据中心，导致与社区在土地使用、能源消耗和排放方面产生冲突。

**标签**: `#AI`, `#data centers`, `#energy`, `#tech industry`

---

<a id="item-12"></a>
## [荷兰消费者组织起诉索尼数字游戏控制权](https://www.pcgamer.com/gaming-industry/dutch-consumer-group-suing-playstation-argues-the-end-of-physical-discs-just-proves-its-point-sony-alone-decides-what-a-game-costs-and-even-how-long-you-are-allowed-to-use-it/) ⭐️ 6.0/10

荷兰一个消费者组织正在起诉索尼，认为放弃实体光盘使索尼对游戏定价和使用拥有过度控制权，包括随时撤销访问权限的能力。 这起诉讼凸显了游戏领域数字所有权日益增长的担忧，消费者失去了转售或永久拥有游戏的能力，可能为数字市场中的消费者权利树立先例。 该消费者组织声称，索尼单方面决定游戏价格和用户允许游玩的时间，而实体光盘的终结消除了竞争和消费者选择。

rss · PC Gamer · Jul 12, 22:05

**背景**: 实体游戏光盘允许转售、借出和永久拥有，而数字游戏与账户绑定并受平台政策约束。索尼的 PlayStation Store 是一个封闭平台，索尼设定价格和条款，不像 Steam 那样提供更友好的消费者功能如退款。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://digitechbytes.com/emerging-consumer-tech-explained/it-s-not-about-physical-vs-digital-games-it-s-about-ownership/">It’s Not About Physical Vs. Digital Games, It’s About Ownership</a></li>
<li><a href="https://www.thecoreitech.com/gaming-computers/digital-vs-physical-games/">Digital vs Physical Games: Pros and Cons Compared</a></li>
<li><a href="https://choostgames.com/blog/physical-vs-digital-games/">Physical vs Digital Games: The Real Trade-Offs in 2026</a></li>

</ul>
</details>

**标签**: `#consumer rights`, `#digital ownership`, `#PlayStation`, `#gaming industry`

---