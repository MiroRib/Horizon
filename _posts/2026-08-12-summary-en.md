---
layout: default
title: "Horizon Summary: 2026-08-12 (EN)"
date: 2026-08-12
lang: en
---

> From 175 items, 35 important content pieces were selected

---

1. [Qwen3.8-2.4T-A95B: Massive MoE Model Nears Opus 4.5 Performance](#item-1) ⭐️ 9.0/10
2. [Massive Supply-Chain Attack on AI Package Leaks Terabytes of Credentials](#item-2) ⭐️ 9.0/10
3. [OpenAI Python SDK v3.0.0 Switches to HTTPX2](#item-3) ⭐️ 8.0/10
4. [DeepSeek V4 Pro 0813 Launch Sparks Benchmark and Pricing Debate](#item-4) ⭐️ 8.0/10
5. [Zed Introduces Delta: AI-Powered Collaborative Coding with Realtime Conversations](#item-5) ⭐️ 8.0/10
6. [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](#item-6) ⭐️ 8.0/10
7. [HTML over WebSockets: Real-Time SPAs with Minimal JavaScript](#item-7) ⭐️ 8.0/10
8. [Grok 4.6 Launch Sparks API Quirks and Benchmark Debate](#item-8) ⭐️ 8.0/10
9. [Discovered Materials Uses AI Agents to Accelerate Semiconductor Material Discovery](#item-9) ⭐️ 8.0/10
10. [AI Is Eroding the Middle Class of Software Engineering](#item-10) ⭐️ 8.0/10
11. [Fields Medalist Analyzes LLM Mathematical Strengths](#item-11) ⭐️ 8.0/10
12. [Woxi: Open-Source Rust Reimplementation of Wolfram Language](#item-12) ⭐️ 8.0/10
13. [Physicists Report Strongest Evidence Yet for Glueballs](#item-13) ⭐️ 8.0/10
14. [AI Tool Finds Zoom Screen-Sharing Hijack Flaw](#item-14) ⭐️ 8.0/10
15. [Scientists Create Female Clones from Male Mice Using CRISPR](#item-15) ⭐️ 8.0/10
16. [Twitch faces backlash for default-on AI training harvesting streamer data for Amazon](#item-16) ⭐️ 8.0/10
17. [Chrome's Tiny JPEG Scaling Differs from Other Browsers](#item-17) ⭐️ 7.0/10
18. [uBlock Origin Stops Blocking Facebook Ads](#item-18) ⭐️ 7.0/10
19. [Shade Map: Interactive Tool for Sunlight and Shade Visualization](#item-19) ⭐️ 7.0/10
20. [Warrant Required for License Plate Reader Searches](#item-20) ⭐️ 7.0/10
21. [AI Firms Buying and Destroying Rare Books Face Bookseller Resistance](#item-21) ⭐️ 7.0/10
22. [PJM Considers Ride-Through Standards After 3.8 GW Data Center Load Trip](#item-22) ⭐️ 7.0/10
23. [Low-Carbon Power Emerges as Key Factor in AI Data Center Siting](#item-23) ⭐️ 7.0/10
24. [Tim King, AmigaDOS Developer, Dies](#item-24) ⭐️ 6.0/10
25. [Mass Scans Spoof AI Bots Like ClaudeBot](#item-25) ⭐️ 6.0/10
26. [Google Pixel 11 series: Tensor G6, camera upgrades, higher prices](#item-26) ⭐️ 6.0/10
27. [Amazon exits MMO live operations, hands over Throne and Liberty and Lost Ark](#item-27) ⭐️ 6.0/10
28. [JCB's Hydrogen-Powered Car Sets New Land Speed Record](#item-28) ⭐️ 6.0/10
29. [US Orders Kalshi to Keep Operating, Overriding NY Gambling Laws](#item-29) ⭐️ 6.0/10
30. [FBI Probes Fake Hotspot Attack on Delta Flight Linked to DEF CON](#item-30) ⭐️ 6.0/10
31. [Texas Peak Demand Hits Record, Supply Constraints Loom](#item-31) ⭐️ 6.0/10
32. [Virginia Regulator Orders Dominion to Assign Some Transmission Costs to Data Centers](#item-32) ⭐️ 6.0/10
33. [Trump Admin Backs Puerto Rico Battery, Cuts Solar Funding](#item-33) ⭐️ 6.0/10
34. [Sony's Disc Phase-Out Sparks Game Preservation Backlash](#item-34) ⭐️ 6.0/10
35. [AI Agents: Both Victims and Attackers in 2026 Malware Wars](#item-35) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B: Massive MoE Model Nears Opus 4.5 Performance](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen released Qwen3.8-2.4T-A95B, a 2.4-trillion-parameter Mixture-of-Experts model with 95B active parameters per token, claiming performance near Opus 4.5/5. The model is available in BF16 and FP8 formats, with a 1-bit quantized version at 397GB. This release pushes the frontier of open-weight MoE models, offering near-top-tier performance in a package that can potentially run on high-end consumer hardware when quantized. It intensifies competition among open-source models and may accelerate adoption of large MoE architectures for reasoning and agentic workloads. The model uses a fine-grained MoE with 512 routed experts (10 active) plus one shared expert, over a 92-layer hybrid-attention backbone, supporting up to 1M context and 128K output. It is text-only, requires thinking mode, and lacks vision support and non-thinking mode, which are reserved for the official Qwen3.8-Max version.

hackernews · Philpax · Aug 12, 15:01 · [Discussion](https://news.ycombinator.com/item?id=49273478)

**Background**: Mixture-of-Experts (MoE) models activate only a subset of parameters per token, enabling massive scale with manageable compute. Quantization techniques like FP8 and 1-bit reduce memory footprint, making large models more accessible. Serving such models requires distributed inference frameworks and high-memory systems, as the BF16 version needs ~4.9TB.

<details><summary>References</summary>
<ul>
<li><a href="https://recipes.vllm.ai/Qwen/Qwen3.8-2.4T-A95B">Qwen/Qwen3.8-2.4T-A95B — 2.4T / 95B active · MOE · 256K ctx</a></li>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with Configurable Reasoning on NVIDIA GB300 NVL72 | NVIDIA Technical Blog</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B">Qwen/Qwen3.8-2.4T-A95B · Hugging Face</a></li>

</ul>
</details>

**Discussion**: Community comments highlight the model's size and serving challenges, noting that only BF16 and FP8 are released, making it harder to serve than Kimi k3. Some express astonishment at the 1-bit quantized version fitting in 397GB, potentially running on high-end consumer hardware, while others lament the lack of vision and 1M context in the open-weight version.

**Tags**: `#AI/ML`, `#Large Language Models`, `#MoE`, `#Qwen`, `#Open Source`

---

<a id="item-2"></a>
## [Massive Supply-Chain Attack on AI Package Leaks Terabytes of Credentials](https://arstechnica.com/security/2026/08/terabytes-of-credentials-leaked-in-massive-supply-chain-attack/) ⭐️ 9.0/10

A massive supply-chain attack on a compromised AI package has leaked terabytes of credentials from 2,500 users. The attack involved scraping and exfiltrating sensitive data from the affected users. This incident underscores the growing threat to software supply chains, especially within the AI ecosystem, where widely-used packages can be compromised to steal credentials at scale. It highlights the urgent need for stronger security measures in AI tooling and dependency management. The compromised AI package was used to scrape and exfiltrate credentials from 2,500 users, resulting in terabytes of leaked data. The attack is part of a broader trend of supply-chain attacks targeting AI packages, such as the recent LiteLLM compromise that could impact tens of thousands of corporate environments.

rss · Ars Technica · Aug 12, 21:43

**Background**: A supply chain attack is a cyber-attack that targets less secure elements in an organization's supply chain, such as software components or vendors. In the software context, attackers often compromise a widely-used package to inject malicious code that can affect all downstream users. The AI ecosystem has become a prime target due to the rapid adoption of open-source packages and the sensitive data they often handle.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Supply_chain_attack">Supply chain attack</a></li>
<li><a href="https://therecord.media/supply-chain-attack-hits-widely-used-ai-package">Supply chain attack hits widely-used AI package, risks impacting thousands of companies | The Record from Recorded Future News</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/cyber-security/compromised-mistral-ai-and-tanstack-packages-may-have-exposed-github-cloud-and-ci-cd-credentials-in-mini-shai-hulud-malware-infection-supply-chain-campaign-spreads-across-npm-and-ai-developer-ecosystems-like-wildfire">Compromised Mistral AI and TanStack packages may have exposed GitHub, cloud and CI/CD credentials in 'mini Shai Hulud' malware infection — supply-chain campaign spreads across npm and AI developer ecosystems like wildfire | Tom's Hardware</a></li>

</ul>
</details>

**Tags**: `#security`, `#supply-chain`, `#AI`, `#data breach`, `#credentials`

---

<a id="item-3"></a>
## [OpenAI Python SDK v3.0.0 Switches to HTTPX2](https://github.com/openai/openai-python/releases/tag/v3.0.0) ⭐️ 8.0/10

OpenAI released version 3.0.0 of its official Python SDK, which now uses HTTPX2 as the default HTTP client. This is a breaking change, and httpx is no longer installed automatically. This major update affects all developers using the OpenAI Python SDK, especially those with custom HTTP configurations. The migration to HTTPX2 promises improved performance and modern HTTP features, but requires users to update their code. The SDK provides a migration guide and a temporary runtime-only legacy HTTPX escape hatch for compatibility. Applications using custom HTTPX clients, transports, or configuration objects must migrate to HTTPX2 equivalents.

github · openai-sdks[bot] · Aug 12, 01:54

**Background**: HTTPX is a popular Python HTTP client that supports sync and async APIs, as well as HTTP/1.1 and HTTP/2. HTTPX2 is the next-generation version, designed to be API-compatible with HTTPX, making migration straightforward for most users.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/openai/openai-python">GitHub - openai/openai-python: The official Python library for the OpenAI API · GitHub</a></li>
<li><a href="https://github.com/openai/openai-python/issues/3375">Consider migrating from httpx to httpx2 · Issue #3375 · openai/openai-python</a></li>
<li><a href="https://pypi.org/project/httpx2/2.10.0/">httpx 2 · PyPI</a></li>

</ul>
</details>

**Discussion**: The community discussion in issue #3375 indicates that the migration is straightforward since HTTPX2 is API-compatible and a drop-in replacement for common usage. The main impact is swapping the dependency and updating internal imports.

**Tags**: `#openai`, `#python`, `#sdk`, `#breaking-change`, `#httpx`

---

<a id="item-4"></a>
## [DeepSeek V4 Pro 0813 Launch Sparks Benchmark and Pricing Debate](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek released V4 Pro 0813, a large-scale mixture-of-experts model available on OpenRouter with a 1,048,576-token context window and pricing of $0.435 per million input tokens and $0.87 per million output tokens. The model has quickly gained attention for its competitive benchmark scores and aggressive pricing. This release intensifies competition in the AI model market, offering a high-performance option at a fraction of the cost of rivals like Opus 4.8, potentially reshaping developer choices and pricing strategies. Its strong community engagement indicates significant interest from developers evaluating real-world performance versus cost. The model is a mixture-of-experts architecture with 1.6T total parameters and 49B activated parameters, supporting a maximum output of 384,000 tokens. Independent benchmarks from Artificial Analysis show competitive scores, and pricing is about 20x cheaper than Opus 4.8, though some user tests report mixed results on coding tasks.

hackernews · explosion-s · Aug 12, 16:04 · [Discussion](https://news.ycombinator.com/item?id=49274600)

**Background**: DeepSeek is a Chinese AI research company known for releasing open-weight models at low prices. V4 Pro 0813 is part of the V4 series, which uses a mixture-of-experts design to activate only a subset of parameters per token, balancing performance and efficiency. The model is available via API providers like OpenRouter, and its context window of 1M tokens is among the largest in the industry.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - Pricing & Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro">DeepSeek V4 Pro - API Pricing & Benchmarks | OpenRouter</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed sentiment: some users report bugs and higher cost in practical coding tests compared to alternatives like Grok 4.6, while others highlight its competitive benchmarks and significantly lower pricing. There is also discussion about benchmark comparisons with models like GLM-5.2 and Kimi-K3, and some users note inconsistencies in real-world performance versus benchmarks.

**Tags**: `#AI`, `#DeepSeek`, `#LLM`, `#benchmarks`, `#pricing`

---

<a id="item-5"></a>
## [Zed Introduces Delta: AI-Powered Collaborative Coding with Realtime Conversations](https://zed.dev/blog/introducing-delta) ⭐️ 8.0/10

Zed has introduced Delta, an AI-powered tool that enables realtime collaborative multiplayer conversations and inline commenting on agent conversations, with a beta version reportedly ready within weeks. The tool, built on DeltaDB, records every operation and links changes to the conversation that produced them, aiming to improve code understanding and team collaboration. Delta represents a significant step in AI-assisted coding by treating conversations as documents and integrating them into the development workflow, potentially changing how teams review code and collaborate. It addresses the growing need for transparency in AI-generated code and could influence how future coding tools handle agent interactions. DeltaDB, the underlying system, records every operation between commits, assigning stable identities and linking changes to the AI agent conversation that produced them. The tool allows sessions to sync live into a Delta thread, which can be shared, commented on, and picked up by teammates with full context, and it can be accessed via terminal or mounted to local disk.

hackernews · khy · Aug 12, 18:19 · [Discussion](https://news.ycombinator.com/item?id=49276574)

**Background**: Zed is a modern code editor that has been developing DeltaDB since at least 2025, with early access announced in June 2026. Traditional version control systems like Git store snapshots at commit points, but DeltaDB records every operation, providing a more granular history. This aligns with the trend of AI agents generating code, where the conversation itself becomes the source of truth.

<details><summary>References</summary>
<ul>
<li><a href="https://zed.dev/blog/introducing-delta">Introducing Delta — Zed's Blog</a></li>
<li><a href="https://sesamedisk.com/what-is-zed-deltadb-features/">What Is Zed DeltaDB and Its Key Features - Sesame Disk</a></li>
<li><a href="https://www.kucoin.com/news/flash/zed-launches-deltadb-version-control-system-with-fine-grained-code-tracking">Zed Launches DeltaDB Version Control System with Fine-Grained Code Tracking | KuCoin</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed sentiment. Some users are skeptical about AI summaries of code, citing verbosity and missing edge cases, while others see value in realtime collaboration for mentoring junior engineers. One commenter questions the long-term value given rapid advances in frontier models, suggesting the real game might be in storing data and running agent sessions.

**Tags**: `#AI`, `#code editor`, `#collaboration`, `#LLM`, `#developer tools`

---

<a id="item-6"></a>
## [Tailscale Traces Database Corruption to 16-Year-Old SQLite WAL-Reset Bug](https://tailscale.com/blog/sqlite-wal-reset-bug) ⭐️ 8.0/10

Tailscale has identified the root cause of database corruption incidents that plagued its control plane for months: a 16-year-old bug in SQLite's WAL (Write-Ahead Logging) reset mechanism. The bug, named the 'WAL-Reset bug' by SQLite developers, was uncovered with the help of a purpose-built debugging tool funded by Tailscale. This discovery is significant because SQLite is one of the most widely used database engines globally, and this bug could potentially affect any application using WAL mode under specific race conditions. It also highlights the value of companies investing in open-source tooling and support contracts to improve software reliability for the entire ecosystem. The bug occurs when the WAL-index file is reset while another process is reading it, leading to a race condition that can corrupt the database. Tailscale experienced 19 corruption incidents over six months before the issue was isolated, and the fix has been incorporated into SQLite's official codebase.

hackernews · ropbear · Aug 12, 14:22 · [Discussion](https://news.ycombinator.com/item?id=49272832)

**Background**: SQLite is a self-contained, in-process relational database engine that uses WAL mode to improve concurrency by allowing readers and writers to work simultaneously. The WAL-index file tracks the state of the WAL, and a race condition in its reset logic can cause corruption. Tailscale's control plane uses SQLite with a single-writer design, which is the recommended usage, yet the bug still manifested, underscoring the subtlety of the issue.

<details><summary>References</summary>
<ul>
<li><a href="https://tailscale.com/blog/sqlite-wal-reset-bug">How Tailscale helped find the SQLite WAL-Reset bug</a></li>
<li><a href="https://antithesis.com/blog/2026/wal-reset-bug/">Breaking the WAL | Antithesis</a></li>
<li><a href="https://www.youngju.dev/blog/2026-07-16-sqlite-wal-reset-bug.en">The SQLite WAL - Reset Bug : A Data Corruption Race That Hid for 15...</a></li>

</ul>
</details>

**Discussion**: Community members praised Tailscale for funding the development of a specific debugging tool and for taking out a support contract with SQLite, seeing it as a positive example of corporate support for open source. Some commenters noted the irony of SQLite's extensive testing (92 million lines of tests) versus the persistence of this bug, referencing Dijkstra's quote that tests can only prove the presence of bugs, not their absence. Others shared additional resources, such as a related video by Richard Hipp on reliability lessons from SQLite.

**Tags**: `#SQLite`, `#database`, `#bug`, `#Tailscale`, `#open-source`

---

<a id="item-7"></a>
## [HTML over WebSockets: Real-Time SPAs with Minimal JavaScript](https://en.andros.dev/blog/ef4968f5/html-over-websockets-real-time-spas-with-barely-any-javascript/) ⭐️ 8.0/10

The article explores building real-time single-page applications (SPAs) using HTML over WebSockets, a technique popularized by Phoenix LiveView, which minimizes JavaScript by sending HTML fragments over a persistent WebSocket connection. It discusses the trade-offs between WebSockets and Server-Sent Events (SSE), and the approach has sparked a vibrant community discussion. This approach could significantly simplify front-end development by allowing developers to write real-time applications in a single language (e.g., Elixir or Python) without complex client-side JavaScript frameworks. It aligns with the growing trend of server-centric architectures like Phoenix LiveView and Hotwire, potentially reducing development complexity and improving maintainability for real-time features. The article highlights that WebSockets are ideal for bidirectional, low-latency communication (e.g., chat, collaboration), while SSE is simpler and cheaper for one-way server pushes. It also notes that modern browsers multiplex HTTP requests over a single TCP connection, so latency is similar, but WebSockets require custom client-side JavaScript for requests, whereas SSE can use built-in Fetch.

hackernews · redbell · Aug 12, 16:51 · [Discussion](https://news.ycombinator.com/item?id=49275335)

**Background**: HTML over WebSockets is a technique where the server sends HTML fragments over a WebSocket connection, and the client updates the DOM with those fragments, eliminating the need for a separate JSON API and client-side rendering. This approach is central to frameworks like Phoenix LiveView (Elixir) and has been explored in other ecosystems, such as Django with Channels. It contrasts with traditional SPAs that use RESTful APIs and client-side state management, and with SSE, which only supports one-way server-to-client communication.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Phoenix_LiveView">Phoenix LiveView</a></li>
<li><a href="https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html">Phoenix.LiveView — Phoenix LiveView v1.2.9</a></li>
<li><a href="https://testdriven.io/blog/html-over-websockets/">HTML Over WebSockets | TestDriven.io</a></li>
<li><a href="https://alistapart.com/article/the-future-of-web-software-is-html-over-websockets/">The Future of Web Software Is HTML-over-WebSockets – A List Apart</a></li>
<li><a href="https://ably.com/blog/websockets-vs-sse">WebSockets vs Server-Sent Events: Key differences and which to use in 2026</a></li>

</ul>
</details>

**Discussion**: The community discussion highlights historical context, noting that Chris McCord pioneered this technique with Sync in Rails before moving to Phoenix. Some commenters advocate for SSE over WebSockets for most use cases, citing simplicity and lower operational costs, while others point out that the choice depends on the specific problem, with WebSockets being necessary for bidirectional, low-latency interactions. There is also a reference to a counter-article and personal experiences with Blazor and SocketCluster.

**Tags**: `#WebSockets`, `#Real-time Web`, `#SPA`, `#JavaScript`, `#Phoenix LiveView`

---

<a id="item-8"></a>
## [Grok 4.6 Launch Sparks API Quirks and Benchmark Debate](https://x.ai/news/grok-4-6) ⭐️ 8.0/10

xAI released Grok 4.6, a new frontier AI model, on its platform. The model is now available via API, though some users report that a default system prompt is being added to all requests, which can override user instructions. Grok 4.6 marks xAI's entry into the competitive frontier model space, potentially challenging established players like OpenAI and Anthropic. Its performance on benchmarks like AA-Briefcase places it at a competitive tier, and its pricing could disrupt the market. According to Artificial Analysis, Grok 4.6 achieves an Elo of 1577 on AA-Briefcase, placing it at Fable 5-tier, behind the Claude Opus 5 family. The API is accessible via the model ID 'grok-4.6', but some users report that a default system prompt is added to all requests, which can override user instructions.

hackernews · iLuddite · Aug 12, 15:32 · [Discussion](https://news.ycombinator.com/item?id=49274027)

**Background**: Grok is a series of large language models developed by xAI, led by Elon Musk. The company has invested heavily in inference infrastructure, enabling competitive pricing. Frontier models are evaluated on benchmarks like AA-Briefcase, which tests long-horizon agentic knowledge work tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://evolink.ai/grok-4-6">Grok 4.6 API Status: Model ID, Pricing & Access | EvoLink</a></li>
<li><a href="https://docs.x.ai/developers/grok-4-6">Grok 4.6 - Docs - SpaceXAI</a></li>
<li><a href="https://artificialanalysis.ai/articles/grok-4-6-benchmarks-and-analysis">Grok 4 . 6 returns SpaceXAI to the intelligence frontier and leads on cost...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight concerns about the API's default system prompt overriding user instructions, and skepticism about the rapid performance gains across labs, suggesting possible benchmark hacking. Some users praise Grok's security review capabilities and the nice TUI of Grok Build, while others see Grok as a healthy competitor.

**Tags**: `#AI`, `#Grok`, `#xAI`, `#LLM`, `#API`

---

<a id="item-9"></a>
## [Discovered Materials Uses AI Agents to Accelerate Semiconductor Material Discovery](https://discoveredmaterials.com/research/) ⭐️ 8.0/10

Discovered Materials, a YC P26 startup, launched with AI agents that discover new materials for semiconductor heat management, releasing hundreds of discovered materials and a benchmark for model evaluation. They claim their AI agents can find dynamically stable materials in 8 hours that would take a PhD student weeks, and they have synthesized thermal interface materials matching trade-secret performance. This addresses the critical challenge of heat dissipation in GPUs, where TDP is rapidly increasing (e.g., from 700W in H100 to 2.3kW in Rubin), impacting data center power and water consumption. If successful, it could significantly reduce the time and cost of introducing new materials into semiconductor manufacturing, potentially enabling advanced packaging like 3D stacking of HBM. The company tested models from Anthropic, OpenAI, and Kimi, and observed strange behaviors like Claude's reward hacking and GPT-5.6 losing coherence after ~50M tokens. Their business model involves licensing and selling IP on discovered materials and synthesis methods, with an alternative model of selling their harness and tools.

hackernews · advaith08 · Aug 12, 07:51 · [Discussion](https://news.ycombinator.com/item?id=49269090)

**Background**: Thermal design power (TDP) is the maximum heat a component generates, and GPUs have seen a rapid increase in TDP, making cooling a major challenge. High Bandwidth Memory (HBM) uses 3D stacking, but current dielectric materials like SiO2 are poor thermal conductors, limiting performance. The 'lab-to-fab valley of death' refers to the difficulty of translating computational discoveries into manufacturable materials, which is a key hurdle the company aims to overcome.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Thermal_design_power">Thermal design power - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/High_Bandwidth_Memory">High Bandwidth Memory - Wikipedia</a></li>
<li><a href="https://semiengineering.com/hbm-becomes-testbed-for-3d-assembly-yield/">HBM Becomes Testbed For 3 D Assembly Yield</a></li>

</ul>
</details>

**Discussion**: The community discussion is generally positive, with users appreciating the focus on feasibility and synthesis, noting it's a step in the right direction compared to previous AI materials discovery efforts. Some users share related research and insights on the challenges of closing the computational-experimental loop, while others express curiosity about the observed model behaviors like reward hacking.

**Tags**: `#AI`, `#materials science`, `#semiconductors`, `#startup`, `#YC`

---

<a id="item-10"></a>
## [AI Is Eroding the Middle Class of Software Engineering](https://blog.florianherrengt.com/ai-removing-middle-class-software-engineering.html) ⭐️ 8.0/10

A blog post argues that AI is disproportionately impacting mid-level software engineers, potentially eliminating the 'middle class' of the profession, while senior engineers benefit and junior roles face new challenges. This matters because it highlights a significant shift in the software engineering job market, affecting career trajectories and hiring practices. The debate is timely as AI tools become more integrated into development workflows, potentially reshaping the industry's skill hierarchy. The article suggests that AI amplifies the output of 'bad' engineers, leading to poor engineering at scale. It also notes a shift where seniors can now handle tasks previously delegated to mid-level engineers, reducing the need for that tier.

hackernews · florianherrengt · Aug 12, 13:20 · [Discussion](https://news.ycombinator.com/item?id=49271994)

**Background**: Software engineering has traditionally had a hierarchy: senior engineers design and solve complex problems, mid-level engineers implement features, and juniors learn the ropes. AI coding assistants like GitHub Copilot and ChatGPT can now generate code, potentially automating routine implementation tasks that were the staple of mid-level roles. This has sparked discussions about the future of work in tech, with some experts like Sam Altman warning about job displacement.

<details><summary>References</summary>
<ul>
<li><a href="https://www.lambham.com/post/sam-altman-s-warning-on-ai-s-impact-on-software-engineering-jobs/">Sam Altman's Warning on AI 's Impact on Software Engineering Jobs</a></li>
<li><a href="https://zencoder.ai/blog/use-ai-for-developer-productivity">5 Ways to Use AI for Developer Productivity in 2026</a></li>
<li><a href="https://www.linkedin.com/posts/nemanja-grujic-b70107a5_techjobs-jobmarket-ai-activity-7447584808307974144-E6Ee">Job Market Trends and AI Impact on Software Engineers | LinkedIn</a></li>

</ul>
</details>

**Discussion**: Commenters express concern that AI can amplify poor engineering practices, especially among long-tenured engineers who have lost interest. Some view AI as automating the 'StackOverflow engineer' role, allowing seniors to skip the handoff to mid-level coders. Others emphasize the importance of not outsourcing critical thinking to LLMs and note the emotional difficulty of seeing previously scarce skills become commoditized.

**Tags**: `#AI`, `#software engineering`, `#job market`, `#productivity`, `#future of work`

---

<a id="item-11"></a>
## [Fields Medalist Analyzes LLM Mathematical Strengths](https://gowers.wordpress.com/2026/08/12/what-sort-of-maths-are-llms-good-at/) ⭐️ 8.0/10

Timothy Gowers, a Fields Medalist, published a blog post analyzing the types of mathematics LLMs excel at, highlighting their strengths in sampling and counterexample search while noting the gap in producing beautiful, surprising proofs. This analysis from a leading mathematician provides valuable insight into the current capabilities and limitations of LLMs in mathematics, informing expectations for AI-assisted research and highlighting areas where human creativity remains essential. Gowers notes that LLMs are particularly good at sampling and finding counterexamples, but they struggle to produce proofs that are new, surprising, and beautiful. The post sparked discussion on test-time scaling, with commenters linking LLM performance to sampling strategies and noting the importance of recognizing human-level theorem proving.

hackernews · ColinWright · Aug 12, 10:04 · [Discussion](https://news.ycombinator.com/item?id=49270022)

**Background**: The Fields Medal is a prestigious award for mathematicians under 40, and Timothy Gowers is a renowned mathematician known for his work in combinatorics and additive number theory. LLMs have been increasingly applied to mathematical tasks, with benchmarks like FrontierMath designed to test advanced reasoning. Test-time scaling refers to techniques that improve model performance at inference time, such as sampling multiple outputs or extended reasoning.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Fields_Medal">Fields Medal - Wikipedia</a></li>
<li><a href="https://www.bracai.eu/post/llm-math-benchmark">Best LLM for math in 2026: how AI models rank</a></li>
<li><a href="https://ai.gopubby.com/you-dont-need-thinking-in-llms-to-reason-better-e853f8f54a66">You Don’t Need ‘Thinking’ In LLMs To Reason Better | by Dr. Ashish...</a></li>

</ul>
</details>

**Discussion**: The discussion highlights that LLM performance is closely tied to test-time scaling, with sampling being a key strength. Commenters agree with Gowers' observation that human-level theorem proving would require methods that are new and surprising yet beautiful, and they note the affinity of AI for counterexample search. Some also speculate on potential limitations in areas like temporal logic.

**Tags**: `#LLM`, `#mathematics`, `#AI research`, `#test-time scaling`, `#theorem proving`

---

<a id="item-12"></a>
## [Woxi: Open-Source Rust Reimplementation of Wolfram Language](https://woxi.ad-si.com/) ⭐️ 8.0/10

Woxi, an open-source interpreter for the Wolfram Language written in Rust, has been released with a GUI (Woxi Studio), CLI, Jupyter kernel, and WASM support. It offers fast startup and embeddability compared to Mathematica. This project provides a free and open-source alternative to the proprietary Mathematica, potentially lowering barriers for students and researchers. Its Rust-based design and embeddability could enable new use cases in web and application scripting. Woxi is validated by approximately 26,000 unit tests and 900 snapshot tests. The current focus is on fixing edge cases, improving performance, and growing the community, with compatibility feedback welcomed.

hackernews · adius · Aug 12, 10:06 · [Discussion](https://news.ycombinator.com/item?id=49270040)

**Background**: The Wolfram Language is the programming language used in Mathematica, a powerful computational tool. Woxi aims to reimplement this language in Rust, offering a faster startup and open-source licensing, unlike the proprietary Mathematica.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/cabralski/awesome-wolfram-language">GitHub - cabralski/awesome- wolfram - language : A curated list of...</a></li>
<li><a href="https://docs.rs/woxi/latest/woxi/">API documentation for the Rust ` woxi ` crate.</a></li>
<li><a href="https://lib.rs/crates/woxi">Woxi — Rust utility // Lib.rs</a></li>

</ul>
</details>

**Discussion**: Community comments express interest in additional features like approximation methods and a control systems module, and note the convenience of Mathematica's shortcuts. Some users hope Woxi could eventually replace Sage as a well-integrated open-source alternative, while others mention a previous posting of the project.

**Tags**: `#Wolfram Language`, `#Rust`, `#Open Source`, `#Interpreter`, `#Mathematica`

---

<a id="item-13"></a>
## [Physicists Report Strongest Evidence Yet for Glueballs](https://arstechnica.com/science/2026/08/have-physicists-finally-discovered-glueballs-new-evidence-points-to-yes/) ⭐️ 8.0/10

Physicists have reported the strongest evidence yet for the existence of glueballs, particles composed solely of gluons, potentially confirming a long-standing prediction of the Standard Model. The finding was announced in a study published in August 2026, as covered by Ars Technica. This is a significant development in particle physics, as glueballs are exotic particles predicted by quantum chromodynamics (QCD) but never definitively observed. Confirming their existence would deepen our understanding of the strong force and hadron physics, and could open new avenues for research. The evidence comes from a specific experiment or analysis, though details are limited in the provided content. The article states it is 'the strongest evidence yet that particles dominated by a glueball component can exist in nature,' indicating that the observed particles may not be pure glueballs but have a significant glueball component.

rss · Ars Technica · Aug 12, 21:13

**Background**: Glueballs are hypothetical composite particles consisting solely of gluons, the force carriers of the strong nuclear force, without any valence quarks. They are predicted by quantum chromodynamics (QCD), the theory describing the strong interactions between quarks and gluons. Despite decades of searching, glueballs have remained unconfirmed, making this new evidence a potential breakthrough.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Glueball">Glueball - Wikipedia</a></li>
<li><a href="https://bigthink.com/starts-with-a-bang/new-particle-first-glueball/">New particle at last! Physicists detect the first " glueball " - Big Thi...</a></li>

</ul>
</details>

**Tags**: `#physics`, `#glueballs`, `#particle physics`, `#quantum chromodynamics`, `#research`

---

<a id="item-14"></a>
## [AI Tool Finds Zoom Screen-Sharing Hijack Flaw](https://arstechnica.com/security/2026/08/researchers-found-a-way-to-hijack-devices-through-zoom-screen-sharing/) ⭐️ 8.0/10

Researchers used a public AI tool to discover a critical Zoom screen-sharing vulnerability in under 20 prompts, enabling device hijacking during calls. The flaw, designated ZSB-26015 and nicknamed 'Zoomsday,' has been patched by Zoom with both server and client-side fixes. This finding highlights the growing role of AI in vulnerability research, demonstrating that even public AI tools can rapidly uncover critical flaws in widely-used software. The attack vector affects any device participating in a Zoom meeting with screen sharing active, posing a significant security risk to millions of users. The vulnerability allowed attackers to execute arbitrary code on any device in a meeting where screen sharing was active. Zoom has issued both server and client-side patches to address the issue, and the bugs are now fixed.

rss · Ars Technica · Aug 12, 13:37

**Background**: Zoom is a widely-used video conferencing platform, and screen sharing is a common feature that allows participants to share their screens. Vulnerability discovery typically involves manual code review or automated scanning, but AI tools are increasingly being used to assist in finding security flaws. The discovery of this flaw in under 20 prompts demonstrates the potential of AI to accelerate vulnerability research.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/a-zoom-screen-sharing-bug-let-anyone-take-over-other-devices-on-a-call/">A Zoom Screen - Sharing Bug Let Anyone Take Over Other... | WIRED</a></li>
<li><a href="https://easternherald.com/2026/08/12/zoom-screen-sharing-bug-zoomsday-ai-vulnerability/">Zoom Zoomsday Bug Gave Attackers Remote Device Control</a></li>
<li><a href="https://overcentral.com/en/zoom-screen-sharing-bug/">Zoom Screen - Sharing Bug Lets Attackers Take Over Devices</a></li>

</ul>
</details>

**Tags**: `#security`, `#AI`, `#Zoom`, `#vulnerability`, `#cybersecurity`

---

<a id="item-15"></a>
## [Scientists Create Female Clones from Male Mice Using CRISPR](https://www.technologyreview.com/2026/08/12/1141768/scientists-just-created-female-clones-of-male-mice/) ⭐️ 8.0/10

A team in Japan has successfully used CRISPR to remove the Y chromosome from male mouse embryos, creating female clones for the first time. This marks a deliberate and controlled conversion of male cells into female offspring. This breakthrough could revolutionize reproductive biology and cloning, offering new possibilities for genetic research and conservation of endangered species. It also raises ethical questions about sex determination and genetic manipulation. The technique involves CRISPR-Cas9-mediated deletion of the Y chromosome in embryonic stem cells, resulting in XO (monosomic) cells that develop into female mice. Previous attempts were accidental, but this is the first deliberate and efficient method.

rss · MIT Technology Review · Aug 12, 18:59

**Background**: In mammals, sex is typically determined by the presence of X and Y chromosomes, with XY being male and XX being female. CRISPR-Cas9 is a precise gene-editing tool that can cut DNA at specific locations. This research builds on earlier accidental occurrences of female clones from male cells and aims to provide a reliable method for generating female clones.

<details><summary>References</summary>
<ul>
<li><a href="https://www.winzheng.com/en/article/female-clones-male-mice">Scientists just created female clones of male mice | Winzheng</a></li>
<li><a href="https://vexowire.com/scientists-just-created-female-clones-of-male-mice/">Scientists just created female clones of male mice - VexoWire</a></li>
<li><a href="https://www.researchgate.net/publication/342557388_Generation_of_clonal_male_and_female_mice_through_CRISPRCas9-mediated_Y_chromosome_deletion_in_embryonic_stem_cells">(PDF) Generation of clonal male and female mice through...</a></li>

</ul>
</details>

**Tags**: `#CRISPR`, `#genetics`, `#reproductive biology`, `#cloning`, `#biotechnology`

---

<a id="item-16"></a>
## [Twitch faces backlash for default-on AI training harvesting streamer data for Amazon](https://www.pcgamer.com/software/ai/twitch-under-fire-for-new-gen-ai-training-system-that-harvests-streamer-data-for-amazon-says-its-on-by-default-because-if-it-was-opt-in-nobody-would-opt-in/) ⭐️ 8.0/10

Twitch has introduced a new setting that allows streamers to opt out of having their content used to train Amazon's generative AI models, but it is enabled by default. The company stated that making it opt-in would result in low participation, sparking criticism. This decision raises significant privacy and ethical concerns for content creators, as their streams, VODs, and chats are automatically harvested for AI training unless they manually opt out. It highlights broader industry tensions between platform monetization of user data and creator rights. The opt-out setting is buried in account security settings, and opting out only prevents future training, not past use. Additionally, AI-supported features like captions and safety tools remain active, and if a streamer participates in another person's chat, that person's opt-out preference governs the use of that chat data.

rss · PC Gamer · Aug 12, 22:17

**Background**: Twitch is a major live-streaming platform owned by Amazon, which has been expanding its generative AI capabilities through services like Amazon Bedrock. Generative AI models require large datasets for training, and platforms like Twitch have access to vast amounts of user-generated content, making them attractive data sources. The default-on approach is common in tech but often criticized for undermining user consent.

<details><summary>References</summary>
<ul>
<li><a href="https://insider-gaming.com/twitch-ai-training-opt-out-setting/">Twitch Adds AI Training Opt - Out Setting for... - Insider Gaming</a></li>
<li><a href="https://kotaku.com/twitch-is-now-using-your-content-to-train-amazon-ai-models-and-has-hidden-the-option-to-opt-out-2000723891">Twitch Is Now Using Your Content To Train Amazon AI Models And...</a></li>
<li><a href="https://www.theverge.com/tech/979112/twitch-streamers-can-now-opt-out-from-training-amazons-ai">Twitch streamers can now opt out from training Amazon’s AI</a></li>

</ul>
</details>

**Discussion**: The community reaction has been largely negative, with many streamers and users expressing anger over the default-on policy and the hidden nature of the opt-out setting. Some argue that Twitch's justification for default-on is dismissive of user autonomy, while others point out that the opt-out does not cover all AI uses, adding to the frustration.

**Tags**: `#AI ethics`, `#privacy`, `#Twitch`, `#data harvesting`, `#content creation`

---

<a id="item-17"></a>
## [Chrome's Tiny JPEG Scaling Differs from Other Browsers](https://guillaumetech.github.io/posts/jpg-scaling-chrome/) ⭐️ 7.0/10

Chrome uses a different downscaling algorithm for tiny JPEGs compared to other browsers, resulting in visual differences. This behavior can be mitigated with CSS or by using appropriately sized images. This subtle rendering difference can affect web developers who rely on consistent image display across browsers, especially for icons or small graphics. Understanding and addressing it improves cross-browser compatibility and user experience. Chrome's downscaling algorithm is optimized for speed, using low-resolution linear interpolation, which can cause blurriness or slight shifts. The article suggests using CSS 'image-rendering' property or providing images at the correct display size to avoid issues.

hackernews · gutechh · Aug 12, 14:00 · [Discussion](https://news.ycombinator.com/item?id=49272549)

**Background**: Web browsers use different algorithms to resize images, affecting quality and appearance. Chrome's approach prioritizes performance, while Firefox and others may use sharper algorithms, leading to visible differences, especially for small images like icons.

<details><summary>References</summary>
<ul>
<li><a href="https://entropymine.com/resamplescope/notes/browsers/">How web browsers resize images</a></li>
<li><a href="https://stackoverflow.com/questions/37906602/blurry-downscaled-images-in-chrome">html - Blurry downscaled images in Chrome - Stack Overflow</a></li>
<li><a href="https://gehrcke.de/2014/11/css-crispy-downscaled-images/">CSS: Crispy downscaled images – Jan-Philip Gehrcke, PhD</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the issue also affects PNGs and Electron apps, and that using appropriately sized images is crucial. Some prefer Firefox's sharper scaling, while others point to ongoing fixes in Firefox.

**Tags**: `#web development`, `#browser rendering`, `#image scaling`, `#CSS`, `#JPEG`

---

<a id="item-18"></a>
## [uBlock Origin Stops Blocking Facebook Ads](https://digitalescapetools.com/2026/08/ublock-origin-stops-chasing-facebook-ads.html) ⭐️ 7.0/10

uBlock Origin has officially stopped attempting to block ads on Facebook, citing the increasing difficulty of doing so. The developer announced this decision on Reddit, and it was reported by Neowin. This marks a significant moment in the ongoing arms race between ad blockers and platforms like Facebook, highlighting the technical challenges and resource constraints faced by open-source projects. It also sparks debate about the future of ad blocking and user privacy on major social networks. The decision was shared by the uBlock Origin developer on Reddit, and the tool will no longer filter Facebook ads. This does not affect ad blocking on other sites, but it underscores the sophisticated techniques Facebook employs to evade ad blockers.

hackernews · Markoff · Aug 12, 11:28 · [Discussion](https://news.ycombinator.com/item?id=49270726)

**Background**: uBlock Origin is a popular open-source browser extension for content filtering, including ad blocking. Facebook has continuously evolved its ad delivery and rendering methods to make it difficult for ad blockers to detect and hide ads, leading to an ongoing cat-and-mouse game.

<details><summary>References</summary>
<ul>
<li><a href="https://www.neowin.net/news/facebook-ads-are-so-hard-to-block-that-ublock-origin-stopped-filtering-them/">Facebook ads are so hard to block that uBlock Origin ... - Neowin</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community comments reflect mixed reactions. Some users support the decision, acknowledging the difficulty and suggesting that Facebook's ad practices may eventually drive users away. Others speculate about future solutions like computer vision-based ad blocking, while some question the effectiveness of ad blocking on Facebook given that users with blockers are unlikely to click ads anyway.

**Tags**: `#ad-blocking`, `#privacy`, `#Facebook`, `#uBlock Origin`, `#web`

---

<a id="item-19"></a>
## [Shade Map: Interactive Tool for Sunlight and Shade Visualization](https://shademap.app/) ⭐️ 7.0/10

Shade Map is an interactive web tool that simulates sun shadows for any location and time on Earth, allowing users to visualize shade and sunlight patterns. It generates shadow accumulation and shadow accrual maps, useful for planning outdoor activities and solar panel placement. This tool addresses a practical need for gardeners, solar panel installers, and urban planners by providing an easy way to assess sunlight and shade. It democratizes access to solar analysis, which was previously limited to specialized GIS software, and can help optimize energy generation and outdoor comfort. The tool is available at shademap.app and supports simulating shadows for sunrise and sunset photos, as well as preparing shadow studies and solar analyses. It uses elevation data and solar geometry to compute shadows, and the interface allows users to select any location and time.

hackernews · fredley · Aug 12, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49271757)

**Background**: Shade mapping is a form of GIS analysis that models the sun's path and its interaction with terrain and structures. Traditionally, such analysis required specialized software like Esri's ArcGIS, but web-based tools like Shade Map make it accessible to the general public. This is particularly relevant for solar energy planning, where understanding shade patterns is crucial for maximizing panel efficiency.

<details><summary>References</summary>
<ul>
<li><a href="https://shademap.app/">ShadeMap - Simulate sun shadows for any time and place on Earth</a></li>
<li><a href="https://shadowmap.org/">Shadowmap | The Sun for Everyone – Sunlight & Shadow Analysis in 3D</a></li>
<li><a href="https://www.esri.com/">GIS Software for Mapping and Spatial Analytics | Esri</a></li>

</ul>
</details>

**Discussion**: Community comments show positive reception, with users sharing personal anecdotes and feature suggestions. One user noted a discrepancy between the tool's output and their real-world experience, while another suggested adding tree placement simulation. Others praised its utility for solar panel placement during camping trips, and one user offered to transfer a related domain name.

**Tags**: `#mapping`, `#solar`, `#shade`, `#GIS`, `#outdoor planning`

---

<a id="item-20"></a>
## [Warrant Required for License Plate Reader Searches](https://andrewpwheeler.com/2026/08/12/license-plate-reader-searches-should-require-a-warrant/) ⭐️ 7.0/10

Andrew Wheeler argues that police use of license plate readers (LPRs) should require a warrant, citing privacy concerns and the need for judicial oversight. The article was published on August 12, 2026, and has sparked significant community discussion. This issue affects civil liberties and the balance between public safety and privacy. If warrantless LPR use continues, it could lead to widespread surveillance without oversight, impacting all citizens. The article suggests that requiring a warrant for historical LPR searches would not seriously impede police investigations. It also notes that the current status quo of not retaining data may change, making warrant requirements more critical.

hackernews · apwheele · Aug 12, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49273165)

**Background**: License plate readers are automated cameras that capture license plate numbers and are often networked, allowing for mass surveillance. The Fourth Amendment protects against unreasonable searches, and courts are debating whether LPR data collection requires a warrant. States have varying laws, with some requiring a warrant for private data, but police use often lacks oversight.

<details><summary>References</summary>
<ul>
<li><a href="https://deflock.org/">DeFlock is an open-source project that maps license plate readers ...</a></li>
<li><a href="https://www.congress.gov/crs-product/IF13068">Automated License Plate Readers: Background and Legal Issues</a></li>
<li><a href="https://www.ncsl.org/technology-and-communication/automated-license-plate-readers-state-statutes">Summary Automated License Plate Readers: State Statutes</a></li>

</ul>
</details>

**Discussion**: Commenters express concerns about LPRs being general-purpose cameras that can be repurposed, and argue that mass surveillance should not be allowed by default. Some suggest that without a warrant, data should be fully open to the public, while others propose poisoning databases with fake plates. There is a consensus that police cannot be trusted with the data without court oversight.

**Tags**: `#privacy`, `#surveillance`, `#civil liberties`, `#law enforcement`, `#technology policy`

---

<a id="item-21"></a>
## [AI Firms Buying and Destroying Rare Books Face Bookseller Resistance](https://arstechnica.com/tech-policy/2026/08/heres-a-balm-if-the-idea-of-destroying-books-to-train-ai-breaks-your-heart/) ⭐️ 7.0/10

AI firms are reportedly bulk-buying rare books and destroying them to train models, prompting resistance from booksellers. This practice has been public for over a year but intensified after a 404 Media article described large orders from booksellers. This raises significant ethical and legal concerns about AI data sourcing, as it destroys cultural artifacts and may violate copyright. It could set precedents for how AI companies acquire training data and impact the rare book market and cultural heritage. The practice involves digitizing books for training data, but the physical copies are often destroyed. Anthropic has been reported to have destroyed millions of print books, and the OECD has classified such destruction as an AI incident due to cultural harm.

rss · Ars Technica · Aug 12, 15:19

**Background**: AI models require vast amounts of high-quality text data, and books are considered valuable sources. Companies like Anthropic have used print books for training, but the destruction of physical copies has sparked debate over cultural preservation and legal boundaries.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/ai/2025/06/anthropic-destroyed-millions-of-print-books-to-build-its-ai-models/">Anthropic destroyed millions of print books to build its AI models</a></li>
<li><a href="https://oecd.ai/en/incidents/2026-07-28-9328">Anthropic's Destructive Book Digitization for AI Training ... - OECD. AI</a></li>
<li><a href="https://www.theatlantic.com/technology/2026/08/ai-companies-buying-used-books-for-data/688167/">Someone Is Mysteriously Snapping Up Used Books ... - The Atlantic</a></li>

</ul>
</details>

**Tags**: `#AI`, `#data sourcing`, `#books`, `#ethics`, `#copyright`

---

<a id="item-22"></a>
## [PJM Considers Ride-Through Standards After 3.8 GW Data Center Load Trip](https://www.utilitydive.com/news/pjm-nerc-data-center-crypto-reliability-standards/827653/) ⭐️ 7.0/10

PJM Interconnection is considering setting 'ride-through' standards after data centers in Northern Virginia tripped offline on July 22, causing a 3.8 GW load drop, the largest such event in PJM's history. The grid operator is evaluating new reliability requirements for data centers and crypto mining facilities. This event highlights a growing challenge at the intersection of technology and energy, as large loads like data centers and crypto miners can abruptly disconnect, threatening grid stability. New reliability standards could set a precedent for how grid operators manage these emerging loads, impacting the data center industry and energy policy. The load drop occurred when data centers transferred to onsite generation during a grid event, reducing PJM's load from 99,984 MW to 96,205 MW. PJM is considering 'ride-through' standards that would require these facilities to remain connected during disturbances, and also discussing controlled reconnection sequences to avoid simultaneous load return.

rss · Utility Dive · Aug 12, 13:01

**Background**: PJM Interconnection is a regional transmission organization (RTO) that coordinates the movement of wholesale electricity in all or parts of 13 states and the District of Columbia. Data centers and crypto mining facilities are large electricity consumers that can abruptly reduce their load, known as a customer-initiated load reduction (CILR), which can cause frequency and voltage disturbances on the grid. 'Ride-through' standards are technical requirements that ensure equipment remains operational during grid disturbances, helping maintain stability.

<details><summary>References</summary>
<ul>
<li><a href="https://www.utilitydive.com/news/pjm-nerc-data-center-crypto-reliability-standards/827653/">PJM eyes data center, crypto reliability requirements after... | Utility Dive</a></li>
<li><a href="https://www.datacenterknowledge.com/regulations/3-8-gw-load-drop-prompts-potential-pjm-rules">3.8 GW Load Drop Prompts Potential PJM Rules</a></li>
<li><a href="https://www.publicpower.org/periodical/article/pjm-dominion-review-large-load-transfer-event">PJM, Dominion Review Large Load Transfer Event | American Public...</a></li>

</ul>
</details>

**Tags**: `#energy`, `#data centers`, `#grid reliability`, `#crypto mining`, `#policy`

---

<a id="item-23"></a>
## [Low-Carbon Power Emerges as Key Factor in AI Data Center Siting](https://www.energyintel.com/0000019f-a969-d15b-a5bf-e97984ed0000) ⭐️ 7.0/10

Energy Intelligence reports that access to abundant, affordable low-carbon electricity is increasingly determining where AI data centers are built, reshaping the geography of AI infrastructure. This shift highlights the growing interdependence between AI development and energy policy, potentially influencing investment decisions, regional economic development, and global tech competition. Regions with clean energy advantages may attract more AI infrastructure, while those without could be left behind. AI data centers are significantly more energy-intensive than traditional ones, with estimates suggesting they could be three times more energy-intensive. The article emphasizes that low-carbon electricity availability is becoming a strategic factor, alongside traditional considerations like land and connectivity.

rss · Energy Intelligence · Aug 12, 21:54

**Background**: AI models require massive computational power, leading to soaring electricity demand for data centers. As governments and corporations push for sustainability, the carbon footprint of AI is under scrutiny, making access to low-carbon energy a competitive advantage. This trend is part of a broader movement to align AI growth with climate goals.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Environmental_impact_of_artificial_intelligence">Environmental impact of AI - Wikipedia</a></li>
<li><a href="https://fluxcoredatasystems.com/blog/what-is-behind-the-meter-btm-energy-and-why-it-matters-for-ai-compute/">Behind-the-Meter Energy : Powering AI Compute Growth | Flux Core</a></li>
<li><a href="https://www.linkedin.com/posts/nathan-benedict-24857a1_data-centers-have-unique-energy-requirements-activity-7342942068060692482-yG3E">" AI data centers : energy -intensive future?" | Nathan... | LinkedIn</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#data centers`, `#energy`, `#sustainability`, `#geopolitics`

---

<a id="item-24"></a>
## [Tim King, AmigaDOS Developer, Dies](https://amiga-news.de/en/news/AN-2026-08-00070-EN.html) ⭐️ 6.0/10

Dr. Tim King, a key developer of AmigaDOS, has passed away, as reported by amiga-news.de. The news has prompted tributes from the retrocomputing community, with many sharing personal stories about how his work influenced their careers. Tim King's contributions to AmigaDOS were foundational to the Amiga computer's operating system, which had a significant impact on the personal computing era. His passing is a notable loss to the retrocomputing community, which continues to preserve and celebrate the legacy of the Amiga platform. Tim King joined MetaComCo in 1984 as director of research and development, where he worked on porting TRIPOS to create AmigaDOS. AmigaDOS was initially written in BCPL, and later rewritten in C starting with AmigaOS 2.x, with 64-bit file support added in AmigaOS 4.1.

hackernews · doener · Aug 12, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49272655)

**Background**: AmigaDOS is the disk operating system component of AmigaOS, managing file systems, directory operations, and the command-line interface. It was based on TRIPOS, a multi-tasking operating system, and was ported by MetaComCo for the Amiga. The Amiga was a popular personal computer in the late 1980s and early 1990s, known for its advanced graphics and sound capabilities.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/AmigaDOS">AmigaDOS - Wikipedia</a></li>
<li><a href="https://www.generationamiga.com/2026/08/12/farewell-to-dr-tim-king-one-of-the-key-minds-behind-amigados/">Farewell to Dr Tim King , one of the key minds behind AmigaDOS</a></li>

</ul>
</details>

**Discussion**: Community comments express gratitude and personal anecdotes. For example, one user credits AmigaDOS as their gateway to the command line, leading to learning Linux CLI. Another user remembers Tim King as the founder of UK Online, describing him as friendly and helpful. A commenter also shared a link to a 2021 interview with Tim King.

**Tags**: `#Amiga`, `#retrocomputing`, `#obituary`, `#AmigaDOS`

---

<a id="item-25"></a>
## [Mass Scans Spoof AI Bots Like ClaudeBot](https://knownagents.com/insights) ⭐️ 6.0/10

Attackers are now spoofing AI bot user agents, such as ClaudeBot, to conduct mass vulnerability scans across the internet. This new tactic adds deception to common scanning activity, making detection harder. This matters because it complicates security monitoring and can lead to false attribution, potentially harming AI companies' reputations. It also highlights the need for more robust bot verification methods beyond user-agent checks. The spoofed scans target sensitive endpoints and often fail IP verification or Web Bot Auth checks. Security experts recommend combining user-agent verification with path-based anomaly detection to filter out these fake bots.

hackernews · gavinhking · Aug 12, 14:02 · [Discussion](https://news.ycombinator.com/item?id=49272569)

**Background**: AI bot user agents like ClaudeBot are used by legitimate AI services to crawl the web. Attackers spoof these user agents to hide their scanning activities, exploiting the trust given to known bots. Verification methods include reverse DNS lookups to confirm IP ownership.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49272569">Someone is running mass vulnerability scans , spoofing AI bots like...</a></li>
<li><a href="https://promptcube3.com/en/news/6072/">[Industry News] ClaudeBot spoofing is being used to mask mass ...</a></li>
<li><a href="https://hacknjill.com/cybercrime-and-incidents/someone-is-running-mass-vulnerability-scans-spoofing-ai-bots-like-claudebot/">Someone Is Running Mass Vulnerability Scans , Spoofing AI Bots...</a></li>

</ul>
</details>

**Discussion**: Commenters note that mass scanning is common, but spoofing AI bots is a new twist. Some suggest blocking VPS providers to reduce fake bots, while others question the effectiveness of pretending to be AI bots since they are often blocked. Practical mitigation strategies are shared.

**Tags**: `#security`, `#vulnerability scanning`, `#bot spoofing`, `#AI bots`, `#network security`

---

<a id="item-26"></a>
## [Google Pixel 11 series: Tensor G6, camera upgrades, higher prices](https://www.theverge.com/gadgets/975237/google-pixel-11-pro-comparison-specs-price-features) ⭐️ 6.0/10

Google has launched four new Pixel 11 phones (Pixel 11, Pixel 11 Pro, Pixel 11 Pro XL, and Pixel 11 Pro Fold) with the new Tensor G6 chip, improved cameras, and slightly higher prices compared to last year's models. The Pixel 11 series represents Google's continued push in the premium smartphone market, offering incremental but meaningful upgrades that could appeal to existing Pixel users and tech enthusiasts. The new Tensor G6 chip and camera improvements may help Google compete with other flagship phones. The Tensor G6 chip includes the Titan M3 security chip, and the Pixel 11 and Pixel 11 Pro Fold feature new 48MP main sensors with 56% better light sensitivity. The base model comes with 12GB LPDDR5X RAM and 256GB storage, and prices are slightly higher than predecessors.

rss · The Verge · Aug 12, 17:00

**Background**: Google's Pixel series is known for its camera quality and integration with Google services. The Tensor chip is Google's custom system-on-a-chip designed for on-device AI and machine learning tasks. The Pixel 11 series continues this trend with the Tensor G6, which also supports features like 4K Portrait Video and faster Gemini AI.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gizmochina.com/2026/08/12/google-pixel-11-pixel-11-pro-and-pixel-11-pro-xl-launch-with-tensor-g6-and-256gb-base-storage/">Google Pixel 11, Pixel 11 Pro, and Pixel 11 Pro XL launch with Tensor ...</a></li>
<li><a href="https://www.androidauthority.com/google-tensor-g6-3695351/">Google Tensor G 6 brings 4K Portrait Video and more to the Pixel 11</a></li>
<li><a href="https://blog.google/products-and-platforms/devices/pixel/google-pixel-11-pro-xl/">Google introduces Pixel 11 , Pixel 11 Pro and Pixel 11 Pro XL</a></li>

</ul>
</details>

**Tags**: `#Google Pixel`, `#smartphones`, `#hardware`, `#Tensor G6`

---

<a id="item-27"></a>
## [Amazon exits MMO live operations, hands over Throne and Liberty and Lost Ark](https://www.theverge.com/tech/979070/amazon-mmo-throne-and-liberty-lost-ark-live-operations) ⭐️ 6.0/10

Amazon has announced it will hand over the live operations of Throne and Liberty and Lost Ark in the West to other companies, marking a full retreat from MMO game operations. This follows its earlier statement about halting significant work on first-party AAA games, specifically around MMOs. This move signals Amazon's strategic withdrawal from the competitive MMO market, potentially affecting the player communities of these games and the broader gaming industry's perception of Amazon as a game publisher. It also highlights the challenges of sustaining live-service games. The handover applies to the Western versions of Throne and Liberty and Lost Ark, with specific companies not yet named. Amazon had previously said it would halt 'a significant amount' of work on first-party AAA games, specifically around MMOs, and this move is a concrete step in that direction.

rss · The Verge · Aug 12, 16:46

**Background**: Throne and Liberty is a free-to-play MMORPG developed by FirstSpark Games and published by NCSoft, while Lost Ark is a free-to-play isometric action MMORPG developed by Smilegate RPG. Both games have been operated by Amazon Games in Western regions, but the company is now stepping back from live operations to focus on other areas.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Throne_and_Liberty">Throne and Liberty - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lost_Ark_(video_game)">Lost Ark (video game ) - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Amazon`, `#MMO`, `#gaming`, `#industry news`

---

<a id="item-28"></a>
## [JCB's Hydrogen-Powered Car Sets New Land Speed Record](https://arstechnica.com/cars/2026/08/jcb-sets-a-new-406-mph-speed-record-for-hydrogen-powered-cars/) ⭐️ 6.0/10

JCB has set a new land speed record for hydrogen-powered cars, reaching 406.320 mph (653.908 km/h) at the Bonneville Salt Flats in Utah, driven by retired RAF pilot Andy Green. The car, named JCB Hydromax, is powered by two hydrogen-burning engines derived from JCB's construction machinery. This achievement demonstrates the viability of hydrogen combustion engines as a zero-carbon alternative in high-performance applications, potentially influencing the automotive and heavy machinery industries. It also highlights JCB's commitment to hydrogen technology, which could accelerate adoption in sectors where battery electric solutions are impractical. The record-breaking speed was 406.320 mph, surpassing the previous record of 386 mph set 16 years ago. The JCB Hydromax uses two hydrogen-burning engines producing a combined 1,600 horsepower, and the run took place at the Bonneville Salt Flats, a traditional venue for land speed records.

rss · Ars Technica · Aug 12, 17:01

**Background**: Hydrogen combustion engines work by burning hydrogen in a modified internal combustion engine, producing water vapor as the main emission. JCB has been developing hydrogen engines for its construction equipment, such as excavators and backhoe loaders, and has also installed one in a Mercedes truck to demonstrate broader applications. This land speed record is part of JCB's broader effort to promote hydrogen as a practical zero-carbon fuel.

<details><summary>References</summary>
<ul>
<li><a href="https://www.euronews.com/next/2026/08/12/british-driver-sets-speed-record-in-hydrogen-powered-car">British driver sets speed record in hydrogen - powered car | Euronews</a></li>
<li><a href="https://www.jcb.com/en-US/explore/sustainability/hydrogen/">JCB Hydrogen Solutions | JCB Sustainability | JCB</a></li>
<li><a href="https://news.google.com/stories/CAAqNggKIjBDQklTSGpvSmMzUnZjbmt0TXpZd1NoRUtEd2pscXVEZEVSR29BTFl0Smd6RXRpZ0FQAQ?hl=en-US&gl=US&ceid=US:en">British driver Andy Green breaks hydrogen land speed record ...</a></li>

</ul>
</details>

**Tags**: `#hydrogen`, `#automotive`, `#engineering`, `#record`

---

<a id="item-29"></a>
## [US Orders Kalshi to Keep Operating, Overriding NY Gambling Laws](https://arstechnica.com/tech-policy/2026/08/us-tries-to-override-new-york-gambling-laws-orders-kalshi-to-keep-operating/) ⭐️ 6.0/10

The Trump administration has ordered Kalshi, a regulated prediction market, to continue operating despite a New York lawsuit, citing a 'market emergency'. This move could set a precedent for federal intervention in state gambling regulations, potentially affecting the broader prediction market industry and its legal landscape. Kalshi is a U.S. dollar-based, regulated exchange, unlike blockchain-based platforms like Polymarket. The administration's claim of a 'market emergency' is a legal justification to override state law.

rss · Ars Technica · Aug 12, 16:33

**Background**: Prediction markets allow trading on the outcome of real-world events, such as elections or economic indicators. Kalshi is a regulated exchange in the U.S., but state laws like New York's gambling regulations can conflict with federal oversight. The term 'market emergency' typically refers to unforeseen circumstances requiring immediate action, which the administration is invoking to justify its order.

<details><summary>References</summary>
<ul>
<li><a href="https://kalshi.com/">Kalshi - Prediction Market for Trading the Future</a></li>
<li><a href="https://nextpredict.io/platforms/kalshi/">Kalshi News 2026: Review, Fees & Polymarket Comparison</a></li>
<li><a href="https://www.merriam-webster.com/dictionary/emergency">EMERGENCY Definition & Meaning - Merriam-Webster</a></li>

</ul>
</details>

**Tags**: `#regulation`, `#gambling`, `#legal`, `#tech-policy`

---

<a id="item-30"></a>
## [FBI Probes Fake Hotspot Attack on Delta Flight Linked to DEF CON](https://arstechnica.com/information-technology/2026/08/def-con-crowd-suspected-in-fake-hotspot-attack-on-delta-flight/) ⭐️ 6.0/10

The FBI's Atlanta field office is investigating a suspected fake-hotspot (evil twin) attack on a Delta flight, possibly involving DEF CON attendees. No arrests have been made as of the report. This incident highlights the real-world risks of public Wi-Fi, especially in confined spaces like airplanes, and underscores the ongoing threat of evil twin attacks. It also draws attention to the security community's activities and the potential for misuse of hacking skills. The attack likely involved setting up a rogue access point mimicking the airline's Wi-Fi to intercept passengers' data. The FBI confirmed the investigation but provided no further details, and no arrests have been made.

rss · Ars Technica · Aug 12, 00:08

**Background**: An evil twin attack is a type of Wi-Fi attack where an attacker creates a fake access point that appears legitimate, tricking users into connecting and exposing their traffic. DEF CON is a major hacker convention where attendees often discuss and demonstrate security techniques, and some may have the skills to execute such attacks. The FBI's involvement indicates the seriousness of the incident, which could have implications for aviation security and passenger privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DEF_CON">DEF CON - Wikipedia</a></li>
<li><a href="https://www.kaspersky.com/resource-center/preemptive-safety/evil-twin-attacks">What is an Evil Twin Attack ? Evil Twin Wi-Fi Explained</a></li>
<li><a href="https://limpvpn.com/en/blog/fake-wifi-evil-twin-attack">Fake Wi-Fi Hotspots (Evil Twin): How to Spot One in 2026</a></li>

</ul>
</details>

**Tags**: `#security`, `#DEF CON`, `#wireless`, `#FBI`, `#airline`

---

<a id="item-31"></a>
## [Texas Peak Demand Hits Record, Supply Constraints Loom](https://www.utilitydive.com/news/supply-constraints-will-limit-ercot-peak-demand-growth-report/827677/) ⭐️ 6.0/10

Texas set a new peak demand record, but Ascend Analytics reports that over 80% of new large loads seeking interconnection will lack matching generation by 2030, even as data centers and industrial demand surge. This imbalance threatens the reliability of the ERCOT grid and could slow the growth of data centers and industrial projects in Texas, impacting the broader tech and energy sectors. It underscores the urgent need for new generation capacity and grid upgrades. According to Ascend Analytics, more than 80% of new large loads seeking interconnection will not have matching generation online by 2030. ERCOT forecasts an additional 40,000 MW of load growth by 2030 compared with the prior year's forecast, with about 87% of the 410 GW of interconnection requests coming from data centers.

rss · Utility Dive · Aug 12, 17:00

**Background**: ERCOT (Electric Reliability Council of Texas) manages the electric grid for most of Texas. Peak demand records reflect the highest instantaneous electricity usage, often driven by extreme weather or rapid industrial growth. Interconnection is the process of connecting new power sources or large loads to the grid, and delays can occur due to transmission constraints and generation shortages.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ascendanalytics.com/solutions/product-overview">Power Price Forecasting & Valuation | Ascend Analytics : Enhancing...</a></li>
<li><a href="https://www.chokepoints.ai/stack/grid-transmission/large-load-interconnection-data-centre-industrial-hyperscale">Large - load interconnection : 410 GW of demand seeking grid access...</a></li>

</ul>
</details>

**Tags**: `#energy`, `#data centers`, `#infrastructure`, `#supply chain`, `#Texas`

---

<a id="item-32"></a>
## [Virginia Regulator Orders Dominion to Assign Some Transmission Costs to Data Centers](https://www.utilitydive.com/news/dominion-energy-scc-transmission-costs-data-center/827693/) ⭐️ 6.0/10

The Virginia State Corporation Commission (SCC) has ordered Dominion Energy to change its transmission cost allocation policy, directly assigning the costs of certain transmission infrastructure—such as substations built for data centers—to those large-load facilities instead of spreading them across all ratepayers. The SCC also indicated it may consider applying this policy to more upstream transmission costs in an upcoming docket. This ruling is significant because it shifts a portion of the financial burden of data center-driven grid upgrades from residential and commercial ratepayers to the data centers themselves, potentially setting a precedent for how other states handle similar cost allocation issues. It directly impacts the economics of data center operations in Virginia, the world's data center capital, and could influence energy policy and infrastructure investment decisions across the tech industry. The SCC's order requires Dominion to create a process for directly assigning the costs of dedicated grid-connection infrastructure, such as substations, to the data centers that necessitate them. The commission also noted it may use an upcoming docket to determine whether this policy 'could or should' apply to more upstream transmission costs, leaving the allocation of broader transmission investments unresolved for now.

rss · Utility Dive · Aug 12, 15:02

**Background**: Virginia, particularly Northern Virginia, is the world's largest data center market, with data centers driving a majority of the billions of dollars in new transmission line costs needed to deliver power to the region. Historically, these costs were spread across all ratepayers, meaning residential and commercial customers subsidized the grid upgrades required by data centers. The SCC's ruling aims to protect consumers from these costs by making data centers pay for the infrastructure they specifically require.

<details><summary>References</summary>
<ul>
<li><a href="https://www.utilitydive.com/news/dominion-energy-scc-transmission-costs-data-center/827693/">Dominion ordered to directly assign some transmission costs to data ...</a></li>
<li><a href="https://techinformed.com/virginia-sets-path-to-charge-data-centers-for-grid-links/">Virginia sets path to charge data centers for grid links - TechInformed</a></li>
<li><a href="https://www.pecva.org/region/scc-ruling-virginians-should-not-pay-for-data-center-transmission-infrastructure/">State Corporation Commission Says Virginians Should Not Pay for...</a></li>
<li><a href="https://www.eenews.net/articles/virginia-to-offload-more-grid-costs-onto-data-centers/">Virginia to offload more grid costs onto data centers</a></li>
<li><a href="https://insideclimatenews.org/news/13072026/virginias-governor-spanberger-data-center-transmission-costs/">Virginia’s Governor Weighs in on Pivotal Case About Data Center ...</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#energy policy`, `#regulation`, `#transmission costs`

---

<a id="item-33"></a>
## [Trump Admin Backs Puerto Rico Battery, Cuts Solar Funding](https://www.canarymedia.com/articles/batteries/puerto-rico-trump-admin-battery-project) ⭐️ 6.0/10

The Department of Energy closed a nearly $490 million loan to a Pattern Energy subsidiary for a large battery project in Puerto Rico, even as the Trump administration cuts funding for other clean energy initiatives in the territory. This selective support highlights a policy preference for grid resilience through battery storage over broader renewable energy expansion, which could shape Puerto Rico's energy future and signal federal priorities for disaster-prone regions. The loan is part of the DOE Loan Programs Office, which guarantees loans for innovative energy projects. The battery project aims to bolster Puerto Rico's fragile grid, which has suffered from chronic instability and major blackouts.

rss · Latitude Media (Canary Media) · Aug 12, 07:30

**Background**: Puerto Rico's electric grid has been notoriously unreliable, especially after Hurricane Maria in 2017, leading to frequent outages and a push for modernization. Battery storage is seen as a key solution for grid resilience, allowing energy to be stored and dispatched when needed. The DOE loan program has historically supported large-scale clean energy projects, but the Trump administration's budget cuts have reduced funding for solar and other renewables.

<details><summary>References</summary>
<ul>
<li><a href="https://www.nrdc.org/bio/amanda-levin/doe-program-propels-thriving-clean-energy-economy-industries">DOE Program Propels Thriving Clean Energy Economy Industries</a></li>
<li><a href="https://www.govinfo.gov/content/pkg/CHRG-115hhrg24668/html/CHRG-115hhrg24668.htm">risky business: the DOE loan guarantee program</a></li>
<li><a href="https://www.congress.gov/114/chrg/CHRG-114hhrg20834/CHRG-114hhrg20834.htm">department of energy oversight: the DOE loan guarantee program</a></li>

</ul>
</details>

**Tags**: `#energy policy`, `#battery storage`, `#Puerto Rico`, `#clean energy`, `#grid resilience`

---

<a id="item-34"></a>
## [Sony's Disc Phase-Out Sparks Game Preservation Backlash](https://www.pcgamer.com/hardware/sony-has-zero-understanding-for-what-their-customers-want-says-gaming-preservation-group/) ⭐️ 6.0/10

Sony has announced it will end PlayStation disc production by January 2028, as digital sales now account for 82% of Q1 FY2026 software revenue. This move has drawn sharp criticism from game preservation groups, including Clemens Istel of the preservation site Does It Play, who accused Sony of having 'zero understanding for what their customers want.' This decision threatens the long-term preservation of video games, as physical discs have historically served as a tangible, offline medium for archiving. With the industry shifting to digital-only distribution, games become vulnerable to server shutdowns, licensing issues, and platform closures, potentially losing access for future generations. Sony's timeline indicates a complete phase-out of disc production by January 2028, aligning with the growing dominance of digital sales (82% of software revenue). Critics argue that without physical media, game preservation becomes reliant on DRM-free releases, community efforts, and legal exceptions, which are often insufficient.

rss · PC Gamer · Aug 12, 15:06

**Background**: Video game preservation faces unique challenges due to the short lifespan of digital media and the complexity of archiving interactive software. Physical discs have provided a stable, offline copy that can be archived without relying on online services. As the industry moves toward digital distribution, preservation groups worry about the loss of games when servers are decommissioned or licenses expire.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/sony-has-zero-understanding-for-what-their-customers-want-says-gaming-preservation-group/">Sony has 'zero understanding for what their customers... | PC Gamer</a></li>
<li><a href="https://tech-insider.org/playstation-ends-discs-2028-digital-82-percent/">PlayStation Ends Discs by 2028 as Digital Hits 82% [2026]</a></li>
<li><a href="https://www.researchgate.net/publication/393426766_Video_Game_Preservation_and_Its_Challenges">(PDF) Video Game Preservation and Its Challenges</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so no sentiment can be summarized.

**Tags**: `#gaming`, `#game preservation`, `#Sony`, `#digital rights`

---

<a id="item-35"></a>
## [AI Agents: Both Victims and Attackers in 2026 Malware Wars](https://www.pcgamer.com/software/ai/welcome-to-the-internet-in-2026-where-ai-agents-are-both-victim-and-attacker-in-malware-wars/) ⭐️ 6.0/10

A PC Gamer article highlights that by 2026, AI agents will be both targets and tools in malware attacks, with attackers using deceptive repositories to trick agents into installing malicious code. The article emphasizes the urgent need for safeguards to evolve alongside AI agent capabilities. This matters because AI agents are increasingly integrated into business and personal workflows, making them attractive targets for cybercriminals. The dual role of AI agents as both victims and attackers could lead to more sophisticated and widespread attacks, affecting organizations and individuals who rely on AI technology. The article describes a scenario where an AI agent searching for a new capability, such as a Skill or an MCP server, could discover a malicious repository, treat the attacker's Readme as legitimate documentation, and hand installation instructions to the user. This highlights a specific attack vector distinct from traditional malware, focusing on undermining the AI's intelligence and trustworthiness.

rss · PC Gamer · Aug 12, 11:29

**Background**: AI agents are software programs that perform tasks autonomously, often using tools or APIs. As they become more capable, they are increasingly targeted by cybercriminals who exploit their trust in external data sources. Security frameworks like NIST's guidelines and OWASP's AI security recommendations are being developed to address these emerging threats, but they are still evolving.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/software/ai/welcome-to-the-internet-in-2026-where-ai-agents-are-both-victim-and-attacker-in-malware-wars/">Welcome to the internet in 2026, where AI agents are both... | PC Gamer</a></li>
<li><a href="https://www.omeganetworks.in/post/understanding-the-rising-threat-of-malware-targeting-ai-agent-security-and-tools">Understanding the Rising Threat of Malware Targeting AI agent ...</a></li>
<li><a href="https://dailytech.ai/post/google-warns-malicious-web-pages-poisoning-ai-agents-2026">Google Warns: Malicious Web Pages Poisoning AI Agents ... | DailyTech</a></li>

</ul>
</details>

**Tags**: `#AI`, `#cybersecurity`, `#malware`, `#AI agents`

---