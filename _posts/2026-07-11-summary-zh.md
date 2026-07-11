---
layout: default
title: "Horizon Summary: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
---

> From 41 items, 6 important content pieces were selected

---

1. [ClickHouse 将 PgBouncer 吞吐量提升 4 倍](#item-1) ⭐️ 8.0/10
2. [Hotz：AI 必须将自由置于安全之上](#item-2) ⭐️ 8.0/10
3. [强化学习实现量子纠错的持续校准](#item-3) ⭐️ 8.0/10
4. [英伟达、CoreWeave、Nebius：GPU 热潮中的循环融资内幕](#item-4) ⭐️ 7.0/10
5. [在 SQLite 中优先使用严格表](#item-5) ⭐️ 7.0/10
6. [Ant：一个拥有自有引擎的 JavaScript 运行时](#item-6) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [ClickHouse 将 PgBouncer 吞吐量提升 4 倍](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

ClickHouse 详细介绍了他们如何通过使用 SO_REUSEPORT 套接字选项并实现一种对等（peering）机制来处理连接取消转发，从而将 PgBouncer 的吞吐量提升了 4 倍。 这一改进解决了 PostgreSQL 连接池中的一个关键瓶颈，为大规模部署提供了更高的并发性和更好的资源利用率。它还提供了一个实用的开源解决方案，其他面临类似可扩展性挑战的团队可以采用。 SO_REUSEPORT 选项允许多个 PgBouncer 进程绑定到同一端口，将传入连接分发到各个工作进程。对等机制确保取消请求被转发到拥有该会话的正确进程，从而防止取消操作丢失。

hackernews · saisrirampur · Jul 11, 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是 PostgreSQL 的轻量级连接池，用于管理客户端连接以减少开销。在高流量环境中，单个 PgBouncer 进程可能成为瓶颈，并且如果取消请求落在错误的工作进程上，可能会失败。SO_REUSEPORT 是一个 Linux 套接字选项，允许多个套接字监听同一端口，实现内核级别的负载均衡。对等是 PgBouncer 的一个功能，允许实例之间转发取消请求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/pulse/how-modern-kernels-handle-massive-traffic-use-jisan-ahmed-ghg1c">How Modern Kernels Handle Massive Traffic : the use of...</a></li>
<li><a href="https://www.pgbouncer.org/config.html">PgBouncer config</a></li>
<li><a href="https://github.com/pgbouncer/pgbouncer/issues/328">pgbouncer unavailable while churning through cancellations · Issue #328 · pgbouncer/pgbouncer</a></li>

</ul>
</details>

**社区讨论**: 社区成员推荐了 Odyssey 和 pgdog 等替代工具，并询问了对等设置的简便性。讨论总体上是积极的，大家对 SO_REUSEPORT 和对等的技术细节很感兴趣。

**标签**: `#PostgreSQL`, `#PgBouncer`, `#connection pooling`, `#scalability`, `#systems engineering`

---

<a id="item-2"></a>
## [Hotz：AI 必须将自由置于安全之上](https://geohot.github.io//blog/jekyll/update/2026/07/11/ai-2040.html) ⭐️ 8.0/10

George Hotz 发表了一篇博客文章，认为未来的 AI 系统应优先考虑自由而非安全，并警告反对可能导致威权控制的“智能崇拜”。 这场辩论触及了 AI 对齐和治理中的核心矛盾，对社会如何平衡言论自由与 AI 代理可能带来的危害具有深远影响。 Hotz 认为限制 AI 输出等同于审查，真正的自由 AI 必须允许用户询问任何内容，甚至包括非法目的，只要 AI 不直接在物理世界中行动。

hackernews · rvz · Jul 11, 18:04 · [社区讨论](https://news.ycombinator.com/item?id=48874200)

**背景**: AI 对齐是指确保 AI 系统按照人类价值观和目标行动。“智能崇拜”是 Hotz 用来描述过度依赖 AI 可能导致集中控制的术语。

**社区讨论**: 评论者提出了对 AI 记录和偏见注入的担忧，并指出自由并非二元对立。一些人同意 Hotz 关于信息聊天机器人的观点，但认为现实世界中的代理需要不同的规则。

**标签**: `#AI safety`, `#censorship`, `#freedom`, `#alignment`, `#ethics`

---

<a id="item-3"></a>
## [强化学习实现量子纠错的持续校准](https://arstechnica.com/science/2026/07/quantum-error-correction-can-constantly-recalibrate-a-processor/) ⭐️ 8.0/10

研究人员将强化学习应用于量子纠错，使处理器能够利用错误信息持续重新校准其控制算法。 该方法通过自动化纠错调整，解决了量子计算中的一个关键可扩展性挑战，可能使容错量子计算机更接近现实。 强化学习代理利用实时错误数据调整控制参数，无需人工干预即可适应变化的噪声条件。

rss · Ars Technica · Jul 10, 23:02

**背景**: 量子纠错保护量子信息免受退相干和噪声的影响，但传统方法需要定期重新校准。强化学习是一种机器学习技术，代理通过试错学习最优动作，可以自动化这一重新校准过程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quantum_error_correction">Quantum error correction</a></li>
<li><a href="https://askfilo.com/user-question-answers-smart-solutions/how-can-reinforcement-learning-be-used-to-design-quantum-3439353539323035">How can reinforcement learning be used to design quantum gates in...</a></li>

</ul>
</details>

**标签**: `#quantum computing`, `#error correction`, `#reinforcement learning`, `#scalability`

---

<a id="item-4"></a>
## [英伟达、CoreWeave、Nebius：GPU 热潮中的循环融资内幕](https://io-fund.com/ai-stocks/nvidia-coreweave-nebius-circular-financing-gpu-boom) ⭐️ 7.0/10

一项分析显示，英伟达对 CoreWeave 和 Nebius 的投资是对超大规模云厂商主导地位的战略对冲，社区对融资是否真正循环展开辩论。 这很重要，因为 GPU 融资动态可能塑造 AI 基础设施格局，影响竞争、定价以及 AI 行业泡沫的风险。 英伟达投资 20 亿美元获得 CoreWeave 9%的股权，而 CoreWeave 计划 2026 年资本支出 350 亿美元，英伟达的贡献仅占该年支出的 5.7%。文章质疑此类投资是否构成循环融资。

hackernews · adletbalzhanov · Jul 11, 17:21 · [社区讨论](https://news.ycombinator.com/item?id=48873836)

**背景**: 循环融资是指公司投资于客户，客户再用这些资金购买该公司产品，形成自我强化的循环。在 GPU 热潮中，英伟达投资于 CoreWeave 和 Nebius 等 AI 云初创公司，这些公司再购买英伟达的 GPU 用于数据中心。这种做法引发了对需求膨胀和潜在金融脆弱性的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CoreWeave">CoreWeave</a></li>
<li><a href="https://en.wikipedia.org/wiki/Nebius_Group">Nebius Group</a></li>
<li><a href="https://trendytechtribe.com/markets/the-silicon-debt-trap">Nvidia GPU Financing Loop 2026: The New... | Trendy Tech Tribe</a></li>

</ul>
</details>

**社区讨论**: 评论者对循环融资的说法展开辩论：有人认为英伟达的投资相对于 CoreWeave 的总资本支出太小，不足以视为循环；另一些人则警告，此类投资的规模可能引发比 2007 年更严重的金融危机。还有讨论关注这些建设是否能够实现经济盈利，建议将每 token 的 ROI 和企业 token 预算等指标作为关键观察点。

**标签**: `#GPU`, `#AI infrastructure`, `#venture capital`, `#Nvidia`, `#cloud computing`

---

<a id="item-5"></a>
## [在 SQLite 中优先使用严格表](https://evanhahn.com/prefer-strict-tables-in-sqlite/) ⭐️ 7.0/10

Evan Hahn 的一篇博文推荐在 SQLite 中使用 STRICT 表来强制静态类型，防止类型转换错误。该文章引发了社区关于将 STRICT 设为默认行为的讨论。 严格表提高了数据完整性并减少了应用程序中的错误，尤其是在多个应用程序共享数据库时。这场辩论凸显了 SQLite 灵活的类型系统与现代软件工程中对类型安全需求之间的张力。 在严格表中，每一列都必须指定数据类型，并且只接受该类型的值；ANY 类型的行为略有不同。然而，严格表不支持某些类型如 DATE，这可能是一些用例的限制。

hackernews · ingve · Jul 11, 17:33 · [社区讨论](https://news.ycombinator.com/item?id=48873940)

**背景**: SQLite 传统上使用清单类型，即类型与值本身关联，而不是与列关联。这提供了灵活性，但可能导致意外行为，例如在 INTEGER 列中存储字符串。STRICT 表在 SQLite 3.37.0（2021 年 11 月）中引入，强制实施类似于传统 SQL 数据库的静态类型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sqlite.org/stricttables.html">STRICT Tables - SQLite</a></li>
<li><a href="https://www.sqlitetutorial.net/sqlite-strict-tables/">SQLite Strict Tables</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持严格表，有些人主张将其设为默认。一位用户指出，SQLite 的主要用例（嵌入式、单应用）使得灵活类型可以接受，而另一位用户将其类比为选择 UDP 而非 TCP 然后重新实现可靠性。少数人指出严格表缺少某些数据类型如 DATE。

**标签**: `#SQLite`, `#database`, `#type safety`, `#software engineering`

---

<a id="item-6"></a>
## [Ant：一个拥有自有引擎的 JavaScript 运行时](https://antjs.org/) ⭐️ 6.0/10

Ant 是一个新的 JavaScript 运行时和生态系统，包含自有引擎（Ant Silver）、包管理器、包注册表（ants.land）、部署平台和桌面应用框架（Ant Desktop）。它声称轻量（9 MB 二进制文件）且从头构建，并非 V8 或其他引擎的封装。 如果成功，Ant 可能为边缘计算、无服务器和嵌入式系统提供比 Node.js 和 Deno 更小、更快的替代方案。然而，其早期阶段和关于起源的争议引发了对其长期可行性和可信度的质疑。 Ant 的引擎 Ant Silver 使用 MIR 的分支作为其 JIT 编译器，旨在实现接近编译的性能。该项目因最初是 AGPL 许可的 Elk 引擎的分支而受到批评，尽管作者声称此后已重写。

hackernews · theMackabu · Jul 11, 20:07 · [社区讨论](https://news.ycombinator.com/item?id=48875377)

**背景**: 像 Node.js 和 Deno 这样的 JavaScript 运行时在浏览器之外执行 JavaScript。大多数依赖 Google 的 V8 引擎，该引擎体积庞大且针对浏览器优化。Ant 旨在通过从头构建自有引擎来提供更小、更快的运行时，针对大小和启动时间至关重要的用例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://antjs.org/">Ant, a lightweight JavaScript runtime</a></li>
<li><a href="https://github.com/theMackabu/ant">GitHub - theMackabu/ant: javascript for 's, a tiny runtime ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论褒贬不一：一些人质疑引擎的原创性，因为它最初是从 Elk 分支而来，而另一些人则对其快速开发印象深刻。还提出了关于信任和项目商业模式（例如，公司招聘页面无法访问）的担忧。

**标签**: `#JavaScript`, `#runtime`, `#ecosystem`, `#open source`, `#web development`

---