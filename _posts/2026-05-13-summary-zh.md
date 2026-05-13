---
layout: default
title: "Horizon Summary: 2026-05-13 (ZH)"
date: 2026-05-13
lang: zh
---

> From 178 items, 30 important content pieces were selected

---

1. [CERT 发布六个严重的 dnsmasq 漏洞 CVE](#item-1) ⭐️ 9.0/10
2. [Elevator：无需启发式方法的确定性静态二进制翻译](#item-2) ⭐️ 8.0/10
3. [分支恢复 Bambu Lab 打印机的完整 BambuNetwork 支持](#item-3) ⭐️ 8.0/10
4. [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](#item-4) ⭐️ 8.0/10
5. [DuckDB 发布 Quack：面向扩展的客户端-服务器协议](#item-5) ⭐️ 8.0/10
6. [Scrcpy v4.0 新增动态虚拟显示调整功能](#item-6) ⭐️ 8.0/10
7. [Obsidian 推出新插件社区网站与自动化审核系统](#item-7) ⭐️ 8.0/10
8. [SpaceX 发布配备 Raptor 3 升级的 Starship V3](#item-8) ⭐️ 8.0/10
9. [双胞胎兄弟被解雇后删除 96 个政府数据库](#item-9) ⭐️ 8.0/10
10. [青少年因 ChatGPT 药物建议死亡，诉讼指控](#item-10) ⭐️ 8.0/10
11. [资深开发者为何难以传达专业知识](#item-11) ⭐️ 7.0/10
12. [利用大气散射渲染逼真的天空和行星](#item-12) ⭐️ 7.0/10
13. [请愿书敦促《纽约时报》《大西洋月刊》《今日美国》解除对 Wayback Machine 的屏蔽](#item-13) ⭐️ 7.0/10
14. [亚马逊员工为展示 AI 使用而进行“Tokenmaxxing”](#item-14) ⭐️ 7.0/10
15. [MIT 将世界模型列为 AI 关键趋势](#item-15) ⭐️ 7.0/10
16. [视频编解码器困扰游戏开发者，尚无解决方案](#item-16) ⭐️ 7.0/10
17. [铁拳制作人原田胜弘在 SNK 旗下成立 VS Studio](#item-17) ⭐️ 7.0/10
18. [虚假面试传播密码窃取木马](#item-18) ⭐️ 7.0/10
19. [谷歌 DeepMind 用 AI 重新构想鼠标指针](#item-19) ⭐️ 6.0/10
20. [Android Auto 获得通用屏幕适配和 AI 功能](#item-20) ⭐️ 6.0/10
21. [谷歌预告 Googlebook 笔记本系列，将取代 Chromebook](#item-21) ⭐️ 6.0/10
22. [家庭微型数据中心提案加速 AI 计算](#item-22) ⭐️ 6.0/10
23. [安卓将在 2026 年迎来重大 AI 改造](#item-23) ⭐️ 6.0/10
24. [诺贝尔经济学奖得主的 AI 观点与维护创新](#item-24) ⭐️ 6.0/10
25. [Constellation Energy 在 PJM 队列中新增 5 GW 容量，数据中心不确定性犹存](#item-25) ⭐️ 6.0/10
26. [亚马逊签署新型屋顶热泵协议](#item-26) ⭐️ 6.0/10
27. [EIA 因中东战争调整石油展望](#item-27) ⭐️ 6.0/10
28. [世嘉因 Rovio 亏损降低服务型游戏优先级](#item-28) ⭐️ 6.0/10
29. [微软以色列总经理因 Azure 道德指控离职](#item-29) ⭐️ 6.0/10
30. [内存危机中涌现逼真假 DDR5 模块](#item-30) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [CERT 发布六个严重的 dnsmasq 漏洞 CVE](https://lists.thekelleys.org.uk/pipermail/dnsmasq-discuss/2026q2/018471.html) ⭐️ 9.0/10

CERT 发布了六个针对广泛使用的 DNS/DHCP 服务器 dnsmasq 的严重安全漏洞 CVE。这些漏洞是通过 AI 辅助安全审计发现的，引发了关于内存安全的讨论。 这些漏洞影响无数设备，包括家用路由器和物联网设备，构成严重的安全隐患。讨论凸显了从 C 等内存不安全语言迁移到 Rust 等内存安全语言的紧迫性。 这六个 CVE 涵盖了各种内存安全问题，如缓冲区溢出和悬空指针。漏洞存在于用 C 编写且资源需求低的 dnsmasq 中。

hackernews · chizhik-pyzhik · May 12, 18:12 · [社区讨论](https://news.ycombinator.com/item?id=48112042)

**背景**: dnsmasq 是一个轻量级 DNS 转发器和 DHCP 服务器，常用于小型网络、家用路由器和物联网设备。内存安全指防止缓冲区溢出等 bug；C 和 C++是内存不安全的，而 Rust 和 Java 是内存安全的。CVE（通用漏洞与暴露）为公开已知的安全漏洞提供标准化参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dnsmasq">Dnsmasq</a></li>
<li><a href="https://en.wikipedia.org/wiki/Memory_safety">Memory safety</a></li>
<li><a href="https://en.wikipedia.org/wiki/Common_Vulnerabilities_and_Exposures">Common Vulnerabilities and Exposures - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了 AI 在安全审计中的作用以及内存安全语言的必要性。有人指出 AI 能发现缓冲区溢出，但可能无法发现协议级缺陷如 Kaminsky 攻击。还有人批评 Debian 使用过时的 dnsmasq 版本，并询问 OpenWRT 的响应。

**标签**: `#security`, `#dnsmasq`, `#CVE`, `#memory safety`, `#open source`

---

<a id="item-2"></a>
## [Elevator：无需启发式方法的确定性静态二进制翻译](https://arxiv.org/abs/2605.08419) ⭐️ 8.0/10

研究人员推出了 Elevator，这是首个完全静态的二进制翻译器，通过预先计算每个字节的所有可行解释，无需启发式方法、调试信息或源代码，即可确定性地将整个 x86-64 可执行文件翻译为 AArch64。 这种方法使得在监管行业（如航空、医疗设备）中能够进行认证，这些行业无法接受基于 JIT 的翻译，因为输出二进制必须可签名且确定。其性能也达到或优于 QEMU 用户态 JIT 模拟。 Elevator 生成自包含的二进制文件，可信代码库中无运行时组件，但由于枚举所有可行翻译，.text 段可能增大至 50 倍。目前尚不支持多线程和异常处理。

hackernews · matt_d · May 13, 04:25 · [社区讨论](https://news.ycombinator.com/item?id=48117810)

**背景**: 二进制翻译将可执行代码从一种指令集架构（ISA）转换为另一种。传统静态二进制翻译依赖启发式方法来区分代码和数据，这可能引入非确定性。JIT（动态）翻译是确定性的，但引入了运行时组件，在安全关键系统中难以认证。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.08419">[2605.08419] Deterministic Fully-Static Whole-Binary Translation without Heuristics</a></li>
<li><a href="https://en.wikipedia.org/wiki/Static_binary_translation">Static binary translation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Binary_translation">Binary translation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者强调认证角度是一个重大突破，尽管有人担心 50 倍的代码膨胀会导致缓存性能问题。其他人则认为这种权衡对于确定性翻译是可以接受的，并赞扬了未来支持多线程和异常处理的潜力。

**标签**: `#binary translation`, `#static analysis`, `#certification`, `#systems research`, `#determinism`

---

<a id="item-3"></a>
## [分支恢复 Bambu Lab 打印机的完整 BambuNetwork 支持](https://github.com/FULU-Foundation/OrcaSlicer-bambulab) ⭐️ 8.0/10

一个名为 OrcaSlicer-bambulab 的 OrcaSlicer GitHub 分支已被创建，旨在恢复 Bambu Lab 打印机的完整 BambuNetwork 支持，允许无需云认证限制的互联网打印。 该分支直接对抗 Bambu Lab 有争议的固件更新——该更新要求本地网络打印也需云认证，回应了社区的强烈反对，并维护了用户对其设备的控制权。 该分支基于 Bambu Lab 更改之前的 OrcaSlicer 仓库状态，通过 BambuNetwork 实现完整的互联网访问和打印功能，而不仅限于局域网模式。

hackernews · Murfalo · May 12, 21:55 · [社区讨论](https://news.ycombinator.com/item?id=48115127)

**背景**: Bambu Lab 是一家以封闭生态系统著称的 3D 打印机制造商。2025 年初，该公司宣布了一项固件更新，要求即使本地网络打印也需云认证，引发了 3D 打印社区的广泛批评。OrcaSlicer 是一款用于准备 3D 打印的开源切片软件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/unS0uL/OrcaSlicer-bambulab">GitHub - unS0uL/OrcaSlicer-bambulab: OrcaSlicer with restored BambuNetwork support for Bambu Lab printers, with full internet access and printing just like before. · GitHub</a></li>
<li><a href="https://github.com/dafik/OrcaSlicer-bambulab">GitHub - dafik/OrcaSlicer-bambulab: OrcaSlicer with restored BambuNetwork support for Bambu Lab printers, with full internet access and printing just like before. · GitHub</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bambu_Lab">Bambu Lab - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区普遍支持该分支，用户表达了对 Bambu Lab 云认证要求的不信任。一些人将 Bambu 的做法与 Ubiquiti 等提供更用户可控远程访问的供应商进行不利比较。其他人因争议而重新考虑购买 Bambu 打印机。

**标签**: `#3D printing`, `#open source`, `#firmware`, `#privacy`, `#community backlash`

---

<a id="item-4"></a>
## [Needle：从 Gemini 蒸馏出的 2600 万参数工具调用模型](https://github.com/cactus-compute/needle) ⭐️ 8.0/10

Cactus 开源了 Needle，一个从 Gemini 蒸馏出的 2600 万参数函数调用模型，仅使用注意力层，没有前馈网络。在消费级设备上达到 6000 tok/s 预填充和 1200 tok/s 解码速度。 Needle 挑战了大型模型对于智能体任务必要的假设，表明一个极小的模型在单次工具调用中可以超越大得多的模型。这使得在手机、手表和眼镜上运行设备端 AI 智能体成为可能。 该模型在 16 个 TPU v6e 上预训练了 200B token，耗时 27 小时，然后在 2B token 的合成函数调用数据上后训练了 45 分钟。在单次函数调用基准测试中，它击败了 FunctionGemma-270M、Qwen-0.6B、Granite-350M 和 LFM2.5-350M。

hackernews · HenryNdubuaku · May 12, 18:03 · [社区讨论](https://news.ycombinator.com/item?id=48111896)

**背景**: 工具调用（或函数调用）允许 LLM 与外部 API 和工具交互，实现智能体行为。模型蒸馏将知识从大型“教师”模型转移到小型“学生”模型。传统 Transformer 同时使用注意力和前馈网络（FFN），但 Needle 认为对于工具调用这类基于检索的任务，FFN 参数是浪费的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@yasir_siddique/tool-calling-for-llms-a-detailed-tutorial-a2b4d78633e2">Tool Calling for LLMs: A Detailed Tutorial | by Yasir Siddique | Medium</a></li>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Transformer_(deep_learning_architecture)">Transformer (deep learning architecture)</a></li>

</ul>
</details>

**社区讨论**: 评论者对模型在复杂工具使用中的判别能力表示兴趣，并担心 Google 可能对蒸馏行为进行反击。一些人提出了实际应用，如自然语言命令行解析，其他人则请求提供在线演示。

**标签**: `#tool calling`, `#model distillation`, `#edge AI`, `#open source`, `#NLP`

---

<a id="item-5"></a>
## [DuckDB 发布 Quack：面向扩展的客户端-服务器协议](https://duckdb.org/2026/05/12/quack-remote-protocol) ⭐️ 8.0/10

DuckDB 宣布了 Quack，一种新的客户端-服务器协议，支持远程连接和并发写入，允许多个 DuckDB 实例相互通信并实现水平扩展。 Quack 解决了 DuckDB 的关键限制——其嵌入式单进程特性——通过支持并发访问和水平扩展，为可观测性数据或内部应用等场景开辟了新的用例。 Quack 是一种基于成熟技术构建的远程过程调用（RPC）协议，设计上易于设置。它允许多个并发写入者，但写入在服务器端是串行化的。

hackernews · aduffy · May 12, 17:54 · [社区讨论](https://news.ycombinator.com/item?id=48111765)

**背景**: DuckDB 是一种嵌入式、进程内的 OLAP 数据库，传统上缺乏客户端-服务器模型，这意味着它在宿主进程内运行，无法处理并发远程连接。Quack 通过引入一个独立的服务器进程改变了这一点，DuckDB 客户端可以通过 quack: 协议连接到该服务器，从而实现水平扩展和并发写入。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol">Quack: The DuckDB Client-Server Protocol – DuckDB</a></li>
<li><a href="https://duckdb.org/quack/">Quack Remote Protocol – DuckDB</a></li>
<li><a href="https://en.wikipedia.org/wiki/DuckDB">DuckDB - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 社区对 Quack 感到兴奋，用户指出它解决了实际问题，如传感器数据管道的并发访问和内部应用的水平扩展。一些评论者质疑“并发写入者”的定义，怀疑写入在服务器端是串行化的，而另一些人则对 DuckDB 不断演变的定位表示不确定。

**标签**: `#DuckDB`, `#database`, `#client-server protocol`, `#scalability`, `#open source`

---

<a id="item-6"></a>
## [Scrcpy v4.0 新增动态虚拟显示调整功能](https://github.com/Genymobile/scrcpy/releases/tag/v4.0) ⭐️ 8.0/10

Scrcpy v4.0 引入了灵活的虚拟显示功能，可随客户端窗口动态调整大小，无需重启显示即可更改分辨率或宽高比。 此更新显著提升了屏幕镜像和远程控制的用户体验，使 scrcpy 更适合桌面式使用，并与 Samsung DeX 等解决方案竞争。 该功能通过 --flex-display（或 -x）标志启用。它解决了长期以来的动态分辨率缩放功能请求，此前只能通过重新创建虚拟显示来实现。

hackernews · xnx · May 12, 20:50 · [社区讨论](https://news.ycombinator.com/item?id=48114356)

**背景**: Scrcpy 是一款免费开源工具，可通过 USB 或 TCP/IP 从桌面计算机镜像并控制 Android 设备。它被开发者和爱好者广泛用于调试、演示和远程协助。在 v4.0 之前，更改虚拟显示分辨率需要重启显示，这对动态工作流来说很不方便。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Scrcpy">scrcpy - Wikipedia</a></li>
<li><a href="https://github.com/Genymobile/scrcpy/issues/5651">Dynamic resolution scaling of virtual displays. · Issue #5651 · Genymobile/scrcpy</a></li>

</ul>
</details>

**社区讨论**: 社区参与度很高，用户分享了创造性的用例，例如将手机用作 WiFi 桥接器。一些用户报告了三星设备上的手势导航问题，而另一些用户则称赞该工具对非技术用户的无缝操作。

**标签**: `#scrcpy`, `#android`, `#screen-mirroring`, `#open-source`, `#tools`

---

<a id="item-7"></a>
## [Obsidian 推出新插件社区网站与自动化审核系统](https://obsidian.md/blog/future-of-plugins/) ⭐️ 8.0/10

Obsidian 宣布推出新的社区网站和自动化审核系统，以应对插件提交量的激增，取代了此前成为瓶颈的手动审核流程。 这一变化缓解了开发者的挫败感和团队倦怠，加快了插件审批速度，并可持续地扩展生态系统。它也表明 Obsidian 致力于维护开放的插件平台，同时解决安全问题。 新系统包括代码质量和安全性的自动化检查，但未引入权限系统或沙箱机制；插件仍然可以完全访问文件系统和网络。社区网站提供了开发者仪表板，并通过 GitHub 简化了提交流程。

hackernews · xz18r · May 12, 15:45 · [社区讨论](https://news.ycombinator.com/item?id=48109970)

**背景**: Obsidian 是一款流行的笔记应用，支持社区开发的插件。随着用户群的增长，插件提交量压垮了小型团队的手动审核流程，导致长时间延迟和开发者不满。新的自动化系统旨在扩大审核能力，同时不牺牲安全性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://obsidian.md/blog/future-of-plugins/">The future of Obsidian plugins - Obsidian</a></li>
<li><a href="https://docs.obsidian.md/Plugins/Getting+started/Build+a+plugin">Build a plugin - Developer Documentation</a></li>
<li><a href="https://forum.obsidian.md/t/recurrent-why-does-it-take-so-long-to-review-plugins-whats-the-usual-time-it-takes-to-review-a-new-plugin-how-long-does-it-take-to-review-a-plugin/107899/42">Recurrent: Why does it take so long to review plugins? What's the usual time it takes to review a new plugin? How long does it take to review a plugin? - #42 by DRRO - Developers: Plugin & API - Obsidian Forum</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：CEO kepano 对发布表示兴奋并邀请反馈，用户 dtkav 称赞缓解了瓶颈。但 varun_ch 和 troad 批评缺乏权限系统或沙箱机制，认为仅靠自动化检查无法防止恶意插件。

**标签**: `#Obsidian`, `#plugins`, `#developer tools`, `#automation`, `#security`

---

<a id="item-8"></a>
## [SpaceX 发布配备 Raptor 3 升级的 Starship V3](https://www.spacex.com/updates#starship-v3) ⭐️ 8.0/10

SpaceX 宣布了 Starship V3，这是 Starship 系列的首次重大升级，采用了集成传感器和辅助系统的 Raptor 3 发动机，并简化了生产流程。 此次升级显著提升了推力和生产效率，推进了 SpaceX 快速复用和火星殖民的目标，同时引发了关于将 AI 整合到太空操作的讨论。 Raptor 3 发动机是首批生产型迭代发动机，内部集成了大量传感器和辅助系统，超重型助推器成功完成了 33 台发动机的静态点火测试。

hackernews · fprog · May 13, 01:29 · [社区讨论](https://news.ycombinator.com/item?id=48116781)

**背景**: Starship 是 SpaceX 设计的完全可重复使用超重型运载火箭，用于月球、火星及其他任务。Raptor 发动机采用全流量分级燃烧循环，提高了效率和可靠性。V3 升级吸收了此前试飞的经验教训。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Raptor">SpaceX Raptor - Wikipedia</a></li>
<li><a href="https://www.indiatoday.in/science/story/spacex-starship-super-heavy-v3-static-fire-33-raptor-engines-test-2908557-2026-05-08">SpaceX Starship Super Heavy fires 33 Raptor engines ... - India Today</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：有人称赞 Raptor 3 的工程简洁性，也有人批评 Elon Musk 关于太空 AI 的愿景不切实际，并担心 SpaceX 被 Grok 等 AI 项目‘污染’。

**标签**: `#SpaceX`, `#Starship`, `#Raptor engine`, `#space technology`, `#engineering`

---

<a id="item-9"></a>
## [双胞胎兄弟被解雇后删除 96 个政府数据库](https://arstechnica.com/tech-policy/2026/05/drop-database-what-not-to-do-after-losing-an-it-job/) ⭐️ 8.0/10

双胞胎兄弟在被解雇后，因离职前未撤销其凭证，删除了 96 个政府数据库。 此事件凸显了在解雇员工前撤销访问凭证的关键重要性，尤其是对于拥有数据库访问权限的 IT 岗位。它强烈提醒组织必须严格执行离职流程，以防止数据丢失和安全漏洞。 兄弟俩在被解雇后不久就能访问并删除数据库，表明他们的系统访问权限仍然有效。删除 96 个数据库的规模表明他们拥有广泛的权限，很可能是数据库管理员。

rss · Ars Technica · May 12, 19:12

**背景**: 在许多组织中，IT 员工拥有管理关键系统的高级权限。当员工被解雇时，标准安全实践要求立即撤销所有访问凭证。未能做到这一点可能导致恶意或意外的数据破坏，正如本案例所示。

**标签**: `#security`, `#access management`, `#IT policy`, `#data breach`

---

<a id="item-10"></a>
## [青少年因 ChatGPT 药物建议死亡，诉讼指控](https://arstechnica.com/tech-policy/2026/05/will-i-be-ok-teen-died-after-chatgpt-pushed-deadly-mix-of-drugs-lawsuit-says/) ⭐️ 8.0/10

一项诉讼指控一名青少年在遵循 ChatGPT 关于混合药物的建议后死亡，聊天记录显示该青少年信任 AI 帮助他安全地尝试药物。 此案凸显了 AI 聊天机器人提供未经审核的医疗建议的现实危险，引发了对 AI 安全护栏和法律责任的紧迫讨论。 这些互动发生在已不可用的早期版本 ChatGPT 上，OpenAI 表示 ChatGPT 不能替代医疗护理。

rss · Ars Technica · May 12, 19:00

**背景**: 像 ChatGPT 这样的 AI 聊天机器人基于互联网数据训练的大型语言模型生成回复，但它们缺乏真正的理解能力，可能产生有害建议。这一事件凸显了在健康等敏感领域需要强有力的安全措施。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2lMZ2NDSEVSRTNHdk5pX3RodkRDZ0FQAQ?hl=en-GH&gl=GH&ceid=GH:en">OpenAI sued for wrongful death after ChatGPT drug advice - Overview</a></li>
<li><a href="https://www.cnet.com/tech/services-and-software/openai-chatgpt-drug-advice-lawsuit-teen-death/">Lawsuit Claims ChatGPT Gave Drug -Taking Advice That Led... - CNET</a></li>

</ul>
</details>

**标签**: `#AI safety`, `#ethics`, `#ChatGPT`, `#legal`, `#health`

---

<a id="item-11"></a>
## [资深开发者为何难以传达专业知识](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise) ⭐️ 7.0/10

Nair.sh 上的一篇文章探讨了资深开发者为何难以表达自己的专业知识，将其归因于内化知识和沟通差距。 这一点很重要，因为专业知识沟通不畅会导致知识孤岛、团队效率降低，并错失软件工程团队中的指导机会。 文章指出，资深开发者通常依赖难以用语言表达的内部“世界模型”，沟通失败并非因为缺乏知识，而是因为隐性知识转移的困难。

hackernews · nilirl · May 12, 15:08 · [社区讨论](https://news.ycombinator.com/item?id=48109460)

**背景**: 在软件工程中，专业知识常常变得隐性——即深度内化且难以解释的知识。这种现象被称为“专业知识悖论”，即专家尽管有深刻理解，却可能难以教导他人。

**社区讨论**: 评论者就原因展开辩论：有人认为资深开发者的内部世界模型使沟通变得困难，而另一些人则指出初级开发者通常对指导兴趣不大。少数人指出，对资深开发者一概而论并无帮助，因为具体情况差异很大。

**标签**: `#software engineering`, `#communication`, `#senior developers`, `#expertise`

---

<a id="item-12"></a>
## [利用大气散射渲染逼真的天空和行星](https://blog.maximeheckel.com/posts/on-rendering-the-sky-sunsets-and-planets/) ⭐️ 7.0/10

Maxime Heckel 发布了一篇详细的博客文章，包含交互式演示和代码，解释了如何使用大气散射技术渲染逼真的天空、日落和行星。 这项工作使高级计算机图形技术对 Web 开发者和爱好者更加可及，从而在浏览器和游戏中实现更沉浸的视觉体验。 文章涵盖了瑞利散射和米氏散射、天空穹顶渲染以及行星大气模拟，并提供了交互式 WebGL 演示和源代码。

hackernews · ibobev · May 12, 13:26 · [社区讨论](https://news.ycombinator.com/item?id=48107997)

**背景**: 大气散射是导致天空呈现蓝色、日落变红的物理过程。在计算机图形学中，它通过瑞利散射（针对小颗粒）和米氏散射（针对较大颗粒）等数学模型进行模拟。实时渲染这些效果需要高效的着色器实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/gpugems/gpugems2/part-ii-shading-lighting-and-shadows/chapter-16-accurate-atmospheric-scattering">Chapter 16. Accurate Atmospheric Scattering | NVIDIA Developer</a></li>
<li><a href="https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@10.5/manual/Atmospheric-Scattering.html">Atmospheric Scattering | High Definition RP | 10.5.1</a></li>
<li><a href="https://www.cg.tuwien.ac.at/research/publications/2019/kerbl_2019_planet_poster/">Real-time Rendering of Procedural Planets at Arbitrary Altitudes | TU Wien – Research Unit of Computer Graphics</a></li>

</ul>
</details>

**社区讨论**: 评论者称赞了这篇文章，有人提到了 Sebastian Lague 关于大气层的视频以及 Nishita 等人 1993 年的经典论文。一位评论者指出一个物理上的不准确之处：演示中的天空在日落后立即变黑，而真实的暮光会持续到太阳位于地平线以下 18 度。

**标签**: `#computer graphics`, `#atmospheric rendering`, `#web development`, `#shaders`, `#visual effects`

---

<a id="item-13"></a>
## [请愿书敦促《纽约时报》《大西洋月刊》《今日美国》解除对 Wayback Machine 的屏蔽](https://www.savethearchive.com/newsleaders/) ⭐️ 7.0/10

一份发布在 savethearchive.com 上的请愿书呼吁《纽约时报》《大西洋月刊》和《今日美国》停止阻止互联网档案馆的 Wayback Machine 抓取和存档其内容。 这凸显了出版商对其内容的控制权与公众保存数字历史的利益之间日益紧张的矛盾，可能为新闻机构如何与网络档案馆互动树立先例。 请愿书专门针对阻止 Wayback Machine 存档这些网站的 robots.txt 屏蔽，争论焦点在于遵守 robots.txt 在道德上是否正确，还是过于严格。

hackernews · doener · May 12, 23:11 · [社区讨论](https://news.ycombinator.com/item?id=48115807)

**背景**: Wayback Machine 由互联网档案馆运营，用于存档网页以供历史参考。它遵守 robots.txt 标准，网站所有者通过该标准指示爬虫可以访问网站的哪些部分。一些出版商屏蔽 Wayback Machine 以控制其内容，而档案管理员则认为这会抹去数字历史。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Robots.txt">robots.txt - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Wayback_Machine">Wayback Machine - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Internet_Archive">Internet Archive - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者就 robots.txt 的道德问题展开辩论，一些人认为遵守它是正确的做法，但会导致不公平的限制。其他人建议采用延迟发布或托管服务等替代方案，而少数人批评请愿书来自非付费读者。

**标签**: `#internet archiving`, `#digital preservation`, `#robots.txt`, `#Wayback Machine`, `#web history`

---

<a id="item-14"></a>
## [亚马逊员工为展示 AI 使用而进行“Tokenmaxxing”](https://arstechnica.com/ai/2026/05/amazon-employees-are-tokenmaxxing-due-to-pressure-to-use-ai-tools/) ⭐️ 7.0/10

亚马逊员工正在使用名为 MeshClaw 的内部 AI 工具来自动化非必要任务，这种做法被称为“tokenmaxxing”，其驱动力来自内部排行榜上展示 AI 使用情况的压力。 这突显了一种不正当的激励，员工为了游戏 AI 使用指标而非专注于真正的生产力，可能削弱工作场所采用 AI 的预期收益。 MeshClaw 允许员工创建 AI 代理，这些代理可以触发代码部署、分类电子邮件并与 Slack 等工具交互。术语“tokenmaxxing”借用了 Z 世代俚语，意为最大化 token 使用量作为生产力基准。

rss · Ars Technica · May 12, 13:33

**背景**: Tokenmaxxing 指的是最大化 AI 服务中 token 消耗以夸大感知生产力的做法。亚马逊的内部 AI 工具 MeshClaw 是 Amazon Q 套件的一部分，旨在协助软件开发和业务任务。内部排行榜根据 AI 使用情况对员工进行排名，创造了激励 tokenmaxxing 的竞争环境。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Token_maxxing">Token maxxing - Wikipedia</a></li>
<li><a href="https://letsdatascience.com/news/amazon-employees-inflate-ai-usage-with-meshclaw-56f85677">Amazon employees inflate AI usage with MeshClaw | Let's Data Science</a></li>
<li><a href="https://the-decoder.com/tokenmaxxing-spreads-at-amazon-as-employees-game-internal-ai-leaderboards/">"Tokenmaxxing" spreads at Amazon as employees game internal AI leaderboards</a></li>

</ul>
</details>

**社区讨论**: 文章和相关讨论的评论表达了担忧，认为 tokenmaxxing 反映了科技工作场所中更广泛的指标游戏问题。一些人认为这表明缺乏有意义的 AI 整合，而另一些人则认为这是对设计不当的激励措施的自然反应。

**标签**: `#AI`, `#workplace`, `#Amazon`, `#productivity`, `#automation`

---

<a id="item-15"></a>
## [MIT 将世界模型列为 AI 关键趋势](https://www.technologyreview.com/2026/05/12/1137134/world-models-10-things-that-matter-in-ai-right-now/) ⭐️ 7.0/10

MIT Technology Review 将世界模型列入其 2026 年“当前 AI 最重要的 10 件事”榜单，并举办了一场仅限订阅者参与的圆桌讨论，主题为“AI 能否学会理解世界？”。 世界模型代表了从模式匹配 AI 向能够模拟物理和因果关系的系统的转变，这有望赋能更强大的机器人、自动驾驶汽车和交互式视频生成。 文章由执行编辑 Niall Firth 进行讲解，圆桌讨论仅限订阅者参与，表明内容经过精心策划且具有深度。

rss · MIT Technology Review · May 12, 16:22

**背景**: 世界模型是学习环境内部表示并预测其随时间变化的神经网络。它们不同于仅进行分类或生成输出的传统 AI，而是模拟物理和物体交互等动态。早期概念可追溯到 1990 年代，但现代版本正因机器人、自动驾驶和视频生成等领域的需求而受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/World_model_(artificial_intelligence)">World model (artificial intelligence)</a></li>
<li><a href="https://www.nature.com/articles/d41586-026-00820-5">‘World models’ are AI’s latest sensation: what are they and what can they do?</a></li>
<li><a href="https://www.nvidia.com/en-us/glossary/world-models/">What Are World Models and How Are They Built?</a></li>

</ul>
</details>

**标签**: `#AI`, `#world models`, `#MIT Technology Review`, `#emerging technology`

---

<a id="item-16"></a>
## [视频编解码器困扰游戏开发者，尚无解决方案](https://www.gamedeveloper.com/programming/video-codecs-are-a-nightmare-for-game-developers-but-there-s-no-solution-in-sight) ⭐️ 7.0/10

最近一篇文章指出，游戏开发者被迫使用极端变通方法来集成视频编解码器，例如过场动画在 PC 上正常但在 Steam Deck 上无法播放，原因是缺乏通用解决方案。 这个问题阻碍了游戏开发效率和跨平台兼容性，影响开发者和玩家，导致不同设备上视频播放不一致。 编解码器支持在不同平台上差异很大；例如，H.264 是通用的，但 VP9 和 AV1 不是，而 Bink Video 等工具存在但并不总是适用。开发者通常依赖平台特定的编解码器，导致不可预测的行为。

rss · Game Developer (Gamasutra) · May 12, 16:09

**背景**: 视频编解码器压缩视觉媒体以减少文件大小，但压缩通常有损，且编解码器兼容性因硬件和软件而异。游戏开发者需要确保视频在多个平台上播放，但没有一种编解码器能通用，迫使他们实现复杂的回退系统或使用 Bink 等中间件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gamedeveloper.com/programming/video-codecs-are-a-nightmare-for-game-developers-but-there-s-no-solution-in-sight">Why video codecs are a nightmare for game developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/Bink_Video">Bink Video - Wikipedia</a></li>
<li><a href="https://www.mux.com/articles/best-practices-for-video-playback-a-complete-guide-2025">Best Practices for Video Playback: A Complete Guide (2025) | Mux</a></li>

</ul>
</details>

**标签**: `#game development`, `#video codecs`, `#technical debt`, `#software engineering`

---

<a id="item-17"></a>
## [铁拳制作人原田胜弘在 SNK 旗下成立 VS Studio](https://www.4gamer.net/games/999/G999901/20260511002/) ⭐️ 7.0/10

《铁拳》系列传奇制作人原田胜弘在 SNK 旗下成立了一家名为 VS Studio 的新游戏开发工作室，SNK 计划将其纳入合并子公司。 此举将最具影响力的格斗游戏创作者之一纳入 SNK 旗下，有望重振该工作室的格斗游戏阵容，并加剧该品类的竞争。 VS Studio 将与 SNK 合作进行游戏软件开发以增强能力，同时作为独立工作室运营。原田将担任该工作室的代表。

rss · 4Gamer.net · May 12, 15:00

**背景**: 原田胜弘是万代南梦宫《铁拳》格斗游戏系列的长期制作人和代言人。SNK 是一家经典的格斗游戏公司，以《拳皇》和《侍魂》等系列闻名。此次合作将原田的专业知识与 SNK 的经典 IP 相结合。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.snk-corp.co.jp/us/press/2026/announcement-of-new-studio-establishment-katsuhiro-harada-appointed-as-representative/">Announcement of New Studio Establishment Katsuhiro Harada Appointed as Representative｜PRESS RELEASE｜SNK Corporation</a></li>

</ul>
</details>

**标签**: `#fighting games`, `#SNK`, `#Harada`, `#studio announcement`, `#gaming industry`

---

<a id="item-18"></a>
## [虚假面试传播密码窃取木马](https://www.pcgamer.com/software/security/a-jobstealer-trojan-virus-has-popped-up-that-attacks-pcs-via-fake-job-interviews/) ⭐️ 7.0/10

黑客通过虚假面试诱骗求职者在电脑上下载密码窃取木马。 这种新型社会工程攻击针对求职者这一弱势群体，可能导致大规模凭证窃取和财务损失。 该恶意软件是一种密码窃取木马，能够从受感染系统中提取存储的凭证、用户名和密码。

rss · PC Gamer · May 12, 10:31

**背景**: 密码窃取木马是一种恶意软件，旨在从受害者计算机中窃取登录凭证等敏感信息。它们通常通过钓鱼邮件或恶意下载传播，但利用虚假面试是一种新的欺骗手段。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.malwarebytes.com/blog/detections/trojan-passwordstealer">Malwarebytes Threat Alert | Trojan.PasswordStealer</a></li>
<li><a href="https://encyclopedia.kaspersky.com/glossary/psw-trojans-password-stealing-trojans/">PSW Trojans (Password-stealing Trojans) | Kaspersky IT Encyclopedia</a></li>

</ul>
</details>

**标签**: `#cybersecurity`, `#social engineering`, `#malware`, `#job scams`, `#password theft`

---

<a id="item-19"></a>
## [谷歌 DeepMind 用 AI 重新构想鼠标指针](https://deepmind.google/blog/ai-pointer/) ⭐️ 6.0/10

谷歌 DeepMind 发布了 AI 增强鼠标指针的实验性演示，该指针结合语音指令和指向操作，利用 Gemini AI 执行上下文相关操作，如编辑文本或与网页元素交互。 这一概念可能从根本上改变用户与计算机的交互方式，减少对传统菜单和键盘快捷键的依赖，但也引发了关于日常使用中实用性和隐私问题的讨论。 该指针利用 Gemini 理解用户指向的内容，并允许语音指令如“把这个改成 2”来修改内容。然而，系统需要互联网连接进行 AI 处理，这可能限制离线使用。

hackernews · devhouse · May 12, 17:40 · [社区讨论](https://news.ycombinator.com/item?id=48111581)

**背景**: 传统鼠标指针仅跟踪光标位置并通过点击触发操作。谷歌 DeepMind 的 AI 指针旨在增加上下文感知能力，使指针理解光标下的元素，并通过语音或手势对其操作，超越简单的指向点击。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/ai-pointer/">Shaping the future of AI interaction by reimagining the mouse pointer — Google DeepMind</a></li>
<li><a href="https://officechai.com/ai/google-deepmind-says-its-reimagining-the-mouse-pointer-by-integrating-it-with-ai/">Google DeepMind Says It's Reimagining The Mouse Pointer By Integrating It With AI</a></li>
<li><a href="https://www.therift.ai/news-feed/google-deepmind-reimagines-mouse-pointer-with-ai-powered-context-understanding">Google DeepMind Reimagines Mouse Pointer with AI-Powered Context Understanding</a></li>

</ul>
</details>

**社区讨论**: 社区评论普遍持怀疑态度，用户质疑语音控制在共享空间中的实用性，并指出许多任务可以通过现有工作流（如右键菜单）更快完成。一些人认为这个概念有趣，但觉得对于日常任务来说过于复杂。

**标签**: `#AI`, `#HCI`, `#voice control`, `#mouse pointer`, `#Google DeepMind`

---

<a id="item-20"></a>
## [Android Auto 获得通用屏幕适配和 AI 功能](https://www.theverge.com/tech/927759/android-auto-is-now-one-screen-size-fits-all) ⭐️ 6.0/10

在 Google I/O 上，Google 宣布了 Android Auto 的更新，包括针对非标准显示屏的自适应屏幕尺寸、YouTube 视频流、小部件支持以及 Gemini AI 功能的集成。 这些更新使 Android Auto 在不同车型和屏幕形状上更加通用，同时增加了娱乐和 AI 功能，提升了车载体验。 屏幕尺寸更新允许 Android Auto 自动适应非常规屏幕比例，解决了长期以来的抱怨。YouTube 流媒体仅在汽车停放时可用，而 Gemini AI 可以在搭载 Google 原生系统的车辆上回答特定于汽车的问题。

rss · The Verge · May 12, 17:00

**背景**: Android Auto 是 Google 的车载信息娱乐系统，将手机应用镜像到仪表盘显示屏上。此前，它在非标准屏幕尺寸上表现不佳，经常出现黑条或元素错位。Google I/O 是该公司每年一度的开发者大会，会上会发布新功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/tech/927759/android-auto-is-now-one-screen-size-fits-all">Android Auto is now one (screen) size fits all | The Verge</a></li>

</ul>
</details>

**标签**: `#Android Auto`, `#Google I/O`, `#AI`, `#infotainment`

---

<a id="item-21"></a>
## [谷歌预告 Googlebook 笔记本系列，将取代 Chromebook](https://www.theverge.com/tech/928479/google-googlebook-laptops-android-tease-aluminium-chromebook) ⭐️ 6.0/10

谷歌在 Android Show 上预告了名为 Googlebook 的新笔记本系列，更多细节预计秋季公布。Googlebook 被定位为 Chromebook 的继任者，主打 AI 功能。 这标志着谷歌笔记本战略的重大转变，从 ChromeOS 转向以 AI 为中心的新平台。通过深度融合 Android 和 AI 功能，可能重塑笔记本市场，影响消费者和竞争对手。 目前细节很少；预告是更广泛的 Android 公告的一部分。Googlebook 被描述为“明天的 AI 笔记本”，但除了“秋季”外，没有提供规格或具体发布日期。

rss · The Verge · May 12, 17:00

**背景**: Chromebook 是谷歌十多年来推出的笔记本产品，运行 ChromeOS。Googlebook 似乎是品牌重塑或进化，可能更深度集成 Android 应用和 AI 功能，甚至可能脱离 ChromeOS。

**标签**: `#Google`, `#laptops`, `#Android`, `#hardware`

---

<a id="item-22"></a>
## [家庭微型数据中心提案加速 AI 计算](https://arstechnica.com/ai/2026/05/the-newest-ai-boom-pitch-host-a-mini-data-center-at-your-home/) ⭐️ 6.0/10

一项提案建议在住宅中放置微型数据中心，以加速 AI 计算部署，并向居民提供补偿。 这可能减少新建大型数据中心的需求，利用分布式边缘计算降低延迟并利用现有电力容量。 这些微型数据中心将使用智能面板吸收当地电网的未用电力容量，一个由这些节点组成的网络可以相当于一个中小型传统数据中心。

rss · Ars Technica · May 12, 21:59

**背景**: 边缘计算将计算靠近数据源，减少延迟。分布式 AI 计算将任务拆分到多台机器上，实现可扩展处理。微型数据中心是传统数据中心的缩小版，常用于边缘计算。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.inc.com/moses-jeanfrancois/nvidia-mini-ai-data-center-house/91340588">Nvidia's New Partnership Wants to Put Mini AI Data Centers on Your House</a></li>
<li><a href="https://www.vertiv.com/en-us/about/news-and-events/articles/educational-articles/what-is-a-micro-data-center/">What Is a Micro Data Center?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Edge_computing">Edge computing</a></li>

</ul>
</details>

**标签**: `#AI`, `#data centers`, `#edge computing`, `#distributed systems`

---

<a id="item-23"></a>
## [安卓将在 2026 年迎来重大 AI 改造](https://arstechnica.com/gadgets/2026/05/google-says-android-is-getting-a-big-ai-overhaul-in-2026/) ⭐️ 6.0/10

谷歌宣布计划在 2026 年对安卓进行重大 AI 改造，旨在将人工智能深度集成到操作系统中。 这可能改变用户与设备的交互方式，使安卓更加主动和个性化，并为移动 AI 集成树立新标准。 该公告缺乏具体的技术细节或功能，但暗示了 AI 在安卓生态系统中的广泛、系统级集成。

rss · Ars Technica · May 12, 17:00

**背景**: 安卓是全球最流行的移动操作系统，AI 已越来越多地集成到应用和服务中。系统级的 AI 改造可以实现更智能的助手、预测性操作和情境感知功能。

**标签**: `#Android`, `#AI`, `#Google`, `#mobile`

---

<a id="item-24"></a>
## [诺贝尔经济学奖得主的 AI 观点与维护创新](https://www.technologyreview.com/2026/05/12/1137103/the-download-nobel-winner-ai-maintenance-of-everything/) ⭐️ 6.0/10

《麻省理工科技评论》的新闻通讯介绍了诺贝尔经济学奖得主达龙·阿西莫格鲁关于三个值得关注的 AI 趋势的观点，同时呼吁优先考虑以维护为核心的创新，而非不断追求新奇。 阿西莫格鲁的观点因其诺贝尔奖地位及对 AI 宏观经济影响的 influential 研究而具有分量，为炒作驱动的叙事提供了反平衡。维护论点挑战了科技行业对颠覆的痴迷，倡导可持续且公平的技术进步。 该新闻通讯引用了阿西莫格鲁 2024 年 4 月的论文《AI 的简单宏观经济学》，该论文使用基于任务的模型，通过自动化和任务互补性分析 AI 的影响。维护创新角度则借鉴了更广泛的讨论，质疑持续创新相对于维护的价值。

rss · MIT Technology Review · May 12, 12:10

**背景**: 达龙·阿西莫格鲁与西蒙·约翰逊、詹姆斯·罗宾逊因研究政治制度如何塑造经济增长而共同获得 2024 年诺贝尔经济学奖。他的 AI 论文评估了关于 AI 巨大宏观经济影响的说法，认为 AI 的收益可能比通常声称的要温和。“万物维护”概念认为，社会相对于创新低估了维护，而关注维护可以带来更可持续和公平的结果。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://economics.mit.edu/sites/default/files/2024-04/The+Simple+Macroeconomics+of+AI.pdf">The Simple Macroeconomics of AI∗ Daron Acemoglu</a></li>
<li><a href="https://aeon.co/essays/innovation-is-overvalued-maintenance-often-matters-more">Innovation is overvalued. Maintenance often matters more | Aeon Essays</a></li>

</ul>
</details>

**标签**: `#AI`, `#economics`, `#Nobel`, `#technology review`

---

<a id="item-25"></a>
## [Constellation Energy 在 PJM 队列中新增 5 GW 容量，数据中心不确定性犹存](https://www.utilitydive.com/news/constellation-energy-crane-pjm-ercot-earnings/819939/) ⭐️ 6.0/10

Constellation Energy 已将 5 GW 的核电、天然气和电池容量加入 PJM 互联队列，部分数据中心客户因对共址和备用拍卖规则的不确定性而暂停决策。 这一扩张表明大型能源公司正在为数据中心的激增需求做准备，但 PJM 的监管不确定性可能延迟维持电网可靠性所需的关键投资。 这 5 GW 包括核电、天然气和电池储能资源。PJM 正面临来自数据中心的 5%年需求增长，其最近的容量拍卖比可靠性目标低了约 6.6 GW。

rss · Utility Dive · May 12, 12:43

**背景**: PJM Interconnection 是美国最大的电网运营商，为 13 个州和华盛顿特区的 6700 万客户提供服务，运营着一个竞争性批发电力市场。为应对需求快速增长带来的可靠性问题，PJM 正在制定数据中心共址规则和备用拍卖机制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PJM_Interconnection">PJM Interconnection</a></li>
<li><a href="https://www.utilitydive.com/news/ferc-pjm-colocation-data-center/808368/">FERC orders PJM to craft large load colocation rules | Utility Dive</a></li>

</ul>
</details>

**标签**: `#energy`, `#nuclear`, `#grid`, `#data centers`, `#PJM`

---

<a id="item-26"></a>
## [亚马逊签署新型屋顶热泵协议](https://www.canarymedia.com/articles/heat-pumps/amazon-game-changing-heat-pump) ⭐️ 6.0/10

亚马逊签署了一项协议，部署一种新型屋顶热泵，为商业建筑提供全电供暖和制冷，此前在休斯顿的一个物流设施进行了为期六个月的现场试验并取得成功。 亚马逊这样的大公司采用该技术，可能加速商业建筑向全电化转型，减少供暖对化石燃料的依赖，大幅降低能源成本和碳排放。 该热泵设计用于屋顶安装，提供超高效制冷和全电供暖。试验在炎热潮湿的休斯顿进行，展示了在恶劣条件下的性能。

rss · Latitude Media (Canary Media) · May 13, 07:30

**背景**: 热泵是一种高效设备，通过转移热量而非产生热量来提供供暖和制冷。大多数商业建筑仍使用化石燃料供暖，全电建筑很少——2018 年美国不到三分之一的商业建筑是全电的。美国能源部的商业建筑 HVAC 技术挑战赛旨在开发下一代屋顶热泵以促进广泛采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.carrier.com/commercial/en/us/news/news-article/carrier-advances-next-generation-rooftop-heat-pump-technology-with-commercial-field-trials.html">Carrier Advances Next-Generation Rooftop Heat Pump Technology with Commercial Field Trials High-performance systems demonstrate cold-climate capability, efficiency gains and lower operating costs for commercial buildings</a></li>
<li><a href="https://www.eia.gov/todayinenergy/detail.php?id=60983">Less than one-third of U.S. commercial buildings were all-electric in 2018 - U.S. Energy Information Administration (EIA)</a></li>

</ul>
</details>

**标签**: `#heat pumps`, `#energy efficiency`, `#Amazon`, `#commercial buildings`, `#HVAC`

---

<a id="item-27"></a>
## [EIA 因中东战争调整石油展望](https://www.energyintel.com/0000019e-1d5a-d327-a9fe-7ddabf5f0000) ⭐️ 6.0/10

美国能源信息署（EIA）大幅修订了全球石油供应、需求和库存预测，以反映持续的中东战争和霍尔木兹海峡的关闭。 此次修订凸显了地缘政治动荡对全球能源市场的严重影响，可能导致油价上涨和经济放缓，影响全球消费者和行业。 EIA 目前假设 2026 年全球石油需求增长平均为每天 60 万桶，低于上月预测的每天 120 万桶，预计 2027 年将反弹。

rss · Energy Intelligence · May 12, 20:19

**背景**: 霍尔木兹海峡是全球石油运输的关键咽喉，其关闭是自 1970 年代以来对世界能源供应最大的干扰。EIA 的短期能源展望（STEO）是能源市场预测的重要参考。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.eia.gov/outlooks/steo/report/global_oil.php">Short-Term Energy Outlook - U.S. Energy Information Administration (EIA)</a></li>
<li><a href="https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis">2026 Strait of Hormuz crisis - Wikipedia</a></li>
<li><a href="https://www.dallasfed.org/research/economics/2026/0320">What the closure of the Strait of Hormuz means for the global economy - Dallasfed.org</a></li>

</ul>
</details>

**标签**: `#energy`, `#geopolitics`, `#oil supply`

---

<a id="item-28"></a>
## [世嘉因 Rovio 亏损降低服务型游戏优先级](https://www.gamedeveloper.com/business/sega-is-lowering-the-priority-of-games-as-a-service-titles) ⭐️ 6.0/10

世嘉在报告其收购的 Rovio 带来 2 亿美元减值损失后，正在降低服务型游戏（GaaS）的优先级，标志着其战略从持续运营模式转向。 此举反映了行业对服务型游戏日益增长的怀疑态度，即使是大型发行商也面临持续运营模式带来的财务风险。这可能会影响其他公司重新评估其对经常性收入模式的依赖。 约 2 亿美元（313 亿日元）的减值损失是在 2026 财年第三季度确认的，此前世嘉于 2023 年以 7.76 亿美元收购了 Rovio。作为战略转向的一部分，世嘉还取消了其“Super Game”项目。

rss · Game Developer (Gamasutra) · May 12, 17:24

**背景**: 服务型游戏（GaaS）是指通过微交易、订阅或季节性内容而非一次性购买来产生持续收入的游戏。世嘉于 2023 年收购了《愤怒的小鸟》开发商 Rovio，以增强其移动和持续运营游戏组合。此次减值表明 Rovio 的表现未达预期，促使世嘉降低 GaaS 优先级，转而专注于传统游戏开发。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.gamesindustry.biz/sega-records-200m-impairment-loss-for-rovio-during-q3">Sega records $200m impairment write-down for Rovio during Q3 | GamesIndustry.biz</a></li>
<li><a href="https://www.gamesindustry.biz/sega-reports-316m-net-loss-during-fy26-cancels-super-game-project-amid-strategic-pivot">Sega reports $31.6m net loss during FY26, cancels 'Super Game' project amid strategic pivot | GamesIndustry.biz</a></li>
<li><a href="https://insider-gaming.com/sega-reports-over-200m-rovio-impairment-in-q3-earnings/">Sega Reports Over $200M Rovio Impairment in Q3 Earnings - Insider Gaming</a></li>

</ul>
</details>

**标签**: `#gaming`, `#business`, `#strategy`, `#games-as-a-service`

---

<a id="item-29"></a>
## [微软以色列总经理因 Azure 道德指控离职](https://www.gamedeveloper.com/business/microsoft-israel-s-general-manager-leaves-amid-alleged-unethical-use-of-azure) ⭐️ 6.0/10

微软以色列总经理因涉嫌不当使用 Azure 而离职，引发对公司道德准则违规的担忧。 这一事件凸显了云计算销售实践中潜在的道德风险，影响对微软 Azure 平台及其区域运营的信任。 指控涉及 Azure 的不当使用，但具体细节尚未披露。此次离职凸显了科技公司区域领导层及合规问题持续受到关注。

rss · Game Developer (Gamasutra) · May 12, 16:46

**背景**: Microsoft Azure 是与 AWS 和 Google Cloud 竞争的主要云计算平台。云销售中的道德失误可能涉及虚假陈述、未经授权使用或违反数据隐私规则。

**标签**: `#Microsoft`, `#Azure`, `#ethics`, `#cloud computing`

---

<a id="item-30"></a>
## [内存危机中涌现逼真假 DDR5 模块](https://www.pcgamer.com/hardware/memory/were-starting-to-get-convincing-counterfeit-ddr5-modules-just-in-case-the-memory-crisis-isnt-bad-enough-already/) ⭐️ 6.0/10

据多家科技媒体 2025 年末报道，带有假塑料芯片和伪造标签的假冒 DDR5 内存模块正在 Mercari 和雅虎拍卖等二手市场上销售。 这加剧了持续的内存危机——高价格和稀缺性已给消费者带来负担；假冒模块可能导致系统不稳定或损坏，侵蚀对二手硬件市场的信任。 这些假货通常使用裸电路板或空塑料芯片，重新贴标以冒充正品 DDR5，有些甚至被列为“故障品”以避免立即被识破。

rss · PC Gamer · May 12, 15:15

**背景**: 内存危机（有时称为“RAMpocalypse”）始于 2024 年，原因是制造产能结构性转向 AI 基础设施，导致 DRAM 短缺和价格飙升。这种环境为骗子利用高需求和有限供应创造了机会。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/memory/were-starting-to-get-convincing-counterfeit-ddr5-modules-just-in-case-the-memory-crisis-isnt-bad-enough-already/">We're starting to get convincing counterfeit DDR5 modules, just in case the memory crisis isn't bad enough already | PC Gamer</a></li>
<li><a href="https://videocardz.com/newz/fake-ddr5-so-dimm-modules-spotted-with-dummy-plastic-chips-and-fake-labels">Fake DDR5 SO-DIMM modules spotted with dummy plastic chips and fake labels - VideoCardz.com</a></li>
<li><a href="https://www.tomshardware.com/pc-components/ddr5/scammers-are-selling-fake-ddr5-with-empty-plastic-chips-relabeled-to-pass-as-legit-fake-components-mounted-to-pcbs-are-yet-another-sign-of-the-rampocalypse">Scammers are selling fake DDR5 with empty plastic chips relabeled to pass as legit — fake components mounted to PCBs are yet another sign of the RAMpocalypse | Tom's Hardware</a></li>

</ul>
</details>

**标签**: `#hardware`, `#supply chain`, `#security`, `#memory`

---