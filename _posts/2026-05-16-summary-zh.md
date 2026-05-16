---
layout: default
title: "Horizon Summary: 2026-05-16 (ZH)"
date: 2026-05-16
lang: zh
---

> From 43 items, 14 important content pieces were selected

---

1. [NVIDIA 开源 2.6B 世界模型 SANA-WM，可生成 1 分钟 720p 视频](#item-1) ⭐️ 8.0/10
2. [Δ-Mem：基于增量规则的高效 LLM 在线记忆方法](#item-2) ⭐️ 8.0/10
3. [AI 颠覆开放式 CTF 竞赛](#item-3) ⭐️ 8.0/10
4. [DeepSeek-V4-Flash 重燃 LLM 操控兴趣](#item-4) ⭐️ 8.0/10
5. [Julia Evans 告别 Tailwind CSS](#item-5) ⭐️ 7.0/10
6. [《加速》2005 年科幻小说预言 AI 代理](#item-6) ⭐️ 7.0/10
7. [Futhark：带依赖类型的函数式 GPU 语言](#item-7) ⭐️ 7.0/10
8. [粪便移植在自闭症临床试验中展现希望](#item-8) ⭐️ 7.0/10
9. [美国用 AI 检测预测市场内幕交易](#item-9) ⭐️ 7.0/10
10. [博客文章指现代社会过于复杂](#item-10) ⭐️ 6.0/10
11. [深入剖析 HTML 列表，揭示隐藏陷阱](#item-11) ⭐️ 6.0/10
12. [Snap、YouTube、TikTok 和解学校成瘾诉讼](#item-12) ⭐️ 6.0/10
13. [马斯克诉奥特曼案：最后一周双方攻击可信度](#item-13) ⭐️ 6.0/10
14. [欧盟法规推动 Firefox 新增 600 万用户](#item-14) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [NVIDIA 开源 2.6B 世界模型 SANA-WM，可生成 1 分钟 720p 视频](https://nvlabs.github.io/Sana/WM/) ⭐️ 8.0/10

NVIDIA 发布了 SANA-WM，这是一个 26 亿参数的开源世界模型，可在单个 GPU 上生成带精确相机控制的一分钟 720p 视频。 该模型通过生成长时长、高分辨率、物理连贯的视频推动了视频生成技术，在游戏、仿真和机器人领域具有潜在应用。 SANA-WM 基于混合线性扩散变换器，支持六自由度相机控制，但模型权重尚未公开，仅承诺“即将”发布。

hackernews · mjgil · May 16, 12:06 · [社区讨论](https://news.ycombinator.com/item?id=48159445)

**背景**: 世界模型是学习环境内部表示以预测未来状态的 AI 系统，常用于机器人和视频生成。SANA-WM 将此概念扩展到带相机控制的分钟级视频合成，区别于更短、可控性较差的视频生成器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://nvlabs.github.io/Sana/WM/">SANA-WM | Efficient Minute-Scale World Modeling</a></li>
<li><a href="https://arxiv.org/abs/2605.15178">[2605.15178] SANA-WM: Efficient Minute-Scale World Modeling with Hybrid Linear Diffusion Transformer</a></li>
<li><a href="https://www.marktechpost.com/2026/05/16/nvidia-introduces-sana-wm-a-2-6b-parameter-open-source-world-model-that-generates-minute-scale-720p-video-on-a-single-gpu/">NVIDIA Introduces SANA-WM: A 2.6B-Parameter Open-Source World Model ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对“开源”标签表示怀疑，因为权重尚未发布，有人称之为“雾件”。其他人则争论该模型是否真正代表“世界模型”，还是仅仅是一个物理连贯的视频生成器，并注意到合成训练数据类似于电子游戏。

**标签**: `#world model`, `#video generation`, `#open-source`, `#NVIDIA`, `#AI`

---

<a id="item-2"></a>
## [Δ-Mem：基于增量规则的高效 LLM 在线记忆方法](https://arxiv.org/abs/2605.12357) ⭐️ 8.0/10

Δ-Mem 提出了一种基于增量规则学习的方法，将历史信息压缩为固定大小的状态矩阵，以实现大型语言模型的高效在线记忆。 这项研究解决了 LLM 上下文窗口有限的关键挑战，能够在计算成本不按比例增加的情况下实现更高效的长时记忆。它可能改善需要跨会话保留信息的应用，如对话代理和代码助手。 该方法使用增量规则学习来更新固定大小的状态矩阵，将过去的上下文压缩为紧凑表示。然而，社区评论指出，这并未从根本上解决记忆容量问题，因为将压缩信息与查询关联仍然困难。

hackernews · 44za12 · May 16, 09:30 · [社区讨论](https://news.ycombinator.com/item?id=48158506)

**背景**: 大型语言模型通常具有固定的上下文窗口，限制了它们记住对话早期或跨会话信息的能力。在线记忆方法旨在将过去的上下文压缩为更小的表示，以便高效保留和更新。增量规则学习是一种经典的神经网络学习规则，根据预测输出与实际输出之间的误差调整权重。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Learning_rule">Learning rule - Wikipedia</a></li>
<li><a href="https://arxiv.org/html/2602.02195v1">State Rank Dynamics in Linear Attention LLMs</a></li>

</ul>
</details>

**社区讨论**: 社区评论意见不一：一些人欣赏这种方法，但指出它并未解决根本的容量问题；另一些人质疑其新颖性，将其与现有的 DeltaNet 超网络进行比较。此外，还有人对实际应用（如代理记忆指南）感兴趣。

**标签**: `#LLM`, `#memory`, `#efficiency`, `#research`, `#deep learning`

---

<a id="item-3"></a>
## [AI 颠覆开放式 CTF 竞赛](https://kabir.au/blog/the-ctf-scene-is-dead) ⭐️ 8.0/10

一篇博客文章指出，前沿 AI 通过快速获取 flag 的能力破坏了开放式 CTF 格式，削弱了 CTF 旨在培养的协作学习体验。 这很重要，因为 CTF 是网络安全领域的关键教育工具，如果 AI 使挑战变得过于简单，可能会减少动手学习和社区参与。这场辩论凸显了 AI 辅助与技术领域技能发展之间的更广泛张力。 作者指出，AI 现在可以在几分钟内解决许多 CTF 挑战，将焦点从解决问题转向获取 flag。一些评论者建议提高 CTF 难度或禁止 AI，但另一些人认为问题在于当前挑战过于简单。

hackernews · frays · May 16, 07:01 · [社区讨论](https://news.ycombinator.com/item?id=48157559)

**背景**: 夺旗赛（CTF）是网络安全竞赛，参与者需要在存在漏洞的程序或网站中寻找隐藏的文本字符串（flag）。通常采用 jeopardy 或 attack-defense 格式，是道德黑客和安全技能的实践学习方式。开放式 CTF 格式指任何人都可以尝试的公开挑战，通常伴有社区协作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Capture_the_flag_(cybersecurity)">Capture the flag (cybersecurity) - Wikipedia</a></li>
<li><a href="https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/capture-the-flag-ctf-cybersecurity/">What is Capture The Flag? | CTF Types & Important in Cybersecurity</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了复杂情绪：一些人哀叹 AI 破坏了有回报的协作解决问题体验，而另一些人则将其视为创造更难 CTF 的挑战。一位评论者指出，AI 可用于改进混淆工具，暗示挑战创建者与 AI 之间可能存在军备竞赛。

**标签**: `#AI`, `#CTF`, `#cybersecurity`, `#education`, `#community`

---

<a id="item-4"></a>
## [DeepSeek-V4-Flash 重燃 LLM 操控兴趣](https://www.seangoedecke.com/steering-vectors/) ⭐️ 8.0/10

DeepSeek-V4-Flash 这一快速且经济的模型重新激发了人们对 LLM 操控的兴趣，社区项目如 DwarfStar 4 实现了有效的拒绝移除和新型交互方式。 这一进展使操控向量更易用且实用，可能让用户无需重新训练即可定制模型行为，例如去除审查或改变政治倾向，适用于特定应用场景。 DwarfStar 4 是基于 llama.cpp 的独立项目，而非精简版本；它利用 DeepSeek-V4-Flash 内置的操控功能，配合合适的数据集可完全移除拒绝回答。

hackernews · Brajeshwar · May 16, 14:58 · [社区讨论](https://news.ycombinator.com/item?id=48160807)

**背景**: LLM 操控是指在推理过程中向模型激活添加“操控向量”，以引导输出朝向期望行为。2024 年的一篇论文发现，LLM 中的拒绝回答由一个单一方向调控，从而实现了“abliteration”等越狱方法，可精准禁用拒绝功能且副作用极小。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.seangoedecke.com/steering-vectors/">DeepSeek-V4-Flash means LLM steering is interesting again</a></li>
<li><a href="https://arxiv.org/abs/2406.11717">[2406.11717] Refusal in Language Models Is Mediated by a Single Direction</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash">deepseek-ai/DeepSeek-V4-Flash · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出 DwarfStar 4 成功移除了 DeepSeek-V4-Flash 的拒绝回答功能，用户正在探索如何将操控集成到用户界面中以实现有益的交互。有评论纠正称 DwarfStar 4 是独立项目，而非 llama.cpp 的精简版本。

**标签**: `#LLM`, `#steering vectors`, `#DeepSeek`, `#AI safety`, `#uncensoring`

---

<a id="item-5"></a>
## [Julia Evans 告别 Tailwind CSS](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/) ⭐️ 7.0/10

Julia Evans 发表了一篇博文，详细说明了她决定放弃 Tailwind CSS，转而专注于语义化 HTML 和结构化 CSS。她分享了自己学习编写更可维护、更有意义的样式的历程。 这一转变凸显了前端社区中关于实用优先 CSS 框架（如 Tailwind）与传统语义化 HTML 加结构化 CSS 之间日益激烈的争论。它鼓励开发者重新思考他们的样式和可访问性方法。 Evans 强调 Tailwind 颠倒了思考 HTML 和 CSS 的自然顺序，即 HTML 应首先传达含义，然后 CSS 添加样式。她还指出，CSS Modules 提供了更简单的级联问题解决方案，没有 Tailwind 的可读性和工具链缺陷。

hackernews · mpweiher · May 16, 09:14 · [社区讨论](https://news.ycombinator.com/item?id=48158400)

**背景**: Tailwind CSS 是一个实用优先的 CSS 框架，提供底层实用类，可直接在 HTML 中构建设计。语义化 HTML 使用 HTML 元素传达含义，而不仅仅是呈现。争论的焦点在于实用类是否以牺牲语义清晰性和可维护性为代价来提高生产力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Tailwind_CSS">Tailwind CSS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_HTML">Semantic HTML</a></li>
<li><a href="https://tailwindcss.com/">Tailwind CSS - Rapidly build modern websites without ever leaving...</a></li>

</ul>
</details>

**社区讨论**: 社区讨论大多支持 Evans 的观点，许多评论者同意 Tailwind 鼓励不良的 CSS 实践。一些用户主张将 CSS Modules 作为中间方案，而另一些人则认为 Tailwind 的实用类对于快速原型设计仍然有价值。

**标签**: `#CSS`, `#Tailwind CSS`, `#semantic HTML`, `#frontend development`, `#web design`

---

<a id="item-6"></a>
## [《加速》2005 年科幻小说预言 AI 代理](https://www.antipope.org/charlie/blog-static/fiction/accelerando/accelerando.html) ⭐️ 7.0/10

查理·斯特罗斯 2005 年的小说《加速》在 Hacker News 上因其预言准确性而引发讨论，尤其是书中描绘的 AI 代理能自主为用户执行任务，类似于现代的 AI 助手。 这一讨论凸显了科幻小说如何预见现实技术趋势，而小说中的悲剧主题则对追求进步过程中可能失去人性提出了警示。 小说主角通过眼镜使用 AI 代理，以至于离开它们就无法正常生活，这反映了当前对数字助手的依赖。故事由一系列最初于 2001 年至 2004 年发表的相互关联的短篇构成。

hackernews · eamag · May 16, 11:36 · [社区讨论](https://news.ycombinator.com/item?id=48159241)

**背景**: 《加速》是查理·斯特罗斯于 2005 年出版的科幻小说，探讨技术奇点、AI 和后人类主义等主题。小说讲述了 Macx 家族三代人在快速加速的技术环境中的经历。该书以其密集、充满创意的文笔著称，并因其富有想象力的预言而受到赞誉。

**社区讨论**: 评论者指出小说的预言惊人地准确，一位用户提到主角的 AI 代理类似于现代工具如 OpenClaw。另一位读者将这本书重新解读为悲剧，认为人性在技术进步中逐渐被侵蚀。讨论还推荐了类似作品如《量子窃贼》，因其合理的怪异感。

**标签**: `#science fiction`, `#AI agents`, `#futurism`, `#book discussion`

---

<a id="item-7"></a>
## [Futhark：带依赖类型的函数式 GPU 语言](https://futhark-lang.org/examples.html) ⭐️ 7.0/10

Futhark 是一种用于 GPU 计算的函数式数组语言，它利用依赖类型来编码数组大小，从而减少 CUDA 内核中的调试开销。该语言的示例页面展示了其语法和功能。 Futhark 通过在编译时捕获大小不匹配问题，提供了一种更安全、更具表现力的 GPU 代码编写方式，可能减少高性能计算中的错误和开发时间。它在 GPU 编程领域代表了一种小众但创新的方法。 Futhark 属于 ML 语言家族，语法源自 OCaml、Standard ML 和 Haskell，并具有大小依赖类型。该语言是纯函数式的，专为 GPU 上的高性能数值计算而设计。

hackernews · tosh · May 16, 09:50 · [社区讨论](https://news.ycombinator.com/item?id=48158606)

**背景**: 传统的 GPU 编程使用 CUDA 或 OpenCL 等语言，需要手动管理数组大小和内存，容易导致错误。依赖类型允许类型依赖于值，从而在编译时检查数组维度。Futhark 将这一概念应用于 GPU 计算，旨在提高安全性和生产力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Futhark_(programming_language)">Futhark (programming language) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dependent_type">Dependent type - Wikipedia</a></li>
<li><a href="https://dev.to/viz-x/futhark-the-functional-language-built-for-high-performance-parallel-computing-3ofj">⚡ Futhark — The Functional Language Built for High ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示，用户对 Futhark 的 bug 修复速度和数组依赖类型系统持积极态度，尽管一些用户对名称与卢恩字母的相似性感到困惑。总体情绪是正面的，用户欣赏该语言在减少 CUDA 调试方面的潜力。

**标签**: `#Futhark`, `#GPU programming`, `#dependent types`, `#array programming`, `#functional programming`

---

<a id="item-8"></a>
## [粪便移植在自闭症临床试验中展现希望](https://refractor.io/adhd-autism/fecal-transplants-for-autism-delivers-success-in-clinical-trials/) ⭐️ 7.0/10

一项有 60 名参与者和安慰剂组的临床试验（NCT03408886）发现，粪便微生物群移植（FMT）减轻了自闭症症状并改善了胃肠道问题，更新了 2019 年一项较小研究的早期结果。 这为目前缺乏有效疗法的自闭症提供了一条新的治疗途径，并支持了肠-脑轴假说。但由于样本量小且需要在更大规模、良好对照的研究中重复，怀疑仍然存在。 该试验包括安慰剂组，有 60 名参与者，比之前没有安慰剂组的 18 人研究有所改进。结果已提交至 ClinicalTrials.gov，但质量审查尚未完成。

hackernews · breve · May 16, 09:27 · [社区讨论](https://news.ycombinator.com/item?id=48158494)

**背景**: 粪便微生物群移植（FMT）涉及将健康捐赠者的粪便转移到患者肠道以恢复微生物多样性。肠-脑轴是一个连接肠道微生物组与大脑的双向通信系统，其紊乱与自闭症谱系障碍（ASD）有关。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nature.com/articles/s41593-023-01361-0">Multi-level analysis of the gut–brain axis shows autism ...</a></li>
<li><a href="https://link.springer.com/article/10.1007/s12035-025-05321-6">The Gut–Brain Axis in Autism: Inflammatory Mechanisms ...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，自闭症儿童通常饮食有限，这可能会使肠道微生物组失衡，并且胃肠道问题是常见的共病。一些人表示谨慎，指出小规模试验显示希望但在更大研究中未能复制的模式。

**标签**: `#autism`, `#gut microbiome`, `#clinical trials`, `#fecal transplant`, `#medical research`

---

<a id="item-9"></a>
## [美国用 AI 检测预测市场内幕交易](https://arstechnica.com/tech-policy/2026/05/the-us-is-betting-on-ai-to-catch-insider-trading-in-prediction-markets/) ⭐️ 7.0/10

美国商品期货交易委员会（CFTC）正在部署机器学习算法，以检测 Polymarket 等预测市场上的内幕交易，这一消息在 CFTC 主席 Michael Selig 最近的采访中被披露。 这标志着将 AI 与金融监管相结合的重大监管举措，可能威慑内幕交易并提高预测市场的合法性。它可能为监管机构如何监控去中心化平台树立先例。 CFTC 使用 AI 扫描大量交易数据，帮助工作人员识别可疑账户，并决定是否启动调查或发出传票。该系统重点关注 Polymarket 等加密预测市场。

rss · Ars Technica · May 16, 11:00

**背景**: 预测市场是一种交易所交易市场，参与者对事件结果下注，价格反映集体信念。CFTC 在美国监管这些市场，而利用非公开信息获利的内幕交易是非法的。现在 AI 被用于检测表明此类滥用的模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/polymarket-insider-trading-cftc-michael-selig-interview/">The US Is Using AI to Hunt Down Insider Trading on Polymarket | WIRED</a></li>
<li><a href="https://www.mexc.com/news/1096176">Government AI tracks insider trading as bots take over prediction markets | MEXC News</a></li>

</ul>
</details>

**标签**: `#AI`, `#regulation`, `#prediction markets`, `#insider trading`, `#finance`

---

<a id="item-10"></a>
## [博客文章指现代社会过于复杂](https://user8.bearblog.dev/the-world-is-too-complicated/) ⭐️ 6.0/10

一篇题为《我们把世界弄得太复杂了》的博客文章认为现代社会已变得过于复杂，引发了关于简单与进步之间权衡的讨论。 这种反思引起了许多感到被技术和社会复杂性压垮的人的共鸣，引发了关于简化是否可取甚至是否可能的辩论。 该帖子得分为 6.0/10，获得 139 个点赞和 132 条评论，表明参与度中等。评论者提供了从进化生物学到历史森林砍伐等多元视角。

hackernews · James72689 · May 16, 08:25 · [社区讨论](https://news.ycombinator.com/item?id=48158065)

**背景**: 这篇博客文章是一篇关于社会复杂性的哲学文章，不涉及具体事件。它涉及技术、人性和生命意义等主题。

**社区讨论**: 评论者意见不一：一些人认为复杂性令人不堪重负，而另一些人则争辩说自然本身就很复杂，过度简化可能很危险。引用亚当·柯蒂斯的《超正常化》和历史实例丰富了辩论。

**标签**: `#society`, `#complexity`, `#philosophy`, `#technology`

---

<a id="item-11"></a>
## [深入剖析 HTML 列表，揭示隐藏陷阱](https://blog.frankmtaylor.com/2026/05/13/you-dont-know-html-lists/) ⭐️ 6.0/10

一篇全面的博客文章探讨了 HTML 列表元素，包括鲜为人知的特性以及浏览器兼容性问题，尤其是 datalist 和 optgroup 在移动端 Safari 上的问题。 这很重要，因为许多开发者忽视了 HTML 列表的细微差别，导致可访问性和可用性问题；讨论中强调了影响移动用户的现实兼容性问题。 文章涵盖了 datalist、optgroup 和 dl 元素，指出 datalist 在移动端 Safari 上表现不佳，且 optgroup 的 disabled 属性在移动端 Safari 上不被尊重。

hackernews · speckx · May 16, 16:58 · [社区讨论](https://news.ycombinator.com/item?id=48161861)

**背景**: HTML 列表包括 ul、ol、dl 以及相关的 datalist 和 optgroup 元素。Datalist 为输入字段提供自动完成建议，而 optgroup 用于在 select 元素中对选项进行分组。这些特性的浏览器支持情况各不相同，尤其是在移动平台上。

**社区讨论**: 评论者确认了 datalist 和 optgroup 在移动端 Safari 上的兼容性问题，有人认为 datalist 缺乏足够的钩子用于生产环境。一位评论者感叹新开发者跳过 HTML 基础直接学习 React，错过了简单的解决方案。

**标签**: `#HTML`, `#web development`, `#frontend`, `#browser compatibility`

---

<a id="item-12"></a>
## [Snap、YouTube、TikTok 和解学校成瘾诉讼](https://www.theverge.com/tech/932153/snap-youtube-tiktok-lawsuit-social-media-addiction-schools) ⭐️ 6.0/10

Snap、YouTube 和 TikTok 已和解肯塔基州一个学区提起的诉讼，该诉讼指控社交媒体成瘾损害了学生并加重了学校预算负担。 此次和解标志着在追究社交媒体平台对学生造成伤害的责任方面取得了显著的法律进展，可能影响未来的诉讼和学校政策。 该诉讼由肯塔基州布雷西特县学区提起，是同类案件中首个达成和解的，但和解条款未披露。

rss · The Verge · May 16, 18:34

**背景**: 社交媒体平台因其可能导致年轻用户成瘾和心理健康问题而面临越来越多的审查。学校报告称学习受到干扰，且与学生心理健康危机相关的成本增加，从而引发了寻求赔偿的诉讼。

**标签**: `#social media`, `#lawsuits`, `#education`, `#tech policy`

---

<a id="item-13"></a>
## [马斯克诉奥特曼案：最后一周双方攻击可信度](https://www.technologyreview.com/2026/05/15/1137357/musk-v-altman-week-3/) ⭐️ 6.0/10

在马斯克诉奥特曼案的最后一周，双方律师攻击了埃隆·马斯克和萨姆·奥特曼的可信度，奥特曼被质疑涉嫌撒谎和与 OpenAI 有业务往来的公司进行自我交易，而他则称马斯克是一个追求权力的人。 此案可能为法院如何看待 AI 创始人与其公司之间的纠纷树立先例，影响 AI 行业未来的治理和法律斗争。 审判聚焦于个人可信度而非技术问题，预计陪审团将根据证词和证据做出裁决。

rss · MIT Technology Review · May 15, 23:39

**背景**: 马斯克诉奥特曼案源于埃隆·马斯克对 OpenAI 和萨姆·奥特曼的诉讼，指控其违反合同和信托义务，涉及 OpenAI 从非营利向营利模式的转变。由于涉及知名人物及其对 AI 发展的影响，此案备受关注。

**标签**: `#legal`, `#AI`, `#OpenAI`, `#Elon Musk`

---

<a id="item-14"></a>
## [欧盟法规推动 Firefox 新增 600 万用户](https://www.pcgamer.com/software/6-million-more-people-are-using-firefox-because-of-new-eu-rules-which-is-good-news-for-chrome-haters-like-me/) ⭐️ 6.0/10

欧盟法规（很可能是《数字市场法案》）导致 Firefox 新增了 600 万用户，因为用户在移动和桌面平台上有了更多浏览器选择。 这一转变表明，监管干预可以有效挑战 Chrome 等主导浏览器，可能促进更具竞争力和多样性的浏览器生态系统。 这一增长归因于欧盟法规要求平台提供浏览器选择屏幕，其他第三方浏览器的用户数量也在上升。

rss · PC Gamer · May 16, 13:00

**背景**: 欧盟的《数字市场法案》（DMA）旨在遏制大型科技平台的反竞争行为，包括要求它们允许用户选择默认浏览器。Firefox 是由 Mozilla 开发的注重隐私的开源浏览器，与 Chrome、Safari 和 Edge 竞争。

**标签**: `#browsers`, `#EU regulations`, `#Firefox`, `#market share`

---