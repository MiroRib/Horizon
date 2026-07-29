---
layout: default
title: "Horizon Summary: 2026-07-29 (EN)"
date: 2026-07-29
lang: en
---

> From 177 items, 39 important content pieces were selected

---

1. [AI worms self-propagate through Microsoft Copilot for Word](#item-1) ⭐️ 9.0/10
2. [Open-source engine runs Gemma 4 26B in 2 GB RAM on M-series Macs](#item-2) ⭐️ 8.0/10
3. [Mitchell Hashimoto Launches Superlogical on libghostty](#item-3) ⭐️ 8.0/10
4. [Kimi K3-256k: Half Cost, Same Performance](#item-4) ⭐️ 8.0/10
5. [Long Policy Documents Fail to Govern AI Agents](#item-5) ⭐️ 8.0/10
6. [Microsoft Confirms Copilot 'Super App' Launching This Year](#item-6) ⭐️ 8.0/10
7. [Anthropic finds Microsoft bugs faster than patches](#item-7) ⭐️ 8.0/10
8. [Google's SynthID watermark is robust but not a cure for AI disinformation](#item-8) ⭐️ 8.0/10
9. [KOReader: Open-Source E-Reader App Enhances Kindle and Kobo](#item-9) ⭐️ 7.0/10
10. [AI Companies Hire Thousands of Electricians and Carpenters](#item-10) ⭐️ 7.0/10
11. [Self-hosting Kimi K3: 20% more cost, 20% better task resolution](#item-11) ⭐️ 7.0/10
12. [Meta to Push Personal AI Agents Acting on Users' Behalf](#item-12) ⭐️ 7.0/10
13. [xAI sues Minnesota over anti-nudification law](#item-13) ⭐️ 7.0/10
14. [US FCC Ban on Advanced Robots Includes Robot Vacuums](#item-14) ⭐️ 7.0/10
15. [US Ban on Foreign Robots May Backfire](#item-15) ⭐️ 7.0/10
16. [AMD Linux Patch Boosts Steam Deck Low-End Gaming by 32%](#item-16) ⭐️ 7.0/10
17. [Trump admin bans foreign-made inverters, threatening clean energy projects](#item-17) ⭐️ 7.0/10
18. [PearlAbyss Reveals 'World First' Process for Crimson Desert](#item-18) ⭐️ 7.0/10
19. [Cygames Reveals Dialect Localization Secrets for Uma Musume](#item-19) ⭐️ 7.0/10
20. [Keychron to Open-Source Gaming Mouse Firmware](#item-20) ⭐️ 7.0/10
21. [Vision Pro Used for VR House Design Walkthrough](#item-21) ⭐️ 6.0/10
22. [Darktable: Free RAW Editor Draws Mixed Reviews](#item-22) ⭐️ 6.0/10
23. [Qualcomm to Raise Phone Chip Prices from September 1](#item-23) ⭐️ 6.0/10
24. [OpenAI President Reveals Plans for AI Device Family](#item-24) ⭐️ 6.0/10
25. [Google Play Store gets privacy-preserving age verification API](#item-25) ⭐️ 6.0/10
26. [Boeing CEO Hints Starliner Could Launch This Year](#item-26) ⭐️ 6.0/10
27. [AI Deciphers Lost Languages with Human Insight](#item-27) ⭐️ 6.0/10
28. [Elon Musk Launches X Money, Excluding Major US Markets](#item-28) ⭐️ 6.0/10
29. [Revived Geothermal Plant in New Mexico Runs at Full Capacity](#item-29) ⭐️ 6.0/10
30. [MIT Tech Review Examines AI Hype vs. Practical Reality](#item-30) ⭐️ 6.0/10
31. [Biggest battery east of Mississippi to power AI complex](#item-31) ⭐️ 6.0/10
32. [US Clean Energy Boom Faces Post-2030 Uncertainty](#item-32) ⭐️ 6.0/10
33. [Double Fine lays off staff after being dropped by Xbox](#item-33) ⭐️ 6.0/10
34. [Donkey Kong Bananza Devs Explain Destruction-Based Game Design at CEDEC 2026](#item-34) ⭐️ 6.0/10
35. [Fostering Digital Talent Through 'Garage' Environments](#item-35) ⭐️ 6.0/10
36. [Polyphony Digital & Sony Demo 10,000-nit HDR Pipeline with Gran Turismo 7](#item-36) ⭐️ 6.0/10
37. [Halo: Campaign Evolved Full Remake Released](#item-37) ⭐️ 6.0/10
38. [CEDEC Talk Debunks Mobile Game Marketing Myths with Data](#item-38) ⭐️ 6.0/10
39. [EverQuest Legends Launches with Solo Play and Multiclassing](#item-39) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [AI worms self-propagate through Microsoft Copilot for Word](https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/) ⭐️ 9.0/10

Researchers demonstrated document-borne AI worms that can self-propagate through Microsoft Copilot for Word by embedding malicious instructions in documents, exploiting the inability of LLMs to distinguish between instructions and data. This highlights a critical vulnerability class with no current mitigation, as AI agents with broad access to user data and actions can be hijacked via indirect prompt injection, potentially leading to widespread data theft or malware propagation. The attack works by hiding malicious instructions in document content (e.g., using white text or Unicode tricks), which Copilot then reads and executes, causing it to alter documents or propagate the worm to new files. The researcher has been working with Microsoft since March 2026, but no robust fix is available yet.

hackernews · Canopy9560 · Jul 29, 11:44 · [Discussion](https://news.ycombinator.com/item?id=49096188)

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause LLMs to behave unintendedly, as models cannot distinguish developer instructions from user data. Indirect prompt injection occurs when adversarial prompts are embedded in content the LLM retrieves, such as web pages or documents. This research extends the concept to document-borne worms that self-propagate through AI assistants like Copilot.

<details><summary>References</summary>
<ul>
<li><a href="https://enklypesalt.com/posts/context-collapse-part3-ai-worming-through-word/">Context Collapse, Part 3 - AI Worming through Word | En Klype Salt</a></li>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection_attack">Prompt injection attack</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that this vulnerability is fundamentally unfixable as long as AI mixes instructions with data, and warned that granting broad access to AI agents will lead to severe attacks, such as stealing credit cards or propagating through GitHub. Some noted that simple tricks like white text still work, demonstrating the difficulty of mitigation.

**Tags**: `#AI security`, `#prompt injection`, `#Copilot`, `#vulnerability`, `#LLM`

---

<a id="item-2"></a>
## [Open-source engine runs Gemma 4 26B in 2 GB RAM on M-series Macs](https://github.com/drumih/turbo-fieldfare) ⭐️ 8.0/10

TurboFieldfare, an open-source inference engine written in Swift and Metal, can run the 4-bit quantized Gemma 4 26B-A4B-IT model on any M-series Mac using only about 2 GB of RAM by streaming experts from SSD. This approach enables running large Mixture-of-Experts models on memory-constrained devices like 8 GB MacBooks, democratizing on-device AI. It achieves 5–6 tok/s on an M2 MacBook Air and 31–35 tok/s on an M5 MacBook Pro, making powerful models practical for personal use. The model's 4-bit quantized weights occupy roughly 14 GB, but TurboFieldfare keeps only the shared layers and KV cache in RAM, streaming routed experts from SSD using a small expert cache and bounded parallel pread. It also includes an experimental OpenAI-compatible local server with streaming and tool call support.

hackernews · gitpusher42 · Jul 29, 15:05 · [Discussion](https://news.ycombinator.com/item?id=49098510)

**Background**: Gemma 4 26B-A4B-IT is a Mixture-of-Experts (MoE) model from Google, where only a subset of experts is activated per token, reducing computation. 4-bit quantization compresses model weights to reduce memory footprint, but conventional inference still requires loading all weights into RAM. TurboFieldfare exploits the MoE architecture to load only needed experts on demand, using SSD as a slower but larger memory tier.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/4bit-transformers-bitsandbytes">Making LLMs even more accessible with bitsandbytes, 4-bit quantization and QLoRA</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>

</ul>
</details>

**Discussion**: Commenters praised the innovation and compared it to llama.cpp's mmap approach, noting that TurboFieldfare's synchronization of SSD reads with inference is a key differentiator. Some users provided compilation tips for older macOS versions, and one developer working on a similar project for DiffusionGemma expressed interest in collaboration.

**Tags**: `#machine learning`, `#inference engine`, `#on-device AI`, `#Swift`, `#Metal`

---

<a id="item-3"></a>
## [Mitchell Hashimoto Launches Superlogical on libghostty](https://www.superlogical.com/) ⭐️ 8.0/10

Mitchell Hashimoto announced Superlogical, a new company that will build terminal applications on the open source libghostty library, and plans to transfer ownership of the Ghostty terminal emulator to a non-profit organization. This move establishes a sustainable open-source business model where a company builds on a community-owned library, ensuring the core technology remains free and independent while enabling commercial innovation. Superlogical will use the same MIT-licensed libghostty components available to everyone and will upstream shared terminal work to benefit all libghostty consumers. Ghostty is a fast, cross-platform terminal emulator using GPU acceleration and native UI.

hackernews · yan · Jul 29, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49098965)

**Background**: Ghostty is a fast, feature-rich, cross-platform terminal emulator that uses platform-native UI and GPU acceleration. It is built on libghostty, an open-source library that handles terminal emulation core functions like VT sequence parsing and cursor management.

<details><summary>References</summary>
<ul>
<li><a href="https://ghostty.org/">Ghostty</a></li>
<li><a href="https://github.com/ghostty-org">Ghostty · GitHub</a></li>
<li><a href="https://webteractive.co/blog/ghostty-and-libghostty-the-terminal-core-quietly-reshaping-the-ecosystem">Ghostty and libghostty : The Terminal Core Quietly... — Webteractive</a></li>

</ul>
</details>

**Discussion**: Commenters praised the open-source governance model, comparing it to past technologies like OLE for composability. Some expressed frustration with the enigmatic title, but overall sentiment was positive, with high engagement.

**Tags**: `#open source`, `#terminal`, `#software engineering`, `#business model`

---

<a id="item-4"></a>
## [Kimi K3-256k: Half Cost, Same Performance](https://www.kimi.com/code/docs/en/kimi-code/models) ⭐️ 8.0/10

Kimi released the K3-256k model, which offers a 256k context window and delivers the same performance as the 1M version while consuming only half the quota cost. This reduces the cost for users who do not need the full 1M context, making advanced AI more accessible and alleviating infrastructure pressure on Kimi. The K3-256k model is available on all plans, while the 1M context version is restricted to higher-tier plans like Allegretto. The K3 model itself has 2.8T parameters and supports multimodal reasoning.

hackernews · monneyboi · Jul 29, 19:25 · [Discussion](https://news.ycombinator.com/item?id=49101852)

**Background**: Kimi K3 is a 2.8T parameter open-weight multimodal reasoning model from Moonshot AI, featuring a 1M token context window. The new K3-256k variant halves the context length but maintains the same quality, addressing user feedback about cost and infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.kimi.com/code/docs/en/kimi-code/models">Model Configuration | Kimi Code Docs</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K3 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>

</ul>
</details>

**Discussion**: Community members welcomed the move, noting that 256k context is often sufficient and that the price reduction is significant. Some expressed concerns about recent model quality degradation and suspected use of quantized models.

**Tags**: `#AI`, `#LLM`, `#context window`, `#pricing`, `#Kimi`

---

<a id="item-5"></a>
## [Long Policy Documents Fail to Govern AI Agents](https://arxiv.org/abs/2607.25398) ⭐️ 8.0/10

A new research paper, Handbook.md, demonstrates that long policy documents do not reliably govern AI agents, revealing fundamental limitations of long-context models in agentic tasks. This finding challenges the assumption that long-context LLMs can effectively follow complex instructions, impacting the deployment of AI agents in real-world applications where policy compliance is critical. The paper likely introduces a benchmark to evaluate policy adherence, showing that even models with 1M token context windows fail to consistently follow lengthy guidelines due to issues like KV cache quantization and limited working memory.

hackernews · spIrr · Jul 29, 13:01 · [Discussion](https://news.ycombinator.com/item?id=49096969)

**Background**: Long-context large language models (LLMs) claim to handle up to millions of tokens, enabling tasks like processing entire books or lengthy policy documents. However, research shows that these models struggle with information retrieval and instruction following over long contexts due to attention decay and memory constraints. AI agents rely on such models to autonomously execute tasks while adhering to given policies, making this limitation critical for safe deployment.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2502.17129v1?trk=article-ssr-frontend-pulse_little-text-block">Thus Spake Long - Context Large Language Model</a></li>
<li><a href="https://github.com/microsoft/agent-governance-toolkit">GitHub - microsoft/agent-governance-toolkit: AI Agent Governance Toolkit — Policy enforcement, zero-trust identity, execution sandboxing, and reliability engineering for autonomous AI agents. Covers 10/10 OWASP Agentic Top 10.</a></li>
<li><a href="https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/">Introducing the Agent Governance Toolkit: Open-source runtime security for AI agents | Microsoft Open Source Blog</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree with the findings, sharing anecdotal evidence that models like Claude ignore instructions in CLAUDE.md files after a short time. Some highlight that local inference can mitigate the issue, while others note that humans also struggle with long policy documents, suggesting the problem is not unique to AI.

**Tags**: `#LLM`, `#AI agents`, `#long context`, `#benchmark`, `#limitations`

---

<a id="item-6"></a>
## [Microsoft Confirms Copilot 'Super App' Launching This Year](https://www.theverge.com/tech/972927/microsoft-copilot-super-app-confirmed) ⭐️ 8.0/10

Microsoft CEO Satya Nadella confirmed during an earnings call that the company is building a Copilot 'super app' that combines chat, coding, and agentic capabilities, targeting both consumer and commercial users, with a launch planned for this year. This move signals Microsoft's ambition to unify its fragmented AI assistants into a single platform, potentially boosting adoption rates and setting a new standard for AI-powered productivity tools across both personal and enterprise environments. The super app is expected to include modes such as Copilot Chat, GitHub Copilot coding, Copilot Cowork for knowledge workers, and an Autopilot always-on agent mode, though specific features and pricing remain unconfirmed.

rss · The Verge · Jul 29, 22:17

**Background**: Microsoft has been developing multiple AI assistants under the Copilot brand, including Microsoft 365 Copilot for productivity and GitHub Copilot for coding. A 'super app' would consolidate these into one interface, addressing user complaints about fragmentation and low adoption rates (below 4.5%). Agentic AI refers to systems that can autonomously set goals, plan, and execute tasks with minimal human intervention.

<details><summary>References</summary>
<ul>
<li><a href="https://fortune.com/2026/05/29/microsoft-working-on-super-app/">Exclusive: Microsoft is building a super app that combines coding, chat, and other Copilot AI tools | Fortune</a></li>
<li><a href="https://www.geekwire.com/2026/mary-jo-foley-no-copilot-super-app-at-microsoft-build-but-plenty-of-agentic-fodder/">Mary Jo Foley: No Copilot 'Super App' at Microsoft Build, but plenty of agentic fodder – GeekWire</a></li>
<li><a href="https://cryptobriefing.com/microsoft-copilot-super-app/">Microsoft builds super app integrating Copilot AI tools and chat into one platform</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Microsoft`, `#Copilot`, `#super app`, `#announcement`

---

<a id="item-7"></a>
## [Anthropic finds Microsoft bugs faster than patches](https://arstechnica.com/security/2026/07/anthropic-is-finding-bugs-faster-than-microsoft-can-fix-them/) ⭐️ 8.0/10

Anthropic is using its Claude Mythos AI model to discover security vulnerabilities in Microsoft products at a rate that outpaces Microsoft's ability to patch them, creating a widening exploit window. This trend signals a shift in the cybersecurity landscape where AI-powered vulnerability discovery can outrun traditional patch management, increasing the risk of zero-day exploits and pressuring vendors to accelerate their response times. Anthropic follows a 90-day coordinated disclosure policy, but the rapid discovery rate means many vulnerabilities remain unpatched within that window. Claude Mythos is a general-purpose AI model that unexpectedly exhibited advanced cybersecurity capabilities, surpassing most humans at finding and exploiting software flaws.

rss · Ars Technica · Jul 29, 15:52

**Background**: Vulnerability disclosure typically involves a finder notifying the vendor and allowing time for a patch before public release. However, the exploit window—the time between discovery and exploitation—is shrinking due to AI tools that can generate working exploits within hours. Microsoft, as a major software vendor, faces pressure to keep up with AI-driven discoveries from companies like Anthropic.

<details><summary>References</summary>
<ul>
<li><a href="https://red.anthropic.com/2026/cvd/">Anthropic's coordinated vulnerability disclosure dashboard</a></li>
<li><a href="https://www.anthropic.com/coordinated-vulnerability-disclosure">Coordinated vulnerability disclosure for Claude-discovered vulnerabilities \ Anthropic</a></li>
<li><a href="https://www.armorcode.com/blog/anthropics-claude-mythos-and-what-it-means-for-security">Anthropic’s Claude Mythos and What it Means for Security</a></li>

</ul>
</details>

**Tags**: `#security`, `#vulnerability disclosure`, `#Microsoft`, `#Anthropic`, `#patch management`

---

<a id="item-8"></a>
## [Google's SynthID watermark is robust but not a cure for AI disinformation](https://arstechnica.com/ai/2026/07/tested-google-synthid-works-great-but-labeling-ai-content-may-be-a-losing-game/) ⭐️ 8.0/10

A practical test of Google DeepMind's SynthID watermarking system shows it is technically difficult to remove, but the article argues that watermarking alone cannot solve the broader problem of AI-generated disinformation. As AI-generated content becomes ubiquitous, reliable authentication methods are critical; SynthID represents a significant technical advance, but the piece highlights that technical fixes alone are insufficient without complementary policy and media literacy efforts. SynthID embeds watermarks at the generation level rather than as removable metadata, making it more tamper-resistant. However, the watermark can still be weakened by heavy editing or compression, and it does not prevent malicious actors from simply using other AI models without watermarking.

rss · Ars Technica · Jul 29, 11:00

**Background**: AI watermarking aims to label content as machine-generated to help combat disinformation. SynthID, developed by Google DeepMind, works across images, audio, text, and video. Unlike metadata-based labels, SynthID's watermark is designed to survive common modifications. However, the challenge of AI disinformation also involves social and regulatory dimensions that technology alone cannot address.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/models/synthid/">SynthID — Google DeepMind</a></li>
<li><a href="https://ai.google.dev/responsible/docs/safeguards/synthid">SynthID: Tools for watermarking and detecting LLM-generated Text | Responsible Generative AI Toolkit | Google AI for Developers</a></li>
<li><a href="https://medium.com/@karanbhutani477/synthid-a-technical-deep-dive-into-googles-ai-watermarking-technology-0b73bd384ff6">SynthID: A Technical Deep Dive into Google’s AI Watermarking Technology | by Karan_bhutani | Medium</a></li>

</ul>
</details>

**Tags**: `#AI`, `#watermarking`, `#disinformation`, `#Google`, `#content authenticity`

---

<a id="item-9"></a>
## [KOReader: Open-Source E-Reader App Enhances Kindle and Kobo](https://koreader.rocks/) ⭐️ 7.0/10

KOReader is an open-source document viewer for E Ink devices that supports a wide range of file formats including EPUB, PDF, DjVu, MOBI, and more. It can be installed on jailbroken Kindles and Kobo devices to replace or complement the default reading software. KOReader significantly improves the reading experience on proprietary e-readers by offering better format support, customization, and features like reading progress sync and Calibre integration. It empowers users to take control of their devices, highlighting the advantages of open-source software in the e-reader ecosystem. KOReader requires a jailbroken Kindle or a Kobo device for installation, and some users report that its UI/UX can be non-intuitive and occasionally laggy. The software is actively maintained and has a strong community, with plugins available for additional functionality like downloading books from Z-Library.

hackernews · Cider9986 · Jul 29, 11:05 · [Discussion](https://news.ycombinator.com/item?id=49095865)

**Background**: E Ink devices like Kindle and Kobo typically run proprietary firmware that limits file format support and customization. Jailbreaking a Kindle allows users to access the underlying Linux OS and run third-party applications like KOReader. KOReader is a free, open-source alternative that aims to provide a more versatile and user-controlled reading experience.

<details><summary>References</summary>
<ul>
<li><a href="https://koreader.rocks/">KOReader</a></li>
<li><a href="https://kindlemodding.org/jailbreaking/">KindleModding - Jailbreaking Your Kindle</a></li>
<li><a href="https://www.mobileread.com/forums/showthread.php?t=344865">Alternative firmware for Kobo - Plato only, Nickel (Rakuten terminal)...</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users praise KOReader for vastly improving their reading experience and enabling features like sync and Calibre integration, while others criticize its non-intuitive UI and occasional lag. A few users prefer the default viewer despite KOReader's advantages, and one user noted difficulty with gesture controls.

**Tags**: `#open-source`, `#e-reader`, `#software`, `#kindle`, `#kobo`

---

<a id="item-10"></a>
## [AI Companies Hire Thousands of Electricians and Carpenters](https://www.nytimes.com/2026/07/29/business/economy/data-center-electricians-training.html) ⭐️ 7.0/10

AI companies are recruiting thousands of electricians and carpenters to build data centers, but the boom-bust nature of the industry poses career risks. This trend highlights a significant shift in labor demand driven by AI infrastructure, offering high wages but also exposing workers to volatile employment cycles. The article notes that workers can earn $300,000 in a boom year but only $30,000 in a bust year, and the rise of liquid cooling may shift skill demands from ductwork to plumbing.

hackernews · thm · Jul 29, 14:43 · [Discussion](https://news.ycombinator.com/item?id=49098198)

**Background**: Data centers are critical for AI computing, requiring massive electrical and construction work. The industry is known for rapid build-out phases followed by slowdowns, creating a boom-bust cycle.

**Discussion**: Commenters warn about the boom-bust risk, with one noting that electricians could earn $300k one year and $30k the next. Another highlights the shift to liquid cooling, which may require more plumbers than ductworkers.

**Tags**: `#AI infrastructure`, `#data centers`, `#labor market`, `#trades`

---

<a id="item-11"></a>
## [Self-hosting Kimi K3: 20% more cost, 20% better task resolution](https://aistack.imec-int.com/blog/gpu-self-hosting) ⭐️ 7.0/10

A detailed comparison shows that self-hosting Kimi K3 achieves 86.4% task resolution, 24 percentage points higher than alternatives, but at 20% higher hardware cost and with lower throughput and longer task times. This analysis provides concrete metrics for organizations deciding between self-hosted models and cloud APIs, highlighting the trade-off between cost and quality for large language model deployment. Kimi K3 served 16 concurrent sessions with 122 tok/s aggregate throughput and median task time of 38 minutes, compared to 24 sessions, 170 tok/s, and 26 minutes for GLM-5.2. The hardware cost increase is 20%.

hackernews · flifenstein · Jul 29, 14:38 · [Discussion](https://news.ycombinator.com/item?id=49098130)

**Background**: Kimi K3 is an open-weights large language model with 2.8 trillion parameters, released by Moonshot AI in July 2026. Task resolution measures the percentage of tasks an LLM agent completes successfully, a key metric for evaluating real-world performance.

<details><summary>References</summary>
<ul>
<li><a href="https://huggingface.co/blog/ResterChed/kimi-k3-model-overview-mxfp4-quantization-open-wei">Kimi K3 Model Overview: 2.8T Parameters, MXFP4 Quantization, and What the Open Weights Mean for the Community</a></li>
<li><a href="https://platform.kimi.ai/docs/guide/kimi-k3-quickstart">Kimi K3 - Kimi API Platform</a></li>

</ul>
</details>

**Discussion**: Commenters noted the trade-off between quality and speed, with some praising K3's quality but others pointing out the lack of concrete pricing. One user suggested comparing quantized versions for smaller hardware.

**Tags**: `#self-hosting`, `#LLM`, `#GPU`, `#cost-analysis`, `#model-comparison`

---

<a id="item-12"></a>
## [Meta to Push Personal AI Agents Acting on Users' Behalf](https://www.theverge.com/tech/972294/meta-q2-2026-earnings-mark-zuckerberg-personal-ai-agents) ⭐️ 7.0/10

On Meta's Q2 2026 earnings call, CEO Mark Zuckerberg previewed a high-level vision for a major push into personal AI agents that can perform tasks on users' behalf. This signals a strategic shift for Meta towards proactive AI assistants, potentially transforming how users interact with digital services and setting a new industry direction for personal AI. The announcement was high-level with few concrete details; Meta has already launched Meta Business Agent for businesses and offers Meta AI for general tasks, indicating a gradual expansion into personal agents.

rss · The Verge · Jul 29, 21:48

**Background**: Personal AI agents are AI systems that operate on behalf of a user, with dedicated memory, files, and tools, capable of autonomous actions like research, content creation, and tool integration. Meta has been investing heavily in AI, including large language models and AI-powered products across its platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://instaclaw.io/blog/what-is-a-personal-ai-agent">What is a Personal AI Agent? The Complete Guide (2026)</a></li>
<li><a href="https://about.fb.com/news/2026/06/meta-business-agent/">Be There for Every Customer With Meta Business Agent</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Meta`, `#personal agents`, `#earnings call`

---

<a id="item-13"></a>
## [xAI sues Minnesota over anti-nudification law](https://www.theverge.com/policy/972850/xai-grok-minnesota-nudification-lawsuit) ⭐️ 7.0/10

xAI filed a lawsuit against Minnesota Attorney General Keith Ellison, arguing that the state's new law targeting nudification apps violates the First Amendment and forces the company to restrict features of its Grok Imagine image generator. This case could set a precedent for how states regulate AI-generated content, particularly nonconsensual deepfakes, while balancing First Amendment protections. It highlights the tension between combating harmful deepfakes and preserving free expression in AI development. The Minnesota law, passed in May 2026, is the first in the U.S. to ban nudification apps that use AI to digitally undress people in photos. xAI claims the law's punitive provisions leave it with no practical choice but to restrict Grok Imagine's image-editing features.

rss · The Verge · Jul 29, 21:06

**Background**: Nudification apps use generative AI to create realistic nude images of clothed individuals, often without consent, leading to nonconsensual deepfake pornography. Minnesota's law was passed unanimously in the state Senate to address this issue. Grok Imagine is an AI image and video generator developed by xAI, integrated with the X social network.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Nudification_apps">Nudification apps</a></li>
<li><a href="https://19thnews.org/2026/04/minnesota-nudification-ban-ai-deepfake/">Minnesota passes first 'nudification' app ban</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#First Amendment`, `#xAI`, `#Grok`, `#image generation`

---

<a id="item-14"></a>
## [US FCC Ban on Advanced Robots Includes Robot Vacuums](https://www.theverge.com/policy/972312/us-robot-ban-sweep-up-chinese-vacuums) ⭐️ 7.0/10

The FCC has confirmed that its ban on foreign-made advanced robotic devices, initially reported as targeting humanoid and quadruped robots, also applies to robot vacuum cleaners. The ban, citing national security risks, effectively bars Chinese-made robotic vacuums from the US market. This expansion significantly impacts the consumer robotics industry, as robot vacuums are among the most widely adopted home robots. It signals a broad interpretation of 'advanced robotic devices' that could affect other consumer robotics categories and reshape global supply chains. The FCC's Covered List now includes foreign-produced advanced robotic devices and connected power inverters. The ban was confirmed by FCC media relations director Katie Gorscak, who stated that robot vacuums are swept up in the regulation due to their advanced sensing and connectivity capabilities.

rss · The Verge · Jul 29, 18:13

**Background**: The FCC's Covered List identifies communications equipment deemed a national security risk, effectively banning its import or use in the US. The recent addition of advanced robotic devices stems from concerns over data collection and remote access by foreign entities. Robot vacuums, which often include cameras, microphones, and Wi-Fi connectivity, are considered capable of espionage.

<details><summary>References</summary>
<ul>
<li><a href="https://thehill.com/homenews/5996462-fcc-bans-foreign-humanoid-robots/">FCC bans foreign humanoid robots and power inverters over security risks</a></li>
<li><a href="https://www.bbc.com/news/articles/cp9e2ex3ekyo">Trump administration bans new Chinese humanoid robots</a></li>
<li><a href="https://roboticsandautomationnews.com/2026/07/29/fcc-updates-covered-list-to-include-foreign-produced-advanced-robotic-devices-and-power-inverters/103658/">FCC adds foreign-made advanced robots to Covered List over...</a></li>

</ul>
</details>

**Tags**: `#policy`, `#robotics`, `#regulation`, `#consumer tech`

---

<a id="item-15"></a>
## [US Ban on Foreign Robots May Backfire](https://arstechnica.com/ai/2026/07/who-wins-and-who-loses-after-us-bans-foreign-robots/) ⭐️ 7.0/10

An analysis suggests that a US government ban on foreign-made robots could harm the domestic robotics industry rather than help it. This policy could disrupt supply chains, increase costs, and stifle innovation in the US robotics sector, potentially weakening its global competitiveness. The ban targets foreign robots, but US companies rely on foreign components and technology, so the restriction could backfire by limiting access to essential parts and expertise.

rss · Ars Technica · Jul 29, 20:03

**Background**: The US robotics industry is deeply integrated with global supply chains. Many domestic manufacturers use foreign-made components or entire robots to stay competitive. A ban could force them to find alternative sources, potentially raising costs and slowing development.

**Tags**: `#robotics`, `#policy`, `#US`, `#technology`, `#regulation`

---

<a id="item-16"></a>
## [AMD Linux Patch Boosts Steam Deck Low-End Gaming by 32%](https://arstechnica.com/gaming/2026/07/new-amd-linux-patch-boosts-low-end-gaming-performance-on-steam-deck/) ⭐️ 7.0/10

A new AMD Linux kernel patch, proposed by Meta engineer David Vernet, improves the Energy Performance Preference (EPP) mode efficiency, resulting in a ~32% increase in 1% low frame rates on the Steam Deck and other AMD-based handhelds. This patch significantly reduces stuttering and improves gaming smoothness on the popular Steam Deck, enhancing the user experience for low-end gaming. It also demonstrates ongoing optimization of AMD's Linux driver ecosystem, benefiting the broader Linux gaming community. The patch, called 'epp_boost', focuses on the AMD P-State driver's EPP mode, which balances performance and power consumption. The 32% improvement specifically targets 1% low frame rates, a metric that indicates worst-case smoothness and is critical for perceived gaming fluidity.

rss · Ars Technica · Jul 29, 15:33

**Background**: The Steam Deck uses a custom AMD APU and runs on Linux. EPP (Energy Performance Preference) mode allows the system to dynamically adjust CPU frequency between minimum and maximum based on workload hints, but can cause frame hitches in games. The 1% low frame rate measures the average frame rate of the slowest 1% of frames, providing a better sense of stutter than average FPS alone.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/gaming/2026/07/new-amd-linux-patch-boosts-low-end-gaming-performance-on-steam-deck/">New AMD Linux patch boosts low-end gaming... - Ars Technica</a></li>
<li><a href="https://www.phoronix.com/news/AMD-P-State-Better-1p-Lows">AMD P-State Linux Driver Patches Can Boost 1%-Low FPS... - Phoronix</a></li>
<li><a href="https://en.wikipedia.org/wiki/Micro_stuttering">Micro stuttering - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#Linux`, `#Steam Deck`, `#gaming`, `#performance`

---

<a id="item-17"></a>
## [Trump admin bans foreign-made inverters, threatening clean energy projects](https://www.canarymedia.com/articles/corporate-procurement/trump-admin-bans-new-foreign-inverters) ⭐️ 7.0/10

The Trump administration has banned the import and domestic use of new power inverters made outside the United States, citing national security concerns. This ban could disrupt gigawatts of planned solar, wind, and battery storage projects, which rely heavily on inverters, and may jeopardize U.S. climate targets. The ban applies to new inverters, not existing ones, and is part of a broader technology restriction that also includes advanced robots. China is the dominant supplier of inverters globally.

rss · Latitude Media (Canary Media) · Jul 29, 21:00

**Background**: A power inverter converts direct current (DC) electricity from solar panels or batteries into alternating current (AC) used by the grid. Inverters are essential for integrating renewable energy into the power system. The U.S. relies heavily on imported inverters, especially from China.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Power_inverter">Power inverter - Wikipedia</a></li>
<li><a href="https://www.energy.gov/eere/solar/solar-integration-inverters-and-grid-services-basics">Solar Integration: Inverters and Grid Services Basics | Department of Energy</a></li>
<li><a href="https://getclimatebrief.com/story/climate-impact-fcc-import-ban-solar-inverters">Solar Inverter Ban Puts U . S . Climate Targets at Risk</a></li>

</ul>
</details>

**Tags**: `#energy policy`, `#renewable energy`, `#inverters`, `#regulation`, `#solar`

---

<a id="item-18"></a>
## [PearlAbyss Reveals 'World First' Process for Crimson Desert](https://www.4gamer.net/games/484/G048495/20260729039/) ⭐️ 7.0/10

At CEDEC 2026, PearlAbyss presented their 'World First' development process and custom XML scripting system that enabled a team of about 200 people to build the large open-world game Crimson Desert over approximately 7 years. This talk provides rare insight into how a relatively small team can tackle massive open-world development, offering valuable lessons for the game industry. The 'World First' approach—building the world before quests—challenges conventional design hierarchies. The team built a custom XML scripting system that allowed designers to define gimmick behaviors without coding each case from scratch. The presentation also covered unresolved challenges, not just successes.

rss · 4Gamer.net · Jul 29, 08:37

**Background**: Crimson Desert is an open-world action-adventure game developed by PearlAbyss, the studio behind Black Desert Online. The game uses an upgraded version of the proprietary BlackSpace Engine. 'World First' refers to a development philosophy where the open world is built before quests or narrative are designed.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Crimson_Desert">Crimson Desert - Wikipedia</a></li>
<li><a href="https://www.invenglobal.com/articles/24095/pearl-abyss-unveils-crimson-desert-development-process">Pearl Abyss Unveils 'Crimson Desert' Development Process - Inven Global</a></li>

</ul>
</details>

**Tags**: `#game development`, `#open world`, `#XML`, `#CEDEC`, `#PearlAbyss`

---

<a id="item-19"></a>
## [Cygames Reveals Dialect Localization Secrets for Uma Musume](https://www.4gamer.net/games/414/G041434/20260729025/) ⭐️ 7.0/10

At CEDEC 2026, Cygames' localization team presented how they handled Japanese dialects and character voices in the English version of Uma Musume: Pretty Derby, focusing on recreating personality rather than direct translation. This approach sets a new standard for game localization, showing how to preserve character identity across languages, which is crucial for narrative-driven games with strong regional accents. The talk included real translation examples and explained the team's workflow for adapting dialects into English text, ensuring the localized version maintains the original's charm without confusing international players.

rss · 4Gamer.net · Jul 29, 08:21

**Background**: Uma Musume: Pretty Derby is a popular Japanese mobile game featuring anthropomorphic horse girls, each with distinct dialects and speech patterns. Localizing such culturally specific elements is challenging because direct translation often fails to convey the intended personality. CEDEC is a major game developer conference in Japan where industry professionals share technical insights.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Video_game_localization">Video game localization - Wikipedia</a></li>
<li><a href="https://www.gameslocalizationschool.com/en/video-game-localization-how-do-dialects-fit-in/">Video Game Localization: How Do Dialects Fit In? - GLOS</a></li>

</ul>
</details>

**Tags**: `#localization`, `#game development`, `#translation`, `#dialect`, `#CEDEC`

---

<a id="item-20"></a>
## [Keychron to Open-Source Gaming Mouse Firmware](https://www.pcgamer.com/hardware/gaming-mice/keychrons-gaming-mouse-firmware-is-going-open-source-while-the-company-critiques-firmware-you-cant-read-cant-audit-cant-change/) ⭐️ 7.0/10

Keychron announced on X that it is developing ZGM (Zephyr Gaming Mouse), an open-source firmware for gaming mice, and plans to release it in Q1 2027. The first mouse to run ZGM will be the upcoming G6 HE, which features hybrid optical-magnetic switches. This move challenges the industry norm of proprietary, un-auditable firmware, giving users transparency and control over their hardware. It could set a precedent for other peripheral manufacturers to embrace open-source firmware, benefiting security and customization. The firmware is built on Zephyr RTOS and will be hosted on GitHub under the repository Keychron/zgm. Keychron criticizes existing gaming mouse firmware as 'firmware you can't read, can't audit, can't change', highlighting the need for openness.

rss · PC Gamer · Jul 29, 14:24

**Background**: Most gaming mice use proprietary firmware that cannot be inspected or modified by users, limiting customization and security auditing. Open-source firmware, like QMK for keyboards, allows community-driven improvements and transparency. Keychron's ZGM aims to bring similar benefits to gaming mice.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/gaming-mice/keychrons-gaming-mouse-firmware-is-going-open-source-while-the-company-critiques-firmware-you-cant-read-cant-audit-cant-change/">Keychron's gaming mouse firmware is going open-source, while the company critiques 'firmware you can't read, can't audit, can't change' | PC Gamer</a></li>
<li><a href="https://www.notebookcheck.net/Keychron-reveals-open-source-mouse-firmware-for-upcoming-Logitech-killer-magnetic-switch-gaming-mouse.1354378.0.html">Keychron reveals open-source mouse firmware for upcoming Logitech-killer magnetic switch gaming mouse - Notebookcheck News</a></li>
<li><a href="https://www.digitalfoundry.net/news/2026/07/keychron-announces-first-open-source-firmware-for-gaming-mice">Keychron announces first open-source firmware for gaming mice | Digital Foundry</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some praise the move but note the release is far off (Q1 2027), calling it 'vaporware' for now. Others question the need for a new project when QMK already exists for mice, and express concern about limited mouse form factors from Keychron.

**Tags**: `#open-source`, `#firmware`, `#gaming mouse`, `#hardware`, `#transparency`

---

<a id="item-21"></a>
## [Vision Pro Used for VR House Design Walkthrough](https://christianselig.com/2026/07/vision-pro-house/) ⭐️ 6.0/10

Christian Selig describes using Apple Vision Pro to walk through a house design in VR, enabling intuitive spatial validation of proportions and layout. This application highlights Vision Pro's potential in architecture and design, though similar capabilities already exist with other VR headsets like HTC Vive and Quest 3. The walkthrough uses a 3D model exported from design software; users can immediately sense if spaces are correctly proportioned, which is valuable for early design validation.

hackernews · robbiet480 · Jul 29, 20:39 · [Discussion](https://news.ycombinator.com/item?id=49102774)

**Background**: Spatial computing devices like Apple Vision Pro blend digital content with the physical world. VR walkthroughs for architecture have been used for years with headsets like HTC Vive and Quest 3, allowing clients to experience unbuilt spaces.

<details><summary>References</summary>
<ul>
<li><a href="https://uxatc.medium.com/embracing-the-next-frontier-unleashing-the-potential-of-spatial-ux-in-the-era-of-apple-vision-pro-e4744754d940">Embracing the Next Frontier: Unleashing the Potential of Spatial UX in...</a></li>
<li><a href="https://ai.plainenglish.io/a-closer-look-into-spatial-computing-651dc2fb2421">A Closer Look Into Spatial Computing | by Luís Fernando Torres</a></li>
<li><a href="https://www.linkedin.com/posts/ozguroyman_introducing-apple-vision-pro-apples-first-activity-7071608894841647104-qDgE">Introducing Apple Vision Pro : Apple ’s first spatial computer</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar experiences: one used HTC Vive a decade ago for house design, another uses Quest 3 daily in their design-build firm. A suggestion was made to use VR for tracing wiring and plumbing in existing homes.

**Tags**: `#Vision Pro`, `#VR`, `#architecture`, `#design`

---

<a id="item-22"></a>
## [Darktable: Free RAW Editor Draws Mixed Reviews](https://www.darktable.org/) ⭐️ 6.0/10

Darktable, a free and open-source RAW photo editor, continues to receive community attention with a mix of strong praise for its features and criticism over performance and breaking changes between versions. 作为Adobe Lightroom的主要免费替代品，Darktable的演变影响着许多依赖开源工具进行专业RAW处理的摄影师，其社区反馈凸显了维护复杂软件的挑战。 Users report that Darktable offers extensive features and viable workflows for free, but some experience slow performance on decent hardware and encountered rendering issues when upgrading from version 2 to 3, with certain modules becoming obsolete.

hackernews · siatko · Jul 29, 12:33 · [Discussion](https://news.ycombinator.com/item?id=49096654)

**Background**: Darktable is a free and open-source photography application and raw developer, designed for non-destructive raw image post-production. It competes with Adobe Lightroom, which is a paid subscription service. The software has a steep learning curve and its own unique workflow concepts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Darktable">Darktable - Wikipedia</a></li>
<li><a href="https://expertphotography.com/lightroom-vs-darktable">Darktable vs Lightroom (Is Darktable Really Just as Good?)</a></li>

</ul>
</details>

**Discussion**: Community comments are mixed: some users praise Darktable as a fantastic free tool that makes other RAW editors obsolete, while others criticize its slowness and breaking changes that ruined old edits. A fork called Ansel was created by ex-maintainers who disagreed with Darktable's direction.

**Tags**: `#photography`, `#open-source`, `#image-editing`, `#raw-processing`

---

<a id="item-23"></a>
## [Qualcomm to Raise Phone Chip Prices from September 1](https://www.theverge.com/tech/972894/qualcomm-price-hikes-q2-2026-earnings) ⭐️ 6.0/10

Qualcomm CEO Cristiano Amon announced that the company will raise prices on all its processors starting September 1st, as reported by CNBC. This price hike will contribute to higher smartphone costs for consumers, potentially affecting the entire mobile device market. The price increases apply to all Qualcomm processors, and the announcement follows rumors from the previous week.

rss · The Verge · Jul 29, 21:41

**Background**: Qualcomm is a leading supplier of processors for smartphones, and its chips are used in many Android devices. Price increases by Qualcomm often lead to higher costs for phone manufacturers, which are then passed on to consumers.

**Tags**: `#Qualcomm`, `#smartphone`, `#pricing`, `#hardware`

---

<a id="item-24"></a>
## [OpenAI President Reveals Plans for AI Device Family](https://www.theverge.com/ai-artificial-intelligence/972709/openai-hardware-greg-brockman-interview) ⭐️ 6.0/10

OpenAI president Greg Brockman stated in an interview that the company is developing a 'family of devices' for interacting with its AI chatbots, though he did not confirm specific products like a rumored smart speaker. This signals OpenAI's expansion beyond software into hardware, potentially creating a new ecosystem for AI interaction and challenging existing smart device makers. Brockman did not confirm reports of a smart speaker launch in 2027 or earlier, and no technical specifications or release dates were provided.

rss · The Verge · Jul 29, 18:15

**Background**: OpenAI is best known for its ChatGPT chatbot and GPT language models. The company has primarily operated as a software and AI research organization, but hardware development would mark a significant strategic shift.

**Tags**: `#OpenAI`, `#AI hardware`, `#chatbots`, `#smart devices`

---

<a id="item-25"></a>
## [Google Play Store gets privacy-preserving age verification API](https://arstechnica.com/gadgets/2026/07/google-begins-global-rollout-of-age-verification-api-in-google-play/) ⭐️ 6.0/10

Google has begun a global rollout of a new privacy-preserving age verification API for the Play Store, which relies on parents to set age ranges via the Family Link app. This move helps app developers comply with age-restriction regulations without collecting sensitive personal data, potentially setting a standard for privacy-preserving age verification in mobile ecosystems. The API delegates age verification to parents via Family Link, meaning it only works for children whose parents have set up the service; it does not verify age directly for adult users.

rss · Ars Technica · Jul 29, 18:08

**Background**: Age verification is increasingly required by laws like the UK's Age Appropriate Design Code and various US state laws. Traditional methods often require uploading ID documents, which raises privacy concerns. Privacy-preserving approaches, such as using zero-knowledge proofs, allow verification without revealing unnecessary personal information.

<details><summary>References</summary>
<ul>
<li><a href="https://hyperverge.co/blog/age-verification-api/">Top 10 Age Verification APIs in 2026 | HyperVerge</a></li>
<li><a href="http://newamerica.org/oti/briefs/exploring-privacy-preserving-age-verification/">Exploring Privacy-Preserving Age Verification: A Close Look at Zero-Knowledge Proofs</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#age verification`, `#Google Play`, `#Android`, `#Family Link`

---

<a id="item-26"></a>
## [Boeing CEO Hints Starliner Could Launch This Year](https://arstechnica.com/space/2026/07/actually-starliner-might-fly-into-space-this-year/) ⭐️ 6.0/10

Boeing CEO Kelly Ortberg expressed optimism that the Starliner spacecraft might launch into space this year, marking a potential return to flight after a series of technical setbacks. If successful, this would restore Boeing's role in NASA's Commercial Crew Program and provide an alternative to SpaceX's Crew Dragon for crew transport to the ISS. The Starliner has faced years of delays and cost overruns, with its crewed test flight in 2024 experiencing thruster malfunctions that led to an uncrewed return. The planned Starliner-1 mission has been restructured as an uncrewed cargo flight.

rss · Ars Technica · Jul 29, 17:24

**Background**: Boeing's Starliner is a reusable crew capsule developed under NASA's Commercial Crew Program to transport astronauts to the ISS. It has suffered multiple delays and technical issues, including thruster problems during its first crewed test flight in June 2024, which forced an uncrewed return and left its astronauts to return via SpaceX Dragon.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Boeing_Starliner">Boeing Starliner - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Boeing_Starliner-1">Boeing Starliner-1 - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#space`, `#Boeing`, `#Starliner`, `#spaceflight`

---

<a id="item-27"></a>
## [AI Deciphers Lost Languages with Human Insight](https://arstechnica.com/science/2026/07/what-happens-when-you-put-ai-to-work-deciphering-lost-languages/) ⭐️ 6.0/10

An article explores how AI can assist in deciphering lost languages through pattern recognition, but emphasizes that human expertise remains essential for interpretation. This highlights the potential of AI to accelerate linguistic research and recover historical knowledge, while underscoring the irreplaceable role of human judgment in complex cultural contexts. The article provides a high-level overview without specific technical details or case studies, focusing on the complementary strengths of AI and human researchers.

rss · Ars Technica · Jul 29, 13:23

**Background**: Deciphering lost languages involves analyzing inscriptions or texts in unknown scripts, often with limited data. AI excels at detecting patterns and statistical regularities, but understanding meaning requires cultural and historical context that humans provide.

**Tags**: `#AI`, `#linguistics`, `#pattern recognition`, `#human-AI collaboration`

---

<a id="item-28"></a>
## [Elon Musk Launches X Money, Excluding Major US Markets](https://arstechnica.com/tech-policy/2026/07/elon-musk-finally-launches-x-money-what-could-possibly-go-wrong/) ⭐️ 6.0/10

Elon Musk has launched X Money, a digital payments service for X Premium and Premium+ subscribers in the US, but major US financial markets are excluded from the initial rollout. This launch marks Musk's long-awaited entry into fintech, but the exclusion of major markets suggests a bumpy rollout and may limit adoption, affecting X's ambition to become an 'everything app'. X Money offers instant transfers and a 6% yield, but is currently invite-only and limited to Premium subscribers, with no support for major US financial markets like New York or California.

rss · Ars Technica · Jul 29, 10:00

**Background**: X, formerly Twitter, was acquired by Elon Musk in 2022 and rebranded to X in 2023. Musk has long envisioned turning X into an 'everything app' with integrated financial services, similar to WeChat. X Money is the first major step toward that goal, but regulatory hurdles and technical challenges have delayed its launch.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/07/elon-musk-finally-launches-x-money-what-could-possibly-go-wrong/">Elon Musk finally launches X Money. What could possibly go wrong? - Ars Technica</a></li>
<li><a href="https://www.lowyat.net/2026/399915/x-money-premium-x-subscribers-us/">X Money Rolls Out To Premium X Subscribers In The US - Lowyat.NET</a></li>
<li><a href="https://americanbazaaronline.com/2026/07/29/elon-musks-x-rolls-out-x-money-offering-instant-transfers-and-6-yield-485437/">Elon Musk’s X rolls out X Money, offering instant transfers and 6% yield</a></li>

</ul>
</details>

**Tags**: `#Elon Musk`, `#X Money`, `#fintech`, `#product launch`

---

<a id="item-29"></a>
## [Revived Geothermal Plant in New Mexico Runs at Full Capacity](https://www.technologyreview.com/2026/07/29/1140896/geothermal-second-chance/) ⭐️ 6.0/10

In June 2024, Zanskar purchased a failing geothermal plant in New Mexico and, using AI-driven techniques, restored it to full capacity within two years. This revival demonstrates that AI and advanced geoscience can extend the life of aging geothermal plants, potentially unlocking more clean energy from existing resources. The plant's underground reservoir was cooling, making it uneconomical; Zanskar's AI models identified new drilling targets and optimized reinjection to restore heat output.

rss · MIT Technology Review · Jul 29, 17:58

**Background**: Geothermal power plants generate electricity by tapping underground reservoirs of hot water or steam. Over time, reservoirs can cool or deplete, reducing efficiency. Zanskar, an AI-native geothermal startup founded in 2021, uses machine learning to analyze geological data and improve exploration and reservoir management.

<details><summary>References</summary>
<ul>
<li><a href="https://grokipedia.com/page/Zanskar_geothermal_company">Zanskar (geothermal company)</a></li>
<li><a href="https://zanskar.com/">Zanskar Geothermal</a></li>

</ul>
</details>

**Tags**: `#geothermal`, `#energy`, `#technology`

---

<a id="item-30"></a>
## [MIT Tech Review Examines AI Hype vs. Practical Reality](https://www.technologyreview.com/2026/07/29/1140795/the-ai-hype-index-unsexy-ai/) ⭐️ 6.0/10

MIT Technology Review published an article analyzing the gap between AI hype and practical applications, highlighting dexterous robotics from 1X and the threat of job displacement. This analysis helps readers distinguish between overhyped AI promises and real-world progress, which is crucial for informed decision-making in business and policy. The article references 1X's demonstration of dexterous robotic hands capable of tasks like cooking, and cites economists' warnings about job displacement.

rss · MIT Technology Review · Jul 29, 08:42

**Background**: AI hype often focuses on futuristic breakthroughs, but practical applications like dexterous robotics are advancing steadily. 1X is a company developing humanoid robots for home chores, competing with Tesla and others.

<details><summary>References</summary>
<ul>
<li><a href="https://www.1x.tech/">1 X | Home Robots | 1 X Tech</a></li>
<li><a href="https://dawentsit.com/1x-robotics-just-built-the-worlds-most-advanced-robotic-hand/">1 X Robotics Just Built The World’s Most Advanced... - DawentsIT</a></li>

</ul>
</details>

**Tags**: `#AI`, `#hype`, `#robotics`, `#job displacement`

---

<a id="item-31"></a>
## [Biggest battery east of Mississippi to power AI complex](https://www.canarymedia.com/articles/batteries/eolian-build-pjm-biggest-battery-ai-ohio) ⭐️ 6.0/10

Eolian is building the largest battery storage facility east of the Mississippi River in Ohio to support an AI computing complex, marking a major integration of energy storage with AI infrastructure. This project highlights the surging energy demands of AI and the need for reliable, flexible power solutions, potentially setting a precedent for pairing large-scale batteries with data centers. The facility will be located near Columbus, Ohio, in an area already dense with AI computing infrastructure; its exact capacity and timeline have not been disclosed.

rss · Latitude Media (Canary Media) · Jul 29, 20:30

**Background**: AI computing, especially training large models, consumes enormous amounts of electricity, straining grids and raising environmental concerns. Battery storage can help stabilize the grid by storing excess renewable energy and discharging it during peak demand, ensuring reliable power for energy-intensive AI operations.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai">Energy demand from AI – Energy and AI – Analysis - IEA</a></li>
<li><a href="https://iee.psu.edu/news/blog/why-ai-uses-so-much-energy-and-what-we-can-do-about-it">AI’s Energy Demand: Challenges and Solutions for a Sustainable Future</a></li>

</ul>
</details>

**Tags**: `#AI`, `#energy storage`, `#infrastructure`, `#battery`

---

<a id="item-32"></a>
## [US Clean Energy Boom Faces Post-2030 Uncertainty](https://www.canarymedia.com/articles/clean-energy/us-clean-energy-boom-rhodium) ⭐️ 6.0/10

The article analyzes how the US clean energy boom, driven by recent policies, is expected to continue until 2030 but faces an uncertain future due to potential political changes, particularly under President Donald Trump's return to office. This matters because the US clean energy trajectory directly impacts global climate goals and the energy transition; political shifts could stall or reverse progress, affecting investments, jobs, and emissions reductions. The article notes that Trump has taken actions to undercut clean energy policies, but the boom is expected to persist through 2030 due to existing momentum and market forces; after 2030, the outlook becomes hazy depending on policy continuity.

rss · Latitude Media (Canary Media) · Jul 29, 09:00

**Background**: The US clean energy boom refers to rapid growth in renewable energy deployment, electric vehicles, and related industries, largely driven by the Inflation Reduction Act and other federal policies. Political changes, such as a new administration, can alter regulatory support and funding, creating uncertainty for long-term investments.

**Tags**: `#clean energy`, `#US policy`, `#climate`, `#energy transition`

---

<a id="item-33"></a>
## [Double Fine lays off staff after being dropped by Xbox](https://www.gamedeveloper.com/business/double-fine-making-layoffs-after-being-jettisoned-by-xbox) ⭐️ 6.0/10

Double Fine, the studio behind Psychonauts 2, announced layoffs after being jettisoned by Xbox, citing studio survival as the reason. This layoff reflects the ongoing trend of studio closures and downsizing in the game industry, even affecting acclaimed developers. It highlights the precarious nature of studio-publisher relationships. The exact number of layoffs was not disclosed, but the studio stated that the decision was made solely for survival. Double Fine was previously acquired by Xbox in 2019.

rss · Game Developer (Gamasutra) · Jul 29, 09:18

**Background**: Double Fine is a renowned independent game developer founded by Tim Schafer, known for titles like Psychonauts and Grim Fandango. Xbox acquired the studio in 2019 as part of its push to bolster first-party content. Being jettisoned likely means Xbox decided to divest or end support, leading to financial strain.

**Tags**: `#game development`, `#layoffs`, `#Xbox`, `#Double Fine`

---

<a id="item-34"></a>
## [Donkey Kong Bananza Devs Explain Destruction-Based Game Design at CEDEC 2026](https://www.4gamer.net/games/897/G089771/20260729064/) ⭐️ 6.0/10

At CEDEC 2026, the directors of Donkey Kong Bananza presented a session on how the game's core concept of destroying almost everything was realized from both game design and programming perspectives. This session offers valuable insights into how a seemingly chaotic destruction mechanic can be structured into a coherent and engaging gameplay loop, which is relevant for game developers working on physics-based or open-world action games. The game, released for Nintendo Switch 2 in July 2025, allows players to destroy terrain, enemies, and decorations. The session likely covered technical challenges such as real-time mesh destruction and maintaining performance on the new hardware.

rss · 4Gamer.net · Jul 29, 22:00

**Background**: Donkey Kong Bananza is the first original Donkey Kong game since 2014 and the first 3D platformer in the series since 1999. It was acclaimed as a killer app for the Switch 2. CEDEC is Japan's largest game developers conference, held annually in Yokohama.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Donkey_Kong_Bananza">Donkey Kong Bananza - Wikipedia</a></li>
<li><a href="https://infosec-conferences.com/event/20260722-computer-entertainment-developers-conference-cedec-2026/">Computer Entertainment Developers Conference (CEDEC) 2026, Yokohama, Japan | Cyber Event</a></li>

</ul>
</details>

**Tags**: `#game design`, `#programming`, `#Nintendo Switch 2`, `#action game`

---

<a id="item-35"></a>
## [Fostering Digital Talent Through 'Garage' Environments](https://www.4gamer.net/games/991/G999104/20260729026/) ⭐️ 6.0/10

At CEDEC 2026, Daiyuu Nobori of IPA delivered a keynote on nurturing Japan's digital talent by creating 'garage' environments where young people can freely play and fail, and proposed measuring outcomes by annual social benefit. This approach addresses Japan's critical shortage of digital infrastructure talent by emphasizing autonomy, experimentation, and tolerance of failure, which could reshape how organizations and educational institutions develop future engineers. Nobori is the creator of SoftEther VPN, a widely-used open-source multi-protocol VPN software, and currently serves at IPA (Information-technology Promotion Agency). The 'garage' concept draws from his own experience developing SoftEther VPN as a student project.

rss · 4Gamer.net · Jul 29, 08:02

**Background**: Japan faces a 'digital national crisis' due to an imbalance in IT talent distribution, with many workers in low-profit sectors. Nobori advocates shifting talent to scalable areas like cloud and AI. The 'garage' model encourages hands-on learning and risk-taking, inspired by successful examples like SoftEther VPN, which started as a university research project.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/SoftEther_VPN">SoftEther VPN</a></li>
<li><a href="https://www.itmedia.co.jp/enterprise/articles/2512/17/news037.html">IT人材の偏りが招く「国難」 IPA ... - ITmedia エンタープライズ</a></li>
<li><a href="https://jp.ign.com/cedec-2026">CEDEC 2026 | IGN Japan</a></li>

</ul>
</details>

**Tags**: `#talent development`, `#software engineering`, `#education`, `#CEDEC`

---

<a id="item-36"></a>
## [Polyphony Digital & Sony Demo 10,000-nit HDR Pipeline with Gran Turismo 7](https://www.4gamer.net/games/512/G051215/20260729033/) ⭐️ 6.0/10

At CEDEC 2026, Polyphony Digital and Sony demonstrated an end-to-end HDR pipeline using a 10,000-nit display and HDR camera, with Gran Turismo 7 as the showcase title. This demonstration highlights the potential of ultra-high brightness displays and unified HDR workflows for gaming and content creation, pushing the boundaries of visual realism. The display exceeded 10,000 nits peak brightness, far above typical HDR displays (around 1,000 nits), and the pipeline covered capture, processing, and display in HDR.

rss · 4Gamer.net · Jul 29, 08:00

**Background**: HDR (High Dynamic Range) technology expands the range of brightness and color in images, making them more lifelike. Most current HDR displays peak at around 1,000 nits, but 10,000-nit displays can reproduce extreme highlights like sunlight or reflections more accurately. End-to-end HDR pipelines ensure that HDR content is captured, processed, and displayed without loss of quality.

<details><summary>References</summary>
<ul>
<li><a href="https://jp.ign.com/cedec-2026">CEDEC 2026 | IGN Japan</a></li>
<li><a href="https://www.sciencedirect.com/science/article/abs/pii/S0923596518307859">Displaying detail in bright environments: A 10,000 nit display and its evaluation - ScienceDirect</a></li>

</ul>
</details>

**Tags**: `#HDR`, `#game graphics`, `#display technology`, `#Gran Turismo 7`

---

<a id="item-37"></a>
## [Halo: Campaign Evolved Full Remake Released](https://www.4gamer.net/games/956/G095668/20260729035/) ⭐️ 6.0/10

Halo Studios and Xbox Game Studios released 'Halo: Campaign Evolved' on July 29, 2026, a full remake of the original Halo: Combat Evolved campaign with modernized gameplay, graphics, and audio. This remake revitalizes a classic FPS campaign for a new generation of players, potentially rekindling interest in the Halo franchise and setting a precedent for how classic games can be updated without losing their core identity. The remake modernizes various aspects of the original game, including updated visuals, refined gameplay mechanics, and enhanced audio, while preserving the original campaign's story and structure.

rss · 4Gamer.net · Jul 29, 07:18

**Background**: Halo: Combat Evolved, released in 2001 for the original Xbox, is a landmark first-person shooter that defined the console FPS genre. 'Halo: Campaign Evolved' is a full remake, not a remaster, meaning it rebuilds the campaign from the ground up with modern technology.

**Tags**: `#Halo`, `#game remake`, `#FPS`, `#Xbox Game Studios`

---

<a id="item-38"></a>
## [CEDEC Talk Debunks Mobile Game Marketing Myths with Data](https://www.4gamer.net/games/991/G999104/20260729007/) ⭐️ 6.0/10

At CEDEC 2026, CyberAgent's Masaaki Kado presented a talk titled 'Lies in Smartphone Game Marketing 2026,' using real data to challenge common beliefs about pre-registration, launch ads, and measurement. This talk provides data-backed insights that could help mobile game developers optimize their marketing strategies and avoid costly mistakes based on unverified assumptions. The talk specifically examined the myth that shorter pre-registration periods are better, and analyzed the effectiveness of launch-day advertising and proper measurement techniques.

rss · 4Gamer.net · Jul 29, 05:28

**Background**: CEDEC (Computer Entertainment Developers Conference) is Japan's largest game developer conference, held annually. Mobile game marketing often relies on industry heuristics that may not be backed by data. This talk aimed to provide empirical evidence to guide better decision-making.

<details><summary>References</summary>
<ul>
<li><a href="https://www.global.toshiba/jp/company/digitalsolution/event/2026/0722-0724.html">CEDEC 2026 | イベント情報：デジタル事業 | 東芝</a></li>
<li><a href="https://infosec-conferences.com/event/20260722-computer-entertainment-developers-conference-cedec-2026/">Computer Entertainment Developers Conference (CEDEC) 2026, Yokohama, Japan | Cyber Event</a></li>

</ul>
</details>

**Tags**: `#mobile gaming`, `#game marketing`, `#data-driven`, `#industry analysis`

---

<a id="item-39"></a>
## [EverQuest Legends Launches with Solo Play and Multiclassing](https://www.4gamer.net/games/993/G099328/20260729021/) ⭐️ 6.0/10

Daybreak Game Company and indie studio GameJawn have officially launched EverQuest Legends, a modernized MMORPG that reimagines the original EverQuest. The game introduces solo-friendly content and a multiclass system allowing players to combine up to three classes. This launch revitalizes a classic MMORPG franchise for modern audiences, lowering barriers for solo players while retaining the nostalgic world of Norrath. It could attract both veteran EverQuest fans and new players seeking a classic MMO experience with contemporary quality-of-life features. The multiclass system lets players combine up to three classes, with the third class unlocking at level 10. All content, including raids, can be completed solo, though group play remains optional.

rss · 4Gamer.net · Jul 29, 04:55

**Background**: EverQuest, launched in 1999, is one of the pioneering MMORPGs that defined the genre. EverQuest Legends rebuilds the classic game with modern features such as solo-friendly gameplay, multiclassing, smaller raids, and quality-of-life improvements, while preserving the original's world, races, zones, and music.

<details><summary>References</summary>
<ul>
<li><a href="https://eqlegends.wiki/">EQ Legends Wiki — EverQuest Legends Classes, Guides & Database</a></li>
<li><a href="https://everquest-legends-wiki.wiki/">EverQuest Legends Wiki — Classes, Solo Guide</a></li>
<li><a href="https://expcarry.com/everquest-legends-classic-norrath">EverQuest Legends Revives Classic Norrath</a></li>

</ul>
</details>

**Tags**: `#MMORPG`, `#EverQuest`, `#game launch`, `#multiclass`

---