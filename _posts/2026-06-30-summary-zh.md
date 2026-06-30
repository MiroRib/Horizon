---
layout: default
title: "Horizon Summary: 2026-06-30 (ZH)"
date: 2026-06-30
lang: zh
---

> From 156 items, 26 important content pieces were selected

---

1. [Anthropic 发布 Claude Sonnet 5，增强智能体能力](#item-1) ⭐️ 8.0/10
2. [Claude Code 隐写标记请求](#item-2) ⭐️ 8.0/10
3. [Anthropic 推出 Claude Science 数据科学工具](#item-3) ⭐️ 8.0/10
4. [开发者构建毫米波雷达用于材料分类](#item-4) ⭐️ 8.0/10
5. [ZLUDA 6 发布：在非 Nvidia GPU 上运行未修改的 CUDA 应用](#item-5) ⭐️ 8.0/10
6. [Google 关闭 Tenor GIF API，X、Discord 等平台被迫调整](#item-6) ⭐️ 8.0/10
7. [新攻击利用虚假前提绕过 AI 浏览器护栏](#item-7) ⭐️ 8.0/10
8. [RFK Jr. 在 FDA 小组中安插肽类支持者](#item-8) ⭐️ 8.0/10
9. [Anthropic SDK Python v0.115.0 新增托管代理与 Webhook 支持](#item-9) ⭐️ 7.0/10
10. [Google DeepMind 发布 Nano Banana 2 Lite](#item-10) ⭐️ 7.0/10
11. [通过 WebAssembly 将 Kubernetes 移植到浏览器](#item-11) ⭐️ 7.0/10
12. [农业 AI 的未来取决于数据准备度](#item-12) ⭐️ 7.0/10
13. [Godot 禁止 AI 编写的代码贡献](#item-13) ⭐️ 7.0/10
14. [Valve 确认探索 Arm 游戏未来](#item-14) ⭐️ 7.0/10
15. [Valve：内存和存储危机威胁 Steam Machine 供应](#item-15) ⭐️ 7.0/10
16. [Knoppix Live CD 怀旧引发社区反思](#item-16) ⭐️ 6.0/10
17. [1852 年关于群体疯狂的书籍仍引发共鸣](#item-17) ⭐️ 6.0/10
18. [Rockstar 员工在 GTA VI 发布前寻求工会认可](#item-18) ⭐️ 6.0/10
19. [Reddit 将要求登录才能访问旧版 Reddit](#item-19) ⭐️ 6.0/10
20. [亚马逊以恶意软件为由阻止 Fire Stick 侧载](#item-20) ⭐️ 6.0/10
21. [苹果就 Epic 案藐视法庭裁决上诉至最高法院](#item-21) ⭐️ 6.0/10
22. [佛罗里达州禁止地方净零排放目标](#item-22) ⭐️ 6.0/10
23. [Ars Live 讨论 New Glenn 灾难后续](#item-23) ⭐️ 6.0/10
24. [长寿新前沿：细胞重编程](#item-24) ⭐️ 6.0/10
25. [空气产品公司取消路易斯安那州蓝氢项目](#item-25) ⭐️ 6.0/10
26. [Xbox 据报道考虑出售或关闭 Arkane 及其他工作室](#item-26) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Sonnet 5，增强智能体能力](https://www.anthropic.com/news/claude-sonnet-5) ⭐️ 8.0/10

Anthropic 发布了 Claude Sonnet 5，这是一个更快、能力更强的模型，在智能体能力和指令遵循方面有显著改进，且价格具有竞争力。 此次发布推动了智能体 AI 的发展趋势，使自主任务执行更加可及和经济，可能加速在编程、自动化和专业工作流程中的应用。 Claude Sonnet 5 是 Anthropic 最新一代的首个 Sonnet 模型，以 Sonnet 价格提供顶级智能，适用于编程、智能体和日常办公。社区基准测试显示，其性能达到 GLM-5.2 水平，成本翻倍但速度也翻倍，不过在常识问答和组合工具调用任务上表现不佳。

hackernews · marinesebastian · Jun 30, 17:59 · [社区讨论](https://news.ycombinator.com/item?id=48736605)

**背景**: 智能体 AI 指能够自主决策并在有限监督下行动的系统，可使用浏览器和终端等工具。之前的 Sonnet 模型（3.5、3.6、3.7）是首批在编程中展现出色智能体能力的模型，Sonnet 5 在此基础上进一步发展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-sonnet-5">Introducing Claude Sonnet 5 \ Anthropic</a></li>
<li><a href="https://aws.amazon.com/blogs/machine-learning/introducing-claude-sonnet-5-on-aws-anthropics-most-capable-sonnet-model/">Introducing Claude Sonnet 5 on AWS: Anthropic’s most capable ...</a></li>

</ul>
</details>

**社区讨论**: 社区反馈不一：一些用户报告指令遵循和一次性完成复杂任务方面有显著改进，而另一些用户则指出在常识问答和工具调用方面存在弱点。关于成本效益存在争议，有人认为在更高努力水平下 Opus 可能更优。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#Claude`, `#agentic`

---

<a id="item-2"></a>
## [Claude Code 隐写标记请求](https://thereallo.dev/blog/claude-code-prompt-steganography) ⭐️ 8.0/10

一名开发者发现，Anthropic 的 Claude Code 工具会根据用户的 API 基础 URL 和时区，在系统提示中静默嵌入隐写标记，从而对请求进行指纹识别以检测中国用户。 这种未公开的行为引发了开发者对 AI 工具隐私和信任的严重担忧，因为它未经同意秘密收集并传输用户特定数据，可能违反 CFAA 等法律框架。 标记根据三种检测结果（中国时区、中国代理域名或中国 AI 实验室）修改系统提示中的日期格式等元素。该技术称为提示隐写术，是通过检查 Claude Code 二进制文件发现的。

hackernews · kirushik · Jun 30, 15:44 · [社区讨论](https://news.ycombinator.com/item?id=48734373)

**背景**: 隐写术是将信息隐藏在其他数据中以避免检测的做法。在此背景下，Claude Code 在 AI 提示中嵌入隐藏标记，以谨慎标记来自某些地区的流量，可能是为了防止中国公司进行模型蒸馏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aimadetools.com/blog/claude-code-steganography-explained/">Claude Code Is Steganographically Marking Requests: What It Means</a></li>
<li><a href="https://byteiota.com/claude-code-is-marking-requests-what-anthropic-hid/">Claude Code Is Marking Requests: What Anthropic Hid</a></li>
<li><a href="https://cybersecuritynews.com/anthropic-claude-hidden-code/">Anthropic's Claude Code Reportedly Uses Hidden Code to Detect ...</a></li>

</ul>
</details>

**社区讨论**: 社区意见分歧：一些人批评缺乏透明度和潜在的法律违规，而另一些人则认为意图（防止模型窃取）明确，反应过度。评论者还指出，这种粗糙的实现本可以更巧妙。

**标签**: `#AI`, `#privacy`, `#steganography`, `#ethics`, `#developer tools`

---

<a id="item-3"></a>
## [Anthropic 推出 Claude Science 数据科学工具](https://claude.com/product/claude-science) ⭐️ 8.0/10

Anthropic 发布了 Claude Science，这是一个基于本地服务器的 AI 工作台，用于数据科学和计算研究，集成了 HPC 集群和数据库。 该产品将 AI 与科学计算连接起来，使研究人员能够在自己的基础设施上运行复杂分析，同时保持数据隐私和可审计性。 Claude Science 运行一个本地服务器，配有基于 Web 的 UI，与 Claude Code 和 Cowork 不同，并包含 Biomni HPC 等工具的连接器，支持可审计的逐步分析。

hackernews · lebovic · Jun 30, 17:07 · [社区讨论](https://news.ycombinator.com/item?id=48735770)

**背景**: Anthropic 此前提供了用于编程的 Claude Code 和用于桌面自动化的 Claude Cowork。Claude Science 将这一能力扩展到科学研究，面向制药等受监管行业的数据科学家，这些行业的数据不能离开本地环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>
<li><a href="https://grokipedia.com/page/Claude_for_Life_Sciences">Claude for Life Sciences</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调本地服务器架构是安全环境的关键差异化因素，一位连接 HPC 工具的构建者分享了深入的技术见解。在 RNAi 生物农药设计领域的测试显示结果合格但不突出，AI 承认了自身的局限性。

**标签**: `#AI`, `#data science`, `#Anthropic`, `#scientific computing`, `#HPC`

---

<a id="item-4"></a>
## [开发者构建毫米波雷达用于材料分类](https://gauthier-lechevalier.com/radar) ⭐️ 8.0/10

一位开发者构建了一款调频连续波毫米波雷达用于材料分类，旨在检测墙壁中的石棉，并发布了详细的项目成功与失败经验总结。 该项目展示了一种实用、低成本的非破坏性材料识别方法，有助于解决欧洲及全球建筑中普遍存在的石棉检测问题。 该雷达采用调频连续波技术，通过随时间扫频从反射的 chirp 信号中生成材料特征。概念验证设备成功分类了常见材料，但尚未展示在不同浓度下可靠检测石棉的能力。

hackernews · GL26 · Jun 30, 17:29 · [社区讨论](https://news.ycombinator.com/item?id=48736137)

**背景**: 毫米波雷达工作在毫米波频段（通常 24-100+ GHz），能够穿透干墙等非金属材料，适用于穿墙感知。FMCW 雷达发射频率扫频的 chirp 信号，反射信号的时延和频移揭示目标的距离和材料特性。石棉是一种曾广泛用于建筑的有害矿物纤维，非侵入式检测困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://gauthier-lechevalier.com/radar">How I built a mmWave material classification radar</a></li>
<li><a href="https://link.springer.com/chapter/10.1007/978-981-19-2412-5_8">Obstructed Material Classification Using mmWave Radar with ...</a></li>
<li><a href="https://mesothelioma.net/handheld-technology-innovating-asbestos-detection-field/">Handheld Tech for Asbestos Detection | Mesothelioma.net</a></li>

</ul>
</details>

**社区讨论**: 评论者赞扬了详细的经验教训和项目的雄心，但有人质疑该设备能否在低浓度下可靠区分石棉与其他材料。其他人则提出了替代应用，如检测皮肤癌筛查或一般检查中的不连续性。

**标签**: `#mmWave`, `#radar`, `#material classification`, `#asbestos detection`, `#hardware`

---

<a id="item-5"></a>
## [ZLUDA 6 发布：在非 Nvidia GPU 上运行未修改的 CUDA 应用](https://vosen.github.io/ZLUDA/blog/zluda-update-q1q2-2026/) ⭐️ 8.0/10

ZLUDA 6 已发布，允许未修改的 CUDA 应用程序在非 Nvidia GPU 上运行，现作为周末项目开发，新增了预 alpha 阶段的 32 位 PhysX 支持等功能。 此版本意义重大，因为它扩展了依赖 CUDA 的软件的 GPU 兼容性，减少了供应商锁定，使用户能够在 AMD 或其他 GPU 上运行 CUDA 应用程序，这对 AI/ML 工作负载和旧版游戏 PhysX 效果尤其重要。 该项目不再获得商业资助，现为周末项目，优先级从商业可行性转向开发者兴趣。新的 32 位 PhysX 支持处于预 alpha 阶段，允许像《黑手党 2》这样的老游戏在 AMD Radeon GPU 上运行 PhysX 效果，性能显著提升。

hackernews · Tiberium · Jun 30, 10:34 · [社区讨论](https://news.ycombinator.com/item?id=48730713)

**背景**: ZLUDA 是一个兼容层，将 CUDA API 调用转换为 AMD 的 ROCm/HIP 平台，使未修改的 CUDA 程序能够在非 Nvidia GPU 上以接近原生的性能运行。CUDA 是 Nvidia 的专有并行计算平台，广泛应用于 AI、HPC 和游戏领域。此前，ZLUDA 曾获得商业支持，但面临 AMD 的法律挑战，导致其目前转向开源、爱好者驱动的开发模式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/vosen/ZLUDA">GitHub - vosen/ZLUDA: CUDA on non-NVIDIA GPUs · GitHub</a></li>
<li><a href="https://www.tomshardware.com/software/a-project-to-bring-cuda-to-non-nvidia-gpus-is-making-major-progress-zluda-update-now-has-two-full-time-developers-working-on-32-bit-physx-support-and-llms-amongst-other-things">A project to bring CUDA to non-Nvidia GPUs is making major progress — ZLUDA update now has two full-time developers, working on 32-bit PhysX support and LLMs, amongst other things | Tom's Hardware</a></li>
<li><a href="https://videocardz.com/newz/zluda-adds-early-32-bit-physx-support-for-amd-radeon-gpus-mafia-2-performance-triples-on-rx-9070-xt">ZLUDA adds 32-bit PhysX support for Radeon GPUs, Mafia 2 FPS triples on RX 9070 XT - VideoCardz.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调，转向周末项目对创新是积极的一步，尤其是对 32 位 PhysX 支持的兴趣，因为 Nvidia 最初计划在 RTX 50 系列中放弃该支持。用户还询问了与 Vulkan 相比的 LLM 性能，并指出名称 'ZLUDA' 在波兰语中意为 '海市蜃楼'。

**标签**: `#CUDA`, `#GPU`, `#Open Source`, `#Compatibility Layer`, `#HPC`

---

<a id="item-6"></a>
## [Google 关闭 Tenor GIF API，X、Discord 等平台被迫调整](https://arstechnica.com/gadgets/2026/06/google-kills-tenor-gif-api-forcing-changes-at-x-discord-and-more/) ⭐️ 8.0/10

Google 于 2026 年 1 月 13 日弃用了 Tenor GIF API，X、Discord、Bluesky 和 WhatsApp 等第三方平台无法再使用该 API 搜索和嵌入 GIF。Tenor 网站及其 GIF 库仍可访问，但公共 API 已关闭。 此次弃用打乱了主流社交和消息平台的 GIF 集成，迫使它们迁移到替代服务或自行构建解决方案。这凸显了依赖免费第三方 API 的风险，以及科技公司整合或关闭开发者工具的更广泛趋势。 Google 于 2018 年 3 月收购 Tenor 以增强视觉搜索，但 API 关闭于 2026 年 1 月 13 日宣布。Tenor 网站及其可搜索的 GIF 库仍可访问，用户仍可直接获取 GIF，但应用集成已中断。

rss · Ars Technica · Jun 30, 20:38

**背景**: Tenor 是一个流行的 GIF 搜索和分享平台，许多应用通过其免费 API 集成，让用户查找和发送 GIF。API 弃用是指逐步淘汰 API 的过程，通常会提前公布迁移时间表。Google 此举延续了减少免费 API 服务的模式，类似于其他 Google API 的弃用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/Tenor_API_shutdown">Tenor API shutdown</a></li>
<li><a href="https://tenor.com/gifapi/documentation">GIF API - Better, Faster & Free | Tenor Documentation</a></li>
<li><a href="https://document360.com/blog/api-deprecation/">What is API Deprecation & Its Guidelines - Document360</a></li>

</ul>
</details>

**社区讨论**: 未提供社区评论，但鉴于影响巨大，开发者可能对广泛使用的服务突然消失表示沮丧，并担忧迁移成本。部分人可能会讨论替代的 GIF API（如 Giphy）或自托管方案。

**标签**: `#API deprecation`, `#Google`, `#Tenor`, `#GIF`, `#developer ecosystem`

---

<a id="item-7"></a>
## [新攻击利用虚假前提绕过 AI 浏览器护栏](https://arstechnica.com/security/2026/06/ai-browsers-can-be-lulled-into-a-dream-world-where-guardrails-no-longer-apply/) ⭐️ 8.0/10

研究人员发现了一种新型攻击，通过向 AI 浏览器提供虚假前提（例如声称 2+2=5），诱使其忽略安全护栏。这种操纵导致底层 LLM 执行本应被阻止的违禁指令。 此次攻击揭示了依赖 LLM 护栏的 AI 浏览器存在根本性漏洞，随着这类浏览器日益普及，安全风险极为严重。它表明，即使是简单的虚假前提也能完全瓦解安全机制，可能导致数据窃取或有害内容生成等恶意行为。 该攻击通过向 LLM 提供一个明显错误的陈述，模型将其接受为真，从而改变其推理上下文并禁用护栏。这种技术不同于传统的越狱攻击，利用了模型倾向于遵从用户提供前提的特性。

rss · Ars Technica · Jun 30, 20:03

**背景**: AI 浏览器集成大型语言模型（LLM）来帮助用户完成总结网页或填写表单等任务。护栏是旨在防止 LLM 生成有害或禁止输出的安全机制。然而，LLM 容易受到对抗性输入的攻击，这些输入可以绕过护栏，正如这种新的虚假前提攻击所展示的那样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2504.11168">[2504.11168] Bypassing LLM Guardrails: An Empirical Analysis of Evasion Attacks against Prompt Injection and Jailbreak Detection Systems</a></li>
<li><a href="https://arxiv.org/html/2503.10690">Battling Misinformation: An Empirical Study on Adversarial Factuality in Open-Source Large Language Models</a></li>
<li><a href="https://fuzzinglabs.com/attacking-reasoning-models/">LLM Vulnerabilities - Attacking Reasoning Models</a></li>

</ul>
</details>

**标签**: `#AI security`, `#LLM`, `#browser vulnerability`, `#adversarial attack`, `#guardrail bypass`

---

<a id="item-8"></a>
## [RFK Jr. 在 FDA 小组中安插肽类支持者](https://arstechnica.com/health/2026/06/rfk-jr-stacks-fda-panel-with-peptide-peddlers-as-fda-scientists-oppose-access/) ⭐️ 8.0/10

RFK Jr. 不顾 FDA 科学家的警告，将未经监管的肽类药物的支持者任命到 FDA 咨询小组中，这些肽类药物缺乏严格的安全性和有效性数据。 此举可能损害 FDA 的科学诚信和公众信任，可能导致批准未经充分测试但广泛销售的、不安全或无效的肽类药物。 肽类药物常被宣传用于抗衰老和增肌，但专家警告存在污染、标签错误和未知长期风险。FDA 咨询委员会的作用是就产品的安全性和有效性提供独立的科学建议。

rss · Ars Technica · Jun 30, 18:25

**背景**: 肽是短链氨基酸，在体内可发挥类似激素或信号分子的作用。虽然有些肽被批准为药物，但许多作为未经监管的补充剂销售，声称未经证实。FDA 咨询委员会是独立的专家小组，负责审查证据并就监管决策进行投票，安插有偏见的成员可能损害这一过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.verywellhealth.com/are-peptides-dangerous-11963081">We Asked a Doctor: Should You Trust the Hype Around Peptides?</a></li>
<li><a href="https://www.fda.gov/advisory-committees">Advisory Committees | FDA</a></li>
<li><a href="https://legalclarity.org/what-are-fda-advisory-committees-and-how-do-they-work/">What Are FDA Advisory Committees and How Do They Work?</a></li>

</ul>
</details>

**标签**: `#FDA`, `#peptide drugs`, `#public health`, `#regulatory policy`, `#controversy`

---

<a id="item-9"></a>
## [Anthropic SDK Python v0.115.0 新增托管代理与 Webhook 支持](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.115.0) ⭐️ 7.0/10

Anthropic 发布了其 Python SDK 的 v0.115.0 版本，新增了对托管代理事件增量流式传输、代理覆盖、反向分页、保险库凭据注入范围限定以及代理和部署 webhook 事件的支持。 这些功能使开发者能够构建更具交互性和安全性的基于代理的应用程序，支持实时事件流和细粒度凭据管理，扩展了 SDK 在企业场景中的实用性。 该版本包含一个单一提交 (8c23f7e)，捆绑了所有新的 API 功能。托管代理事件增量流式传输允许实时跟踪代理操作，而反向分页简化了向后浏览大型结果集的操作。

github · stainless-app[bot] · Jun 30, 19:47

**背景**: 托管代理是 Anthropic 用于构建可执行多步骤任务的自主 AI 代理的框架。事件增量流式传输在代理执行期间提供细粒度更新，适用于 UI 监控。保险库凭据注入范围限定允许从外部保险库（如 HashiCorp Vault）安全地、有范围地访问密钥。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/managed-agents/events-and-streaming">Session event stream - Claude Platform Docs</a></li>
<li><a href="https://www.hashicorp.com/en/resources/credential-injection-with-boundary-and-vault">Credential Injection with Boundary and Vault - HashiCorp</a></li>
<li><a href="https://apidog.com/blog/pagination-in-rest-apis/">How to Implement Pagination in REST APIs (Step by Step Guide)</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#SDK`, `#Python`, `#Managed Agents`, `#API`

---

<a id="item-10"></a>
## [Google DeepMind 发布 Nano Banana 2 Lite](https://deepmind.google/models/gemini-image/flash-lite/) ⭐️ 7.0/10

Google DeepMind 发布了 Nano Banana 2 Lite（Gemini 3.1 Flash-Lite Image），这是一个蒸馏后的图像生成模型，比前代更快、成本更低，文本渲染能力有所提升，但长宽比控制有限。 该模型支持快速、低成本的图像生成，适用于 A/B 测试和社交应用等场景，但其易用性也引发了在房地产列表中被滥用的担忧，AI 生成的室内图像可能误导买家。 Nano Banana 2 Lite 生成图像时间不到 5 秒，而基础模型约需 30 秒，但它无法通过编程方式强制设置长宽比。该模型通过 Google AI Studio 提供，需要 Google One 账户，Workspace 用户无法使用。

hackernews · minimaxir · Jun 30, 16:48 · [社区讨论](https://news.ycombinator.com/item?id=48735444)

**背景**: 蒸馏模型是大型模型的压缩版本，以牺牲部分质量为代价换取速度和效率。Nano Banana 2 Lite 是 Nano Banana 2 的蒸馏变体，旨在以更低成本实现高速生成。文本渲染是指模型在图像中生成可读文字的能力，这是许多 AI 图像生成器面临的挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/models/gemini-image/flash-lite/">Gemini 3.1 Flash-Lite Image – Nano Banana 2 Lite — Google ...</a></li>
<li><a href="https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/">Start building with Nano Banana 2 Lite and Gemini Omni Flash</a></li>
<li><a href="https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-2-lite-and-gemini-omni-flash-available/">Nano Banana 2 Lite and Gemini Omni Flash available | Google ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论既表达了对模型速度的兴奋，也表达了对 Google 账户限制的不满。用户还担心 AI 生成的房地产图像会误导买家，并指出该模型在基准测试中未与 ChatGPT 进行比较。

**标签**: `#AI`, `#image generation`, `#Google DeepMind`, `#machine learning`, `#product launch`

---

<a id="item-11"></a>
## [通过 WebAssembly 将 Kubernetes 移植到浏览器](https://ngrok.com/blog/i-ported-kubernetes-to-the-browser) ⭐️ 7.0/10

一位开发者使用 WebAssembly 和 ngrok 将 Kubernetes 完全移植到浏览器中运行，创建了一个名为 Webernetes 的交互式学习环境。 该项目消除了对本地集群或云资源的需求，使 Kubernetes 教育更加普及，用户可以直接在浏览器中进行动手实验。 该项目在 GitHub 上开源，并包含一个位于 webernetes-demo.ngrok.app 的实时演示，目前侧重于概念和架构学习，而非完整的 kubectl 掌握。

hackernews · peterdemin · Jun 30, 20:48 · [社区讨论](https://news.ycombinator.com/item?id=48738985)

**背景**: Kubernetes 是一个容器编排平台，通常需要一组机器来运行。WebAssembly (Wasm) 是一种轻量级二进制格式，可在浏览器和其他环境中运行，提供沙盒执行。ngrok 提供安全隧道，将本地服务暴露到互联网。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ngrok.com/">ngrok: deliver your apps, APIs, and AI on local and prod</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ngrok">Ngrok</a></li>
<li><a href="https://www.cncf.io/blog/2024/03/12/webassembly-on-kubernetes-from-containers-to-wasm-part-01/">WebAssembly on Kubernetes: from containers to Wasm (part 01)</a></li>

</ul>
</details>

**社区讨论**: 社区称赞该项目的教育潜力，一位评论者指出它非常适合概念学习。另一位开发者分享了一个关于 Kubernetes 调度的相关游戏，还引发了关于使用 AI 验证代码是否符合 Kubernetes 行为的讨论。

**标签**: `#kubernetes`, `#webassembly`, `#education`, `#devtools`, `#cloud-native`

---

<a id="item-12"></a>
## [农业 AI 的未来取决于数据准备度](https://www.technologyreview.com/2026/06/30/1139513/agriculture-is-ready-for-ai-but-its-data-isnt/) ⭐️ 7.0/10

MIT Technology Review 报道称，尽管 AI 在农业领域具有变革潜力，但行业在投资 AI 解决方案之前，必须首先解决数据质量和基础设施方面的挑战。 这很重要，因为农业面临成本波动和气候压力，AI 可以提高效率和产量，但数据准备不足可能导致投资浪费和采用失败。 研究表明，AI 驱动的预测模型可以改善作物管理，但数据噪声、数据迷雾和数据孤岛是阻碍智慧农业的核心质量挑战。

rss · MIT Technology Review · Jun 30, 12:00

**背景**: 农业中的 AI 利用机器学习和物联网为作物管理提供实时监测和预测分析。然而，农业数据通常碎片化、噪声大且孤立，难以训练可靠的模型。解决这些数据问题是成功部署 AI 的前提。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1640805/full">Frontiers | Data quality challenges of AIGC application in ...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S2666154325001334">Artificial intelligence in agriculture: Advancing crop ...</a></li>
<li><a href="https://www.analyticsinsight.net/agriculture/challenges-and-limitations-of-ai-in-agriculture">AI in Agriculture: Challenges Explained - Analytics Insight</a></li>

</ul>
</details>

**标签**: `#AI`, `#agriculture`, `#data quality`, `#technology adoption`

---

<a id="item-13"></a>
## [Godot 禁止 AI 编写的代码贡献](https://www.pcgamer.com/gaming-industry/open-source-game-engine-godot-will-no-longer-accept-ai-authored-code-contributions-we-cant-trust-heavy-users-of-ai-to-understand-their-code-enough-to-fix-it/) ⭐️ 7.0/10

Godot 游戏引擎宣布不再接受由 AI 编写的代码贡献，理由是信任和可维护性问题。 这一政策反映了开源社区对 AI 生成代码质量和可维护性的日益担忧，并可能影响其他项目采取类似限制。 该决定旨在防止大量低质量的“AI 垃圾代码”涌入，这些代码维护者无法可靠地修复或理解。

rss · PC Gamer · Jun 30, 17:36

**背景**: Godot 是一个流行的开源跨平台游戏引擎，采用 MIT 许可证发布。随着 AI 代码生成工具越来越普遍，许多开源项目正在努力处理可能包含贡献者不完全理解的代码的贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="https://godotengine.org/">Godot Engine - Free and open source 2D and 3D game engine</a></li>

</ul>
</details>

**标签**: `#open source`, `#AI`, `#game development`, `#software engineering`, `#policy`

---

<a id="item-14"></a>
## [Valve 确认探索 Arm 游戏未来](https://www.pcgamer.com/hardware/steam-machines/valve-says-it-is-definitely-investigating-an-arm-based-gaming-future-on-top-of-its-work-on-fex/) ⭐️ 7.0/10

Valve 确认其正在“明确地”探索基于 Arm 的游戏未来，并基于其 FEX 模拟器的工作，该模拟器允许 x86 和 x86-64 Linux 二进制文件在 ARM64 设备上运行。 这标志着 PC 游戏硬件可能发生转变，因为基于 Arm 的处理器能效更高，可能带来新的形态，类似于移动和笔记本电脑市场的变化。 FEX 是一个快速的用户态 x86 和 x86-64 模拟器，适用于 ARM64 Linux，支持 32 位和 64 位二进制文件，并可配合 Wine/Proton 运行 Windows 游戏。

rss · PC Gamer · Jun 30, 16:32

**背景**: Arm 处理器因其能效而广泛应用于移动设备，但在桌面游戏领域存在有限。像 FEX 这样的模拟器使 x86 软件能在 Arm 硬件上运行，可能扩展游戏生态系统。Valve 的 Steam Deck 已使用 x86 AMD APU，但基于 Arm 的未来可能为便携游戏带来新机遇。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fex-emu.com/">FEX-Emu – A fast linux usermode x86 and x86-64 emulator</a></li>
<li><a href="https://github.com/FEX-Emu/FEX">GitHub - FEX-Emu/FEX: A fast usermode x86 and x86-64 emulator ... Getting Started | FEX-Emu/FEX | DeepWiki FEX download | SourceForge.net FEX-Emu · GitHub FEX-Emu – A fast linux usermode x86 and x86-64 emulator FEX-Emu: Run x86 and x86-64 Apps on ARM64 Linux Devices ...</a></li>
<li><a href="https://www.technoidgamingpc.com/blogs/gaming-pcs/arm-based-processors-future-of-gaming-pcs">ARM-Based Processors: Powering the Future of Gaming PCs</a></li>

</ul>
</details>

**标签**: `#Valve`, `#Arm`, `#gaming`, `#FEX`, `#hardware`

---

<a id="item-15"></a>
## [Valve：内存和存储危机威胁 Steam Machine 供应](https://www.pcgamer.com/hardware/valve-says-the-memory-and-storage-crisis-is-so-bad-its-not-just-a-problem-of-pricing-they-had-to-negotiate-really-hard-just-to-secure-supply-for-the-steam-machine/) ⭐️ 7.0/10

Valve 透露，当前的内存和存储危机非常严重，他们不得不“非常艰难地谈判”才能确保即将推出的 Steam Machine 的供应，这表明短缺问题已超出价格范畴。 这证实了内存和存储短缺是系统性的，甚至影响到 Valve 这样的主要硬件厂商，可能导致 Steam Machine 及其他设备的生产延迟或受限，从而影响消费者和整个 PC 游戏生态系统。 据 IEEE Spectrum 报道，这场危机源于 DRAM 行业的繁荣-萧条周期与史无前例的 AI 硬件基础设施建设相碰撞。Valve 的承认表明，供应限制（而不仅仅是高价）是关键瓶颈。

rss · PC Gamer · Jun 30, 11:38

**背景**: 始于 2025 年的全球内存供应短缺，因供应限制和价格快速上涨影响了 DRAM 和 NAND 闪存。Valve 的 Steam Machine 是一款专为游戏设计的迷你 PC，计划于 2026 年初推出，依赖这些组件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2025–present_global_memory_supply_shortage">2025–present global memory supply shortage - Wikipedia</a></li>
<li><a href="https://spectrum.ieee.org/dram-shortage">AI Boom Fuels DRAM Shortage and Price Surge - IEEE Spectrum</a></li>

</ul>
</details>

**标签**: `#hardware`, `#supply chain`, `#memory`, `#storage`, `#Valve`

---

<a id="item-16"></a>
## [Knoppix Live CD 怀旧引发社区反思](https://www.knopper.net/knoppix/index-en.html) ⭐️ 6.0/10

一篇关于 Knoppix（开创性的 Linux 发行版）的 Hacker News 怀旧帖子引发了广泛讨论，许多用户回忆他们正是通过它首次接触 Linux。 这反映了 Knoppix 在普及 Linux 访问方面的持久影响，特别是对于没有安装权限或技术专长的用户，并凸显了 Live 发行版在降低入门门槛方面的作用。 Knoppix 由 Klaus Knopper 创建，是最早的 Live Linux 发行版之一，无需安装即可从 CD 完全运行，具有自动硬件检测和大量预装软件的特点。

hackernews · hoangvmpc · Jun 30, 12:54 · [社区讨论](https://news.ycombinator.com/item?id=48732056)

**背景**: Live Linux 发行版允许用户从可移动介质启动并运行完整的操作系统，而无需修改硬盘。Knoppix 于 2000 年首次发布，在向许多用户介绍 Linux 方面发挥了重要作用，尤其是在安装操作系统受限或存在风险的环境中。

**社区讨论**: 评论者分享了在学校计算机实验室使用 Knoppix 的美好回忆，常常绕过受限的 Windows 系统。许多人将其归功于激发了他们对编程和 Linux 的兴趣，并最终从事 DevOps 和系统管理工作。

**标签**: `#Linux`, `#Live CD`, `#Knoppix`, `#nostalgia`

---

<a id="item-17"></a>
## [1852 年关于群体疯狂的书籍仍引发共鸣](https://www.gutenberg.org/ebooks/24518) ⭐️ 6.0/10

查尔斯·麦凯 1852 年的著作《非同寻常的大众幻想与群众性癫狂》在 Hacker News 上被讨论，该书以娱乐性但历史修饰过的笔触描述了金融泡沫和群体妄想。 这本书仍是行为经济学和群体心理学的奠基之作，影响了现代对非理性市场行为和投机泡沫的理解。 该书涵盖了南海泡沫和郁金香狂热等历史事件，但现代学者指出麦凯对郁金香泡沫进行了夸大和渲染，几乎没有证据表明其描述的规模。

hackernews · lstodd · Jun 30, 12:47 · [社区讨论](https://news.ycombinator.com/item?id=48731989)

**背景**: 查尔斯·麦凯 1852 年的作品是一部关于群体歇斯底里和金融投机的经典文集。它常在市场心理学和非理性繁荣的讨论中被引用，尽管其历史准确性受到质疑。

**社区讨论**: 评论者认为这本书有趣且富有洞察力，有人特别提到了南海泡沫中一个欺诈性投资计划的轶事。然而，也有人提醒麦凯对郁金香泡沫进行了修饰，推荐了更可靠的现代书籍，如 Quinn 和 Turner 的《繁荣与崩溃》。

**标签**: `#history`, `#behavioral economics`, `#financial bubbles`, `#crowd psychology`

---

<a id="item-18"></a>
## [Rockstar 员工在 GTA VI 发布前寻求工会认可](https://www.theverge.com/games/959668/rockstar-games-workers-union-gta-vi) ⭐️ 6.0/10

Rockstar Games 的员工在《侠盗猎车手 VI》发布前提交了请求，要求自愿承认他们的工会 IWGB 游戏工人工会。 此举凸显了游戏行业持续的劳资紧张关系，并可能为大型工作室的员工组织树立先例，尤其是在 GTA VI 即将发布之际。 此前 Rockstar 去年解雇了 30 多名员工，被指控为破坏工会行为。工会希望解决薪酬透明度、灵活工作安排及其他工作场所问题。

rss · The Verge · Jun 30, 17:04

**背景**: IWGB 游戏工人工会是英国独立工人工会（IWGB）的一个分支，代表英国游戏工作者。破坏工会行为是指雇主用来破坏或削弱工会组织活动的策略。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gameworkers.co.uk/">IWGB Game Workers Union</a></li>
<li><a href="https://en.wikipedia.org/wiki/Union_busting">Union busting</a></li>

</ul>
</details>

**标签**: `#gaming industry`, `#labor unions`, `#software engineering`, `#workplace issues`

---

<a id="item-19"></a>
## [Reddit 将要求登录才能访问旧版 Reddit](https://arstechnica.com/gadgets/2026/06/reddit-will-require-you-to-log-in-to-use-old-reddit-com/) ⭐️ 6.0/10

Reddit 宣布将要求用户登录才能访问 old.reddit.com，理由是滥用爬虫行为。该变更将在未来一个月内逐步实施。 这一政策变化影响了大量偏好经典界面的 Reddit 用户，并可能降低临时访客和搜索引擎对 Reddit 内容的可访问性。 该要求仅适用于未登录用户；已登录用户仍可像以前一样访问 old.reddit.com。Reddit 声称未登录的旧版 Reddit 访问是滥用爬虫的主要来源。

rss · Ars Technica · Jun 30, 21:46

**背景**: Reddit 于 2018 年推出了重新设计的界面，但许多用户仍然更喜欢通过 old.reddit.com 访问的旧版简洁布局。网络爬虫是从网站自动提取数据的技术，常用于数据分析或内容聚合，但也可能被用于垃圾信息或未经授权的数据收集等恶意目的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/06/reddit-will-require-you-to-log-in-to-use-old-reddit-com/">Reddit will require you to log in to use old.reddit.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/Web_scraping">Web scraping</a></li>

</ul>
</details>

**标签**: `#Reddit`, `#policy change`, `#web scraping`, `#user access`

---

<a id="item-20"></a>
## [亚马逊以恶意软件为由阻止 Fire Stick 侧载](https://arstechnica.com/gadgets/2026/06/exec-blames-malware-threat-for-amazon-blocking-sideloading-on-new-fire-sticks/) ⭐️ 6.0/10

亚马逊已阻止新 Fire Stick 设备的侧载功能，称盗版应用带来的恶意软件威胁是这一变化的原因。 这一政策变化限制了用户自定义和安装第三方应用的能力，影响了高级用户和侧载社区。 新的 Fire OS 更新阻止了第三方主屏幕启动器和广告拦截器，从而有效阻止了从未知来源侧载应用。

rss · Ars Technica · Jun 30, 21:04

**背景**: 侧载允许用户安装官方 Amazon 应用商店中没有的应用，常用于 IPTV 和其他媒体应用。亚马逊声称通过侧载分发的盗版应用通常包含恶意软件，对用户构成安全风险。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.howtogeek.com/336602/how-to-sideload-apps-on-the-fire-tv-and-fire-tv-stick/">How to Sideload Apps on the Fire TV and Fire TV Stick How to Sideload Apps on Amazon Fire Stick: Complete Guide ... Amazon Fire Stick App Blocking 2026 - How to Sideload IPTV ... Amazon Is Killing Fire TV Stick Sideloading: How It Works and ... The Secret Fire TV Stick Hack That Amazon Doesn't Want ... - BGR How to Easily Sideload Apps on FireStick with Downloader How to Sideload Apps on the Fire TV and Fire TV Stick</a></li>
<li><a href="https://optimedia.tv/blog/how-to-sideload-apps-on-amazon-fire-stick">How to Sideload Apps on Amazon Fire Stick: Complete Guide ...</a></li>
<li><a href="https://optimedia.tv/blog/amazon-fire-stick-app-blocking-2026-sideload-guide">Amazon Fire Stick App Blocking 2026 - How to Sideload IPTV ...</a></li>

</ul>
</details>

**标签**: `#Amazon`, `#Fire Stick`, `#sideloading`, `#malware`, `#DRM`

---

<a id="item-21"></a>
## [苹果就 Epic 案藐视法庭裁决上诉至最高法院](https://arstechnica.com/tech-policy/2026/06/apple-takes-epic-fight-over-app-store-fees-to-the-supreme-court/) ⭐️ 6.0/10

苹果已向美国最高法院提交请愿书，要求审查其在与 Epic Games 就 App Store 费用问题长期反垄断诉讼中被判藐视法庭的裁决。 此次上诉可能为法院如何执行针对主导科技平台的反垄断禁令树立先例，从而重塑 App Store 政策及开发者费用。 藐视法庭裁决源于苹果被指控未遵守此前要求其修改 App Store 支付规则的禁令；最高法院是否会受理此案尚不确定。

rss · Ars Technica · Jun 30, 20:20

**背景**: Epic Games 诉苹果案始于 2020 年，Epic 指控苹果对应用内购买收取 30%佣金构成反竞争行为。地区法院基本裁定苹果胜诉，但发布禁令要求苹果允许开发者链接至外部支付选项。苹果后来因未完全遵守禁令而被判藐视法庭。

**标签**: `#Apple`, `#Epic Games`, `#antitrust`, `#App Store`, `#legal`

---

<a id="item-22"></a>
## [佛罗里达州禁止地方净零排放目标](https://arstechnica.com/science/2026/06/florida-bans-local-governments-from-pursuing-net-zero-emissions-goals/) ⭐️ 6.0/10

佛罗里达州州长罗恩·德桑蒂斯签署法律，禁止地方政府采纳净零排放目标，称此类政策为“激进的气候政策”。 该法律限制了一个极易受气候影响州的本地气候行动，可能阻碍实现《巴黎协定》等全球减排目标的进展。 该法律基于 2024 年佛罗里达州的一项法规，该法规将气候变化考量从州能源政策中移除，专家警告称这可能会阻止地方在可再生能源和能效方面的举措。

rss · Ars Technica · Jun 30, 13:40

**背景**: 净零排放是指平衡温室气体排放与清除，是《巴黎协定》将全球变暖限制在 1.5°C 的关键目标。美国许多地方政府已设定自己的净零目标，以补充州和联邦的努力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://insideclimatenews.org/news/30062026/florida-law-bans-net-zero-emission-policies/">New Florida Law Bans Local Net-Zero Emissions Policies</a></li>
<li><a href="https://floridaphoenix.com/2026/02/12/local-florida-governments-would-be-banned-from-enacting-climate-change-policies-under-new-proposal/">Local Florida governments would be banned from enacting ...</a></li>
<li><a href="https://www.un.org/en/climatechange/net-zero-coalition">Net Zero Coalition | United Nations - الأمم المتحدة</a></li>

</ul>
</details>

**标签**: `#climate policy`, `#governance`, `#environment`, `#Florida`

---

<a id="item-23"></a>
## [Ars Live 讨论 New Glenn 灾难后续](https://arstechnica.com/space/2026/06/ars-live-whats-the-latest-in-the-aftermath-of-the-new-glenn-catastrophe/) ⭐️ 6.0/10

Ars Technica 将于美国东部时间下午 1 点举办直播，讨论 New Glenn 火箭灾难的后续，包括 4 月 19 日的任务失败和 5 月 28 日的发射台爆炸。 此次直播为航天界提供了一个平台，了解蓝色起源近期挫折的最新情况并提问，这些挫折可能影响该公司的发射计划及更广泛的商业航天产业。 New Glenn 火箭在 2026 年遭遇两次重大失败：4 月 19 日二级异常导致未能入轨，以及 5 月 28 日测试点火期间灾难性的发射台爆炸。蓝色起源计划在 2026 年底前恢复飞行。

rss · Ars Technica · Jun 30, 13:15

**背景**: New Glenn 是蓝色起源的重型轨道火箭，旨在与 SpaceX 的 Falcon 9 和 Falcon Heavy 竞争。4 月 19 日的任务是第三次飞行；第一级成功着陆，但第二级出现故障。5 月 28 日的爆炸发生在卡纳维拉尔角的静态点火测试期间，火箭被摧毁。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2026_New_Glenn_rocket_explosion">2026 New Glenn rocket explosion - Wikipedia</a></li>
<li><a href="https://arstechnica.com/space/2026/06/ars-live-whats-the-latest-in-the-aftermath-of-the-new-glenn-catastrophe/">Ars Live, today: The latest on the aftermath of the New Glenn ...</a></li>
<li><a href="https://www.youtube.com/watch?v=1O90WZJALYc">Blue Origin New Glenn rocket explodes during launch pad test ... Blue Origin vows to resume New Glenn flights by year’s end Blue Origin plans to fly New Glenn rocket again this year ... Blue Origin's New Glenn rocket explodes during test: What ... New Glenn rocket explosion comes after 'mishap' report on ...</a></li>

</ul>
</details>

**标签**: `#space`, `#New Glenn`, `#rocket failure`, `#livestream`

---

<a id="item-24"></a>
## [长寿新前沿：细胞重编程](https://www.technologyreview.com/2026/06/30/1139958/roundtables-longevitys-next-frontier-reprogramming-your-body/) ⭐️ 6.0/10

由《麻省理工科技评论》主持的一场圆桌讨论探讨了细胞重编程逆转衰老的潜力，科学编辑 Mary Beth Griggs 等专家参与了讨论。 这场讨论凸显了长寿研究从延缓衰老到可能逆转衰老的范式转变，吸引了数十亿美元投资，并引发了人们对变革性抗衰老疗法的期待。 圆桌讨论涵盖了化学诱导重编程等实验性疗法，该疗法已被证明能在不丧失细胞身份的情况下，在一周内恢复细胞的年轻基因表达。

rss · MIT Technology Review · Jun 30, 17:36

**背景**: 细胞重编程涉及将细胞的表观遗传标记重置为更年轻的状态，通常使用山中因子或化学混合物。这种方法基于获得诺贝尔奖的诱导多能干细胞研究，目前正在动物和早期人体试验中测试其逆转衰老的效果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aging-us.com/article/204896/text">Chemically induced reprogramming to reverse cellular aging</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S1568163724000229">Epigenetic reprogramming as a key to reverse ageing and ...</a></li>
<li><a href="https://www.boldsmedia.com/latest-longevity-researches/">Latest Longevity Research 2026: Major Scientific ...</a></li>

</ul>
</details>

**标签**: `#longevity`, `#cellular reprogramming`, `#anti-aging`, `#biotechnology`

---

<a id="item-25"></a>
## [空气产品公司取消路易斯安那州蓝氢项目](https://www.energyintel.com/0000019f-1a08-de8d-a3bf-bb6ee2700000) ⭐️ 6.0/10

空气产品公司取消了其路易斯安那州清洁能源综合体（一个蓝氢项目），转而专注于沙特阿拉伯的 Neom 绿氢项目。 这一转变标志着从依赖天然气并采用碳捕获的蓝氢，转向完全由可再生能源生产的绿氢的战略调整，反映出行业对零碳解决方案的偏好日益增强。 路易斯安那项目是一个蓝氢设施，原本将使用天然气并配备碳捕获与封存技术；而 Neom 项目是与 ACWA Power 和 NEOM 的合资企业，计划到 2026 年利用可再生能源生产绿氢。

rss · Energy Intelligence · Jun 30, 21:14

**背景**: 蓝氢通过天然气生产并配合碳捕获与封存技术，而绿氢则利用可再生能源通过电解水制取，不排放碳。沙特阿拉伯的 Neom 绿氢项目是全球最大的公用事业规模绿氢设施，完全由可再生能源供电。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gevernova.com/gas-power/resources/articles/2024/green-vs-blue-hydrogen_whats-the-difference">Green vs blue hydrogen: What’s the difference? | GEvernova ...</a></li>
<li><a href="https://nghc.com/">NGHC - NEOM Green Hydrogen Company</a></li>
<li><a href="https://www.neom.com/en-us/newsroom/neom-green-hydrogen-investment">NEOM Green Hydrogen Company completes financial close at a ...</a></li>

</ul>
</details>

**标签**: `#hydrogen`, `#energy`, `#clean energy`, `#industry news`

---

<a id="item-26"></a>
## [Xbox 据报道考虑出售或关闭 Arkane 及其他工作室](https://www.gamedeveloper.com/business/report-xbox-considering-sales-or-closures-at-arkane-and-at-least-4-other-studios) ⭐️ 6.0/10

一份新报告称，微软正在考虑出售或关闭 Arkane Studios 及其他至少四个 Xbox 旗下工作室，作为更广泛“重置”的一部分，并可能取消正在开发的《漫威刀锋战士》游戏。 这将标志着微软游戏部门继 2024 年关闭 Arkane Austin 后又一次重大工作室关闭，可能对沉浸式模拟游戏类型及整个游戏开发行业产生重大影响。 以《羞辱》和《死亡循环》闻名的 Arkane Studios 目前正在开发第三人称动作冒险游戏《漫威刀锋战士》。报道称，即使工作室被出售，《刀锋战士》项目也可能被取消。

rss · Game Developer (Gamasutra) · Jun 30, 17:37

**背景**: 微软于 2021 年以 75 亿美元收购了 Bethesda Softworks 的母公司 ZeniMax Media，将 Arkane 等工作室纳入 Xbox 游戏工作室旗下。2024 年 5 月，微软关闭了 Arkane Austin 及其他几家工作室，理由是重组。位于法国的 Arkane Lyon 工作室继续运营，并正在开发《漫威刀锋战士》。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Arkane_Studios">Arkane Studios</a></li>
<li><a href="https://gamerant.com/xbox-arkane-shut-down-blade-cancelled/">Xbox is Reportedly Considering Shutting Down Arkane and ...</a></li>

</ul>
</details>

**标签**: `#gaming`, `#studio closure`, `#Microsoft`, `#Arkane`

---