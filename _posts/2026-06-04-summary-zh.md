---
layout: default
title: "Horizon Summary: 2026-06-04 (ZH)"
date: 2026-06-04
lang: zh
---

> From 165 items, 30 important content pieces were selected

---

1. [Anthropic 开源 AI 漏洞发现框架](#item-1) ⭐️ 8.0/10
2. [Anthropic 探讨 AI 的递归自我改进](#item-2) ⭐️ 8.0/10
3. [华为 KVarN：原生 vLLM 后端的 KV 缓存量化方案](#item-3) ⭐️ 8.0/10
4. [Meta 在智能眼镜上推出人脸识别功能](#item-4) ⭐️ 8.0/10
5. [最高法院支持 FCC 对位置数据销售的罚款](#item-5) ⭐️ 8.0/10
6. [Dashlane 披露加密密码库遭攻击详情](#item-6) ⭐️ 8.0/10
7. [Roblox 收购 Morpheus AI，实现实时逼真世界生成](#item-7) ⭐️ 8.0/10
8. [Cloudflare 收购 Vite 创建者 VoidZero](#item-8) ⭐️ 7.0/10
9. [高斯点溅射：新型实时 3D 渲染技术](#item-9) ⭐️ 7.0/10
10. [台积电难以满足激增的 AI 芯片需求](#item-10) ⭐️ 7.0/10
11. [对走红网络的人形机器人视频的怀疑指南](#item-11) ⭐️ 7.0/10
12. [爱沙尼亚基准测试评估大模型抗俄宣传能力](#item-12) ⭐️ 7.0/10
13. [数据中心应对用水问题面临审查](#item-13) ⭐️ 7.0/10
14. [Waymo 自动驾驶出租车电池被重新用于电网储能](#item-14) ⭐️ 7.0/10
15. [法院被 AI 生成的诉讼淹没](#item-15) ⭐️ 7.0/10
16. [Framework 13 Pro：面向 Linux 用户的 MacBook Pro 替代品](#item-16) ⭐️ 7.0/10
17. [复古科技育儿：限制孩子接触现代科技](#item-17) ⭐️ 6.0/10
18. [欧盟版 Kagi 替代品 Uruky 新增图片搜索和 URL 重写功能](#item-18) ⭐️ 6.0/10
19. [马斯克试图终止 FTC 对 X 数据处理的审计](#item-19) ⭐️ 6.0/10
20. [有线电视游说团体敦促 FCC 放宽外国路由器禁令](#item-20) ⭐️ 6.0/10
21. [熊蜂展现自发解决问题的能力](#item-21) ⭐️ 6.0/10
22. [哥伦比亚大学数据泄露暴露无关人员社保号](#item-22) ⭐️ 6.0/10
23. [AI 诉讼与数据中心虚拟电厂](#item-23) ⭐️ 6.0/10
24. [科罗拉多州合作社首次实现 100%可再生能源月](#item-24) ⭐️ 6.0/10
25. [天然气行业报告呼吁确保电网可靠性的稳定供气](#item-25) ⭐️ 6.0/10
26. [北卡罗来纳州电力合作社采用电网电池提升韧性](#item-26) ⭐️ 6.0/10
27. [PJM 区域公用事业公司未共享智能电表数据](#item-27) ⭐️ 6.0/10
28. [美国各州阳台太阳能法律各不相同](#item-28) ⭐️ 6.0/10
29. [Visual Arts 披露因未授权访问导致数据泄露](#item-29) ⭐️ 6.0/10
30. [英特尔被曝 18A 节点笔记本 CPU 供应困难](#item-30) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 开源 AI 漏洞发现框架](https://github.com/anthropics/defending-code-reference-harness) ⭐️ 8.0/10

Anthropic 在 GitHub 上发布了一个用于 AI 驱动漏洞发现的开源框架，提供了威胁建模、扫描、分类和修复的技能，以及一个可定制的自主扫描框架。 这降低了安全研究人员利用 AI 进行漏洞发现的门槛，可能加速安全缺陷的识别和修复。同时也引发了关于成本效益以及防御者与攻击者之间军备竞赛的讨论。 该框架设计为可定制，粗略成本估计使用 Opus 为数百美元，使用 Mythos 为数千美元。研究人员已使用现成 AI 以每次扫描低于 30 美元的成本复现了 Anthropic 的 Mythos 发现。

hackernews · binyu · Jun 4, 20:11 · [社区讨论](https://news.ycombinator.com/item?id=48403980)

**背景**: AI 驱动的漏洞发现利用大语言模型分析源代码中的安全缺陷，自动化模式匹配和分类等任务。Anthropic 的 Claude Security 是一个托管产品，可扫描仓库并应用多阶段验证以减少误报。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/anthropics/defending-code-reference-harness">GitHub - anthropics/defending-code-reference-harness: Skills for threat modeling, scanning, triage, patching, plus an autonomous scanning harness you can /customize · GitHub</a></li>
<li><a href="https://news.ycombinator.com/item?id=48403980">Anthropic's open-source framework for AI-powered vulnerability discovery | Hacker News</a></li>
<li><a href="https://decrypt.co/364744/anthropic-mythos-replicated-public-models-vidoc-security">Anthropic’s Alarming Mythos Findings Replicated With Off-the-Shelf AI, Researchers Say - Decrypt</a></li>

</ul>
</details>

**社区讨论**: 社区评论指出，这类框架就像车间夹具——最好根据个人工作流程自行构建。关于成本存在争论，估计从数百到数千美元不等，并且有人担心攻击者可以使用相同的工具，导致一场无法获胜的军备竞赛。

**标签**: `#AI`, `#security`, `#open-source`, `#vulnerability discovery`, `#Anthropic`

---

<a id="item-2"></a>
## [Anthropic 探讨 AI 的递归自我改进](https://www.anthropic.com/institute/recursive-self-improvement) ⭐️ 8.0/10

Anthropic 发表了一篇文章，详细介绍了他们在递归自我改进方面的进展，即 AI 系统可以自主提升自身能力。该公司报告称，他们的 AI 现在编写了大部分代码，并显示出生产力加速提升的迹象。 递归自我改进可能导致智能爆炸，可能产生超越人类控制的超级智能。这引发了重大的安全和伦理问题，尤其是像 Anthropic 这样的领先 AI 安全公司正在追求这一路径。 文章承认每位工程师每天的代码行数是一个不完美的衡量标准，但声称在 2026 年第二季度实现了 8 倍的改进。Anthropic 还指出，他们的 AI 可以用 unsafe Rust 重写程序并发现安全漏洞，尽管批评者认为这些并非真正的突破。

hackernews · meetpateltech · Jun 4, 16:20 · [社区讨论](https://news.ycombinator.com/item?id=48400842)

**背景**: 递归自我改进（RSI）是指 AI 系统重写自身代码以变得更强大的过程，可能导致智能爆炸。这一概念是 AGI 和超级智能讨论的核心，具有重大的安全影响。Anthropic 是一家致力于构建可靠、可引导 AI 系统的 AI 安全公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Recursive_self-improvement">Recursive self-improvement</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些用户对 Anthropic 的说法表示怀疑，指出频繁的宕机和缺乏非 AI 领域的突破。另一些人则提出安全担忧，质疑全力追求递归自我改进是否与 Anthropic 宣称的安全目标一致。少数评论者还批评了公司的技术表现，例如终端应用占用内存过高。

**标签**: `#AI safety`, `#recursive self-improvement`, `#Anthropic`, `#machine learning`, `#software engineering`

---

<a id="item-3"></a>
## [华为 KVarN：原生 vLLM 后端的 KV 缓存量化方案](https://github.com/huawei-csl/KVarN) ⭐️ 8.0/10

华为发布了 KVarN，这是一个原生的 vLLM 后端，用于 KV 缓存量化，声称性能优于 TQ，质量优于 FP16。 这可以通过减少内存使用同时保持高输出质量，显著提升 LLM 推理效率，有利于 GPT-4 等模型的大规模部署。 KVarN 作为 vLLM 的原生后端集成，可以直接使用而无需外部依赖，其目标是 KV 缓存量化，以减少长序列推理时的内存占用。

hackernews · theanonymousone · Jun 4, 15:18 · [社区讨论](https://news.ycombinator.com/item?id=48399974)

**背景**: KV 缓存存储先前 token 的键和值张量，以避免自回归 LLM 中的重复计算。量化降低这些张量的精度（例如从 FP16 到 INT4）以节省内存，但通常会降低质量。KVarN 旨在实现更好的权衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/features/quantization/quantized_kvcache/">Quantized KV Cache - vLLM Documentation</a></li>
<li><a href="https://huggingface.co/blog/kv-cache-quantization">Unlocking Longer Generation with Key-Value Cache Quantization</a></li>

</ul>
</details>

**社区讨论**: 评论者对声称的性能-质量权衡表示惊讶，有人询问是否真的优于 TQ 和 FP16。另一个人质疑为什么没有作为 PR 提交给 vLLM，表明对更广泛采用的兴趣。

**标签**: `#quantization`, `#vLLM`, `#KV-cache`, `#LLM inference`, `#Huawei`

---

<a id="item-4"></a>
## [Meta 在智能眼镜上推出人脸识别功能](https://www.buchodi.com/meta-glasses-facial-recognition/) ⭐️ 8.0/10

Meta 已在其 Ray-Ban 智能眼镜中加入人脸识别技术，使佩戴者能够实时识别他人。该功能名为 Name Tag，在更新中悄然加入，立即引发了隐私和法律方面的担忧。 这标志着可穿戴 AI 迈出了重要一步，但也引发了关于监控、同意和生物识别数据使用的严重伦理与法律问题。它可能为消费设备中部署人脸识别开创先例，影响全球隐私规范和法规。 Meta 曾在 2021 年考虑为第一代 Ray-Ban 智能眼镜添加人脸识别，但因技术挑战和伦理担忧而放弃。据报道，新功能通过将实时摄像头画面与已知人脸数据库进行比对来工作，并因可能被跟踪者或犯罪分子滥用而受到批评。

hackernews · buchodi · Jun 4, 19:36 · [社区讨论](https://news.ycombinator.com/item?id=48403588)

**背景**: 人脸识别技术通过数字图像或视频帧识别或验证个人身份。Meta 的 Ray-Ban 等智能眼镜已具备摄像头和 AI 能力，但添加实时人脸识别显著增加了隐私风险，因为旁观者可能在不知情或未同意的情况下被识别。伊利诺伊州的《生物识别信息隐私法》（BIPA）等法律对生物识别数据的收集进行监管，Meta 此举可能面临此类法规下的法律挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nytimes.com/2026/02/13/technology/meta-facial-recognition-smart-glasses.html">Meta Plans to Add Facial Recognition Technology to Its Smart ...</a></li>
<li><a href="https://www.wired.com/story/meta-ray-ban-oakley-smart-glasses-no-face-recognition-civil-society/">Meta Is Warned That Facial Recognition Glasses Will Arm Sexual Predators | WIRED</a></li>

</ul>
</details>

**社区讨论**: 评论者表达了兴趣与担忧的混合情绪。一位用户希望有一个离线版本，在不牺牲隐私的情况下帮助解决面孔失认症（脸盲）。另一位回忆说，Google Glass 明确禁止此类应用。一些人建议使用红外 LED 等反制措施来干扰人脸识别，而另一些人则预测将引发 BIPA 相关的法律诉讼。

**标签**: `#facial recognition`, `#privacy`, `#smart glasses`, `#Meta`, `#ethics`

---

<a id="item-5"></a>
## [最高法院支持 FCC 对位置数据销售的罚款](https://arstechnica.com/tech-policy/2026/06/att-and-verizon-lose-supreme-court-case-over-fines-for-selling-location-data/) ⭐️ 8.0/10

最高法院以 8 比 1 裁定，FCC 可以对 AT&T 和 Verizon 出售客户位置数据的行为处以罚款，且不违反其第七修正案规定的陪审团审判权。 这一裁决确认了 FCC 通过行政罚款执行隐私保护的权力，为针对电信运营商的数据隐私执法树立了先例。 该案解决了巡回法院的分歧——第五巡回法院支持 AT&T，第二巡回法院支持 Verizon；最高法院的裁决有利于 FCC，允许约 1.96 亿美元的罚款继续执行。

rss · Ars Technica · Jun 4, 21:25

**背景**: FCC 曾提议对主要运营商未经同意向第三方出售实时位置数据的行为处以罚款。AT&T 和 Verizon 辩称，根据第七修正案，FCC 寻求金钱处罚的执法行动需要陪审团审判，并援引了 2024 年最高法院的 Jarkesy 诉 SEC 案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.scotusblog.com/2026/06/court-rules-against-cell-service-providers-over-right-to-jury-trial-in-fcc-proceedings/">Court rules against cell service providers over right to jury trial in FCC ...</a></li>
<li><a href="https://www.complianceweek.com/regulatory-enforcement/fcc-finalizes-196m-in-fines-against-telecoms-for-sharing-location-data/34719.article">FCC finalizes $196M in fines against telecoms for sharing location data</a></li>
<li><a href="https://www.jdsupra.com/legalnews/fcc-enforcement-in-flux-circuit-courts-4449988/">FCC Enforcement in Flux: Circuit Courts Split on Forfeiture... - JDSupra</a></li>

</ul>
</details>

**标签**: `#privacy`, `#telecom`, `#supreme court`, `#data regulation`, `#FCC`

---

<a id="item-6"></a>
## [Dashlane 披露加密密码库遭攻击详情](https://arstechnica.com/security/2026/06/dashlane-explains-how-attackers-managed-to-download-encrypted-password-vaults/) ⭐️ 8.0/10

Dashlane 披露，攻击者通过大规模针对用户来下载加密密码库，利用数量优势提高了成功率。 此事件揭示了一种针对密码管理器的新型攻击方式，可能削弱用户信任，并凸显了加强账户保护（如多因素认证）的必要性。 攻击者并未破解加密，而是利用如果获取账户访问权限即可下载许多用户密码库的事实。Dashlane 未披露受影响用户的具体数量。

rss · Ars Technica · Jun 4, 20:02

**背景**: 像 Dashlane 这样的密码管理器将用户凭证存储在加密密码库中，通过主密码在本地解密。零知识架构意味着提供商无法访问密码库内容。然而，如果攻击者获取了用户的主密码或会话令牌，他们可以下载加密密码库并尝试离线暴力破解攻击。

**标签**: `#security`, `#password manager`, `#cyberattack`, `#Dashlane`, `#encryption`

---

<a id="item-7"></a>
## [Roblox 收购 Morpheus AI，实现实时逼真世界生成](https://www.4gamer.net/games/612/G061218/20260604013/) ⭐️ 8.0/10

Roblox 于 2026 年 6 月 4 日宣布收购专注于实时视频生成模型的初创公司 Morpheus AI。此次收购旨在将生成式 AI 与 Roblox 的游戏引擎相结合，实现实时逼真的世界生成。 此次收购标志着将生成式 AI 与传统游戏引擎相结合的重要一步，可能通过允许创作者实时生成逼真环境，彻底改变 Roblox 上的用户生成内容。它可能为交互式 3D 体验树立新标准，并加速 AI 在游戏开发中的应用。 Morpheus AI 的技术能够实时模拟交互式世界，超越了离线预渲染的 AI 视频生成。Roblox 计划利用 Morpheus AI 的模型来增强其 Roblox Reality 愿景，为用户创建的世界添加更高保真度的纹理、逼真的光照和流畅的物理效果。

rss · 4Gamer.net · Jun 4, 03:50

**背景**: Roblox 是一个流行的在线平台，允许用户使用其专有游戏引擎创建和游玩游戏。生成式 AI 模型（如视频生成模型）可以从文本或其他输入创建视觉内容。混合方法将游戏引擎的确定性控制与 AI 的创造性灵活性相结合，能够实现以前难以实时实现的动态逼真环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://about.roblox.com/newsroom/2026/06/pioneering-ai-founders-join-to-accelerate-roblox-reality-vision">Pioneering AI Founders Join to Accelerate Roblox Reality ... | Roblox</a></li>
<li><a href="https://digg.com/ai/f2gs6dgz">Morpheus AI founder Xun Huang and his team join Roblox to develop...</a></li>

</ul>
</details>

**标签**: `#Roblox`, `#AI`, `#game engine`, `#real-time rendering`, `#acquisition`

---

<a id="item-8"></a>
## [Cloudflare 收购 Vite 创建者 VoidZero](https://blog.cloudflare.com/voidzero-joins-cloudflare/) ⭐️ 7.0/10

Cloudflare 收购了 VoidZero，这是一家开源公司，旗下拥有 Vite JavaScript 工具链及相关工具。该收购于 2026 年 6 月 4 日宣布，旨在将 VoidZero 的技术整合到 Cloudflare 的开发者平台中。 此次收购对 JavaScript 生态系统意义重大，因为 Vite 是数百万开发者广泛使用的构建工具。它引发了关于 Vite 及其他 VoidZero 项目在 Cloudflare 旗下未来治理和开源可持续性的疑问。 VoidZero 是 Vite 背后的公司，Vite 是一款以速度和零配置著称的下一代前端构建工具。此次收购包括 VoidZero 的团队及其开源项目，Cloudflare 承诺保持其开源性质和路线图。

hackernews · coloneltcb · Jun 4, 13:00 · [社区讨论](https://news.ycombinator.com/item?id=48398055)

**背景**: Vite 是一款现代 JavaScript 构建工具，为 Web 应用提供快速的热模块替换（HMR）和优化构建。它已成为前端开发生态系统的基石，被 Vue.js、React 和 Svelte 等框架使用。VoidZero 的成立旨在以开源优先的方式开发和维护 Vite 及相关工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.businesswire.com/news/home/20260604108073/en/Cloudflare-Acquires-VoidZero-to-Build-the-Future-of-the-AI-Native-Web">Cloudflare Acquires VoidZero to Build the Future of the AI-Native Web</a></li>
<li><a href="https://siliconangle.com/2026/06/04/cloudflare-acquires-voidzero-maker-vite-javascript-toolchain/">Cloudflare acquires VoidZero, maker of the Vite JavaScript toolchain - SiliconANGLE</a></li>
<li><a href="https://vite.dev/">Vite | Next Generation Frontend Tooling</a></li>

</ul>
</details>

**社区讨论**: 社区评论对此次收购表示不安，担心 Cloudflare 的商业利益最终可能改变 Vite 的方向或开放性。一些用户注意到开源项目被收购的模式，并对可持续性表示担忧，而另一些人则认为这是为开发提供资金的积极一步。

**标签**: `#acquisition`, `#javascript`, `#vite`, `#cloudflare`, `#open-source`

---

<a id="item-9"></a>
## [高斯点溅射：新型实时 3D 渲染技术](https://momentsingraphics.de/Siggraph2026.html) ⭐️ 7.0/10

高斯点溅射提出了一种利用高斯溅射进行实时 3D 图形渲染的新技术，该技术已在 Siggraph 2026 上展示。 该技术可能实现更高效、更逼真的实时渲染，有望影响游戏开发和虚拟现实应用。 该方法基于 SIGGRAPH 2023 的 3D 高斯溅射（3DGS），但侧重于基于点的溅射以提高性能和质量。

hackernews · ibobev · Jun 4, 10:48 · [社区讨论](https://news.ycombinator.com/item?id=48396792)

**背景**: 高斯溅射是一种体积渲染技术，可直接渲染点云而无需转换为多边形。2023 年引入的 3D 高斯溅射为逼真的 3D 重建提供了比 NeRF 更快的替代方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Gaussian_splatting">Gaussian splatting - Wikipedia</a></li>
<li><a href="https://leeyngdo.github.io/blog/computer-graphics/2024-04-09-gaussian-splatting/">[Graphics] Gaussian Splatting</a></li>
<li><a href="https://www.visoric.com/en/gaussian-splatting">Gaussian Splatting - Visoric GmbH</a></li>

</ul>
</details>

**社区讨论**: 社区评论表达了对潜在游戏应用的兴趣，将这项技术与历史方法（如 Ecstatica 的椭球渲染）进行比较，并请求学习溅射的教程。一些用户质疑高斯点溅射在锐利特征方面与网格溅射相比如何。

**标签**: `#computer graphics`, `#3D rendering`, `#Gaussian splatting`, `#real-time rendering`

---

<a id="item-10"></a>
## [台积电难以满足激增的 AI 芯片需求](https://www.theverge.com/tech/943066/tsmc-ai-demand-struggles) ⭐️ 7.0/10

台积电 CEO 魏哲家表示，尽管公司在美国扩建工厂，但仍难以满足美国客户对 AI 芯片激增的需求。 这凸显了 AI 硬件供应链中的关键瓶颈，可能减缓 AI 发展，并影响依赖台积电先进芯片的科技公司。 台积电是全球最大的半导体制造商，目前生产 3 纳米芯片，并计划在 2025 年实现 2 纳米量产。其美国扩张包括在亚利桑那州凤凰城新建一座晶圆厂。

rss · The Verge · Jun 4, 14:15

**背景**: 台积电生产用于数据中心和自动驾驶等 AI 应用的先进芯片。AI 需求的激增使全球半导体供应链承压，台积电的产能无法跟上步伐。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/TSMC">TSMC - Wikipedia</a></li>
<li><a href="https://pr.tsmc.com/english/news/3210">TSMC Intends to Expand Its Investment in the United States to US ...</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#AI`, `#semiconductors`, `#supply chain`, `#hardware`

---

<a id="item-11"></a>
## [对走红网络的人形机器人视频的怀疑指南](https://arstechnica.com/ai/2026/06/the-skeptics-guide-to-humanoid-robots-going-viral-on-the-internet/) ⭐️ 7.0/10

Ars Technica 上的一篇文章批判性地审视了走红网络的人形机器人视频如何经常夸大能力，误导公众对机器人技术的理解。 这很重要，因为扭曲的认知可能导致不切实际的期望、误导政策决策以及机器人研究资金的错误分配。 文章重点介绍了机器人演示被编辑或编排以显得比实际更强大的具体例子，并讨论了病毒式传播成功与实际技术进展之间的差距。

rss · Ars Technica · Jun 4, 22:23

**背景**: 人形机器人旨在模仿人类的形态和运动，但实现稳健的现实世界性能仍然极具挑战性。病毒式传播的视频通常展示精心策划的成功，而忽略失败或限制，从而造成关于技术现状的误导性叙述。

**标签**: `#robotics`, `#AI`, `#public perception`, `#humanoid robots`, `#media analysis`

---

<a id="item-12"></a>
## [爱沙尼亚基准测试评估大模型抗俄宣传能力](https://arstechnica.com/ai/2026/06/these-llms-are-the-best-at-resisting-russian-propaganda/) ⭐️ 7.0/10

爱沙尼亚语言研究所发布了一项新的“宣传抵抗”基准测试，对数十个大语言模型避免附和俄罗斯战略叙事的能力进行了排名。 该基准测试提供了一种评估大模型对抗地缘政治宣传的新方法，对信息战和敏感地区的人工智能部署具有重要意义。 该基准测试专门针对俄罗斯联邦在其战略叙事中使用的主题进行测试，结果显示不同大模型的效果差异显著。

rss · Ars Technica · Jun 4, 20:44

**背景**: 爱沙尼亚是一个波罗的海国家，历史上曾遭苏联占领，因此对俄罗斯的虚假信息尤为敏感。政府资助的 ELI 创建了这一基准测试，以帮助打击通过人工智能系统传播的俄罗斯宣传。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2026/06/these-llms-are-the-best-at-resisting-russian-propaganda/">These LLMs are the best at resisting Russian propaganda</a></li>
<li><a href="https://en.wikipedia.org/wiki/Estonia">Estonia - Wikipedia</a></li>

</ul>
</details>

**标签**: `#LLM`, `#AI safety`, `#propaganda`, `#benchmark`, `#geopolitics`

---

<a id="item-13"></a>
## [数据中心应对用水问题面临审查](https://arstechnica.com/ai/2026/06/how-data-center-operators-are-tackling-their-water-use-problems/) ⭐️ 7.0/10

数据中心运营商正在探索减少用水的方法，例如浸没式冷却和水回收，因为其环境影响受到越来越多的审查。 这很重要，因为数据中心，尤其是支持 AI 的数据中心，每天消耗数百万加仑的水，给干旱地区的当地水源带来压力。减少用水对于可持续技术发展至关重要。 大型数据中心每天可消耗多达 500 万加仑的水，相当于一个 1 万至 5 万人口城镇的用水量。浸没式冷却和水回收是正在采用的方法之一。

rss · Ars Technica · Jun 4, 14:11

**背景**: 数据中心需要大量水来冷却服务器，尤其是在传统冷却系统中。谷歌、微软和亚马逊等超大规模运营商运营着大型设施，其水足迹受到审查。AI 工作负载正在增加能源和水的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eesi.org/articles/view/data-centers-and-water-consumption">Data Centers and Water Consumption | Article | EESI</a></li>
<li><a href="https://submer.com/blog/datacenter-water-usage/">Datacenter Water Usage: Where Does It All Go? - Submer</a></li>
<li><a href="https://www.csrwire.com/press_releases/798026-worlds-ai-generators-rethinking-water-usage-data-centers-build-more">The World’s AI Generators: Rethinking Water Usage in Data Centers ...</a></li>

</ul>
</details>

**标签**: `#data centers`, `#sustainability`, `#water usage`, `#hyperscalers`

---

<a id="item-14"></a>
## [Waymo 自动驾驶出租车电池被重新用于电网储能](https://arstechnica.com/science/2026/06/used-waymo-robotaxi-batteries-become-backup-storage-for-power-grids/) ⭐️ 7.0/10

Waymo 与 B2U Storage Solutions 合作，将其电动自动驾驶出租车车队中退役的电池重新用于加州和德克萨斯州电网的固定式储能系统。 这一举措延长了电动汽车电池的使用寿命，减少了浪费，并提供了经济高效的电网储能，支持可再生能源整合和电网稳定性。 这些重新利用的电池在加州兰开斯特提供了 32 兆瓦时的储能容量，B2U 的解决方案可在要求较低的固定应用中将电池寿命延长数年。

rss · Ars Technica · Jun 4, 11:00

**背景**: 电动汽车电池通常在容量衰减到约 70-80% 时退役，但它们对于电网备用等要求较低的应用仍有很大价值。像 B2U 这样的公司专门从事电池的重新利用而非回收，这些电池在固定储能中可服务超过十年。公用事业规模的电池储能预计将快速增长，从 2020 年的 1.5 吉瓦增加到 2025 年的 30 吉瓦，从而产生了对二次寿命电池的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techcrunch.com/2026/06/04/waymos-spent-robotaxi-batteries-will-be-used-as-grid-storage/">Waymo 's spent robotaxi batteries will be used as grid... | TechCrunch</a></li>
<li><a href="https://electrek.co/2026/06/04/waymo-retired-robotaxi-batteries-are-heading-back-to-work-b2u/">Waymo ’s retired robotaxi batteries are heading back to work | Electrek</a></li>
<li><a href="https://arstechnica.com/science/2026/06/used-waymo-robotaxi-batteries-become-backup-storage-for-power-grids/">Used Waymo robotaxi batteries become backup storage for power...</a></li>

</ul>
</details>

**标签**: `#energy storage`, `#electric vehicles`, `#sustainability`, `#Waymo`, `#grid`

---

<a id="item-15"></a>
## [法院被 AI 生成的诉讼淹没](https://www.technologyreview.com/2026/06/04/1138391/courts-coping-ai-lawsuits/) ⭐️ 7.0/10

由自我代理诉讼人提交的 AI 生成诉讼激增，使法院不堪重负，此类诉讼的比例从 2023 年的 1%上升至 2026 年的 18%。 这一趋势威胁到法律系统的效率和公平性，因为法院必须花费额外时间来识别和处理低质量或无意义的 AI 生成诉讼。 科罗拉多州的联邦治安法官 Maritza Braswell 报告称，她需要仔细审查许多由自我代理诉讼人提交的 AI 撰写文件，但指出并非所有 AI 生成的诉讼都有问题。

rss · MIT Technology Review · Jun 4, 10:50

**背景**: 自我代理诉讼人（pro se litigants）在没有律师的情况下自行出庭，通常是因为费用高昂或案件本身较弱。像大型语言模型这样的 AI 工具现在可以生成法律文件，导致大量可能包含错误或缺乏实质内容的诉讼涌入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/04/1138391/courts-coping-ai-lawsuits/">How courts are coping with a flood of AI - generated lawsuits</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pro_Se_Litigant">Pro Se Litigant</a></li>

</ul>
</details>

**标签**: `#AI`, `#legal`, `#courts`, `#regulation`, `#technology`

---

<a id="item-16"></a>
## [Framework 13 Pro：面向 Linux 用户的 MacBook Pro 替代品](https://www.pcgamer.com/hardware/gaming-laptops/i-got-my-hands-on-frameworks-macbook-pro-for-linux-users-and-its-tagline-isnt-just-marketing-hyperbole/) ⭐️ 7.0/10

Framework 发布了 Laptop 13 Pro，这是一款采用 CNC 铝合金机身、搭载 Intel Core Ultra 处理器和 LPCAMM2 内存、并获得 Ubuntu 认证的笔记本电脑，定位为面向开发者的 MacBook Pro 替代品。 这款笔记本电脑满足了 Linux 开发者对高端、良好支持的硬件的日益增长的需求，提供了可维修和可升级的替代方案，以对抗苹果封闭的生态系统。 Framework 13 Pro 配备触觉触控板，续航时间长达 20 小时，并且是首款获得 Ubuntu 认证的 Framework 笔记本电脑，确保开箱即用的 Linux 兼容性。

rss · PC Gamer · Jun 4, 02:42

**背景**: Framework 以其模块化、可维修的笔记本电脑而闻名，用户可升级 RAM、存储和接口等组件。13 Pro 是高端版本，采用一体式铝合金机身，面向偏好 Linux 而非 macOS 或 Windows 的开发者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Framework_Computer">Framework Computer - Wikipedia</a></li>
<li><a href="https://frame.work/">Framework | Framework Computer | Modular Laptops & PCs You Can...</a></li>
<li><a href="https://the-gadgeteer.com/2026/04/28/framework-13-pro-laptop/">Framework Laptop 13 Pro : 20-Hour Battery, LPCAMM2 Memory</a></li>

</ul>
</details>

**标签**: `#Framework`, `#Linux`, `#laptop`, `#open-source hardware`, `#developer tools`

---

<a id="item-17"></a>
## [复古科技育儿：限制孩子接触现代科技](https://havenweb.org/2026/05/28/retro-tech.html) ⭐️ 6.0/10

一位家长在 Hacker News 上分享了通过精心挑选和限制技术来养育孩子的策略，例如使用一台没有互联网连接的 2012 年 MacBook Pro 和复古游戏机。 这种方法引起了许多担心孩子过度使用屏幕和数字成瘾的家长的共鸣，引发了关于家庭中有意使用技术的更广泛讨论。 这位家长提供了一台装有离线创意工具（如 Affinity Photo、Python）和乐高机器人套件的家庭笔记本电脑，另一位评论者则使用 jmp.chat 在不提供智能手机的情况下实现短信功能。

hackernews · mawise · Jun 4, 16:02 · [社区讨论](https://news.ycombinator.com/item?id=48400588)

**背景**: 数字极简主义倡导有意识地使用技术，以减少干扰并专注于有意义的活动。复古科技育儿通过使用较旧、较简单的设备来限制接触现代联网设备，从而应用了这一理念。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@sebastiantan/digital-minimalism-part-1-what-is-digital-minimalism-now-minimal-5e69210f93c8">Digital minimalism — Part 1: — What is digital minimalism ? | Medium</a></li>
<li><a href="https://www.goneminimal.com/digital-minimalism/">Digital Minimalism - Guide to Simplicity in Our WiFi World</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了个人经验，例如提供离线编程工具和复古游戏机，并指出限制技术使用可以减少社交排斥，同时仍能通过 jmp.chat 等服务进行交流。

**标签**: `#parenting`, `#technology`, `#retro-tech`, `#digital minimalism`

---

<a id="item-18"></a>
## [欧盟版 Kagi 替代品 Uruky 新增图片搜索和 URL 重写功能](https://uruky.com/?il=en) ⭐️ 6.0/10

Uruky，一个基于欧盟的、定位为 Kagi 替代品的隐私搜索引擎，现已推出图片搜索和 URL 重写功能。该服务还宣布计划在六个月内采用源代码可用许可证（PolyForm Shield），取代之前基于 NDA 的代码访问模式。 这为欧盟注重隐私的用户提供了一个功能更丰富的 Kagi 替代品，而 Kagi 是一家总部在美国、服务器在塞尔维亚的公司。转向源代码可用许可证可能提高透明度和信任度，但其中的非竞争条款可能限制社区采用。 图片搜索和 URL 重写功能现已上线；用户首次充值时可解决一个工作量证明验证码获得 2 小时免费试用。计划中的 PolyForm Shield 许可证允许查看和修改源代码，但禁止用于与 Uruky 竞争的目的。

hackernews · BrunoBernardino · Jun 4, 08:56 · [社区讨论](https://news.ycombinator.com/item?id=48396004)

**背景**: Uruky 是一个基于订阅的搜索引擎，强调隐私和欧盟数据主权，作为 Kagi 的替代品推出。Kagi 本身是一个付费搜索引擎，由一位美国企业家创立，其唯一办公室位于塞尔维亚贝尔格莱德，并受美国搜查令约束。像 PolyForm Shield 这样的源代码可用许可证介于专有和开源软件之间，通常包含禁止竞争使用的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/polyformproject/polyform-licenses">GitHub - polyformproject/ polyform - licenses : source text for Polyform ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Source-available_license">Source-available license</a></li>
<li><a href="https://blog.rcaptcha.app/articles/proof-of-work-captcha-explained">Proof - of - Work CAPTCHA Explained: ALTCHA... | rCAPTCHA Blog</a></li>

</ul>
</details>

**社区讨论**: 评论者对 Uruky 基于欧盟的做法表示兴趣，但也提出了与 Kagi 相比搜索质量和用户体验方面的担忧。一些人质疑搜索结果的来源（例如是否使用 Yandex），并建议采用延迟开源发布作为替代许可模式。其他人强调，有效的搜索结果比单纯的隐私更重要。

**标签**: `#search engine`, `#privacy`, `#EU`, `#Kagi alternative`, `#open source`

---

<a id="item-19"></a>
## [马斯克试图终止 FTC 对 X 数据处理的审计](https://arstechnica.com/tech-policy/2026/06/elon-musk-tries-again-to-escape-ftc-audits-of-x-data-handling/) ⭐️ 6.0/10

埃隆·马斯克再次试图终止 FTC 要求对 X 数据处理实践进行独立审计的 20 年同意令，声称公司已改善隐私合规。 如果成功，X 将不再接受定期独立审计，可能增加用户隐私风险，并削弱对主要社交媒体平台的监管。 FTC 的命令是在之前的隐私违规后实施的，要求进行 20 年审计，并赋予该机构索取文件的权力。公众评论警告称，马斯克无法被信任保护用户隐私。

rss · Ars Technica · Jun 4, 19:49

**背景**: FTC 同意令是在 X（前身为 Twitter）被发现未经同意将用户数据用于广告后实施的。独立审计是 FTC 确保公司遵守隐私承诺的常用工具。马斯克此前曾因数据实践与监管机构发生冲突。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/06/elon-musk-tries-again-to-escape-ftc-audits-of-x-data-handling/">Elon Musk tries again to escape FTC audits of X data handling</a></li>

</ul>
</details>

**社区讨论**: FTC 案卷上的公众评论者压倒性地反对马斯克的请求，认为 X 的数据处理历史以及马斯克本人的言论表明缺乏对隐私的承诺。一些人担心终止审计将开创危险先例。

**标签**: `#privacy`, `#regulation`, `#X`, `#FTC`, `#data handling`

---

<a id="item-20"></a>
## [有线电视游说团体敦促 FCC 放宽外国路由器禁令](https://arstechnica.com/tech-policy/2026/06/cable-lobby-warns-of-chaos-if-fcc-doesnt-relax-ban-on-foreign-routers/) ⭐️ 6.0/10

有线电视行业游说团体 NCTA 已请求 FCC 豁免 2026 年对外国制造消费路由器的禁令，理由是内存和 ABF 基板材料短缺。 如果不放宽禁令，供应链中断可能导致路由器短缺和消费者价格上涨，影响全美的互联网接入。 FCC 于 2026 年 3 月发布的禁令以国家安全为由禁止进口新的外国制造消费路由器，但允许公司申请豁免。

rss · Ars Technica · Jun 4, 18:34

**背景**: 2026 年，FCC 以国家安全风险为由禁止了新的外国制造消费路由器。同时，电子行业正面临 ABF 基板的全球短缺，这是路由器中高性能芯片的关键组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/2026_FCC_ban_on_foreign-made_consumer_routers">2026 FCC ban on foreign-made consumer routers</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2026-03-23/fcc-bans-all-foreign-made-routers-citing-security-risks">FCC Bans All Foreign -Made Routers Citing Security Risks - Bloomberg</a></li>
<li><a href="https://a2globalelectronics.com/shortage-mitigation/abf-substrate-shortages/">a2globalelectronics.com/ shortage -mitigation/abf- substrate - shortages</a></li>

</ul>
</details>

**标签**: `#FCC`, `#routers`, `#supply chain`, `#tech policy`, `#lobbying`

---

<a id="item-21"></a>
## [熊蜂展现自发解决问题的能力](https://arstechnica.com/science/2026/06/bumblebees-can-spontaneously-solve-problems-study-finds/) ⭐️ 6.0/10

芬兰的一项研究发现，熊蜂无需事先训练就能自发解决昆虫版的经典“盒子与香蕉”问题。 这一发现挑战了关于昆虫认知的假设，表明熊蜂拥有此前被认为仅限于高等动物的灵活解决问题的能力。 “盒子与香蕉”问题涉及使用工具或中间步骤来达到目标；在本例中，蜜蜂必须移动一个球才能获得奖励。蜜蜂自发解决了任务，表明这是顿悟而非试错学习。

rss · Ars Technica · Jun 4, 18:00

**背景**: “盒子与香蕉”问题是认知心理学中的经典任务，受试者必须使用工具（如盒子）来获取够不到的目标（如香蕉）。它常用于研究动物的解决问题能力和顿悟。熊蜂以其复杂的社会行为和学习能力而闻名，但此前尚未明确证明其具有自发解决问题的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://quizlet.com/1109082094/problem-solving-and-expertise-development-in-cognitive-psychology-flash-cards/">Problem Solving and Expertise Development in Cognitive... | Quizlet</a></li>

</ul>
</details>

**标签**: `#biology`, `#cognition`, `#insects`, `#problem-solving`

---

<a id="item-22"></a>
## [哥伦比亚大学数据泄露暴露无关人员社保号](https://arstechnica.com/tech-policy/2026/06/my-ssn-was-exposed-in-a-breach-at-columbia-a-school-i-have-no-connection-with/) ⭐️ 6.0/10

哥伦比亚大学承认，去年的一次数据泄露暴露了与该学校无关的个人社保号，暴露出其违规通知和第三方数据处理方面的不足。 此事件凸显了第三方数据处理日益增长的风险，以及组织未能通知直接社区之外受影响个人的问题，可能影响数百万从未与泄露实体互动的人。 此次泄露影响范围超出哥伦比亚大学的学生和员工，包括与大学无关的人员。通知流程不足，导致许多人不知其社保号已泄露。

rss · Ars Technica · Jun 4, 13:48

**背景**: 数据泄露常暴露社保号等敏感信息，可能被用于身份盗窃。第三方服务提供商经常处理此类数据，泄露可能通过这些关系的漏洞发生。违规通知法律通常要求组织通知受影响个人，但合规性可能不一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://constella.ai/blog/verifying-the-national-public-data-breach/">Verifying the National Public Data Breach | Constella</a></li>
<li><a href="https://www.malwarebytes.com/cybersecurity/basics/ssn-on-dark-web">Your Social Security Number is already exposed | SSN on Dark Web</a></li>
<li><a href="https://veridion.com/blog-posts/third-party-risk-management-vs-vendor-risk-management/">Third Party Risk Management vs Vendor Risk Management</a></li>

</ul>
</details>

**标签**: `#data breach`, `#privacy`, `#security`, `#SSN exposure`

---

<a id="item-23"></a>
## [AI 诉讼与数据中心虚拟电厂](https://www.technologyreview.com/2026/06/04/1138408/the-download-ai-lawsuits-virtual-power-plants-data-centers/) ⭐️ 6.0/10

一份新闻通讯报道，法院正面临 AI 生成诉讼的激增，被标记的诉状从 2023 年的 1%上升到 2026 年的 18%，并探讨了利用虚拟电厂（VPP）为数据中心供电的方案。 这凸显了 AI 生成的法律文件对司法系统日益增长的挑战，以及虚拟电厂为高能耗数据中心提供灵活清洁能源的潜力，影响技术政策和能源可持续性。 科罗拉多州的法官 Maritza Braswell 指出，AI 生成诉状的增加未必令人担忧，因为法院正在开发应对工具。虚拟电厂聚合太阳能、电池等分布式能源，充当单一发电厂，提供电网服务和削峰填谷。

rss · MIT Technology Review · Jun 4, 12:10

**背景**: 虚拟电厂（VPP）是一个由分布式能源（如家用太阳能和电池）组成的网络，通过协调向电网供电，帮助平衡供需。AI 生成诉讼是指借助 AI 起草的法律文件，可能导致错误或无理索赔，给法院系统带来负担。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/06/04/1138391/courts-coping-ai-lawsuits/">How courts are coping with a flood of AI - generated lawsuits</a></li>
<li><a href="https://en.wikipedia.org/wiki/Virtual_power_plant">Virtual power plant</a></li>
<li><a href="https://rmi.org/clean-energy-101-virtual-power-plants/">Clean Energy 101: Virtual Power Plants - RMI</a></li>

</ul>
</details>

**标签**: `#AI`, `#lawsuits`, `#data centers`, `#energy`, `#policy`

---

<a id="item-24"></a>
## [科罗拉多州合作社首次实现 100%可再生能源月](https://www.utilitydive.com/news/colorado-electric-co-op-marks-first-month-serving-100-renewables/822042/) ⭐️ 6.0/10

科罗拉多州电力合作社 Holy Cross Energy 在 3 月份首次实现了 100%可再生能源供电。首席执行官 Bryan Hannegan 宣布计划扩大智能电气化和需求灵活性项目。 这一里程碑表明，农村电力合作社能够可靠地为成员提供 100%可再生能源，为其他公用事业树立了先例。它凸显了将高比例可再生能源整合到电网中的可行性日益增强。 该合作社通过自有可再生能源发电、购电协议和可再生能源证书的组合实现了这一目标。Holy Cross Energy 为科罗拉多州西部约 4.5 万名成员提供服务。

rss · Utility Dive · Jun 4, 18:19

**背景**: 电力合作社是会员所有的公用事业，通常服务于农村地区。Holy Cross Energy 一直致力于到 2030 年实现 100%清洁能源的目标。智能电气化是指利用数字技术优化用电时间和方式，而需求灵活性允许客户根据电网条件调整用电量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.holycross.com/">Home - Holy Cross Energy</a></li>

</ul>
</details>

**标签**: `#renewable energy`, `#utility`, `#sustainability`, `#electric grid`

---

<a id="item-25"></a>
## [天然气行业报告呼吁确保电网可靠性的稳定供气](https://www.utilitydive.com/news/electric-sector-needs-firm-gas-supply-to-protect-grid-reliability-report/821981/) ⭐️ 6.0/10

一份为天然气委员会准备的报告指出，稳定天然气供应对保障电网可靠性至关重要，并引用了 2021 年冬季风暴 Uri 的教训。 该报告凸显了天然气与电力行业之间持续的协调挑战，这可能影响极端天气事件期间的电网韧性。 报告赞扬了冬季风暴 Uri 后引入的改革，但强调天然气与电力行业之间仍需更好的协调。

rss · Utility Dive · Jun 4, 13:41

**背景**: 2021 年 2 月的冬季风暴 Uri 导致德克萨斯州及其他地区大面积停电，造成数百人死亡和数十亿美元损失。该风暴暴露了能源系统的脆弱性，包括依赖在极端寒冷中失效的可中断天然气供应。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Winter_Storm_Uri">Winter Storm Uri</a></li>
<li><a href="https://tdem.texas.gov/disasters/winter-storm-uri">Texas Severe Winter Storm DR-4586</a></li>

</ul>
</details>

**标签**: `#energy`, `#grid reliability`, `#natural gas`, `#infrastructure`

---

<a id="item-26"></a>
## [北卡罗来纳州电力合作社采用电网电池提升韧性](https://www.canarymedia.com/articles/batteries/north-carolina-electric-co-ops-grid-batteries) ⭐️ 6.0/10

在 2022 年 7 月一场严重风暴导致大面积停电后，北卡罗来纳州的电力合作社正越来越多地部署电网电池，以提升韧性并管理峰值需求。 这一转变表明，服务农村和郊区的电力合作社可以利用电池储能来降低停电风险并节约成本，可能为其他地区提供范例。 为近 6 万用户服务的 Wake Electric 合作社是受风暴影响的合作社之一，目前正转向电池用于备用电源和削峰填谷。

rss · Latitude Media (Canary Media) · Jun 4, 07:30

**背景**: 电网电池（即电池储能系统，BESS）可储存电能，并在峰值需求或停电期间快速放电以稳定电网。电力合作社是会员所有的公用事业，通常服务于电网基础设施较薄弱的农村地区，因此成为分布式储能解决方案的理想候选。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Grid_batteries">Grid batteries</a></li>
<li><a href="https://en.wikipedia.org/wiki/Utility_cooperative">Utility cooperative - Wikipedia</a></li>

</ul>
</details>

**标签**: `#grid batteries`, `#electric cooperatives`, `#energy resilience`, `#North Carolina`

---

<a id="item-27"></a>
## [PJM 区域公用事业公司未共享智能电表数据](https://www.canarymedia.com/articles/utilities/utilities-not-sharing-smart-meter-data) ⭐️ 6.0/10

尽管在 PJM 互联区域投入近 60 亿美元安装了 1200 万个智能电表，但公用事业公司并未与客户或第三方共享数据，削弱了这些设备在节能和节省成本方面的潜力。 这种数据囤积行为阻碍了消费者和能源服务提供商优化用电，从而无法在美国最大的能源市场降低峰值需求和账单，影响 6700 万客户。 PJM 互联是美国最大的竞争性批发电市场，服务 13 个州及华盛顿特区部分地区。智能电表本意是实现实时能源管理，但数据访问受限削弱了其效果。

rss · Latitude Media (Canary Media) · Jun 4, 07:30

**背景**: 智能电表是数字设备，可近乎实时记录用电量并将数据传送给公用事业公司和客户。它们是电网现代化和实现需求响应计划的关键组成部分。PJM 互联是一个区域输电组织，协调东部互联电网的批发电量传输。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PJM_Interconnection">PJM Interconnection</a></li>

</ul>
</details>

**标签**: `#smart meters`, `#energy`, `#data sharing`, `#utilities`, `#PJM`

---

<a id="item-28"></a>
## [美国各州阳台太阳能法律各不相同](https://www.canarymedia.com/articles/solar/states-passing-balcony-solar-laws) ⭐️ 6.0/10

文章报道称，阳台太阳能套件（即插即用的 DIY 系统）正日益流行，但美国各州不一致的法律阻碍了其普及。 这很重要，因为阳台太阳能可以让租房者和公寓住户获得可再生能源，但法律障碍可能限制其对清洁能源转型的潜在影响。 该文章最初发表于 2026 年 4 月 6 日，并于 2026 年 6 月 4 日更新，表明该政策领域正在持续发展。

rss · Latitude Media (Canary Media) · Jun 4, 07:00

**背景**: 阳台太阳能套件是小型太阳能板系统，可插入标准墙壁插座，用户无需专业安装即可发电。它们在屋顶太阳能不可行的城市地区尤其受欢迎。然而，关于并网和安全的规定因州而异，影响了其合法性和普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amosolarpv.com/the-ultimate-guide-to-balcony-solar-kits-powering-your-urban-home-with-a-compact-solar-system/">The Ultimate Guide To Balcony Solar Kits : Powering Your Urban...</a></li>
<li><a href="https://www.pluginsolar.co.uk/">Plug In Solar - Your DIY Solar Solution</a></li>

</ul>
</details>

**标签**: `#solar energy`, `#renewable energy`, `#policy`, `#DIY solar`

---

<a id="item-29"></a>
## [Visual Arts 披露因未授权访问导致数据泄露](https://www.4gamer.net/games/753/G075391/20260604016/) ⭐️ 6.0/10

Visual Arts 宣布因未授权访问可能导致内部信息和个人信息泄露，起因是视觉小说《anemoi》的母数据被未授权上传。 此次泄露暴露了敏感的公司和用户数据，可能影响数千名用户，并损害日本主要视觉小说发行商 Visual Arts 的信任。 泄露涉及云存储，暴露了《anemoi》的母数据和数千条用户记录。Visual Arts 已采取措施并报告了该事件。

rss · 4Gamer.net · Jun 4, 04:22

**背景**: Visual Arts 是一家日本公司，以其 Key 品牌的视觉小说闻名。《anemoi》是一款全年龄视觉小说，于 2026 年 4 月 24 日在日本发行，并计划在全球 Steam 平台发布。其母数据被未授权上传导致发现了更广泛的泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Anemoi_(video_game)">Anemoi (video game ) - Wikipedia</a></li>
<li><a href="https://xeber.world/en/article/visualarts-confirms-data-breach-leaking-anemoi-and-thousands-of-user-records-deed2a">VisualArts Data Breach Exposes Anemoi and Thousands of User...</a></li>

</ul>
</details>

**标签**: `#security`, `#data breach`, `#Japan`, `#gaming`

---

<a id="item-30"></a>
## [英特尔被曝 18A 节点笔记本 CPU 供应困难](https://www.pcgamer.com/hardware/processors/new-report-claims-intel-is-struggling-to-supply-laptop-cpus-based-on-its-latest-18a-node-after-speaking-to-computex-sources/) ⭐️ 6.0/10

一份新报告援引 Computex 消息人士称，英特尔在基于其最新 18A 节点供应笔记本 CPU 方面遇到困难，但该节点本身可能并无缺陷。 这很重要，因为英特尔的 18A 节点对其代工雄心和与台积电的竞争力至关重要；供应问题可能导致产品延迟并削弱客户信任。 该报告基于匿名消息来源，缺乏具体证据，因此应视为传闻。英特尔此前曾表示，18A 节点的流片计划在 2025 年上半年进行。

rss · PC Gamer · Jun 4, 16:20

**背景**: 英特尔的 18A 节点是一种 1.8 纳米级工艺，是 CEO 帕特·基辛格“五年五个节点”战略的一部分。它旨在与台积电的 2 纳米节点竞争，是英特尔代工业务的核心。该公司最近取消了 20A 节点，以专注于 18A。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://overclock3d.net/news/cpu_mainboard/intel-scraps-its-20a-process-node-and-bets-the-farm-on-18a-arrow-lake-is-built-by-tsmc/">Intel scraps its 20A process node and bets the farm on 18 A - OC3D</a></li>
<li><a href="https://www.tweaktown.com/news/112004/intel-introduces-xeon-7-diamond-rapids-cpu-lineup-built-on-the-18a-p-process-node/index.html">Intel introduces Xeon 7 'Diamond Rapids' CPU lineup, built on the...</a></li>
<li><a href="https://www.trendforce.com/news/2025/02/24/news-intel-to-begin-18a-tape-outs-in-1h25-reportedly-leading-tsmcs-2nm-launch/">[News] Intel to Begin 18 A Tape-outs in 1H25, Reportedly Leading...</a></li>

</ul>
</details>

**标签**: `#Intel`, `#18A node`, `#semiconductors`, `#laptop CPUs`

---