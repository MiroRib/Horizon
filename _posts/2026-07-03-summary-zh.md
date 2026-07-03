---
layout: default
title: "Horizon Summary: 2026-07-03 (ZH)"
date: 2026-07-03
lang: zh
---

> From 128 items, 20 important content pieces were selected

---

1. [调查间谍软件的欧洲议会议员遭飞马攻击](#item-1) ⭐️ 8.0/10
2. [Ubicloud 倡导对 PostgreSQL 使用严格内存过量使用](#item-2) ⭐️ 8.0/10
3. [初创公司智能烤箱因缺乏领域专业知识而失败](#item-3) ⭐️ 8.0/10
4. [设备复活捐赠者眼球，为移植铺路](#item-4) ⭐️ 8.0/10
5. [本地运行 SOTA 大模型指南](#item-5) ⭐️ 7.0/10
6. [Costco 的仓储模式规避亚马逊的最后一英里困境](#item-6) ⭐️ 7.0/10
7. [工厂不过是房间：揭秘制造业](#item-7) ⭐️ 7.0/10
8. [Wordgard：ProseMirror 创建者推出的新富文本编辑器](#item-8) ⭐️ 7.0/10
9. [Valve 开源 Steam Machine 电子墨水屏，支持 DIY](#item-9) ⭐️ 7.0/10
10. [LLM 成本黑客：将代码转为图像以利用更便宜的 OCR 令牌](#item-10) ⭐️ 7.0/10
11. [Hacker News 探讨新型 LLM 编码工作流](#item-11) ⭐️ 7.0/10
12. [螺旋蝇的兴衰：一个警示故事](#item-12) ⭐️ 7.0/10
13. [美国数据中心用电量超过任何其他国家](#item-13) ⭐️ 7.0/10
14. [EVE Online 工作室 Fenris 开源 Carbon 引擎](#item-14) ⭐️ 7.0/10
15. [谷歌反垄断案败诉，被罚 41 亿欧元](#item-15) ⭐️ 7.0/10
16. [Meta 定制芯片让 DDR5 服务器用上 DDR4 内存](#item-16) ⭐️ 7.0/10
17. [Anthropic 推出 Claude Science 用于药物研发](#item-17) ⭐️ 6.0/10
18. [游戏行业综述：劳工、光盘与价格操纵](#item-18) ⭐️ 6.0/10
19. [五层 AI 堆栈与日本的主权 AI 角色](#item-19) ⭐️ 6.0/10
20. [Palantir CEO 抨击 AI 代币定价模式“极其疯狂”](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [调查间谍软件的欧洲议会议员遭飞马攻击](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

公民实验室高度确信，曾参与调查间谍软件滥用的欧洲议会议员斯特利奥斯·库洛格卢的 iPhone 在 2022 年和 2023 年至少三次被飞马间谍软件感染。 这一事件表明，即使是负责调查监控滥用的人员也无法免受国家支持的间谍软件侵害，凸显了欧洲机构严重的安全漏洞以及飞马等商业间谍软件的持续威胁。 感染发生在 2022 年 10 月 21 日和 2023 年 3 月 6 日至 7 日，当时库洛格卢是 PEGA 委员会成员。公民实验室指出，一个有权在多个欧洲国家进行监控的飞马客户很可能是幕后黑手。

hackernews · ledoge · Jul 3, 20:38 · [社区讨论](https://news.ycombinator.com/item?id=48779683)

**背景**: 飞马是由以色列 NSO 集团开发的强大间谍软件，能够远程入侵移动设备并提取数据、信息和录音。它被多国政府广泛滥用于针对记者、活动家和政治对手。欧洲议会于 2022 年成立了 PEGA 委员会，以调查飞马及类似间谍软件在欧洲的使用情况。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/">Espionage Against the European Parliament: Member of ...</a></li>
<li><a href="https://www.theguardian.com/world/2026/jul/03/spyware-used-against-mep-investigating-pegasus-abuses-report-finds">Spyware used against MEP investigating Pegasus abuses, report ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>

</ul>
</details>

**社区讨论**: 评论者担心同一部手机同时包含个人医疗信息和机密政府文件，质疑缺乏设备分离政策。一些人指出，使用更安全的手机如 GrapheneOS 本可防止攻击，而另一些人则提到希腊和意大利更广泛的国家支持间谍软件丑闻，暗示此次攻击可能与国内监控有关，而非直接针对欧洲议会。

**标签**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#surveillance`, `#European Parliament`

---

<a id="item-2"></a>
## [Ubicloud 倡导对 PostgreSQL 使用严格内存过量使用](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud 发布了一篇博客文章，解释了他们为何对 PostgreSQL 使用严格内存过量使用（vm.overcommit_memory=2）以避免 OOM killer 干扰，社区讨论则强调了其中的权衡和操作注意事项。 这很重要，因为 PostgreSQL 对内存压力很敏感，而 Linux 默认的过量使用行为可能导致 OOM killer 杀死 Postgres，造成停机。讨论为考虑类似更改的数据库运维人员提供了实用见解。 严格过量使用（模式 2）可防止内核过量承诺内存，降低 OOM killer 风险，但如果过量使用比率未调整，可能导致 fork 失败。作者建议在 QA 环境中测试，并在部署期间动态更改 sysctl 设置。

hackernews · furkansahin · Jul 3, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48774509)

**背景**: Linux 内存过量使用允许进程分配比物理 RAM 更多的虚拟内存。当内存耗尽时，OOM killer 会终止一个进程以释放内存。PostgreSQL 因其大量内存使用而经常成为受害者，导致数据库中断。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/memory-overcommitment-oom-killer">Linux Memory Overcommitment and the OOM Killer - Baeldung</a></li>
<li><a href="https://www.baeldung.com/linux/overcommit-modes">Linux Overcommit Modes - Baeldung</a></li>
<li><a href="https://linuxhandbook.com/oom-killer/">What is Out of Memory Killer (OOM Killer) in Linux?</a></li>

</ul>
</details>

**社区讨论**: 评论者指出 Linux 默认内存管理存在问题，并警告说模式 2 如果未经测试可能导致 fork 失败。Ubicloud 的 Ozgun 承认博客语气强烈，并同意严格过量使用并不适用于所有场景。

**标签**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database operations`

---

<a id="item-3"></a>
## [初创公司智能烤箱因缺乏领域专业知识而失败](https://weli.dev/blog/half-baked-product/) ⭐️ 8.0/10

一位初创公司创始人在没有领域专业知识的情况下尝试制造智能烤箱，结果产品半生不熟，未能满足市场需求。 这个故事凸显了领域专业知识在产品开发中的关键重要性，为创始人和工程师提供了关于进入不熟悉行业陷阱的警示。 创始人的主要动机是致富而非解决实际问题，导致愿景与技术可行性不匹配。文章及 361 条评论讨论了常见的创业失败原因，如缺乏客户理解和过度依赖融资。

hackernews · weli · Jul 3, 08:23 · [社区讨论](https://news.ycombinator.com/item?id=48772388)

**背景**: 领域专业知识指在特定领域的深厚知识和经验，对于识别真实客户需求和可行的技术解决方案至关重要。许多初创公司失败是因为创始人优先考虑市场趋势而非真正的专业知识，正如这个智能烤箱案例所示。

**社区讨论**: 评论者普遍认为创始人的领域专业知识缺乏和对财富的追求是根本原因。一些人指出这种模式在各行业都很常见，而另一些人则幽默地将其与自己无关领域的创业尝试相比较。

**标签**: `#startups`, `#product development`, `#domain expertise`, `#entrepreneurship`

---

<a id="item-4"></a>
## [设备复活捐赠者眼球，为移植铺路](https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/) ⭐️ 8.0/10

研究人员开发出一种设备，能够保存并复活已故捐赠者的眼球，可能克服全眼移植的关键障碍。 全眼移植可能为数百万盲人恢复视力，但死后组织迅速退化一直使其无法实现。该设备可能促成首次成功的恢复视力的眼睛移植。 该设备通过提供营养和氧气来维持眼睛的活力，防止从捐赠者体内取出后发生退化。它解决了视网膜存活和视神经保存的关键问题。

rss · MIT Technology Review · Jul 3, 17:34

**背景**: 全眼移植面临三大挑战：视网膜存活、免疫排斥和视神经再生。之前的尝试，如 2023 年世界首例全眼和部分面部移植，虽然眼睛存活但未能恢复视力。新设备专门针对第一个挑战，通过在体外保持眼睛存活来解决问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aao.org/eyenet/article/eyes-on-the-prize-whole-eye-transplant">Eyes on the Prize: The Quest to Restore Vision With Whole Eye Transplant - American Academy of Ophthalmology</a></li>
<li><a href="https://nyulangone.org/news/worlds-first-whole-eye-partial-face-transplant-recipient-achieves-remarkable-recovery-viable-eye-one-year-after-landmark-surgery">The World’s First Whole-Eye & Partial-Face Transplant Recipient Achieves Remarkable Recovery, with Viable Eye One Year After Landmark Surgery | NYU Langone News</a></li>
<li><a href="https://wyss.harvard.edu/news/vision-for-whole-eye-transplant/">Vision for whole eye transplant - Wyss Institute</a></li>

</ul>
</details>

**标签**: `#biotechnology`, `#medical devices`, `#transplantation`, `#ophthalmology`

---

<a id="item-5"></a>
## [本地运行 SOTA 大模型指南](https://github.com/jamesob/local-llm) ⭐️ 7.0/10

Jamesob 在 GitHub 上发布了一份全面指南，详细介绍了如何构建和本地运行最先进的大语言模型，硬件推荐从预算配置到超过 4 万美元的高端配置。 该指南帮助开发者和爱好者了解本地 LLM 推理的真实成本和权衡，引发了关于本地部署与云订阅相比是否划算的讨论。 高端配置包括 4 块每块 1.2 万美元的 GPU，总价约 5 万至 5.5 万美元，并依赖量化技术来运行接近 Claude Opus 质量的模型。

hackernews · livestyle · Jul 3, 15:03 · [社区讨论](https://news.ycombinator.com/item?id=48775921)

**背景**: 本地运行大语言模型需要大量 GPU 显存；例如，一个 700 亿参数的模型可能需要 48GB 或更多显存。量化可以降低内存需求，但可能降低输出质量。像 ChatGPT 这样的云服务使用更方便，但存在隐私和成本问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/aanoskov/local_llms_quantized">GitHub - aanoskov/ local _llms_quantized: This repository demonstrates...</a></li>
<li><a href="https://specpicks.com/reviews/best-budget-gpu-local-llm-inference-2026">Best Budget GPU for Local LLM Inference in 2026 | SpecPicks</a></li>
<li><a href="https://www.hivenet.com/post/best-7-gpus-for-llm-inference-and-fine-tuning">Best GPUs for LLM inference and fine-tuning in 2026 | Hivenet</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，4 万美元的配置实际花费 5 万至 5.5 万美元，而 4 万美元足以支付 16.8 年的 Claude Opus 订阅。一些人建议替代方案，如统一内存架构（例如 48GB 的 M5 MacBook Pro）或云托管，作为更便宜的选择。

**标签**: `#LLM`, `#local inference`, `#hardware`, `#deep learning`, `#open source`

---

<a id="item-6"></a>
## [Costco 的仓储模式规避亚马逊的最后一英里困境](https://phenomenalworld.org/analysis/the-anti-amazon/) ⭐️ 7.0/10

一篇分析文章指出，Costco 的仓储会员制模式从本质上规避了亚马逊最后一英里配送系统的物流复杂性和社会成本，凸显了零售业根本性的战略分歧。 这一对比之所以重要，是因为它挑战了电商配送总是更优的假设，揭示了便利性、成本和社会影响之间的权衡，这些权衡影响着消费者、零售商和城市规划者。 Costco 的模式依赖顾客自行驾车前往仓库并运输商品，从而避免了与最后一英里物流相关的单件配送成本和交通拥堵。不过，Costco 也与 Instacart 合作提供当日达配送服务，提供了一种混合选项。

hackernews · bookofjoe · Jul 3, 15:14 · [社区讨论](https://news.ycombinator.com/item?id=48776044)

**背景**: 最后一英里配送是供应链的最后一步，即商品从配送中心运送到客户家门口。由于单次配送量小且停靠点多，这通常是物流中最昂贵且效率最低的环节。相比之下，Costco 的仓储模式采用批量运输到集中地点，由顾客自行取货，从而降低了单位物流成本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gofo.com/us/track">Last - Mile Delivery for E-Commerce Parcel Logistics Network | GOFO</a></li>
<li><a href="https://www.solbox.it/how-last-mile-delivery-logistics-has-evolved-in-food-logistics/">How Last Mile Delivery Logistics Has Evolved in Food... - SolBox</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了规避最后一英里问题的工程智慧，有人引用谚语：“聪明人解决问题，智者避免问题。”其他人则提到 Costco 的国际业务和非食品商品，也有人指出 Costco 现在通过 Instacart 提供配送服务，部分弥补了这一差距。

**标签**: `#logistics`, `#retail`, `#business strategy`, `#engineering`, `#e-commerce`

---

<a id="item-7"></a>
## [工厂不过是房间：揭秘制造业](https://interconnected.org/home/2026/07/03/factories) ⭐️ 7.0/10

一篇文章认为，工厂本质上只是制造物品的房间，挑战了工业生产的神秘性，并鼓励以更平易近人的视角看待制造业。 这种观点可能通过降低进入门槛来普及制造业，激励更多人开展小规模生产，并培养动手创造的文化。 这篇文章发表在 interconnected.org 上，在 Hacker News 上获得了 170 分和 71 条评论的高参与度，表明社区对重新思考制造业有浓厚兴趣。

hackernews · arbesman · Jul 3, 15:13 · [社区讨论](https://news.ycombinator.com/item?id=48776035)

**背景**: 制造业通常被视为复杂且资本密集的行业，需要专门的机器和大型设施。文章挑战了这一观念，认为一个配备基本工具的简单房间就可以作为工厂，强调生产的本质是制造行为，而非环境。

**社区讨论**: 评论者分享了个人经历，有人提到英国一家手工装配的小工厂令人愉快，而另一个人指出“仅仅是房间”的方法可能无法维持稳定的业务。讨论反映了对简单性的赞赏与对实际挑战的认识。

**标签**: `#manufacturing`, `#philosophy of technology`, `#making`, `#industrial design`

---

<a id="item-8"></a>
## [Wordgard：ProseMirror 创建者推出的新富文本编辑器](https://wordgard.net/) ⭐️ 7.0/10

Wordgard 0.1.0 已发布，这是 ProseMirror 创建者开发的一款新的浏览器内富文本编辑器。它与 ProseMirror 共享许多概念，但提供了一种全新的方法，且没有升级路径。 Wordgard 为网页富文本编辑引入了新设计，可能影响未来编辑器的发展。使用 ProseMirror 或类似库的开发者需要评估是否采用这个新系统。 Wordgard 不是 ProseMirror 的升级版，迁移需要大量重构。它专为现代 Web 应用设计，强调不同的内部架构。

hackernews · indy · Jul 3, 08:50 · [社区讨论](https://news.ycombinator.com/item?id=48772573)

**背景**: ProseMirror 是一个广泛使用、久经考验的富文本编辑器框架，学习曲线陡峭。Wordgard 是同一作者的新系统，旨在解决 ProseMirror 的一些局限性，同时保持类似的概念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://discuss.prosemirror.net/t/wordgard-0-1-0/9035">Wordgard 0.1.0 - Announce - discuss.ProseMirror</a></li>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**社区讨论**: 社区对 Wordgard 背后的“为什么”表示感兴趣，并指出缺乏升级路径。一些开发者认为该设计验证了他们自己的方法，而另一些则强调需要静态类型的文档表示。

**标签**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-9"></a>
## [Valve 开源 Steam Machine 电子墨水屏，支持 DIY](https://www.gamingonlinux.com/2026/07/valve-open-source-the-steam-machine-e-ink-screen-so-you-can-make-your-own/) ⭐️ 7.0/10

Valve 已发布 Steam Machine 电子墨水屏的开源设计，任何人都可以自行制作兼容的显示屏。该屏幕基于标准的 Adafruit 5.83 英寸电子墨水面板。 此举赋予社区对 Steam Machine 硬件进行定制和创新的能力，进一步巩固了 Valve 开放的形象。它可能激发针对 Framework Desktop 等其他设备的类似 DIY 项目。 该电子墨水屏可显示系统状态，并利用专有波形实现高刷新率和色彩对比度，无需全屏刷新。Valve 不会自行生产该显示屏，但 Jsaux 等第三方正在开发兼容版本。

hackernews · ahlCVA · Jul 3, 13:01 · [社区讨论](https://news.ycombinator.com/item?id=48774518)

**背景**: Steam Machine 是 Valve 推出的客厅游戏主机，运行 SteamOS。电子墨水屏是可选的前面板显示屏，可显示 CPU/GPU 使用率、游戏封面等系统信息。Valve 有开源贡献的历史，包括资助 FEX 模拟器和 Mesa3D Turnip 驱动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/games/961242/valve-just-open-sourced-its-e-ink-screen-for-the-steam-machine">Valve just open-sourced its e-ink screen for the Steam Machine.</a></li>
<li><a href="https://www.gamingonlinux.com/2025/11/igalia-detail-their-open-source-work-for-valves-steam-frame-and-steam-machine/">Igalia detail their open source work for Valve's Steam Frame and Steam Machine | GamingOnLinux</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞 Valve 的开放态度，有人希望更多公司效仿。部分人讨论了如何将该设计用于 Framework Desktop，另一些人则探讨了 Valve 善意的商业利益。还出现了关于支持 HDMI 输入的更大尺寸电子墨水屏的技术问题。

**标签**: `#open-source`, `#hardware`, `#valve`, `#e-ink`, `#steam-machine`

---

<a id="item-10"></a>
## [LLM 成本黑客：将代码转为图像以利用更便宜的 OCR 令牌](https://github.com/teamchong/pxpipe) ⭐️ 7.0/10

一种名为 pxpipe 的技术通过将基于文本的代码转换为图像，然后使用 OCR 提取文本，利用图像令牌通常比文本令牌定价更低的事实，从而降低 LLM API 成本。 这种黑客技术可能显著降低处理大量代码或文本的开发者的 API 成本，但它可能是一个临时漏洞，提供商可能会通过调整令牌定价来关闭它。 据报道，这种方法可将提示令牌减少多达 60%，但可能会增加完成令牌，从整体上看可能更慢且更昂贵，正如之前使用 OpenAI 模型的尝试所指出的那样。

hackernews · dimitropoulos · Jul 3, 15:50 · [社区讨论](https://news.ycombinator.com/item?id=48776464)

**背景**: LLM API 根据令牌使用量收费，输入和输出令牌有单独的定价。图像令牌有时比文本令牌更便宜，从而创造了套利机会。OCR（光学字符识别）用于从图像中提取文本，但模型可能仍将图像作为图像处理，导致潜在的令牌核算漏洞。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/">The unified interface for LLMs. Find the best models & prices for your...</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，这很可能是一个令牌核算漏洞，可能会被关闭，并且之前使用 OpenAI 的类似尝试由于完成令牌增加而导致总体成本更高。一些人还指出，这种技术本质上是在重新发现压缩二进制格式以提高效率。

**标签**: `#LLM`, `#cost optimization`, `#OCR`, `#hack`

---

<a id="item-11"></a>
## [Hacker News 探讨新型 LLM 编码工作流](https://news.ycombinator.com/item?id=48771515) ⭐️ 7.0/10

Hacker News 上的一场讨论展示了替代性 LLM 编码范式的实验，包括标签模型、密封代理和异构 LLM 集群，超越了标准的提示-响应循环。 这些实验可能带来更无缝的 AI 辅助编码工作流，帮助开发者进入心流状态，并通过减少确认偏差和启用多模型协作系统来提高代码质量。 标签模型提供内联补全而非基于聊天的交互，而密封代理将代码编写者和测试编写者分别沙箱化以避免偏差。异构 LLM 集群利用网络硬件上的多个模型进行协作推理。

hackernews · yehiaabdelm · Jul 3, 06:21

**背景**: 当前的 LLM 编码工具（如 Claude Code 和 Codex）依赖提示-响应循环，这可能会打断心流状态。受自动补全启发的标签模型旨在提供连续建议。密封代理和 LLM 集群是新兴方法，旨在提高代码质量并利用分布式资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/jovan_chan_9500711396d4e6/best-local-coding-llm-in-2026-qwen25-coder-vs-deepseek-coder-v2-vs-codestral-45g8">Best Local Coding LLM in 2026: Qwen2.5- Coder vs... - DEV Community</a></li>
<li><a href="https://github.com/anyscale/hermetic">GitHub - anyscale/hermetic: Hermetic is a library for developing, deploying and refining LLM Applications · GitHub</a></li>
<li><a href="https://arxiv.org/html/2606.14711">SWARM - LLM : Collaborative Inference for Edge-based Small...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人实验：一位用户用旧 GPU 构建了异构集群，另一位提倡使用密封代理避免确认偏差，还有用户注意到心流状态的丧失，但提供了替代工作流，如审查 AI 生成的代码。

**标签**: `#LLM`, `#coding`, `#AI-assisted development`, `#workflow`, `#experimentation`

---

<a id="item-12"></a>
## [螺旋蝇的兴衰：一个警示故事](https://www.construction-physics.com/p/the-fall-and-rise-of-screwworm) ⭐️ 7.0/10

Construction Physics 上的一篇文章追溯了利用昆虫不育技术根除螺旋蝇的历史及其近期的重新出现，2026 年在南德克萨斯州已确认病例。 这个故事凸显了过去农业胜利的脆弱性以及螺旋蝇对牲畜和野生动物的持续威胁，强调了持续警惕和国际合作的必要性。 螺旋蝇（Cochliomyia hominivorax）是一种寄生蝇，其幼虫以活组织为食；根除依赖于释放辐射绝育的雄蝇来抑制繁殖，这种方法在 20 世纪 50 年代开创。

hackernews · crescit_eundo · Jul 3, 12:58 · [社区讨论](https://news.ycombinator.com/item?id=48774492)

**背景**: 螺旋蝇侵扰会导致温血动物严重受伤和死亡，给畜牧业造成数十亿损失。昆虫不育技术（SIT）成功根除了美国和中美洲的螺旋蝇，但在达连隘口维持永久屏障一直很困难，导致近期入侵。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cochliomyia_hominivorax">Cochliomyia hominivorax - Wikipedia</a></li>
<li><a href="https://www.nal.usda.gov/exhibits/speccoll/exhibits/show/stop-screwworms--selections-fr/introduction">Introduction · STOP Screwworms : Selections from the Screwworm ...</a></li>
<li><a href="https://publichealth.jhu.edu/2026/what-to-know-about-new-world-screwworm">What to Know About New World Screwworm | Johns Hopkins</a></li>

</ul>
</details>

**社区讨论**: 评论者注意到这种杀死宿主的寄生虫存在进化悖论，并质疑维持屏障是否比在整个大陆范围内根除更具成本效益。其他人感叹，由于伦理限制，最初的研究在今天不可能进行。

**标签**: `#ecology`, `#agriculture`, `#pest control`, `#science history`, `#public health`

---

<a id="item-13"></a>
## [美国数据中心用电量超过任何其他国家](https://www.canarymedia.com/articles/data-centers/data-centers-use-more-power-in-the-us-than-anywhere-else) ⭐️ 7.0/10

根据《世界能源统计年鉴》，2025 年全球近 40%的数据中心电力需求来自美国，使其成为全球数据中心电力消耗最大的国家。 这凸显了美国数据中心巨大的能源足迹，随着需求持续激增，对能源政策、电网基础设施以及科技行业的可持续发展目标具有重大影响。 数据来自 2025 年《世界能源统计年鉴》，该报告追踪全球能源统计数据。仅美国数据中心就占全球数据中心电力需求的近 40%，甚至超过中国。

rss · Latitude Media (Canary Media) · Jul 3, 07:30

**背景**: 数据中心是容纳计算机系统及相关组件（如电信和存储系统）的设施。它们消耗大量电力来为服务器和冷却系统供电。《世界能源统计年鉴》是一份年度报告，提供全球能源生产和消费的全面数据。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Statistical_Review_of_World_Energy">Statistical Review of World Energy</a></li>
<li><a href="https://www.energyinst.org/statistical-review/about">energyinst.org/ statistical - review /about</a></li>
<li><a href="https://kpmg.com/xx/en/our-insights/esg/statistical-review-of-world-energy.html">Energy Institute Statistical Review of World Energy</a></li>

</ul>
</details>

**标签**: `#data centers`, `#energy consumption`, `#US`, `#technology`, `#infrastructure`

---

<a id="item-14"></a>
## [EVE Online 工作室 Fenris 开源 Carbon 引擎](https://www.pcgamer.com/games/mmo/eve-online-studio-fenris-follows-through-on-yearslong-promise-to-make-its-in-house-game-engine-fully-open-source/) ⭐️ 7.0/10

EVE Online 背后的工作室 Fenris Creations 已于 2026 年 7 月 1 日在 GitHub 上完全开源其自研的 Carbon 游戏引擎框架。 此举使得社区能够贡献代码、提升透明度，并可能复用这一经过验证的 MMO 引擎，为其他工作室树立了榜样。 此次开源发布包含了 Carbon 引擎的二十多个模块化组件，该引擎驱动着 EVE Online 和 EVE Frontier。

rss · PC Gamer · Jul 3, 17:18

**背景**: Fenris Creations（前身为 CCP Games）早在 2024 年就承诺开源 Carbon 引擎。Carbon 是一个跨平台游戏引擎框架，经过多年内部开发，支撑着 EVE Online 庞大的单一宇宙。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.opensourceforu.com/2026/07/fenris-creations-carbon-game-engine-goes-open-source-on-github/">Fenris Creations' Carbon Game Engine Goes Open-Source On GitHub - Open Source For You</a></li>
<li><a href="https://www.gamesindustry.biz/eve-onlines-carbon-engine-is-now-open-source-fenris-creations-explains-why">Eve Online's Carbon engine is now open source: Fenris Creations explains why | GamesIndustry.biz</a></li>
<li><a href="https://massivelyop.com/2026/07/01/eve-onlines-fenris-creations-just-open-sourced-the-carbon-engine-framework-its-built-on/">EVE Online’s Fenris Creations just open-sourced the Carbon engine framework it’s built on | Massively Overpowered</a></li>

</ul>
</details>

**社区讨论**: 社区反应总体积极，许多人称赞其透明度和模组潜力。一些讨论指出 Carbon 框架与区块链相关功能的区别，表达了谨慎乐观的态度。

**标签**: `#open source`, `#game engine`, `#EVE Online`, `#Fenris`

---

<a id="item-15"></a>
## [谷歌反垄断案败诉，被罚 41 亿欧元](https://www.pcgamer.com/hardware/google-loses-protracted-antitrust-fight-and-will-have-to-pay-record-breaking-eur4-1-billion-fine-equivalent-to-less-than-3-percent-of-alphabets-annual-profit/) ⭐️ 7.0/10

谷歌在一场旷日持久的反垄断诉讼中败诉，将被处以创纪录的 41 亿欧元罚款，这一金额不到 Alphabet 年利润的 3%。 这一裁决为针对大型科技公司的反垄断执法树立了重要先例，可能导致对谷歌商业行为更严格的监管和审查。 这笔罚款是欧盟反垄断案件中有史以来最高的一笔，但仅占 Alphabet 年利润的一小部分，凸显了对该公司财务影响的有限性。

rss · PC Gamer · Jul 3, 15:29

**背景**: 反垄断法旨在促进竞争并防止垄断行为。欧盟委员会多年来一直在调查谷歌在搜索和广告等领域的做法，并因此多次处以罚款。

**标签**: `#antitrust`, `#Google`, `#regulation`, `#tech industry`, `#legal`

---

<a id="item-16"></a>
## [Meta 定制芯片让 DDR5 服务器用上 DDR4 内存](https://www.pcgamer.com/hardware/memory/metas-solution-to-the-global-memory-shortage-is-to-use-ddr4-in-a-ddr5-server-with-a-custom-chip-making-the-impossible-possible/) ⭐️ 7.0/10

Meta 开发了一款定制芯片，使得原本只支持 DDR5 内存的服务器能够使用 DDR4 内存模块，通过重新利用旧内存来应对内存短缺问题。 这项创新帮助 Meta 应对全球内存短缺，并通过延长 DDR4 模块的使用寿命减少电子垃圾，但该方案不适用于消费级 PC。 该定制芯片将 DDR4 内存条作为独立的、速度较慢的内存池与主 DDR5 内存池一起管理，从而在服务器中实现混合内存配置。

rss · PC Gamer · Jul 3, 12:59

**背景**: DDR4 和 DDR5 是不同代的内存，物理和电气接口不兼容，因此不能在标准主板上混用。Meta 的解决方案使用定制芯片来桥接这一差距，允许旧的 DDR4 模块在服务器中补充 DDR5。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/memory/metas-solution-to-the-global-memory-shortage-is-to-use-ddr4-in-a-ddr5-server-with-a-custom-chip-making-the-impossible-possible/">Meta 's solution to the global memory shortage is to use... | PC Gamer</a></li>

</ul>
</details>

**标签**: `#hardware`, `#memory`, `#Meta`, `#server`, `#innovation`

---

<a id="item-17"></a>
## [Anthropic 推出 Claude Science 用于药物研发](https://www.theverge.com/ai-artificial-intelligence/961311/anthropic-claude-science-ai-drug-development) ⭐️ 6.0/10

Anthropic 发布了 Claude Science，这是一个面向科学家的 AI 工作台，将分散的工具和数据集整合到一个环境中，使研究人员能够生成图表和可视化内容。此次发布在“AI for Science”活动中围绕药物研发展开。 Claude Science 可以通过减少工具集成所花费的时间，让研究人员专注于核心科学，从而加速科学研究，尤其是药物发现。它使 Anthropic 能够在不断增长的 AI 科学市场中与其他科技巨头竞争。 Claude Science 是一款桌面应用，在 macOS 和 Linux 上提供测试版，集成了常用的研究工具和软件包。它生成可审计的产物，并提供灵活的计算资源访问。

rss · The Verge · Jul 3, 13:56

**背景**: Anthropic 以其 Claude AI 模型和编程工具而闻名。该公司于 2025 年 5 月启动了“AI for Science”计划，旨在通过 API 访问加速研究。Claude Science 是该计划下的最新产品，面向需要简化工作流程的科学家。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>
<li><a href="https://claude.com/docs/claude-science/overview">Claude Science - Claude.ai Documentation</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#science`, `#drug development`, `#tools`

---

<a id="item-18"></a>
## [游戏行业综述：劳工、光盘与价格操纵](https://www.gamedeveloper.com/business/rockstar-workers-hit-back-playstation-ditches-physical-discs-and-chipmakers-accused-of-price-fixing-patch-notes-58) ⭐️ 6.0/10

Rockstar Games 解雇了试图组建工会的 QA 测试员，导致其爱丁堡办公室外发生抗议。索尼宣布将在 2028 年前逐步停止 PlayStation 游戏光盘的生产，转向全数字化未来。一项集体诉讼指控三星、SK 海力士和美光操纵内存价格。 这些事件凸显了游戏行业的重大转变：劳工权利冲突、实体媒体的终结以及因涉嫌价格操纵导致的硬件成本上涨。它们影响着开发者、玩家以及更广泛的科技生态系统。 Rockstar 指控被解雇的测试员存在严重不当行为和泄露机密，而工人则声称这是对工会组织的报复。索尼的无光盘转型始于 2028 年，将终止二手交易和租赁。内存价格操纵诉讼引用了 2002 年的 DRAM 丑闻。

rss · Game Developer (Gamasutra) · Jul 3, 10:36

**背景**: 游戏行业的劳工运动日益活跃，QA 工人常面临恶劣的工作条件和就业不稳定。由于数字发行，实体游戏光盘一直在减少，但索尼的举动标志着其终结。内存价格操纵有历史先例，主要芯片制造商此前曾被定罪。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/games/grand-theft-auto/all-you-had-to-do-was-follow-the-damn-law-rockstar-workers-are-protesting-outside-take-two-after-gta-6-devs-alleged-ruthless-union-busting/">'All you had to do was follow the damn law, Rockstar !': Workers are...</a></li>
<li><a href="https://www.msn.com/en-us/entertainment/gaming/playstation-s-disc-less-future-could-heavily-influence-xbox-and-nintendo-former-sony-boss-says/ar-AA279L9e">PlayStation's disc-less future could heavily influence Xbox ...</a></li>
<li><a href="https://www.dualshockers.com/ram-price-fixing-lawsuit-explained/">RAM Price-Fixing Lawsuit Explained: Samsung, SK Hynix, and ...</a></li>

</ul>
</details>

**标签**: `#gaming`, `#industry news`, `#labor`, `#hardware`, `#legal`

---

<a id="item-19"></a>
## [五层 AI 堆栈与日本的主权 AI 角色](https://www.4gamer.net/games/991/G999110/20260703032/) ⭐️ 6.0/10

在 IVS2026 上，一场名为“新 AI 堆栈”的会议介绍了 AI 基础设施的五层模型——涵盖能源、数据中心、网络、GPU 服务器和应用——并强调了日本作为主权 AI 和大型 AI 工厂枢纽的战略地位，以鹿儿岛的一个设施为例。 该框架提供了对支撑现代 AI 的物理和数字基础设施的清晰分层理解，帮助利益相关者识别瓶颈和投资机会。日本对主权 AI 和国内 AI 工厂的重视可以减少对外国技术的依赖，增强国家 AI 自主性。 五层包括：能源（发电和配电）、数据中心（容纳计算的设施）、网络（包括海底电缆的连接）、GPU 服务器（计算硬件）和应用（面向用户的 AI 服务）。鹿儿岛 AI 工厂被引为日本投资大规模 AI 基础设施的具体例子。

rss · 4Gamer.net · Jul 3, 10:22

**背景**: 主权 AI 指一个国家利用自己的基础设施、数据、人才和商业网络生产 AI 的能力，符合其自身的规则和价值观。AI 堆栈概念有助于揭示从原始电力到最终用户应用所需复杂层次的神秘面纱。IVS2026 是日本最大的创业大会，在京都举行。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@ThinkingLoop/the-new-ai-stack-explained-in-5-layers-74fea810df8d">The New AI Stack, Explained in 5 Layers - Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/5-layer-ai-stack-why-understanding-every-layer-your-secret-naik-nguhc">The 5-Layer AI Stack: Why Understanding Every Layer Is Your ...</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#sovereign AI`, `#Japan`, `#GPU`, `#conference`

---

<a id="item-20"></a>
## [Palantir CEO 抨击 AI 代币定价模式“极其疯狂”](https://www.pcgamer.com/software/ai/something-has-gone-completely-wrong-palantir-ceo-rants-on-live-television-about-his-problems-with-the-ai-business-model-why-are-they-charging-for-tokens-if-its-so-valuable/) ⭐️ 6.0/10

Palantir 首席执行官 Alex Karp 在 CNBC 上公开抨击 OpenAI 和 Anthropic 等领先 AI 实验室采用的基于代币的定价模式，称其商业模式“极其疯狂”，是对企业征收的“财富税”。 Karp 的批评凸显了企业对 AI 定价日益增长的不满，可能推动行业转向固定费用或基于结果的定价等替代模式，从而重塑 AI 服务的商业化方式。 Karp 特别指出，按 token 收费存在缺陷，因为它惩罚了重度用户，且成本与交付价值不匹配，同时企业数据可能被用于改进竞争对手的模型。

rss · PC Gamer · Jul 3, 10:04

**背景**: 包括 OpenAI 和 Anthropic 在内的大多数主要 AI 公司都根据处理的 token 数量（输入和输出）向开发者收费。这种模式已成为 API 访问的标准，但批评者认为它会导致成本不可预测，并阻碍广泛采用。Palantir 是一家数据分析公司，为政府和大型企业客户构建定制 AI 解决方案，因此对定价效率低下问题尤为敏感。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.forbes.com/sites/tylerroush/2026/07/01/palantir-billionaire-alex-karp-calls-ai-industry-effing-insane-in-heated-interview/">Palantir Billionaire Karp Blasts AI Industry As ‘Effing Insane’</a></li>
<li><a href="https://cryptobriefing.com/palantir-karp-criticizes-ai-token-chasers/">Palantir CEO criticizes AI labs for 'tokenmaxxing,' backs enterprise.....</a></li>
<li><a href="https://www.alexjoneslive.com/2026/07/02/something-has-gone-completely-wrong-palantirs-alex-karp-goes-ballistic-on-openai-anthropic/">'Something Has Gone Completely Wrong': Palantir 's Alex Karp Goes....</a></li>

</ul>
</details>

**标签**: `#AI`, `#business model`, `#Palantir`, `#industry commentary`

---