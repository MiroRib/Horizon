---
layout: default
title: "Horizon Summary: 2026-06-15 (EN)"
date: 2026-06-15
lang: en
---

> From 169 items, 32 important content pieces were selected

---

1. [Backdoor in LinkedIn Job Offer Exploits npm Prepare Script](#item-1) ⭐️ 9.0/10
2. [Fox to Acquire Roku for $22 Billion](#item-2) ⭐️ 9.0/10
3. [ALS Patient Becomes First Long-Term Power User of Brain Implant for Speech](#item-3) ⭐️ 9.0/10
4. [Iroh 1.0: Dial Keys, Not IPs](#item-4) ⭐️ 8.0/10
5. [TimescaleDB Hypercore Compression Cuts Storage by 98%](#item-5) ⭐️ 8.0/10
6. [Typst 0.15.0 Adds Multiple Bibliographies](#item-6) ⭐️ 8.0/10
7. [US shutdown of Anthropic models fuels sovereign AI push](#item-7) ⭐️ 8.0/10
8. [AMD quietly removes memory encryption from consumer CPUs](#item-8) ⭐️ 8.0/10
9. [Microsoft may close Double Fine, Ninja Theory studios](#item-9) ⭐️ 8.0/10
10. [US Battery Manufacturing Output Hits Record High](#item-10) ⭐️ 7.0/10
11. [Hacker News Users Share Local LLM Coding Setups](#item-11) ⭐️ 7.0/10
12. [Hetzner Announces Major Cloud Server Price Increase](#item-12) ⭐️ 7.0/10
13. [Commander Keen White Papers Detail Smooth Scrolling Tech](#item-13) ⭐️ 7.0/10
14. [Copper transport drug restores memory in Alzheimer's mice](#item-14) ⭐️ 7.0/10
15. [Chrome to Kill Last Ad Blocker Workarounds in Versions 150 and 151](#item-15) ⭐️ 7.0/10
16. [Big Tech Lobbies for Federal AI Preemption](#item-16) ⭐️ 7.0/10
17. [UK Proposes Social Media Ban for Under-16s, Overnight Curfews](#item-17) ⭐️ 7.0/10
18. [China Targets 40% New Energy Heavy Truck Sales by 2030](#item-18) ⭐️ 7.0/10
19. [UCSD to Build Low-Carbon Data Center from 2,000 Pixel Phones](#item-19) ⭐️ 7.0/10
20. [A Personal Reflection on Loving Computers](#item-20) ⭐️ 6.0/10
21. [Homelab AI Dev Platform Sparks Community Discussion](#item-21) ⭐️ 6.0/10
22. [COVID shots still protect hearts, study confirms](#item-22) ⭐️ 6.0/10
23. [Chinese Rocket Breakup Near Starlink Creates Space Debris](#item-23) ⭐️ 6.0/10
24. [20 Years of Intel Macs: Apple's Two Major Switches](#item-24) ⭐️ 6.0/10
25. [Russia to Address Long-Standing ISS Cracks](#item-25) ⭐️ 6.0/10
26. [Why South Koreans Embrace AI So Enthusiastically](#item-26) ⭐️ 6.0/10
27. [Solid-State ACs: Cool Promise, Scientific Doubt](#item-27) ⭐️ 6.0/10
28. [AI Load Growth Reshapes Utility Business Models](#item-28) ⭐️ 6.0/10
29. [US Clean Energy Sets Multiple Records This Spring](#item-29) ⭐️ 6.0/10
30. [EA Launches In-Game Advertising Platform](#item-30) ⭐️ 6.0/10
31. [Google Earth Web Adds Flight Simulator](#item-31) ⭐️ 6.0/10
32. [SteamOS Beta Expands to Intel Handhelds Like MSI Claw](#item-32) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Backdoor in LinkedIn Job Offer Exploits npm Prepare Script](https://roman.pt/posts/linkedin-backdoor/) ⭐️ 9.0/10

A job applicant discovered a backdoor hidden in a GitHub repository sent by a recruiter during a LinkedIn job interview, which uses npm's prepare script to execute arbitrary code upon npm install. This attack vector is particularly dangerous because it mimics a common interview task—reviewing a broken repository—and could compromise many developers' machines, leading to supply chain attacks or credential theft. The backdoor was buried in commented-out test code and executed via npm's prepare lifecycle script, which runs automatically after npm install. The payload could receive commands from a remote server.

hackernews · lwhsiao · Jun 15, 20:00 · [Discussion](https://news.ycombinator.com/item?id=48546294)

**Background**: npm's prepare script is a lifecycle hook that runs before publishing and after npm install, often used for build steps. Supply chain attacks via npm have become increasingly common, with recent incidents like the Sha1-Hulud attack compromising popular packages.

<details><summary>References</summary>
<ul>
<li><a href="https://stackoverflow.com/questions/44499912/why-is-npm-running-prepare-script-after-npm-install-and-how-can-i-stop-it">node.js - Why is npm running prepare script after npm install, and how ...</a></li>
<li><a href="https://thehackernews.com/2026/06/github-to-disable-npm-install-scripts.html">GitHub to Disable npm Install Scripts by Default to Stop Supply Chain ...</a></li>
<li><a href="https://docs.npmjs.com/cli/v8/using-npm/scripts/?v=true">scripts - npm Docs</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that this attack is uncomfortably close to normal interview tasks, and called for better cybercrime reporting mechanisms. Some criticized npm for not blocking scripts by default, while others noted the legal implications.

**Tags**: `#security`, `#supply chain attack`, `#npm`, `#cybercrime`, `#hiring`

---

<a id="item-2"></a>
## [Fox to Acquire Roku for $22 Billion](https://www.wsj.com/business/deals/fox-roku-deal-f6e564f9) ⭐️ 9.0/10

Fox Corporation announced it is acquiring Roku, the leading streaming platform, in a $22 billion deal that will give Fox control over the operating system used by tens of millions of households worldwide. This acquisition raises significant antitrust concerns as it combines a major content producer with a dominant hardware platform, potentially threatening Roku's historical platform neutrality and giving Fox undue influence over the streaming landscape. The deal is valued at $22 billion and is expected to close pending regulatory approval. Roku's familiar purple interface may remain unchanged, but the acquisition could lead to preferential treatment for Fox-owned content and increased advertising integration.

hackernews · thm · Jun 15, 12:50 · [Discussion](https://news.ycombinator.com/item?id=48540499)

**Background**: Roku is a streaming device and platform company known for its simple, app-first user experience and platform neutrality, making it a popular choice for consumers and streaming services alike. Media consolidation has been a growing concern, with recent mergers like Tegna-Nexstar giving one company coverage of 80% of U.S. TV households, prompting antitrust lawsuits.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Concentration_of_media_ownership">Concentration of media ownership - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community sentiment is overwhelmingly negative, with users expressing pessimism about Roku losing its service-agnostic nature and becoming a vehicle for Fox's content. Many commenters argue that Fox should not be allowed to purchase direct access to such a large portion of American households, and some are already migrating to alternative platforms like Nvidia Shield.

**Tags**: `#acquisition`, `#streaming`, `#antitrust`, `#media`, `#Roku`

---

<a id="item-3"></a>
## [ALS Patient Becomes First Long-Term Power User of Brain Implant for Speech](https://www.technologyreview.com/2026/06/15/1138953/man-als-first-power-user-brain-implant-speak-bci/) ⭐️ 9.0/10

Casey Harrell, a man with ALS, has used a brain-computer interface (BCI) for nearly three years, accumulating thousands of hours of use to speak sentences in real time. He is considered the first long-term 'power user' of such a speech BCI. This milestone demonstrates that BCIs can function reliably over years in real-world settings, moving beyond short-term lab demonstrations. It offers hope for restoring communication in paralyzed individuals and accelerates the path toward commercial neuroprosthetics. Harrell first used the BCI to speak in 2023, and the system has been refined over thousands of hours of use. The implant uses electrodes placed in the speech cortex to decode neural signals into synthesized speech.

rss · MIT Technology Review · Jun 15, 15:12

**Background**: A brain-computer interface (BCI) creates a direct communication link between brain activity and an external device. For speech, BCIs record neural signals from areas involved in speech production and translate them into words or sounds. ALS progressively paralyzes muscles, including those for speech, making BCIs a promising assistive technology.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Brain–computer_interface">Brain–computer interface - Wikipedia</a></li>
<li><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11053081/">Online speech synthesis using a chronically implanted...</a></li>
<li><a href="https://spectrum.ieee.org/bci-speech-synthesis">BCI Speech Synthesis Using Voice-Cloning AI Model - IEEE Spectrum</a></li>

</ul>
</details>

**Tags**: `#brain-computer interface`, `#ALS`, `#neuroprosthetics`, `#speech synthesis`, `#medical technology`

---

<a id="item-4"></a>
## [Iroh 1.0: Dial Keys, Not IPs](https://www.iroh.computer/blog/v1) ⭐️ 8.0/10

Iroh 1.0 has been released as a peer-to-peer networking library that uses cryptographic dial keys instead of IP addresses for app-to-app connections. This simplifies secure direct connections for developers, similar to Tailscale but at the application layer, enabling easier peer-to-peer communication in apps without requiring users to manage network configurations. Iroh supports IPv4, IPv6, and relay transports out of the box, and now allows custom transport implementations via a plugin system.

hackernews · chadfowler · Jun 15, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48542480)

**Background**: Traditional networking relies on IP addresses, which can change or be blocked. Iroh uses cryptographic keys as stable identifiers, enabling direct connections even behind NATs or firewalls, similar to how Tailscale creates a secure mesh network at the network layer.

<details><summary>References</summary>
<ul>
<li><a href="https://www.iroh.computer/blog/v1">Iroh 1.0 - Dial Keys, not IPs - Iroh</a></li>
<li><a href="https://github.com/n0-computer/iroh">GitHub - n0-computer/iroh: IP addresses break, dial keys instead. Modular networking stack in Rust. · GitHub</a></li>
<li><a href="https://tailscale.com/kb/1456/osi">Learn how Tailscale relates to the OSI model layers .</a></li>

</ul>
</details>

**Discussion**: Commenters compared Iroh to Tailscale at the application layer, and developers clarified that custom transports like WebRTC or BLE can be added via the new plugin system. Some users expressed confusion about the problem Iroh solves, while others praised its potential for P2P tools.

**Tags**: `#networking`, `#peer-to-peer`, `#rust`, `#open-source`, `#p2p`

---

<a id="item-5"></a>
## [TimescaleDB Hypercore Compression Cuts Storage by 98%](https://roszigit.com/en/blog/timescaledb-compression-hypercore) ⭐️ 8.0/10

TimescaleDB introduced Hypercore compression, which uses columnar storage and type-aware encoding to achieve up to 98% storage reduction for time-series data. This compression significantly lowers storage costs and can accelerate analytical queries on time-series data, making TimescaleDB more competitive with specialized time-series databases. Hypercore employs methods like delta encoding, run-length encoding, and dictionary compression, but query performance trade-offs exist, as noted in community discussions.

hackernews · lkanwoqwp · Jun 15, 17:29 · [Discussion](https://news.ycombinator.com/item?id=48544451)

**Background**: TimescaleDB is a PostgreSQL extension for time-series data. Traditional row-based storage is inefficient for analytical queries that scan many rows but few columns. Columnar storage organizes data by column, enabling better compression and faster scans for such workloads.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.tigerdata.com/use-timescale/latest/hypercore/compression-methods/">Tiger Data Documentation | About compression methods</a></li>
<li><a href="https://docs.timescale.com/use-timescale/latest/compression/">Timescale Documentation | Compression</a></li>
<li><a href="https://www.linkedin.com/pulse/row-vs-columnar-storage-secret-behind-blazing-fast-analytics-rashid-wawec">Row vs . Columnar Storage : The Secret Behind Blazing-Fast Analytics!</a></li>

</ul>
</details>

**Discussion**: Community comments highlight trade-offs: compression can slow down some queries due to decompression overhead. Alternatives like deltaX and swinging-door algorithms are discussed, and licensing concerns are raised as compression requires a non-Apache license.

**Tags**: `#TimescaleDB`, `#compression`, `#time-series`, `#PostgreSQL`, `#database`

---

<a id="item-6"></a>
## [Typst 0.15.0 Adds Multiple Bibliographies](https://typst.app/docs/changelog/0.15.0/) ⭐️ 8.0/10

Typst 0.15.0 introduces support for multiple bibliographies in a single document, along with improved HTML export including automatic MathML conversion for equations. This release addresses a long-standing user request, making Typst more suitable for complex academic documents like dissertations and books that require categorized references. The multiple bibliographies feature allows users to split references into sections (e.g., books, journals) using the new 'bibliography' function with a 'title' parameter. Additionally, HTML export now automatically converts equations to MathML for better web accessibility.

hackernews · schu · Jun 15, 17:24 · [Discussion](https://news.ycombinator.com/item?id=48544396)

**Background**: Typst is a modern markup-based typesetting system designed as an alternative to LaTeX and Word, offering simpler syntax and faster compilation. It is particularly popular in scientific and academic communities for document preparation.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/typst/typst/issues/1097">Multiple bibliographies · Issue #1097 · typst/typst</a></li>
<li><a href="https://github.com/typst/typst">GitHub - typst / typst : A markup-based typesetting system that is...</a></li>

</ul>
</details>

**Discussion**: Community feedback is largely positive, with users praising the multiple bibliographies feature and improved HTML support. However, some users note ongoing issues with footnotes, particularly discursive footnotes containing bibliography references, which can cause layout problems.

**Tags**: `#typesetting`, `#open source`, `#software release`, `#typst`, `#document processing`

---

<a id="item-7"></a>
## [US shutdown of Anthropic models fuels sovereign AI push](https://www.theverge.com/ai-artificial-intelligence/949986/anthropic-fable-mythos-shutdown-sovereign-ai) ⭐️ 8.0/10

The US government ordered Anthropic to shut down its latest AI models, Fable 5 and Mythos 5, blocking access for all foreign nationals, including Anthropic's own employees abroad. This incident highlights the risks of relying on US-controlled AI infrastructure, accelerating global efforts to develop sovereign AI capabilities independent of American technology. Fable 5 and Mythos 5, launched on June 9th, are among the most powerful AI models, with Fable 5 capable of rebuilding web app source code from screenshots alone. The shutdown followed a White House demand and occurred amid Anthropic's ongoing dispute with the Pentagon.

rss · The Verge · Jun 15, 18:10

**Background**: Anthropic is a leading US AI company behind the Claude series of models. Sovereign AI refers to national strategies to build independent AI infrastructure and models, reducing reliance on foreign providers. The UK, for example, established a £500 million Sovereign AI Fund in 2026 to support domestic AI companies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.bbc.com/news/articles/c932g3v3e13o">Anthropic's Claude Fable 5 and Mythos 5 AI suspended over security fears</a></li>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://en.wikipedia.org/wiki/Sovereign_AI_Fund">Sovereign AI Fund</a></li>

</ul>
</details>

**Tags**: `#AI`, `#geopolitics`, `#Anthropic`, `#AI regulation`, `#sovereign AI`

---

<a id="item-8"></a>
## [AMD quietly removes memory encryption from consumer CPUs](https://arstechnica.com/security/2026/06/users-cry-foul-after-amd-stripped-memory-crypto-from-its-consumer-cpus/) ⭐️ 8.0/10

AMD has silently removed Transparent Secure Memory Encryption (TSME) from its consumer Ryzen CPUs, a feature that encrypted all system memory to protect against physical attacks like cold boot attacks. This removal exposes consumer systems to cold boot and other physical memory attacks, potentially compromising sensitive data. It also erodes user trust in AMD's commitment to security, especially as the move was made without public announcement. TSME is a BIOS-level feature that encrypts all memory using a single key generated by the AMD Secure Processor at boot. The option was previously available in BIOS settings under AMD CBS, but AMD has now disabled it in consumer CPU firmware without warning.

rss · Ars Technica · Jun 15, 17:55

**Background**: Transparent Secure Memory Encryption (TSME) is a hardware-based memory encryption technology that encrypts the entire contents of system memory, making data inaccessible to attackers who gain physical access to the machine. It is distinct from standard Secure Memory Encryption (SME), which requires OS or hypervisor support. TSME was previously available on AMD Ryzen CPUs as a BIOS option, but AMD has now removed it from consumer chips, likely to differentiate product lines or reduce costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/developer/sev.html">AMD Secure Encrypted Virtualization (SEV) | AMD</a></li>
<li><a href="https://mricher.fr/post/amd-memory-encryption/">Memory encryption: AMD SME , TSME and SEV</a></li>
<li><a href="https://xeber.world/en/article/amd-removes-tsme-security-from-consumer-ryzen-cpus-without-warning-09496c">AMD Removes TSME from Consumer Ryzen CPUs Without Warning</a></li>

</ul>
</details>

**Discussion**: Users on forums and social media have expressed outrage, accusing AMD of a covert move that undermines security. Many are calling for AMD to restore the feature or provide a clear explanation, while some speculate it may be a cost-cutting measure or a push to upsell enterprise chips.

**Tags**: `#AMD`, `#CPU security`, `#TSME`, `#hardware`, `#controversy`

---

<a id="item-9"></a>
## [Microsoft may close Double Fine, Ninja Theory studios](https://www.pcgamer.com/gaming-industry/double-fine-ninja-theory-and-more-xbox-studios-reportedly-at-risk-of-closure/) ⭐️ 8.0/10

A report from The Verge indicates that Microsoft is planning to close several Xbox Game Studios, including Ninja Theory (Hellblade series) and Double Fine (Psychonauts series), as part of a major restructuring. Staff were informed on a call on Monday, though some studios may seek buyers. These closures would eliminate critically acclaimed studios with strong fan followings, potentially reducing the diversity of Xbox's first-party portfolio. It signals Microsoft's shift toward prioritizing profitability over creative experimentation, which could reshape the gaming industry landscape. The closures come shortly after a report of major Xbox layoffs, and are part of a broader 'Xbox reset' that may also affect Compulsion Games. Ninja Theory was acquired by Microsoft in 2018, while Double Fine joined in 2019.

rss · PC Gamer · Jun 15, 21:43

**Background**: Microsoft has been restructuring its gaming division to focus on high-potential projects and long-term growth, as seen in recent layoffs and studio evaluations. Ninja Theory is known for narrative-driven games like Hellblade, while Double Fine is famous for quirky titles like Psychonauts. Both studios have a history of financial challenges despite critical success.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2025/07/02/microsoft-laying-off-about-9000-employees-in-latest-round-of-cuts.html">cnbc.com/ 2025 /07/02/microsoft-laying-off-about-9000-employees-in...</a></li>
<li><a href="https://www.geeky-gadgets.com/project-helix-next-gen-hardware/">Why Xbox is Returning to Exclusives for Major... - Geeky Gadgets</a></li>
<li><a href="https://www.doublefine.com/about">About Double Fine Productions | Double Fine Productions</a></li>

</ul>
</details>

**Tags**: `#gaming`, `#Microsoft`, `#Xbox`, `#studio closures`, `#industry news`

---

<a id="item-10"></a>
## [US Battery Manufacturing Output Hits Record High](https://fred.stlouisfed.org/series/IPG33591S) ⭐️ 7.0/10

US battery manufacturing output continues to break records, as shown by the Federal Reserve's industrial production index for batteries (IPG33591S). This growth signals strengthening domestic energy storage supply chains, which is crucial for national security and the clean energy transition, though global competition remains intense. Despite record US output, China's cell production capacity in 2025 is estimated at 1,755 GWh, dwarfing the US's 70 GWh and Europe's 252 GWh.

hackernews · epistasis · Jun 15, 20:28 · [Discussion](https://news.ycombinator.com/item?id=48546616)

**Background**: Battery manufacturing is a key industry for electric vehicles and grid storage. The US has been investing in domestic production to reduce reliance on imports, especially from China.

**Discussion**: Commenters note the vast gap between US and Chinese production capacity, with some suggesting strategies like allowing Chinese firms to build plants in the US and then nationalizing them. Others highlight the BYD Blade 2.0 battery's advanced specs.

**Tags**: `#battery manufacturing`, `#energy storage`, `#US economy`, `#industrial policy`, `#global competition`

---

<a id="item-11"></a>
## [Hacker News Users Share Local LLM Coding Setups](https://news.ycombinator.com/item?id=48542100) ⭐️ 7.0/10

Hacker News users are actively sharing their experiences replacing cloud-based coding assistants like Claude and GPT with local models such as Qwen3.6 35B and Gemma, using tools like Pi coding harness, llama.cpp, and Continue extension. This shift highlights growing demand for data privacy, cost savings, and offline capability in AI-assisted coding, potentially reducing reliance on expensive cloud subscriptions and enabling more developers to use powerful models locally. Users report achieving ~150 tokens/second on dual RTX 3090 setups with Qwen3.6 35B, while others note that local models are not as smart as frontier models but sufficient for most daily coding tasks. Some users still fall back to cloud models for complex tasks.

hackernews · cloudking · Jun 15, 14:46

**Background**: Local LLMs are large language models that run on a user's own hardware rather than on cloud servers. Tools like Ollama, llama.cpp, and Continue enable developers to integrate these models into their coding workflow. The Qwen3.6 35B model is a Mixture-of-Experts (MoE) model that balances performance and resource usage.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/data-science-collective/how-to-build-your-own-llm-coding-assistant-with-qwen2-5-coder-b26aaadf071d">How to Build Your Own LLM Coding Assistant With... | Medium</a></li>
<li><a href="https://vasilkoff.com/blog/vscodium-and-ollama">VSCodium + Ollama: Local LLM Coding Setup Guide</a></li>
<li><a href="https://www.packetswitch.co.uk/using-the-continue-vscode-extension-and-local-llms-for-improved-coding/">How to Use Continue and Local LLMs for Better Coding in VSCode?</a></li>

</ul>
</details>

**Discussion**: The community is enthusiastic about local setups, with many sharing detailed configurations and performance metrics. Some users caution that local models still lag behind cloud models in capability, but overall sentiment is positive, especially for privacy-conscious developers. A few commenters question whether the trade-offs are worth it for all users.

**Tags**: `#local LLM`, `#coding assistant`, `#Qwen`, `#data privacy`, `#self-hosted`

---

<a id="item-12"></a>
## [Hetzner Announces Major Cloud Server Price Increase](https://docs.hetzner.com/general/infrastructure-and-availability/price-adjustment/#cloud-servers) ⭐️ 7.0/10

Hetzner has announced a significant price increase for its cloud servers, with some configurations seeing up to a 3x rise, effective from February 1, 2025 for existing servers and June 15, 2026 for dedicated servers. This price hike reflects the broader impact of the AI boom on hardware costs, affecting developers and businesses that rely on Hetzner's affordable cloud services. It may push users to consider alternatives or adjust their infrastructure budgets. The increase applies to cloud servers and load balancers, with new pricing already published. Hetzner cites hardware cost increases and product standardization as reasons, and introduces a 'limited' category for servers with constrained availability.

hackernews · tuhtah · Jun 15, 13:19 · [Discussion](https://news.ycombinator.com/item?id=48540844)

**Background**: Hetzner is a German hosting provider known for its cost-effective dedicated servers and cloud services, popular among developers and small businesses. The AI boom has driven up demand for GPUs and memory, increasing hardware costs across the industry.

<details><summary>References</summary>
<ul>
<li><a href="https://lowendtalk.com/discussion/200033/hetzner-black-friday-price-increase-surprise">Hetzner Black Friday Price Increase Surprise — LowEndTalk</a></li>
<li><a href="https://cloudnews.tech/hetzner-will-increase-prices-on-june-15-and-simplify-its-server-catalog/">Hetzner Will Increase Prices on June 15 and Simplify Its Server Catalog</a></li>

</ul>
</details>

**Discussion**: The community expressed shock at the magnitude of the increase, with many questioning the justification for a 3x rise. Some users noted that hardware costs have indeed surged, while others criticized Hetzner for not refreshing their hardware lineup in years.

**Tags**: `#cloud`, `#pricing`, `#Hetzner`, `#hardware costs`, `#AI boom`

---

<a id="item-13"></a>
## [Commander Keen White Papers Detail Smooth Scrolling Tech](https://forgottenbytes.net/commander_keen.html) ⭐️ 7.0/10

ForgottenBytes.net published white papers detailing the technical innovations behind Commander Keen's smooth scrolling on early PC hardware, including the adaptive tile refresh technique. This documentation preserves a pivotal moment in game engine history, showing how id Software overcame severe hardware limitations to create the first smooth-scrolling platformer on PC, which directly led to the development of Wolfenstein 3D and Doom. The adaptive tile refresh technique built a virtual screen in VRAM and leveraged the EGA CRTC's ability to read four bytes in parallel, achieving smooth scrolling despite the PC's limited sprite-rendering capabilities compared to consoles like the SNES.

hackernews · mfiguiere · Jun 15, 17:52 · [Discussion](https://news.ycombinator.com/item?id=48544781)

**Background**: In the late 1980s, PC hardware lacked dedicated sprite hardware, making smooth side-scrolling games difficult. Commander Keen, released in 1990, was a breakthrough that proved PCs could run colorful platformers. The game's engine, later known as idTech 1, was developed by John Carmack and John Romero.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Commander_Keen">Commander Keen - Wikipedia</a></li>
<li><a href="https://ohtldr.com/summary/commander-keens-adaptive-tile-refresh/">Commander Keen ’s adaptive tile refresh – Oh TL;DR</a></li>
<li><a href="https://www.neogaf.com/threads/i-do-not-understand-why-people-consider-commander-keen-important-and-a-technical-achievement-in-the-industry.1655244/">I do not understand why people consider Commander Keen ... | NeoGAF</a></li>

</ul>
</details>

**Discussion**: Commenters praised the white papers and recommended the book 'Masters of Doom' for context. One user noted the importance of explaining why PCs struggled with sprite rendering compared to contemporary consoles like the SNES, while another suggested the site resembles Fabien Sanglard's work.

**Tags**: `#game development`, `#retro computing`, `#id Software`, `#game engines`, `#technical history`

---

<a id="item-14"></a>
## [Copper transport drug restores memory in Alzheimer's mice](https://www.monash.edu/news/articles/copper-drug-restores-memory-and-clears-toxic-alzheimers-proteins) ⭐️ 7.0/10

Researchers at Monash University found that a copper transport drug, previously evaluated for safety in other diseases, restored memory and cleared toxic amyloid-beta proteins in a mouse model of Alzheimer's disease. This could lead to a fast-tracked human trial for Alzheimer's, offering a new therapeutic approach that targets copper dysregulation rather than the controversial amyloid hypothesis. The drug is a copper transport compound that corrects abnormal copper distribution in the brain, reducing amyloid plaques and improving cognitive function in mice.

hackernews · bookofjoe · Jun 15, 14:48 · [Discussion](https://news.ycombinator.com/item?id=48542132)

**Background**: Alzheimer's disease is characterized by accumulation of amyloid-beta plaques and abnormal copper distribution in the brain. The amyloid hypothesis has been questioned due to repeated failures of amyloid-targeting therapies in clinical trials.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48542132">Copper transport drug restores memory and clears... | Hacker News</a></li>
<li><a href="https://colab.ws/articles/10.1007/s00249-007-0235-2">Copper transport and Alzheimer ’ s disease | CoLab</a></li>
<li><a href="https://www.academia.edu/115715222/In_vivo_reduction_of_amyloid_β_by_a_mutant_copper_transporter">(PDF) In vivo reduction of amyloid-β by a mutant copper transporter</a></li>

</ul>
</details>

**Discussion**: Community comments express skepticism about the amyloid hypothesis and note that many Alzheimer's treatments work in mice but fail in humans. Some commenters appreciate the focus on copper dysregulation as a potential alternative mechanism.

**Tags**: `#Alzheimer's`, `#drug discovery`, `#neuroscience`, `#amyloid-beta`, `#copper`

---

<a id="item-15"></a>
## [Chrome to Kill Last Ad Blocker Workarounds in Versions 150 and 151](https://www.theverge.com/tech/950005/google-chrome-removing-ad-blocker-loopholes) ⭐️ 7.0/10

Google Chrome versions 150 and 151, expected in late June and July 2025, will remove the final workarounds that allowed older Manifest V2 ad blockers like uBlock Origin to continue functioning. This marks the complete transition to Manifest V3, which restricts ad-blocking capabilities, affecting millions of Chrome users who rely on powerful blockers like uBlock Origin. The changes will disable the remaining enterprise policies and flags that allowed Manifest V2 extensions to run. Users who want full ad blocking will need to switch to Manifest V3 alternatives like uBlock Origin Lite.

rss · The Verge · Jun 15, 18:06

**Background**: Manifest V3 is a new extension platform introduced by Google to improve privacy, security, and performance. It replaces Manifest V2, which allowed extensions like uBlock Origin to use the powerful webRequest API for blocking network requests. Under Manifest V3, extensions are limited to the declarativeNetRequest API, which reduces flexibility for ad blockers. Google began phasing out Manifest V2 in 2024, but some workarounds kept older extensions alive until now.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.chrome.com/docs/extensions/develop/migrate/what-is-mv3">Extensions / Manifest V 3 | Chrome for Developers</a></li>
<li><a href="https://en.wikipedia.org/wiki/UBlock_Origin">uBlock Origin - Wikipedia</a></li>
<li><a href="https://chromewebstore.google.com/detail/ublock-origin-lite/ddkjiahejlhfcafbddmgiahcphecmpfh">uBlock Origin Lite - Chrome Web Store</a></li>

</ul>
</details>

**Tags**: `#Chrome`, `#ad blocking`, `#Manifest V3`, `#privacy`, `#browser extensions`

---

<a id="item-16"></a>
## [Big Tech Lobbies for Federal AI Preemption](https://www.theverge.com/policy/949970/ai-regulation-child-safety-kosa-congress) ⭐️ 7.0/10

Big Tech lobbyists are aggressively pushing Congress to pass a federal AI law that would preempt state-level regulations, creating a single national framework for AI governance. If successful, this would override state laws like Colorado's AI Act, potentially weakening consumer protections and consolidating regulatory power in Washington, affecting how AI is developed and deployed nationwide. The proposed preemption would freeze state AI laws for three years, but states would retain authority over AI deployment and use, not development. Child safety is the only area where the federal framework would impose obligations on AI developers.

rss · The Verge · Jun 15, 17:44

**Background**: Currently, the U.S. lacks comprehensive federal AI regulation, leading states like Colorado to pass their own laws. Preemption would replace this patchwork with a single federal standard, but critics argue it could stall stronger state-level protections.

<details><summary>References</summary>
<ul>
<li><a href="https://www.imperiochaos.com/insights/federal-ai-preemption-power-consolidation">Federal AI Preemption Is a Power Consolidation... — Imperio Chaos</a></li>
<li><a href="https://www.justsecurity.org/134693/beware-ai-preemption-trap/">Beware the AI Preemption Trap</a></li>
<li><a href="https://www.stateside.com/blog/trumps-national-framework-vs-state-ai-laws">Trump’s “National Framework” vs . State AI Laws | Stateside Associates</a></li>

</ul>
</details>

**Tags**: `#AI regulation`, `#Big Tech`, `#lobbying`, `#policy`, `#preemption`

---

<a id="item-17"></a>
## [UK Proposes Social Media Ban for Under-16s, Overnight Curfews](https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/) ⭐️ 7.0/10

The UK government announced plans to ban social media for children under 16 and is considering overnight curfews and breaks from infinite scrolling for under-18s, with details to be released in July 2026. This represents one of the most aggressive regulatory moves globally to protect children online, but critics warn it may push kids to unregulated alternatives and can be easily bypassed with VPNs. The ban does not apply to messaging services like WhatsApp and Signal. The government is also consulting on age limits for sign-ups and new restrictions on AI chatbot access.

rss · Ars Technica · Jun 15, 20:14

**Background**: Social media platforms use algorithms and infinite scrolling to maximize engagement, which can be addictive and harmful to young users. VPNs allow users to encrypt traffic and appear to be in a different location, potentially bypassing geo-restrictions or age verification.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/tech-policy/2026/06/uk-to-ban-social-media-for-kids-under-16-may-impose-overnight-curfews/">UK to ban social media for kids under 16, may impose overnight ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/VPN">VPN</a></li>
<li><a href="https://completeaitraining.com/news/uk-ministers-consider-overnight-social-media-curfew-and-ai/">UK ministers consider overnight social media curfew and AI chatbot...</a></li>

</ul>
</details>

**Discussion**: The provided content does not include community comments, so no discussion summary is available.

**Tags**: `#tech policy`, `#social media`, `#child safety`, `#regulation`, `#UK`

---

<a id="item-18"></a>
## [China Targets 40% New Energy Heavy Truck Sales by 2030](https://www.energyintel.com/0000019e-cbe0-d720-af9f-fbe662f40000) ⭐️ 7.0/10

China's central government, through a joint plan by 11 ministries, has set a target for new energy vehicles to account for 40% of heavy truck sales by 2030, aiming for a fleet exceeding 1.6 million vehicles. This policy marks a major shift in China's transportation sector, significantly reducing diesel demand and boosting domestic truck and battery manufacturers, while also contributing to global carbon reduction efforts. The penetration rate of new-energy heavy-duty trucks was about 29% in 2025, indicating rapid progress toward the 2030 goal. The plan covers various new energy types including electric, hydrogen fuel cell, and other clean fuels.

rss · Energy Intelligence · Jun 15, 20:03

**Background**: Heavy trucks are a major source of diesel consumption and carbon emissions in China. Electrifying this segment is challenging due to high energy demands, long ranges, and heavy payloads. China has been promoting new energy vehicles (NEVs) for years, but heavy trucks have lagged behind passenger cars. This policy accelerates the transition by setting binding targets and coordinating across multiple ministries.

<details><summary>References</summary>
<ul>
<li><a href="https://cnevpost.com/2026/06/13/china-targets-40-penetration-new-energy-heavy-trucks-2030/">China targets 40% penetration for new - energy heavy trucks by 2030</a></li>
<li><a href="https://auto.economictimes.indiatimes.com/news/commercial-vehicle/china-sets-sights-on-heavy-truck-electrification-in-blow-to-diesel-demand/131740375">China sets sights on heavy truck electrification in blow to diesel...</a></li>
<li><a href="https://www.automotiveworld.com/news/china-maps-out-heavy-truck-electrification-with-40-2030-goal/">China maps out heavy - truck electrification with 40% 2030 goal</a></li>

</ul>
</details>

**Tags**: `#energy`, `#transportation`, `#policy`, `#electrification`

---

<a id="item-19"></a>
## [UCSD to Build Low-Carbon Data Center from 2,000 Pixel Phones](https://www.pcgamer.com/hardware/uni-researchers-plan-to-build-a-low-carbon-data-center-hivemind-from-2-000-pixel-smartphones-with-googles-help-no-less/) ⭐️ 7.0/10

Researchers at the University of California San Diego, with support from Google, plan to deploy a data center built from 2,000 retired Pixel smartphones, creating a low-cost, low-carbon cloud computing platform. This project demonstrates a novel approach to reducing e-waste and carbon emissions by repurposing old smartphones as computing nodes, potentially offering a sustainable alternative to traditional data centers. The cluster is expected to go live before the upcoming academic year and will be capable of supporting a hundred computer science courses simultaneously. Modern smartphone processors deliver higher single-core performance than comparable multicore servers, making them suitable for certain workloads.

rss · PC Gamer · Jun 15, 16:34

**Background**: Traditional data centers consume vast amounts of energy and require constant hardware upgrades, contributing to e-waste. Researchers have previously experimented with clustering old phones for computing, but this is the largest planned deployment with industry backing.

<details><summary>References</summary>
<ul>
<li><a href="https://research.google/blog/a-low-carbon-computing-platform-from-your-retired-phones/">A low - carbon computing platform from your retired phones</a></li>
<li><a href="https://www.tomshardware.com/desktops/servers/researchers-recycle-old-phones-and-cluster-them-into-computing-platforms-says-processors-on-modern-smartphones-deliver-higher-single-core-performance-than-comparable-multicore-servers">Researchers recycle old phones and cluster them... | Tom's Hardware</a></li>
<li><a href="https://www.pcgamer.com/hardware/uni-researchers-plan-to-build-a-low-carbon-data-center-hivemind-from-2-000-pixel-smartphones-with-googles-help-no-less/">Uni researchers plan to build a low - carbon data center ... | PC Gamer</a></li>

</ul>
</details>

**Tags**: `#green computing`, `#data center`, `#smartphone cluster`, `#sustainability`, `#research`

---

<a id="item-20"></a>
## [A Personal Reflection on Loving Computers](https://michaelenger.com/blog/i-love-the-computer/) ⭐️ 6.0/10

Michael Enger published a personal essay titled 'I Love the Computer,' reflecting on his deep affection for computing and his discomfort with the modern tech industry's focus on AI and gatekeeping. The essay has sparked community debate about the tension between nostalgic love for computing and the current industry trends, including the role of AI and who gets to define what 'real' computing is. The post is a personal reflection, not a technical analysis, and has received high engagement with diverse viewpoints. Commenters discuss the value of AI tools like LLMs and the gatekeeping sentiment in the computing community.

hackernews · speckx · Jun 15, 20:14 · [Discussion](https://news.ycombinator.com/item?id=48546441)

**Background**: The essay touches on the nostalgia for early, niche computing experiences versus the modern, commercialized tech industry. The term 'gatekeeping' refers to the attitude that only those who struggled with low-level programming deserve to call themselves computer enthusiasts.

**Discussion**: Commenters like fasterik defend AI tools as legitimately useful, while tptacek criticizes the essay's gatekeeping undertone. Yhippa resonates with the author's nostalgia but acknowledges it as a selfish view.

**Tags**: `#computing`, `#nostalgia`, `#AI`, `#industry`, `#programming`

---

<a id="item-21"></a>
## [Homelab AI Dev Platform Sparks Community Discussion](https://rsgm.dev/post/ai-dev-platform/) ⭐️ 6.0/10

A developer shared their homelab AI development platform setup, detailing a workflow using OpenCode, Forgejo, and Docker to manage AI-assisted coding tasks. The post generated 208 points and 42 comments on the community. This discussion highlights a growing trend of self-hosting AI tools for development, enabling privacy, customization, and cost savings. It resonates with many developers who are independently exploring similar workflows. The setup uses OpenCode as the AI coding agent, Forgejo for Git hosting, and Docker containers for services. Some commenters noted resource constraints and suggested alternatives like running agents on local machines for faster iteration.

hackernews · rsgm · Jun 15, 15:09 · [Discussion](https://news.ycombinator.com/item?id=48542433)

**Background**: A homelab is a personal server environment used for experimentation and self-hosting services. AI development platforms in homelabs often combine open-source tools like OpenCode (an AI coding assistant), Forgejo (a self-hosted Git service), and Docker for containerization. This setup allows developers to leverage AI without relying on external cloud services.

<details><summary>References</summary>
<ul>
<li><a href="https://rsgm.dev/post/ai-dev-platform/">My Homelab AI Dev Platform • Rsgm's Blog</a></li>
<li><a href="https://github.com/hoangriki/homelab-ai-platform">GitHub - hoangriki/ homelab - ai - platform : Mixed-architecture homelab ...</a></li>
<li><a href="https://llmengg.com/homelab-ai-assistant-setup/">Homelab AI Assistant Setup — Build With OpenClaw and Docker April...</a></li>

</ul>
</details>

**Discussion**: Commenters shared similar setups and workflows, with one mentioning a Forgejo action runner integration for OpenCode. Another noted that many developers independently converge on similar ideas, and a few raised concerns about domain filtering and resource requirements.

**Tags**: `#homelab`, `#AI`, `#dev platform`, `#self-hosting`, `#open-source`

---

<a id="item-22"></a>
## [COVID shots still protect hearts, study confirms](https://arstechnica.com/health/2026/06/covid-vaccines-still-protect-against-heart-problems-large-study-finds/) ⭐️ 6.0/10

A large study found that COVID-19 vaccines continue to protect against heart problems, even as vaccination rates decline due to anti-vaccine rhetoric. This reaffirms the long-term cardiovascular benefits of COVID-19 vaccination, countering misinformation that vaccines cause heart damage. The study did not specify exact effect sizes or populations, but the finding holds amid updated vaccine formulations and waning public trust.

rss · Ars Technica · Jun 15, 21:04

**Background**: COVID-19 vaccines were initially developed to prevent severe illness and death. Some rare heart inflammation cases (myocarditis) were reported after mRNA vaccination, leading to concerns. This study provides evidence that the overall heart protection outweighs risks.

**Tags**: `#COVID-19`, `#vaccines`, `#public health`, `#heart protection`

---

<a id="item-23"></a>
## [Chinese Rocket Breakup Near Starlink Creates Space Debris](https://arstechnica.com/space/2026/06/a-chinese-rocket-breaks-apart-dangerously-close-to-the-starlink-constellation/) ⭐️ 6.0/10

A Chinese rocket broke apart dangerously close to the Starlink constellation, generating an estimated 100 to 150 new pieces of space debris. This event highlights the growing risk of space debris to operational satellite constellations like Starlink, which already has nearly 6,500 satellites in orbit. It underscores the need for better debris mitigation and international coordination in space traffic management. The breakup likely involved the rocket's upper stage, similar to previous incidents with China's Long March 6A rocket, which has a history of fragmentation. The debris cloud poses a collision risk to Starlink and other spacecraft in low Earth orbit.

rss · Ars Technica · Jun 15, 18:55

**Background**: Space debris consists of defunct human-made objects in Earth orbit, including fragments from rocket breakups and satellite collisions. The Starlink constellation, operated by SpaceX, comprises thousands of active satellites providing global internet coverage. As mega-constellations grow, the probability of debris-generating events increases, threatening the sustainability of space operations.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/space/2024/08/us-military-tracks-more-than-300-pieces-of-debris-from-chinese-launch/">China’s Long March 6A rocket is making a mess in... - Ars Technica</a></li>
<li><a href="https://www.wikiwand.com/en/Space_debris">Space debris - Wikiwand</a></li>
<li><a href="https://www.linkedin.com/posts/phantom-space_mega-constellations-are-a-megatrend-starlink-activity-7260648579038347266-cGvN">Mega constellations are a megatrend. Starlink has led the way...</a></li>

</ul>
</details>

**Tags**: `#space debris`, `#Starlink`, `#rocket breakup`, `#space safety`

---

<a id="item-24"></a>
## [20 Years of Intel Macs: Apple's Two Major Switches](https://arstechnica.com/gadgets/2026/06/20-years-of-intel-macs-why-apple-switched-and-why-it-switched-again/) ⭐️ 6.0/10

Ars Technica published a retrospective on the 20-year history of Intel-based Macs, analyzing why Apple switched from PowerPC to Intel in 2006 and then from Intel to its own Apple Silicon starting in 2020. This retrospective provides valuable context for understanding Apple's strategic hardware decisions, which have shaped the modern Mac ecosystem and influenced the broader computing industry's shift toward custom ARM-based processors. The Intel Mac era began in January 2006 with the first Intel-based iMac and MacBook Pro, and officially ended in June 2023 when Apple completed the transition to Apple Silicon across its entire Mac lineup.

rss · Ars Technica · Jun 15, 16:32

**Background**: Apple has transitioned its Mac processors twice: from the IBM PowerPC architecture to Intel x86 in 2006, and from Intel to its own ARM-based Apple Silicon starting in 2020. The first transition was driven by PowerPC's performance and thermal limitations, while the second was motivated by Apple's desire for tighter hardware-software integration, better performance per watt, and a unified architecture across all its devices. Apple Silicon chips, such as the M1, are designed in-house and manufactured by TSMC, offering significant performance and efficiency gains over Intel processors.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mac_transition_to_Intel_processors">Mac transition to Intel processors - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Apple_silicon">Apple silicon</a></li>
<li><a href="https://support.apple.com/en-us/116943">Mac computers with Apple silicon - Apple Support</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#Intel Macs`, `#Apple Silicon`, `#history`

---

<a id="item-25"></a>
## [Russia to Address Long-Standing ISS Cracks](https://arstechnica.com/space/2026/06/russia-appears-set-to-finally-address-long-term-serious-space-station-cracks/) ⭐️ 6.0/10

Russia appears set to finally address long-term, serious cracks on the International Space Station, resolving a dispute with NASA over responsibility and repair plans. This development is significant for the continued safe operation of the ISS, as unresolved cracks could lead to catastrophic failures and jeopardize the station's lifespan. The cracks have been found in the Russian-built Zarya module, and the dispute between Roscosmos and NASA has been ongoing behind the scenes for some time.

rss · Ars Technica · Jun 15, 13:54

**Background**: The International Space Station is a modular space station in low Earth orbit, jointly operated by NASA, Roscosmos, and other space agencies. The Zarya module, launched in 1998, was the first component of the ISS and provides propulsion and storage. Cracks in such a critical module pose risks of air leaks and structural failure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.space.com/international-space-station-cracks-found-zarya-module">Small cracks found in International Space Station module... | Space</a></li>
<li><a href="https://www.independent.co.uk/tech/international-space-station-iss-cracks-b1912379.html">The ISS is cracked and facing ‘irreparable’ failures... | The Independent</a></li>
<li><a href="https://www.newsy-today.com/russia-moves-to-repair-long-term-iss-cracks/">Russia Moves to Repair Long-Term ISS Cracks - Newsy Today</a></li>

</ul>
</details>

**Tags**: `#space`, `#ISS`, `#engineering`

---

<a id="item-26"></a>
## [Why South Koreans Embrace AI So Enthusiastically](https://www.technologyreview.com/2026/06/15/1138983/why-do-south-koreans-love-ai-so-much/) ⭐️ 6.0/10

A newsletter article explores the cultural and societal factors driving South Korea's widespread adoption of AI, citing examples like unmanned immigration checkpoints using facial recognition. Understanding South Korea's AI enthusiasm offers insights into how cultural attitudes can accelerate technology adoption, potentially influencing global AI deployment strategies. The article is part of MIT Technology Review's 'The Algorithm' newsletter and lacks technical depth, focusing instead on cultural observations from the author's travel experience.

rss · MIT Technology Review · Jun 15, 18:46

**Background**: South Korea has a highly digitalized society with strong government support for AI and robotics. Cultural factors such as high trust in technology and collective societal orientation may contribute to AI acceptance.

**Tags**: `#AI`, `#South Korea`, `#culture`, `#technology adoption`

---

<a id="item-27"></a>
## [Solid-State ACs: Cool Promise, Scientific Doubt](https://www.technologyreview.com/2026/06/15/1138552/solid-state-acs-promise-cool-future/) ⭐️ 6.0/10

An article from MIT Technology Review examines the potential of solid-state air conditioners as a climate-friendly alternative, but notes that scientists remain skeptical about their efficiency and scalability. With global AC use projected to triple by 2050, solid-state cooling could reduce energy consumption and eliminate harmful refrigerants, but current doubts may slow adoption and investment. Solid-state ACs use the electrocaloric effect, where an electric field causes a temperature change in a material, but existing devices are inefficient for practical use; the article highlights the gap between promise and reality.

rss · MIT Technology Review · Jun 15, 09:00

**Background**: Traditional air conditioners rely on vapor-compression cycles that use refrigerants with high global warming potential. Solid-state cooling technologies, such as electrocaloric devices, offer a refrigerant-free alternative that could be more efficient and environmentally friendly, but they are still in early development stages.

<details><summary>References</summary>
<ul>
<li><a href="https://northnjhvac.com/solid-state-air-conditioner/">Solid State Air Conditioners : The Future Of Energy-Efficient Cooling...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Electrocaloric_effect">Electrocaloric effect - Wikipedia</a></li>
<li><a href="https://www.cibsejournal.com/technical/electrocaloric-cooling-making-a-difference/">Electrocaloric cooling – making a difference - CIBSE Journal</a></li>

</ul>
</details>

**Tags**: `#climate tech`, `#air conditioning`, `#solid-state`, `#energy`, `#environment`

---

<a id="item-28"></a>
## [AI Load Growth Reshapes Utility Business Models](https://www.utilitydive.com/spons/ai-load-growth-is-changing-the-utility-business-model/822321/) ⭐️ 6.0/10

AI-driven large-load demand is transforming utility strategy, regulation, and investment, as highlighted in a sponsored article on Utility Dive. This shift could fundamentally alter how utilities plan capacity, set rates, and invest in infrastructure, affecting energy costs and reliability for all customers. The article is sponsored content and lacks specific technical details or case studies, but it signals growing industry attention to AI's impact on energy demand.

rss · Utility Dive · Jun 15, 09:00

**Background**: Utilities traditionally operate with predictable load growth, but AI data centers and computing clusters introduce large, variable loads that strain grids and require new planning approaches. This trend is prompting regulators and utilities to rethink rate structures and investment strategies.

**Tags**: `#AI`, `#energy`, `#utilities`, `#business model`

---

<a id="item-29"></a>
## [US Clean Energy Sets Multiple Records This Spring](https://www.canarymedia.com/articles/clean-energy/clean-energy-us-set-records) ⭐️ 6.0/10

During the spring shoulder season, the US achieved record-breaking milestones in clean energy generation, including high levels of solar and wind power output. These records demonstrate accelerating renewable energy deployment, which is crucial for meeting climate goals and reducing fossil fuel dependence. The article highlights that renewable energy sources like solar and wind set new generation records during the spring months, contributing to a cleaner grid.

rss · Latitude Media (Canary Media) · Jun 15, 07:30

**Background**: The shoulder season refers to the period between winter and summer when energy demand is moderate, often allowing renewables to achieve higher penetration. Record clean energy output in this period signals strong growth in renewable capacity and favorable conditions.

**Tags**: `#clean energy`, `#renewable energy`, `#US energy`, `#climate`

---

<a id="item-30"></a>
## [EA Launches In-Game Advertising Platform](https://www.gamedeveloper.com/marketing/ea-announces-advertising-platform-to-launch-ads-directly-into-gameplay-) ⭐️ 6.0/10

Electronic Arts announced the launch of EA Advertising, a new platform that places dynamic, real-time ads directly into gameplay, with initial brand partners including Visa, Red Bull, Xfinity, Lowe's, Peacock, and Mountain Dew. This move signals a major shift in game monetization, potentially generating significant revenue for EA while raising concerns about player experience and privacy. It could set a precedent for other publishers to follow. The ads are designed to be non-disruptive, appearing as stadium signage or custom in-game content, and are placed dynamically in real-time. The platform aims to connect brands with highly engaged gaming audiences.

rss · Game Developer (Gamasutra) · Jun 15, 19:05

**Background**: In-game advertising (IGA) involves placing ads within video games, distinct from advergames made solely for promotion. Dynamic IGA allows ads to change based on context or user data, and companies like Anzu have pioneered this technology. EA's entry into this space with a dedicated platform marks a significant industry development.

<details><summary>References</summary>
<ul>
<li><a href="https://www.ea.com/news/introducing-ea-advertising">Introducing EA Advertising</a></li>
<li><a href="https://www.gamedeveloper.com/marketing/ea-announces-advertising-platform-to-launch-ads-directly-into-gameplay-">EA unveils new platform to insert ads 'directly into gameplay'</a></li>
<li><a href="https://en.wikipedia.org/wiki/In-game_advertising">In - game advertising - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#gaming`, `#advertising`, `#monetization`, `#EA`

---

<a id="item-31"></a>
## [Google Earth Web Adds Flight Simulator](https://www.4gamer.net/games/042/G004283/20260615001/) ⭐️ 6.0/10

On June 12, 2026, Google added a flight simulator feature to the web version of Google Earth, allowing users to fly over global landscapes directly in a browser without any account registration or download. This makes a previously hidden desktop feature widely accessible, potentially attracting more users to explore Google Earth in an engaging way and showcasing the capabilities of WebGL for 3D rendering in browsers. The flight simulator was previously a hidden feature in Google Earth Pro desktop app; the web version now brings it to browsers with no installation required, using WebGL technology for real-time 3D rendering.

rss · 4Gamer.net · Jun 15, 01:53

**Background**: Google Earth is a 3D representation of Earth based on satellite imagery, available as a desktop program and a web application. The desktop version, Google Earth Pro, has long included a hidden flight simulator that users could activate. The web version now replicates this functionality using WebGL, a web standard for 3D graphics.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_Earth">Google Earth - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#Google Earth`, `#flight simulator`, `#web application`, `#mapping`

---

<a id="item-32"></a>
## [SteamOS Beta Expands to Intel Handhelds Like MSI Claw](https://www.pcgamer.com/hardware/handheld-gaming-pcs/it-looks-like-more-handhelds-will-soon-be-able-to-run-steamos-if-this-msi-claw-gameplay-test-is-anything-to-go-by/) ⭐️ 6.0/10

Valve's SteamOS 3.8.7 beta adds official support for Intel-based handheld gaming PCs, including the MSI Claw 8 AI+, with controller mapping and firmware preparation. This expansion breaks SteamOS's previous AMD-only limitation, potentially allowing a wider range of handheld devices to run SteamOS and challenging Windows' dominance in portable gaming. The beta includes initial firmware for upcoming Intel handhelds and controller support for devices like the MSI Claw 8 AI+, but performance on Intel hardware is expected to improve with future updates.

rss · PC Gamer · Jun 15, 16:10

**Background**: SteamOS is Valve's Linux-based operating system designed for gaming, originally exclusive to the Steam Deck which uses AMD processors. The MSI Claw is a handheld gaming PC powered by Intel's Core Ultra 7 155H processor with Intel Arc graphics, marking a shift from AMD dominance in portable gaming.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techradar.com/computing/gaming-pcs/valves-latest-steamos-beta-provides-better-intel-hardware-compatibility-and-thats-great-news-for-upcoming-handhelds">Valve's latest SteamOS beta provides better Intel ... | TechRadar</a></li>
<li><a href="https://otontechnology.com/steamos-3-8-7-beta-intel-handheld-support/">SteamOS 3.8.7 Beta : Intel Handhelds Get Official Support</a></li>
<li><a href="https://www.tweaktown.com/news/112145/youtuber-tests-steamos-on-an-intel-based-msi-claw-8-ai-plus-handheld-steamos-now-supports-intel-handheld-gaming-pcs-in-new-beta/index.html">YouTuber tests SteamOS on an Intel -based MSI Claw 8 AI+ handheld ...</a></li>

</ul>
</details>

**Tags**: `#SteamOS`, `#handheld gaming`, `#Intel`, `#beta`

---