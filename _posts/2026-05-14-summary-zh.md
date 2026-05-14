---
layout: default
title: "Horizon Summary: 2026-05-14 (ZH)"
date: 2026-05-14
lang: zh
---

> From 211 items, 29 important content pieces were selected

---

1. [首个公开的苹果 M5 内核漏洞利用](#item-1) ⭐️ 9.0/10
2. [Bun 从 Zig 重写为 Rust，大规模合并完成](#item-2) ⭐️ 9.0/10
3. [零日漏洞绕过 Windows 11 默认 BitLocker 保护](#item-3) ⭐️ 9.0/10
4. [从 2024 款 RAV4 混动版移除调制解调器和 GPS](#item-4) ⭐️ 8.0/10
5. [RTX 5090 外接显卡在 M4 MacBook Air 上运行：游戏与 AI 可行性](#item-5) ⭐️ 8.0/10
6. [GitHub 上披露新的 Nginx 漏洞利用](#item-6) ⭐️ 8.0/10
7. [硬盘固件黑客技术深度解析](#item-7) ⭐️ 8.0/10
8. [arXiv 对虚假参考文献实施一年封禁](#item-8) ⭐️ 8.0/10
9. [AI 让我变笨：开发者反思认知能力下降](#item-9) ⭐️ 8.0/10
10. [能源供应商优先服务数据中心，忽视太浩湖居民](#item-10) ⭐️ 8.0/10
11. [安大略审计发现 AI 记录仪捏造医疗信息](#item-11) ⭐️ 8.0/10
12. [厄尔尼诺将带来严重野火、洪水和热浪](#item-12) ⭐️ 8.0/10
13. [MIT 校长警告资金与人才管道危机](#item-13) ⭐️ 7.0/10
14. [OpenAI 将 Codex 集成到 ChatGPT 移动应用中](#item-14) ⭐️ 7.0/10
15. [微软取消内部 Claude Code 许可证](#item-15) ⭐️ 7.0/10
16. [Linux 开发者反对科罗拉多年龄验证法案](#item-16) ⭐️ 7.0/10
17. [企业应优先考虑 AI 数据主权](#item-17) ⭐️ 7.0/10
18. [女性遭遇深度伪造色情内容，揭露下架机制漏洞](#item-18) ⭐️ 7.0/10
19. [约克大学展览记录加拿大计算机爱好者运动](#item-19) ⭐️ 6.0/10
20. [AMD 将为旧款 GPU 带来 FSR 4.1 超分辨率技术](#item-20) ⭐️ 6.0/10
21. [数据准备是金融业代理式 AI 的关键](#item-21) ⭐️ 6.0/10
22. [特斯拉 Semi 进入全面量产，最终规格公布](#item-22) ⭐️ 6.0/10
23. [电网安全：低影响资产带来高风险](#item-23) ⭐️ 6.0/10
24. [北卡组织挑战监管机构叫停 2026 年太阳能项目令](#item-24) ⭐️ 6.0/10
25. [印第安纳社区在煤炭与数据中心间挣扎](#item-25) ⭐️ 6.0/10
26. [Fervo IPO 因数据中心能源需求飙升 30%](#item-26) ⭐️ 6.0/10
27. [移动游戏面临日益严重的收入测量问题](#item-27) ⭐️ 6.0/10
28. [美光推出面向 AI 服务器的 256GB 内存模块](#item-28) ⭐️ 6.0/10
29. [英伟达提议在变电站旁建迷你数据中心](#item-29) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [首个公开的苹果 M5 内核漏洞利用](https://blog.calif.io/p/first-public-kernel-memory-corruption) ⭐️ 9.0/10

安全公司 Calif 发布了首个公开的 macOS 内核内存损坏漏洞利用，该利用绕过了苹果 M5 芯片上新的 MIE（内存完整性强制）硬件保护，并附有一份 55 页的技术报告。 该漏洞利用表明，苹果 M5 的旗舰安全功能 MIE 可以被攻破，可能削弱对 macOS 和 iOS 设备基于硬件的内存安全性的信任。 该漏洞利用在五天内使用 Anthropic 的 Claude（Mythos Preview）开发完成，是首个公开证明 M5 上基于 MTE 的保护可以被绕过的实例。

hackernews · quadrige · May 14, 18:25 · [社区讨论](https://news.ycombinator.com/item?id=48139219)

**背景**: MIE（内存完整性强制）是苹果基于 ARM 的 MTE（内存标记扩展）构建的硬件辅助内存安全系统，作为 M5 和 A19 芯片的旗舰安全功能引入，旨在阻止内存损坏漏洞利用。内存损坏漏洞是获取操作系统内核级访问权限的常见攻击向量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.calif.io/p/first-public-kernel-memory-corruption">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://malware.news/t/first-public-macos-kernel-memory-corruption-exploit-on-apple-m5/107008">First public macOS kernel memory corruption exploit on Apple M5</a></li>
<li><a href="https://tech.yahoo.com/cybersecurity/articles/apple-mac-m5-system-exploited-211653412.html">Apple Mac M5 System Exploited With Anthropic's Claude Mythos ...</a></li>

</ul>
</details>

**社区讨论**: 评论者对漏洞能绕过 MTE 表示惊讶，一些人指出该漏洞在苹果漏洞赏金平台上的潜在价值（10 万到 150 万美元）。还有讽刺性的评论称苹果制造虚假漏洞来炒作，一位用户表示后悔专门为了 MIE 购买了 M5。

**标签**: `#security`, `#macOS`, `#kernel exploit`, `#Apple M5`, `#vulnerability`

---

<a id="item-2"></a>
## [Bun 从 Zig 重写为 Rust，大规模合并完成](https://github.com/oven-sh/bun/pull/30412) ⭐️ 9.0/10

流行的 JavaScript 运行时 Bun 已从 Zig 重写为 Rust，该拉取请求新增超过 100 万行 Rust 代码，并删除了 4,024 行 Zig 代码。 这次重写显著提高了内存安全性，减少了释放后使用和双重释放等 bug 类别，这些在 Rust 中会成为编译错误。它还引发了关于 LLM 时代软件复杂性和语言权衡的讨论。 合并包含 1,443 个 Rust 文件，共 929,213 行代码，代码库现在包含超过 10,000 个 unsafe 块，分布在 736 个文件中。重写耗时约一周，但大量准备工作包括将 Zig 惯用法详细映射到 Rust。

hackernews · Chaoses · May 14, 08:15 · [社区讨论](https://news.ycombinator.com/item?id=48132488)

**背景**: Bun 是一个快速的全能 JavaScript 运行时、打包器、测试运行器和包管理器，旨在作为 Node.js 的直接替代品。它最初使用 Zig，一种专注于简洁性和控制的底层系统编程语言。Rust 是另一种系统语言，以其所有权模型强制内存安全而闻名，无需垃圾回收。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oven-sh/bun">GitHub - oven-sh/bun: Incredibly fast JavaScript runtime, bundler, test runner, and package manager – all in one</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bun_(software)">Bun (software) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Zig_(programming_language)">Zig (programming language)</a></li>

</ul>
</details>

**社区讨论**: 社区意见不一：一些人称赞内存安全性的改进，并指出代码库已通过智能指针映射到 Rust 等价物做好了准备；而另一些人则对庞大的代码库规模（接近 Rust 编译器）和大量 unsafe 块表示担忧。有评论者指出，就在 9 天前合并还充满不确定性，颇具讽刺意味。

**标签**: `#Bun`, `#Rust`, `#Zig`, `#JavaScript runtime`, `#software engineering`

---

<a id="item-3"></a>
## [零日漏洞绕过 Windows 11 默认 BitLocker 保护](https://arstechnica.com/security/2026/05/zero-day-exploit-completely-defeats-default-windows-11-bitlocker-protections/) ⭐️ 9.0/10

一个名为 YellowKey 的零日漏洞允许拥有物理访问权限的攻击者绕过 Windows 11 上的默认 BitLocker 加密，并完全访问加密驱动器。微软正在调查此漏洞，该漏洞也影响 Windows Server 2022/2025。 该漏洞破坏了 Windows 11 的核心安全功能，可能使数百万设备上的敏感数据面临风险。它凸显了仅依赖默认加密而不附加 TPM 或 PIN 等保护措施的风险。 该漏洞利用 WinRE USB FsTx 文件绕过 BitLocker，并且需要物理访问目标机器。微软尚未发布补丁，漏洞细节有限。

rss · Ars Technica · May 14, 18:32

**背景**: BitLocker 是 Windows 内置的全盘加密功能，通过加密整个驱动器来保护数据。默认情况下，Windows 11 在兼容设备上启用 BitLocker 加密，但这种默认模式可能不需要 PIN 或 USB 密钥，从而使其在物理攻击面前可能较弱。YellowKey 漏洞专门针对这种默认配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/05/zero-day-exploit-completely-defeats-default-windows-11-bitlocker-protections/">Zero-day exploit completely defeats default Windows 11 ...</a></li>
<li><a href="https://cybersecuritynews.com/windows-bitlocker-0-day-vulnerability/">Windows BitLocker 0-Day Vulnerability Enables Access to ...</a></li>
<li><a href="https://thehackernews.com/2026/05/windows-zero-days-expose-bitlocker.html">Windows Zero-Days Expose BitLocker Bypasses And CTFMON ...</a></li>

</ul>
</details>

**标签**: `#security`, `#zero-day`, `#Windows 11`, `#BitLocker`, `#exploit`

---

<a id="item-4"></a>
## [从 2024 款 RAV4 混动版移除调制解调器和 GPS](https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/) ⭐️ 8.0/10

发布了一份详细指南，介绍如何从 2024 款 RAV4 混动版移除调制解调器和 GPS 以防止遥测数据收集，并包含关于蓝牙和 USB 连接的重要注意事项。 这很重要，因为现代车辆不断传输遥测数据，而本指南为注重隐私的车主提供了实用的 DIY 解决方案，同时指出蓝牙连接仍可能通过手机网络泄露数据。 移除过程涉及断开数据通信模块（DCM）和 GPS 天线；但如果通过蓝牙连接手机，车辆可能利用手机网络发送遥测数据。使用有线 USB 连接可避免此问题。

hackernews · arkadiyt · May 14, 17:08 · [社区讨论](https://news.ycombinator.com/item?id=48138136)

**背景**: 现代汽车配备远程信息处理单元，用于收集和传输驾驶行为、位置和车辆状态数据。丰田的 DCM（数据通信模块）负责此遥测功能。移除它可以防止数据收集，但可能影响紧急呼叫或免提麦克风等功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arkadiyt.com/2026/05/13/removing-the-modem-and-gps-from-my-rav4/">Removing the Modem and GPS from my 2024 RAV4 Hybrid</a></li>
<li><a href="https://www.rav4world.com/threads/2019-rav4-dcm-deactivate-procedure.304339/">2019 Rav4 DCM deactivate procedure - Toyota RAV4 Forums</a></li>
<li><a href="https://forum.ih8mud.com/threads/permanently-disable-telemetry-data-transmission-from-16-200s.1347480/">Permanently Disable Telemetry Data Transmission from 16+ 200s</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了与其他汽车品牌（斯巴鲁、福特）的类似经验，并指出即使移除调制解调器，通过蓝牙连接的手机仍可能传输遥测数据。有人担心 CarPlay/Android Auto 也会捕获数据，还有一位用户想修复 GPS 指南针问题而非出于隐私考虑。

**标签**: `#privacy`, `#automotive`, `#telemetry`, `#DIY`, `#security`

---

<a id="item-5"></a>
## [RTX 5090 外接显卡在 M4 MacBook Air 上运行：游戏与 AI 可行性](https://scottjg.com/posts/2026-05-05-egpu-mac-gaming/) ⭐️ 8.0/10

一篇技术文章展示了通过 Thunderbolt 5 将 NVIDIA RTX 5090 连接到 M4 MacBook Air，首次在 Apple Silicon 上实现了游戏和 LLM 推理。 这一突破挑战了苹果官方关于 Apple Silicon 不支持外接显卡的立场，可能为 Mac 用户在游戏和 AI 工作负载方面开辟新的用例。 该设置使用带有 GPU 直通的 Linux 虚拟机，通过 Thunderbolt 5 实现，在游戏中达到可玩的帧率，并在 LLM 提示处理速度上相比原生 Mac 性能有显著提升。

hackernews · allenleee · May 14, 15:47 · [社区讨论](https://news.ycombinator.com/item?id=48137145)

**背景**: Apple Silicon Mac 使用 CPU 和 GPU 共享的统一内存，限制了外接显卡支持。Thunderbolt 5 提供高达 80 Gbps 带宽，减少了外接显卡的性能损失。虚拟机中的 GPU 直通允许客户操作系统直接使用外接显卡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://egpu.io/forums/pc-setup/game-performance-on-tb5-thunderbolt-5jhl9480/">Game performance on TB5/Thunderbolt 5 (JHL9480) - egpu.io</a></li>
<li><a href="https://www.xda-developers.com/egpus-over-thunderbolt-sound-great-but-be-aware-limitations/">eGPUs over Thunderbolt sound great, but they come with ...</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这一技术成就，一些人指出 LLM 推理的改进比游戏更有影响力。其他人对苹果官方不支持外接显卡表示失望，并讨论了在 Apple Silicon 上实现虚拟机 GPU 直通的复杂性。

**标签**: `#eGPU`, `#Apple Silicon`, `#GPU passthrough`, `#LLM inference`, `#gaming`

---

<a id="item-6"></a>
## [GitHub 上披露新的 Nginx 漏洞利用](https://github.com/DepthFirstDisclosures/Nginx-Rift) ⭐️ 8.0/10

一个名为 Nginx-Rift 的新 Nginx 漏洞利用已在 GitHub 上披露，针对特定配置（包含 rewrite 和 set 指令），且披露声称可以可靠绕过 ASLR。 该漏洞利用意义重大，因为 Nginx 被广泛用作 Web 服务器和反向代理，而绕过 ASLR 的可能性增加了漏洞的严重性，影响众多生产环境。 该漏洞利用要求 rewrite 指令的替换字符串中包含问号，并且后续的 set 指令引用未命名的正则捕获组（例如 $1）。已发布的概念验证禁用了 ASLR，但文章声称可以可靠绕过。

hackernews · hetsaraiya · May 14, 17:17 · [社区讨论](https://news.ycombinator.com/item?id=48138268)

**背景**: Nginx 是一种流行的开源 Web 服务器，使用 rewrite 和 set 等指令进行 URL 操作。ASLR（地址空间布局随机化）是一种安全技术，通过随机化内存地址来增加利用难度。Nginx 中未命名的正则捕获组如果处理不当可能导致内存损坏。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalocean.com/community/tutorials/nginx-rewrite-url-rules">Nginx Rewrite URL Rules Examples | DigitalOcean</a></li>

</ul>
</details>

**社区讨论**: 社区评论对严重性存在争议：一些人认为绕过 ASLR 是可信的威胁，而另一些人指出已发布的 PoC 禁用了 ASLR。缓解建议包括使用命名捕获组代替未命名捕获组，正如 F5 所建议的。

**标签**: `#nginx`, `#security`, `#exploit`, `#vulnerability`, `#ASLR`

---

<a id="item-7"></a>
## [硬盘固件黑客技术深度解析](https://icode4.coffee/?p=1465) ⭐️ 8.0/10

一篇关于硬盘固件黑客技术的详细文章已发布，涵盖了技术、工具以及实际应用，如面试 CTF 挑战和数据恢复。 这篇文章为硬件安全中一个小众但关键的领域提供了宝贵见解，使研究人员和爱好者能够理解并可能防御固件级别的攻击。 文章引用了相关项目，如三星 840 EVO SSD 固件反编译和一系列关于修改/etc/shadow 的硬盘固件黑客文章，社区讨论还链接到了实际应用。

hackernews · jsploit · May 14, 16:19 · [社区讨论](https://news.ycombinator.com/item?id=48137553)

**背景**: 硬盘（HDD）包含控制其运行的固件，这些固件可以被逆向工程和修改。黑客攻击硬盘固件可以允许攻击者隐藏恶意软件、窃取数据或导致驱动器故障。常用的工具包括 HDDTools，技术来源如 spritesmods.com。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/grimdoomer/HDDTools">GitHub - grimdoomer/HDDTools: Tools to help analyze hard ...</a></li>
<li><a href="https://www.malwaretech.com/2015/04/hard-disk-firmware-hacking-part-1.html">Hard Disk Firmware Hacking (Part 1) - Marcus Hutchins</a></li>

</ul>
</details>

**社区讨论**: 社区评论强调了相关项目，如三星 SSD 固件反编译和一系列关于修改密码文件的硬盘固件黑客文章。一些用户讨论了实际应用，如面试 CTF 挑战和数据恢复，而另一些则指出了 NSA 式监控的潜在可能性。

**标签**: `#firmware`, `#hardware hacking`, `#security`, `#reverse engineering`, `#storage`

---

<a id="item-8"></a>
## [arXiv 对虚假参考文献实施一年封禁](https://twitter.com/tdietterich/status/2055000956144935055) ⭐️ 8.0/10

arXiv 宣布了一项新政策，对包含虚假参考文献的提交实施一年封禁，之后要求后续提交必须首先被信誉良好的同行评审场所接受。 这项政策直接解决了日益严重的 AI 生成虚假引用污染学术文献的问题，有助于维护学术交流的诚信。 该禁令适用于包含虚假参考文献的提交，禁令结束后，作者必须先在信誉良好的同行评审场所获得接受，才能重新提交到 arXiv。该政策可能尚未生效，因为 arXiv 的帮助页面上尚未明确列出。

hackernews · gjuggler · May 14, 20:39 · [社区讨论](https://news.ycombinator.com/item?id=48140922)

**背景**: 虚假参考文献是由 AI 模型生成的虚假引用，看似合理但实际并不对应真实出版物。《自然》杂志的一项分析发现，2025 年的数万篇出版物可能包含此类无效引用，凸显了学术文献的危机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://info.arxiv.org/help/submit/index.html">Submission Overview - arXiv info</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00969-z">Hallucinated citations are polluting the scientific ... - Nature</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13051339/">Hallucinated citations produced by generative artificial ...</a></li>

</ul>
</details>

**社区讨论**: 评论者大多支持该政策，称其“对科学非常有益”，并指出对易于检测的虚假引用施加后果是有益的。一些人提出了关于执行难度以及是否允许合法的 AI 生成结果（例如形式化证明的定理）的担忧。

**标签**: `#arXiv`, `#academic integrity`, `#AI-generated content`, `#publishing policy`

---

<a id="item-9"></a>
## [AI 让我变笨：开发者反思认知能力下降](https://jpain.io/god-damn-ai-is-making-me-dumb/) ⭐️ 8.0/10

一位开发者发表了一篇题为“AI 让我变笨”的个人文章，认为过度依赖 AI 编码工具（如 vibe coding）正在侵蚀批判性思维和深度学习能力。该文章在 Hacker News 上引发了激烈讨论，获得了 359 个点赞和 221 条评论。 这场辩论凸显了软件工程界对 AI 辅助认知代价日益增长的担忧。它挑战了 AI 总能提高生产力的说法，暗示不加节制地使用可能会损害学习和解决问题的能力，尤其是对初级开发者而言。 文章提到了由 Andrej Karpathy 推广的术语“vibe coding”，指不加审查地接受 AI 生成的代码。作者警告说，这种做法会导致认知卸载（cognitive offloading），即开发者将思考外包给 AI，从而失去独立理解或调试代码的能力。

hackernews · Eighth · May 14, 18:19 · [社区讨论](https://news.ycombinator.com/item?id=48139148)

**背景**: 认知卸载是一个心理学概念，指人们使用外部工具来减轻大脑负担，但过度依赖会削弱内在能力。在软件开发中，像大语言模型（LLM）这样的 AI 工具可以快速生成代码，但批评者认为这可能会阻碍深度学习和对代码的理解，尤其是对新手而言。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vibe_coding">Vibe coding</a></li>
<li><a href="https://medium.com/@naveenfy/the-cognitive-debt-of-offloading-software-development-to-ai-c012963542d5">The cognitive debt of offloading software development to AI | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论呈现分歧：一些开发者认同作者的担忧，指出 AI 使入职变得更困难，盲目信任会导致错误。另一些人则持相反观点，认为 AI 加速了在不熟悉领域（如硬件接口）的学习。一个反复出现的主题是经验水平很重要——初级开发者更容易受到认知卸载的影响。

**标签**: `#AI`, `#software engineering`, `#developer experience`, `#cognitive effects`, `#vibe coding`

---

<a id="item-10"></a>
## [能源供应商优先服务数据中心，忽视太浩湖居民](https://arstechnica.com/ai/2026/05/energy-supplier-abandons-lake-tahoe-residents-to-serve-data-centers/) ⭐️ 8.0/10

内华达州一家能源供应商决定优先为新建的数据中心供电，而非服务加州太浩湖地区的 49,000 名居民，实质上为了满足 AI 基础设施需求而抛弃了该社区。 这一事件凸显了 AI 基础设施扩张与社区需求之间日益尖锐的现实冲突，引发了关于能源政策、技术伦理以及 AI 能源足迹社会成本的紧迫问题。 根据沙漠研究所的分析，仅北内华达州的 12 个数据中心项目到 2033 年就可能带来 5900 兆瓦的新增需求。数据中心目前消耗全球约 1-2%的电力，其中 AI 约占 15%。

rss · Ars Technica · May 14, 19:17

**背景**: 数据中心需要大量电力来运行服务器和冷却系统，而 AI 工作负载尤其耗能。随着 AI 应用激增，公用事业公司面临艰难抉择：是服务不断增长的技术基础设施，还是维持对居民用户的供电。内华达州最大的公用事业公司已警告，由于数据中心的需求，可能无法实现 2030 年清洁能源目标。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://electrek.co/2026/05/13/data-centers-grid-strain-driving-residential-solar-battery-demand/">Data centers are cutting power to homes, driving homeowners ...</a></li>
<li><a href="https://apnews.com/article/ai-data-centers-nevada-clean-energy-47d1b6633ed720962848f4b5b91e7d6b">States are struggling to meet their clean energy goals. Data ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence">Environmental impact of artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#energy policy`, `#data centers`, `#tech ethics`, `#community impact`

---

<a id="item-11"></a>
## [安大略审计发现 AI 记录仪捏造医疗信息](https://arstechnica.com/health/2026/05/your-doctors-ai-notetaker-may-be-making-things-up-ontario-audit-finds/) ⭐️ 8.0/10

安大略省审计长的一项审计发现，省政府推荐的 AI 记录仪频繁生成错误、不完整和幻觉信息，包括捏造的治疗转诊和不正确的处方。 这凸显了医疗领域 AI 可靠性的关键问题，因为不准确可能导致误诊、不当治疗或患者伤害，并强调了在临床部署 AI 前需要进行严格测试和监管。 审计显示，准确性指标仅占供应商总分的约 4%，即使准确性得零分也容易通过，而“在安大略省的本地存在”指标却占 30%。

rss · Ars Technica · May 14, 17:28

**背景**: AI 幻觉是指 AI 系统生成不基于现实或训练数据的输出。在医疗领域，这种幻觉可能表现为错误的诊断或治疗。AI 记录仪用于自动生成医患对话的临床笔记，但其可靠性对患者安全至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/health/2026/05/your-doctors-ai-notetaker-may-be-making-things-up-ontario-audit-finds/">Your doctor’s AI notetaker may be making things up, Ontario audit finds - Ars Technica</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10552880/">A Call to Address AI “Hallucinations” and How Healthcare Professionals Can Mitigate Their Risks - PMC</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#healthcare`, `#hallucination`, `#audit`, `#reliability`

---

<a id="item-12"></a>
## [厄尔尼诺将带来严重野火、洪水和热浪](https://arstechnica.com/science/2026/05/forecasters-predict-wildfires-floods-severe-heatwaves-from-incoming-el-nino/) ⭐️ 8.0/10

预报员预测，即将到来的厄尔尼诺现象与人为全球变暖相结合，可能在全球范围内引发严重的野火、洪水和热浪。 这种复合气候事件威胁到数据中心和能源电网等关键基础设施，使得技术系统的韧性和灾害准备变得至关重要。 文章强调，海洋热量加上人为全球变暖构成了致命气候极端的严峻组合，但未提及具体日期或区域。

rss · Ars Technica · May 14, 13:09

**背景**: 厄尔尼诺是一种以太平洋变暖为特征的气候模式，会扰乱全球天气并常导致极端事件。人为全球变暖放大了这些影响，增加了灾害的强度和频率。

**标签**: `#climate change`, `#El Niño`, `#extreme weather`, `#disaster preparedness`, `#sustainability`

---

<a id="item-13"></a>
## [MIT 校长警告资金与人才管道危机](https://president.mit.edu/writing-speeches/video-transcript-message-president-kornbluth-about-funding-and-talent-pipeline) ⭐️ 7.0/10

MIT 校长 Sally Kornbluth 发布视频讲话，指出联邦研究资金减少及其对人才管道的影响，引发了关于学术界系统性问题的广泛讨论。 这一讲话凸显了美国研究型大学的关键时刻，资金削减可能驱走顶尖人才并削弱长期创新，影响从 AI 到半导体制造等领域。 视频文字记录指出，未获资助的学生更不可能接受录取，而理科博士平均需要六年才能毕业，薪酬微薄且就业前景不佳，导致许多毕业生离开学术界。

hackernews · dmayo · May 14, 14:51 · [社区讨论](https://news.ycombinator.com/item?id=48136262)

**背景**: 美国研究型大学严重依赖 NSF 和 NIH 等机构的联邦拨款。近年来，预算持平或减少造成了压力，同时学术就业市场收紧，终身教职岗位稀缺，导致博士生和博士后日益失望。

**社区讨论**: 评论者普遍对学术界感到失望，指出他们认识的近 80%的博士毕业生正在离开。一些人认为该系统即将迎来代际重置，而另一些人则指出，即使不留在学术界，博士学位仍为行业提供了宝贵技能。

**标签**: `#academia`, `#research funding`, `#talent pipeline`, `#higher education`, `#systemic issues`

---

<a id="item-14"></a>
## [OpenAI 将 Codex 集成到 ChatGPT 移动应用中](https://www.theverge.com/ai-artificial-intelligence/930763/openai-codex-chatgpt-ios-android-app-preview) ⭐️ 7.0/10

OpenAI 正在将其 Codex AI 编程代理集成到 ChatGPT 移动应用中，使用户能够通过手机编写代码并控制电脑上的应用程序。 此举使 OpenAI 能够在快速增长的 AI 编程工具市场中与 Anthropic 的 Claude Code 直接竞争，让高级编程辅助功能在移动设备上更易获取。 Codex 此前仅限桌面端使用；此次移动集成是在 Anthropic 的 Claude Code 人气激增之后进行的，促使 OpenAI 加快开发并削减副项目。

rss · The Verge · May 14, 20:00

**背景**: OpenAI Codex 是一套 AI 驱动的编程代理，可自动化从规划到部署的软件工程任务。它可以通过 CLI 本地运行，或集成到 VS Code 等 IDE 中。Anthropic 的 Claude Code 是一个竞争性的代理编程工具，可在终端或作为 VS Code 扩展使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://grokipedia.com/page/OpenAI_Codex">OpenAI Codex</a></li>
<li><a href="https://openai.com/codex/">Codex | AI Coding Partner from OpenAI</a></li>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#Codex`, `#ChatGPT`, `#AI coding`, `#mobile app`

---

<a id="item-15"></a>
## [微软取消内部 Claude Code 许可证](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad) ⭐️ 7.0/10

微软正在停止内部使用 Anthropic 的 Claude Code AI 编码工具，该工具自去年 12 月以来已被数千名员工用于鼓励编码实验。 此举标志着微软 AI 编码工具策略的转变，可能影响员工生产力以及第三方 AI 工具在大型企业中的更广泛采用。 该决定是内部做出的，消息人士称，Claude Code 在项目经理、设计师和其他非传统开发者中很受欢迎，用于首次编码实验。

rss · The Verge · May 14, 19:00

**背景**: Claude Code 是 Anthropic 开发的一款代理式 AI 编码工具，可在终端中运行，理解代码库、编辑文件并执行命令。它与 Claude 3.7 Sonnet 一起作为有限研究预览版发布。微软于去年 12 月向数千名员工开放了访问权限，作为跨角色推广编码实验的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/product/claude-code">Claude Code by Anthropic | AI Coding Agent, Terminal, IDE</a></li>
<li><a href="https://www.anthropic.com/news/claude-3-7-sonnet">Claude 3.7 Sonnet and Claude Code \ Anthropic</a></li>

</ul>
</details>

**标签**: `#Microsoft`, `#Claude Code`, `#AI coding tools`, `#enterprise software`

---

<a id="item-16"></a>
## [Linux 开发者反对科罗拉多年龄验证法案](https://www.theverge.com/tech/930573/age-verification-bills-linux-open-source) ⭐️ 7.0/10

Linux 开发者正在反对科罗拉多州的 SB26-051 法案，该法案要求操作系统收集用户年龄区间并与应用开发者共享，可能对开源项目造成损害。 如果该法案通过，可能为全美设备级年龄验证树立先例，给 Linux 等开源操作系统带来沉重的合规成本，并威胁用户隐私。 该法案针对 iOS 和 Android 等商业平台设计，但其宽泛的措辞可能适用于任何操作系统，包括 Linux 发行版。它要求提供年龄信号的 API，仅发送最少信息。

rss · The Verge · May 14, 18:58

**背景**: 美国各州年龄验证法律正在激增，旨在通过要求平台验证用户年龄来保护未成年人。设备级验证将负担转移到操作系统上，引发了开源社区的隐私和技术担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://leg.colorado.gov/bills/SB26-051">SB26-051 Age Attestation on Computing Devices | Colorado ...</a></li>
<li><a href="https://www.pcmag.com/news/colorado-lawmakers-push-for-age-verification-at-the-operating-system-level">Colorado Lawmakers Push for Age Verification at the ... - PCMag</a></li>
<li><a href="https://www.theverge.com/policy/913038/age-verification-flaws">Age verification is a mess but we’re doing it anyway | The Verge</a></li>

</ul>
</details>

**标签**: `#Linux`, `#age verification`, `#open source`, `#privacy`, `#legislation`

---

<a id="item-17"></a>
## [企业应优先考虑 AI 数据主权](https://www.technologyreview.com/2026/05/14/1137168/establishing-ai-and-data-sovereignty-in-the-age-of-autonomous-systems/) ⭐️ 7.0/10

这一转变至关重要，因为将专有数据输入第三方 AI 模型会使企业面临失去数据控制权的风险，可能导致合规违规和竞争劣势。 文章强调，企业常常默认达成“先能力，后控制”的协议，但数据会流经它们不拥有的系统，并受制于它们未设定的治理规则。

rss · MIT Technology Review · May 14, 13:00

**背景**: 数据主权意味着数据受其生成国家或地区的法律约束。AI 治理是指确保 AI 系统安全、合乎道德且合规的流程和标准。随着 AI 应用的普及，企业必须在能力与数据控制之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>
<li><a href="https://www.ibm.com/think/topics/data-sovereignty">What is data sovereignty? | IBM</a></li>
<li><a href="https://www.ibm.com/think/topics/ai-governance">What is AI governance? - IBM</a></li>

</ul>
</details>

**标签**: `#AI governance`, `#data sovereignty`, `#enterprise AI`, `#autonomous systems`

---

<a id="item-18"></a>
## [女性遭遇深度伪造色情内容，揭露下架机制漏洞](https://www.technologyreview.com/2026/05/14/1137161/ai-porn-nonconsensual-deepfakes-takedown-piracy-copyright/) ⭐️ 7.0/10

一位名叫 Jennifer 的女性发现，将她的职业头像通过面部识别程序扫描后，竟关联出她十多年前拍摄的色情视频，这凸显了深度伪造技术如何盗用真实成人内容。 这一案例凸显了非自愿深度伪造色情内容日益严峻的挑战，受害者因下架流程不完善和版权复杂性而难以删除内容，隐私和尊严受到侵害。 Jennifer 使用面部识别程序扫描她的新职业头像，以检查是否会检索到她过去的色情视频，结果确实如此。文章还提到，像 Takedown Piracy 这样的版权执法公司帮助成人内容创作者，但深度伪造使所有权问题复杂化。

rss · MIT Technology Review · May 14, 09:00

**背景**: 深度伪造是利用 AI 生成的媒体，将一个人的形象替换到现有内容中，常被用于制作非自愿色情内容。美国《TAKE IT DOWN 法案》旨在打击非自愿私密图像，但执行仍困难。受害者通常依赖版权声明要求下架，但这可能不涵盖深度伪造内容。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/14/1137161/ai-porn-nonconsensual-deepfakes-takedown-piracy-copyright/">The shock of seeing your body used in deepfake porn | MIT Technology Review</a></li>
<li><a href="https://en.wikipedia.org/wiki/TAKE_IT_DOWN_Act">TAKE IT DOWN Act - Wikipedia</a></li>
<li><a href="https://theconversation.com/how-the-take-it-down-act-tackles-nonconsensual-deepfake-porn-and-how-it-falls-short-255809">How the Take It Down Act tackles nonconsensual deepfake porn − and how it falls short</a></li>

</ul>
</details>

**标签**: `#deepfakes`, `#AI ethics`, `#privacy`, `#nonconsensual porn`, `#copyright`

---

<a id="item-19"></a>
## [约克大学展览记录加拿大计算机爱好者运动](https://museum.eecs.yorku.ca/exhibits/show/hobby_canada/hobby_canada) ⭐️ 6.0/10

约克大学计算机博物馆推出在线展览，详细介绍了 20 世纪 70 年代中期至 80 年代中期加拿大的计算机爱好者场景，重点展示了 TRACE 等俱乐部和 Jim Butterfield 等先驱。 该展览保存了计算史上重要但常被忽视的一章，展示了加拿大草根爱好者如何推动个人计算机革命。 展览聚焦于 1976 年成立的多伦多地区计算机爱好者协会（TRACE），涵盖当地俱乐部、杂志以及 Commodore 专家 Jim Butterfield 等关键人物。

hackernews · rbanffy · May 14, 12:57 · [社区讨论](https://news.ycombinator.com/item?id=48134743)

**背景**: 20 世纪 70 年代中期，很少有加拿大人拥有家用电脑。爱好者们用套件自己组装机器，并组成俱乐部分享知识。这场草根运动为 80 年代的个人计算机繁荣奠定了基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://museum.eecs.yorku.ca/exhibits/show/hobby_canada/hobby_canada">Computer Hobby Movement in Canada - York University</a></li>
<li><a href="https://en.wikipedia.org/wiki/Jim_Butterfield">Jim Butterfield - Wikipedia</a></li>
<li><a href="https://app.daily.dev/posts/computer-hobby-movement-in-canada-computer-hobby-movement-in-canada-york-university-computer-mus-phclaw9kh">Computer Hobby Movement in Canada · Computer Hobby...</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了怀旧回忆，有人指出遗漏了加拿大杂志《Electron》。另一位提到了 Jim Butterfield 为 VIC-20 编写的 TINYMON 监控程序。还有人感叹偏远地区难以接触爱好者文化。

**标签**: `#history`, `#retrocomputing`, `#Canada`, `#hobbyist`

---

<a id="item-20"></a>
## [AMD 将为旧款 GPU 带来 FSR 4.1 超分辨率技术](https://arstechnica.com/gadgets/2026/05/amd-promises-to-bring-improved-hardware-backed-fsr-4-upscaling-to-older-radeon-gpus/) ⭐️ 6.0/10

AMD 宣布计划将基于硬件的 FSR 4.1 超分辨率技术引入旧款 RDNA2（RX 6000 系列）和 RDNA3（RX 7000 系列）GPU，其中 RDNA3 支持将于 2026 年 7 月到来，RDNA2 支持预计在 2027 年初。 此次更新通过 AI 驱动的超分辨率技术提升了旧款 AMD GPU 的图像质量和性能，延长了其使用寿命，使其在与新硬件的竞争中更具优势，并让暂时无法升级的玩家受益。 与 RDNA4 上的原生支持相比，FSR 4.1 在旧款 GPU 上可能会带来更大的性能损失，因为这些旧架构缺乏专用的 AI 加速器。此次推出是在成功的模组和索尼的实现之后，促使 AMD 提供官方支持。

rss · Ars Technica · May 14, 18:55

**背景**: FSR（FidelityFX Super Resolution）是 AMD 的超分辨率技术，通过以较低分辨率渲染游戏再放大来提升性能。FSR 4.1 使用基于 AI 的超分辨率，需要专用硬件才能实现最佳效率。RDNA2 和 RDNA3 是较旧的 GPU 架构，缺少 RDNA4 中的 AI 加速器。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/gadgets/2026/05/amd-promises-to-bring-improved-hardware-backed-fsr-4-upscaling-to-older-radeon-gpus/">Over a year later, AMD is bringing improved FSR 4 upscaling ...</a></li>
<li><a href="https://www.techspot.com/news/112412-fsr-4-upscaling-finally-coming-older-radeon-gpus.html">FSR 4 upscaling is finally coming to older Radeon GPUs, and ...</a></li>
<li><a href="https://www.xda-developers.com/amd-fsr-41-ai-upscaling-finally-coming-to-older-radeon-rx-gpus/">AMD's FSR 4.1 AI upscaling is finally coming to older Radeon ...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#FSR`, `#upscaling`, `#GPU`, `#gaming`

---

<a id="item-21"></a>
## [数据准备是金融业代理式 AI 的关键](https://www.technologyreview.com/2026/05/14/1137034/data-readiness-for-agentic-ai-in-financial-services/) ⭐️ 6.0/10

MIT Technology Review 的一篇新文章指出，代理式 AI 在金融服务领域的成功更多取决于数据准备和监管合规，而非系统复杂性。 这一见解意义重大，因为金融公司受到严格监管并处理敏感数据，关注数据质量和治理可以在避免合规风险的同时释放 AI 的潜力。 文章强调，有效的搜索平台对于解决碎片化、索引不良的数据至关重要，并且必须安全管理结构化和非结构化数据。

rss · MIT Technology Review · May 14, 13:00

**背景**: 代理式 AI 指半自主或全自主的 AI 系统，能够在有限监督下感知、推理并采取行动以实现目标。在金融服务中，这些系统必须在严格监管下运行并处理实时数据，因此数据准备成为基础要求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/05/14/1137034/data-readiness-for-agentic-ai-in-financial-services/">Data readiness for agentic AI in financial services | MIT Technology Review</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>
<li><a href="https://www.ibm.com/think/topics/agentic-ai">What is Agentic AI? | IBM</a></li>

</ul>
</details>

**标签**: `#agentic AI`, `#financial services`, `#data readiness`, `#regulation`

---

<a id="item-22"></a>
## [特斯拉 Semi 进入全面量产，最终规格公布](https://www.technologyreview.com/2026/05/14/1137197/tesla-semi-electric-trucking/) ⭐️ 6.0/10

特斯拉已开始全面量产 Tesla Semi，并在近十年的开发后公布了最终电池规格和官方定价。 这标志着电动卡车运输的一个重要里程碑，因为 Tesla Semi 提供了比竞争对手大得多的电池容量和续航里程，可能加速零排放货运的转型。 Tesla Semi 的 500 英里续航版本配备 822 kWh 电池组，另有 548 kWh 版本可选，并支持 1.2 MW 快充。生产线年产能为 5 万辆卡车。

rss · MIT Technology Review · May 14, 10:00

**背景**: Tesla Semi 是一款电池电动 Class 8 半挂卡车，于 2017 年首次发布。它采用三电机，声称能耗低于每英里 2 kWh。竞争对手如 Freightliner eCascadia 和 Volvo VNR Electric 的电池容量更小、续航更短。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://electrek.co/2026/05/08/tesla-semi-battery-size-822-kwh-548-kwh-carb-official/">Tesla Semi battery sizes confirmed: 822 kWh and 548 kWh... | Electrek</a></li>
<li><a href="https://electrek.co/2026/04/29/tesla-semi-first-truck-high-volume-production-line/">Tesla Semi : first truck rolls off high-volume production line | Electrek</a></li>
<li><a href="https://en.wikipedia.org/wiki/Tesla_Semi">Tesla Semi - Wikipedia</a></li>

</ul>
</details>

**标签**: `#electric vehicles`, `#Tesla`, `#trucking`, `#transportation`

---

<a id="item-23"></a>
## [电网安全：低影响资产带来高风险](https://www.utilitydive.com/news/when-low-impact-doesnt-mean-low-risk-cyber-nerc/819730/) ⭐️ 6.0/10

Black & Veatch 的 Anirban Ghosh 发表文章指出，电网当前的安全重点集中在主要设施上，忽视了众多小型低影响资源同时失效带来的日益增长的风险。 这很重要，因为随着分布式能源资源的普及，对众多小型资产的协同攻击可能导致级联停电，挑战现有优先保护高影响设施的 NERC CIP 框架。 文章指出，NERC CIP 标准按影响级别对资产进行分类，但低影响资产不受同样严格的网络安全要求约束，从而造成了潜在的盲点。

rss · Utility Dive · May 14, 14:55

**背景**: 关键基础设施保护（CIP）是保护电网等基本系统的框架。NERC CIP 标准对高影响和中影响的大容量电力系统资产强制要求网络安全措施，但低影响资产的要求较少。电网越来越依赖分布式能源资源，这些资源通常被归类为低影响。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/U.S._critical_infrastructure_protection">U.S. critical infrastructure protection - Wikipedia</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/critical-infrastructure-protection">Critical Infrastructure Protection (CIP): Defined And Explained</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#critical infrastructure`, `#power grid`, `#risk management`

---

<a id="item-24"></a>
## [北卡组织挑战监管机构叫停 2026 年太阳能项目令](https://www.canarymedia.com/articles/solar/north-carolina-groups-fight-regulator-order) ⭐️ 6.0/10

北卡罗来纳州的清洁能源组织已提交动议，要求推翻监管机构突然叫停杜克能源 2026 年太阳能电站投资的命令。 该命令威胁到作为美国太阳能市场关键州的太阳能发展，可能推迟杜克能源的碳中和目标，并损害当地太阳能产业。 该命令由北卡罗来纳州公用事业委员会主席发布，批评者认为其武断且可能超越权限。动议要求委员会全体重新审议。

rss · Latitude Media (Canary Media) · May 14, 07:30

**背景**: 杜克能源是美国东南部的主要公用事业公司，其计划到 2050 年实现碳中和，太阳能是关键组成部分。北卡罗来纳州公用事业委员会负责监管公用事业投资，其主席的意外命令打乱了 2026 年太阳能采购流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wral.com/business/duke-energy-solar-delay-april-2026/">Regulators hit pause on Duke solar expansion in North Carolina</a></li>
<li><a href="https://carolinapublicpress.org/75590/shunning-the-sunshine-nc-order-for-duke-energy-to-hit-brakes-on-solar-raises-policy-legal-questions/">Solar energy procurement freeze from NC affects Duke Energy</a></li>
<li><a href="https://www.bpr.org/2026-05-06/clean-energy-groups-push-back-on-north-carolina-regulators-solar-energy-pause">Clean energy groups push back on North Carolina regulators ...</a></li>

</ul>
</details>

**标签**: `#solar energy`, `#regulation`, `#clean energy`, `#policy`

---

<a id="item-25"></a>
## [印第安纳社区在煤炭与数据中心间挣扎](https://www.canarymedia.com/articles/fossil-fuels/this-indiana-community-is-caught-between-coal-and-the-data-center-boom) ⭐️ 6.0/10

印第安纳州贾斯珀县的一个社区面临冲突，因为一座燃煤电厂的退役计划与新建数据中心的能源需求相冲突。文章突出了当地环保目标与蓬勃发展的数据中心行业之间的紧张关系。 这个故事说明了数据中心繁荣对当地社区的现实影响，特别是那些依赖煤炭就业和收入的社区。它凸显了在可再生能源转型与人工智能和云计算带来的电力需求激增之间取得平衡的挑战。 文章以教师工会组织者 Barb Deardorff 为主角，她喜欢从家中欣赏玉米地和鹤群的景色。冲突源于数据中心需要大量电力，可能推迟燃煤电厂的退役。

rss · Latitude Media (Canary Media) · May 14, 07:30

**背景**: 数据中心是容纳计算机服务器的设施，需要大量电力来运行和冷却。美国能源部预计，到 2028 年，数据中心的电力需求可能翻倍或增至三倍，这主要受人工智能和云服务的推动。燃煤电厂退役是减少碳排放的关键部分，但对可靠电力的需求可能使老旧电厂运行更长时间。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.energy.gov/articles/doe-releases-new-report-evaluating-increase-electricity-demand-data-centers">DOE Releases New Report Evaluating... | Department of Energy</a></li>
<li><a href="https://www.industrialinfo.com/iirenergy/industry-news/article/us-coal-fired-power-plant-retirements-slowed-in-2025-future-is-uncertain--357093">U.S. Coal -Fired Power Plant Retirements Slowed in 2025, Future is...</a></li>

</ul>
</details>

**标签**: `#energy`, `#data centers`, `#coal`, `#environment`

---

<a id="item-26"></a>
## [Fervo IPO 因数据中心能源需求飙升 30%](https://www.energyintel.com/0000019e-276e-dc13-adfe-37fe999c0000) ⭐️ 6.0/10

Fervo Energy 的股票在 IPO 首日飙升超过 30%，反映出市场对增强型地热技术的强烈信心。 此次 IPO 成功凸显了投资者对清洁、基荷可再生能源的兴趣日益增长，这类能源可以满足数据中心（尤其是 AI 和云计算）激增的电力需求。 Fervo Energy 利用增强型地热系统（EGS）发电，其首个商业试点项目 Project Red 于 2023 年成功产生了 3 兆瓦的基荷电力。

rss · Energy Intelligence · May 14, 19:50

**背景**: 增强型地热系统（EGS）通过向热岩注入流体以制造裂缝，从而在缺乏天然水或渗透性的地热资源中发电。该技术可提供全天候无碳基荷电力，补充太阳能和风能等间歇性可再生能源。Fervo Energy 成立于 2017 年，是下一代地热开发的领导者。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Enhanced_geothermal_system">Enhanced geothermal system - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Fervo_Energy">Fervo Energy</a></li>
<li><a href="https://www.energy.gov/hgeo/geothermal/enhanced-geothermal-systems">Enhanced Geothermal Systems | Department of Energy</a></li>

</ul>
</details>

**标签**: `#geothermal`, `#IPO`, `#clean energy`, `#data centers`

---

<a id="item-27"></a>
## [移动游戏面临日益严重的收入测量问题](https://www.gamesindustry.biz/mobile-gaming-has-a-new-and-growing-measurement-problem-opinion) ⭐️ 6.0/10

Google Play 最近将其商店费用降至 20%（如果开发者集成 Google 的 AI 助手、云存档和成就系统，则降至 15%），但这一变化暴露了一个更深层次的问题：由于许多交易现在通过绕过商店的网页支付选项进行，行业已无法准确衡量移动游戏收入。 这一测量缺口削弱了行业收入图表和市场分析的可靠性，可能误导开发者、投资者和分析师对移动游戏市场真实状况的判断。 文章指出，游戏内商店现在提供两种购买路径：平台购买（通过 Google Play）和网页支付选项，这是一种有意设计的体验，旨在将支出引导至平台之外。这些网页交易均不会出现在商店图表中，因此收入下降可能仅仅是测量缺口所致。

rss · GamesIndustry.biz · May 14, 15:41

**背景**: 历史上，移动游戏收入主要通过应用商店数据（Google Play 和 Apple App Store）来衡量，这些数据捕获了通过商店计费系统处理的应用内购买。然而，近期的监管和竞争压力导致 Google 允许替代计费系统和网页支付选项，从而分散了收入流，使得追踪变得更加困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gamesindustry.biz/mobile-gaming-has-a-new-and-growing-measurement-problem-opinion">Mobile gaming has a new, and growing, measurement problem | Opinion | GamesIndustry.biz</a></li>
<li><a href="https://www.techspot.com/news/111572-google-cuts-play-store-fee-20-opens-door.html">Google cuts Play Store fee to 20% and opens the ... - TechSpot</a></li>
<li><a href="https://support.google.com/googleplay/android-developer/answer/16954621?hl=en">Understanding Google Play's lower service fees</a></li>

</ul>
</details>

**标签**: `#mobile gaming`, `#revenue measurement`, `#Google Play`, `#industry analysis`

---

<a id="item-28"></a>
## [美光推出面向 AI 服务器的 256GB 内存模块](https://www.pcgamer.com/hardware/memory/while-i-can-barely-find-two-sticks-of-16-gb-to-rub-together-micron-unveils-a-256-gb-memory-module-destined-for-ai-servers/) ⭐️ 6.0/10

美光宣布推出一款 256 GB DDR5 RDIMM 内存模块，速度可达 9,200 MT/s，面向下一代 AI 和 HPC 服务器。 与两个 128 GB 模块相比，这款高容量模块功耗降低超过 40%，在内存带宽和容量至关重要的 AI 数据中心中实现更高效率。 该模块采用先进封装技术和 3D 堆叠，在单个 RDIMM 外形中实现 256 GB 容量，美光已开始向服务器生态系统合作伙伴提供样品。

rss · PC Gamer · May 14, 16:22

**背景**: DDR5 RDIMM 是专为服务器设计的内存模块，提供比消费级 DIMM 更高的容量和带宽。AI 工作负载需要大容量内存和高传输速率来处理海量数据集和模型参数。美光的新模块通过将当前高端模块的容量翻倍，同时保持与现有 DDR5 平台的兼容性，满足了这些需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/memory/while-i-can-barely-find-two-sticks-of-16-gb-to-rub-together-micron-unveils-a-256-gb-memory-module-destined-for-ai-servers/">While I can barely find two sticks of 16 GB to rub together, Micron unveils a 256 GB memory module destined for AI servers | PC Gamer</a></li>
<li><a href="https://cloudnews.tech/micron-raises-ddr5-server-memory-with-256-gb-modules/">Micron Raises DDR5 Server Memory with 256 GB Modules | Cloud News</a></li>
<li><a href="https://www.embedded.com/micron-samples-256-gb-ddr5-rdimm-for-ai-servers">Micron Samples 256-GB DDR5 RDIMM for AI Servers - Embedded</a></li>

</ul>
</details>

**标签**: `#hardware`, `#memory`, `#AI`, `#servers`

---

<a id="item-29"></a>
## [英伟达提议在变电站旁建迷你数据中心](https://www.pcgamer.com/hardware/graphics-cards/nvidias-solution-to-the-ai-energy-problem-is-mini-data-centers-next-to-local-power-substations-and-of-course-selling-even-more-gpus/) ⭐️ 6.0/10

英伟达提议在本地变电站附近建设迷你数据中心，以应对 AI 日益增长的能源需求，同时继续销售更多 GPU。 这种方法可能缓解电网压力并加速 AI 基础设施部署，但也引发了关于能源公平和社区影响的问题。 这些迷你数据中心将通过智能面板利用未使用的电力容量，可能形成相当于传统数据中心的分布式网络。

rss · PC Gamer · May 14, 14:21

**背景**: AI 工作负载需要巨大的计算能力，导致数据中心能源消耗激增。传统数据中心常受限于电网容量和漫长的建设周期。靠近变电站的迷你数据中心可以通过更高效地利用本地电力来绕过这些瓶颈。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcmag.com/news/fancy-a-data-center-in-your-backyard-start-up-wants-distributed-data-centers">This Startup Wants to Put a Mini Data Center in Your Backyard | PCMag</a></li>
<li><a href="https://www.inc.com/moses-jeanfrancois/nvidia-mini-ai-data-center-house/91340588">Nvidia's New Partnership Wants to Put Mini AI Data Centers on Your House</a></li>
<li><a href="https://www.reddit.com/r/accelerate/comments/1t5drxr/nvidia_just_figured_out_how_to_put_an_ai_data/">r/accelerate on Reddit: "Nvidia just figured out how to put an AI data center on the side of your house. And pay you to host it. Each XFRA node packs 16 Blackwell RTX Pro 6000 GPUs, 4 AMD EPYC CPUs, and 3TB of RAM in a Dell PowerEdge rack mounted next to the AC condenser. The homeowner pays nothing for"</a></li>

</ul>
</details>

**社区讨论**: Reddit 用户对安全和分区问题表示怀疑，指出将昂贵的 GPU 资产放置在住宅区可能导致盗窃或监管障碍。

**标签**: `#AI`, `#energy`, `#Nvidia`, `#data centers`

---