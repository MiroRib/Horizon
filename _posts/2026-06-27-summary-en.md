---
layout: default
title: "Horizon Summary: 2026-06-27 (EN)"
date: 2026-06-27
lang: en
---

> From 48 items, 13 important content pieces were selected

---

1. [DeepSeek DSpark: Speculative Decoding Accelerates LLM Inference](#item-1) ⭐️ 9.0/10
2. [IP Crawl: Live Atlas of Exposed Webcams Raises Privacy Alarms](#item-2) ⭐️ 8.0/10
3. [Meta Sued for 12-Month Surveillance of Former Executive](#item-3) ⭐️ 8.0/10
4. [Human Behavioral Quirks Revealed by Distribution Discontinuities](#item-4) ⭐️ 8.0/10
5. [The Case for Physical Media Ownership](#item-5) ⭐️ 7.0/10
6. [Post-Mythos Cybersecurity: Keep Calm and Carry On](#item-6) ⭐️ 7.0/10
7. [Apple Seeks Exception to Buy RAM from Blacklisted Chinese Supplier CXMT](#item-7) ⭐️ 7.0/10
8. [OpenRA Revives Classic RTS Games with Modern Features](#item-8) ⭐️ 6.0/10
9. [TownSquare Adds Ephemeral Presence to Websites](#item-9) ⭐️ 6.0/10
10. [Fintech Engineering Handbook Criticized for Shallow Advice](#item-10) ⭐️ 6.0/10
11. [Smart home industry still betting on Matter standard](#item-11) ⭐️ 6.0/10
12. [PUBG's AI Teammate Ella: Natural Chat, Poor Play](#item-12) ⭐️ 6.0/10
13. [Browser Ports of Half-Life 2 and Portal via WebAssembly](#item-13) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [DeepSeek DSpark: Speculative Decoding Accelerates LLM Inference](https://github.com/deepseek-ai/DeepSpec/blob/main/DSpark_paper.pdf) ⭐️ 9.0/10

DeepSeek has released a paper and open-source models (DeepSeek-V4-Flash-DSpark and DeepSeek-V4-Pro-DSpark) implementing speculative decoding, achieving 60% to 85% faster inference in production traffic. This breakthrough significantly reduces LLM inference latency and cost, making advanced AI more accessible. DeepSeek's open approach contrasts with closed-source American labs, fostering community innovation. DSpark reports throughput improvements of 51% to 400% depending on concurrency, and has been deployed in real online traffic for DeepSeek-V4 Flash and Pro models. The Hugging Face models include the speculative decoding module built in.

hackernews · aurenvale · Jun 27, 09:18 · [Discussion](https://news.ycombinator.com/item?id=48696585)

**Background**: Speculative decoding is an inference-time optimization that accelerates LLM token generation by predicting and verifying multiple tokens simultaneously, without reducing output quality. It was introduced by Google in 2022 and has been refined by NVIDIA and others.

<details><summary>References</summary>
<ul>
<li><a href="https://bentoml.com/llm/inference-optimization/speculative-decoding">Speculative decoding | LLM Inference Handbook</a></li>
<li><a href="https://cryptobriefing.com/deepseek-dspark-faster-inference/">DeepSeek unveils DSpark for 60% to 85% faster inference optimization</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro-DSpark">deepseek -ai/ DeepSeek -V4-Pro- DSpark · Hugging Face</a></li>

</ul>
</details>

**Discussion**: The community praised DeepSeek for open innovation, contrasting with American labs that no longer publish such details. Users reported positive real-world experience with DeepSeek V4 Pro, noting its speed, reliability, and low cost. Some speculated on integration with local inference tools like DwarfStar.

**Tags**: `#LLM inference`, `#speculative decoding`, `#DeepSeek`, `#AI acceleration`, `#open source`

---

<a id="item-2"></a>
## [IP Crawl: Live Atlas of Exposed Webcams Raises Privacy Alarms](https://ipcrawl.com/) ⭐️ 8.0/10

IP Crawl (ipcrawl.com) has launched a publicly accessible atlas that maps thousands of open webcams discovered on the public internet, allowing anyone to view live feeds from unsecured cameras worldwide. This site highlights the massive scale of unsecured IoT devices, exposing serious privacy risks for individuals and organizations. It reignites debates about the ethics of internet scanning and the responsibility of device manufacturers and users. The atlas is built by scanning the public internet for cameras that use default credentials or have no authentication. Many feeds show private spaces such as homes, offices, and even illegal activities, raising legal and ethical concerns.

hackernews · arm32 · Jun 27, 19:09 · [Discussion](https://news.ycombinator.com/item?id=48700834)

**Background**: Internet scanning tools like Shodan have long indexed exposed devices, but IP Crawl presents them in a user-friendly map format. Many cheap IP cameras come with default passwords and no firewall, making them easy targets. The practice of scanning and publishing such data sits in a gray area between security research and privacy invasion.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Internet_Scamming">Internet Scamming</a></li>
<li><a href="https://cyberstreams.com/post/unsecured-webcams-are-wide-open-on-the-internet">Unsecured Webcams Are Wide Open On The Internet</a></li>
<li><a href="https://www.fortinet.com/resources/cyberglossary/iot-device-vulnerabilities">Top IoT Device Vulnerabilities: How To Secure IoT Devices - Fortinet</a></li>

</ul>
</details>

**Discussion**: Commenters express unease, comparing the site to using a telescope to look into someone's apartment. Some note that this problem has existed since at least 2012, while others suggest the site should alert owners about their exposed cameras. A few point out specific feeds showing potentially illegal activity.

**Tags**: `#privacy`, `#security`, `#IoT`, `#webcams`, `#internet scanning`

---

<a id="item-3"></a>
## [Meta Sued for 12-Month Surveillance of Former Executive](https://fortune.com/2026/06/26/meta-wynn-williams-surveillance-gag-order-lawsuit-2026/) ⭐️ 8.0/10

Former Meta executive Wynn-Williams filed a lawsuit claiming Meta surveilled her for 12 months and imposed a gag order to silence her about her book 'Careless People'. This lawsuit raises serious concerns about corporate surveillance and the use of NDAs and gag orders to suppress whistleblowers, potentially impacting tech ethics and corporate accountability. The lawsuit alleges Meta tracked her communications and movements for a year, and the gag order prevented her from discussing her experiences. Community comments link to the court docket and archived complaint.

hackernews · 1vuio0pswjnm7 · Jun 27, 21:14 · [Discussion](https://news.ycombinator.com/item?id=48701822)

**Background**: Meta has faced previous controversies over employee surveillance, including a program that tracked staff via laptops. NDAs and gag orders are common in corporate settings to protect confidential information, but their use to silence critics has drawn legal scrutiny.

<details><summary>References</summary>
<ul>
<li><a href="https://www.the-independent.com/tech/meta-staff-surveillance-mci-privacy-ai-b3001251.html">Meta pauses controversial staff surveillance program after massive data leak | The Independent</a></li>
<li><a href="https://en.wikipedia.org/wiki/Non-disclosure_agreement">Non-disclosure agreement - Wikipedia</a></li>
<li><a href="https://shegerianconniff.com/use-of-ndas-gag-orders-in-harassment-claims-whats-legal-and-whats-not/">Use of NDAs & Gag Orders in Harassment Claims: What’s Legal and What’s Not - Shegerian Conniff</a></li>

</ul>
</details>

**Discussion**: Commenters expressed skepticism about Meta's actions, with some suggesting the surveillance indicates the claims might be true. Others highlighted the Streisand effect and called for linking primary sources like the court docket.

**Tags**: `#Meta`, `#surveillance`, `#lawsuit`, `#tech ethics`, `#corporate accountability`

---

<a id="item-4"></a>
## [Human Behavioral Quirks Revealed by Distribution Discontinuities](https://danluu.com/discontinuities/) ⭐️ 8.0/10

Dan Luu's 2020 article analyzes how discontinuities in statistical distributions, such as marathon finish times clustering around round numbers and test scores avoiding just-below-passing thresholds, expose systematic human behavioral biases. This analysis highlights how human goal-setting and threshold effects distort data, with implications for fields like behavioral economics, data science, and policy design where metrics are gamed or behaviors shift near boundaries. Examples include marathon runners clustering around round time goals, Polish language test scores showing a massive distortion at the passing threshold of 30%, and chess ratings on Lichess bunching at multiples of 100.

hackernews · tosh · Jun 27, 13:32 · [Discussion](https://news.ycombinator.com/item?id=48698151)

**Background**: Discontinuities in distributions occur when human behavior changes abruptly at certain thresholds, such as passing scores or round numbers. These artifacts are often invisible in aggregate statistics but become clear when plotting the full distribution. Understanding them helps avoid misinterpretation of data and reveals how incentives shape behavior.

**Discussion**: Commenters shared real-world examples: tax cliffs in the UK creating >60% marginal rates, AWS engineers gaming P90 latency targets, and chess players avoiding dropping below round ratings. The discussion validated the article's thesis with concrete cases from diverse domains.

**Tags**: `#statistics`, `#behavioral economics`, `#data analysis`, `#human behavior`

---

<a id="item-5"></a>
## [The Case for Physical Media Ownership](https://dervis.de/physical/) ⭐️ 7.0/10

An article argues that true ownership of media requires physical possession, sparking debate on digital licensing and DRM. The discussion highlights the fragility of digital ownership, citing examples like the shutdown of Ultraviolet and Sony's removal of purchased content. This matters because consumers increasingly rely on digital purchases that can be revoked, raising concerns about long-term access and preservation. The debate influences how people choose between convenience and true ownership, affecting industries like gaming, movies, and music. The article and comments reference Ultraviolet, a defunct digital rights locker, and Sony's 2026 notice removing Studio Canal content from PlayStation libraries. Some commenters advocate piracy as a practical solution for permanent access.

hackernews · cemdervis · Jun 27, 11:32 · [Discussion](https://news.ycombinator.com/item?id=48697335)

**Background**: Digital rights management (DRM) restricts how consumers use purchased digital content, often tying it to specific platforms or accounts. Physical media, such as Blu-rays and DVDs, offer offline, transferable ownership but are declining in popularity due to convenience of streaming and digital downloads.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Digital_rights_management">Digital rights management - Wikipedia</a></li>
<li><a href="https://jacobin.com/2025/01/digital-ownership-physical-media-control">Digital Ownership and the End of Physical Media - Jacobin</a></li>
<li><a href="https://libertyproject.com/digital-vs-physical-media">Digital Media May Be Convenient, But Is It Yours ...</a></li>

</ul>
</details>

**Discussion**: Commenters largely agree that digital ownership is fragile, with some advocating piracy as a reliable backup. Others emphasize that physical media is not the only path to true ownership, pointing to DRM-free digital stores like GOG and Bandcamp.

**Tags**: `#digital rights`, `#DRM`, `#media ownership`, `#piracy`, `#consumer rights`

---

<a id="item-6"></a>
## [Post-Mythos Cybersecurity: Keep Calm and Carry On](https://cephalosec.com/blog/cybersecurity-in-the-post-mythos-era-keep-calm-and-carry-on/) ⭐️ 7.0/10

A reflective blog post argues that despite the release and controversy surrounding Anthropic's Mythos AI model, core cybersecurity issues remain unchanged, while community comments highlight the growing role of LLMs in vulnerability research. This analysis cuts through vendor hype, reminding the industry that fundamentals like misconfigurations and human error remain the primary security risks, even as LLMs like Mythos demonstrate powerful new capabilities. Mythos, an AI model from Anthropic, can identify and exploit zero-day vulnerabilities in major operating systems and browsers, but the blog argues that most security issues stem from bad configurations and practices, not advanced exploits.

hackernews · Versipelle · Jun 27, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48698559)

**Background**: Mythos is an AI model released by Anthropic in April 2026, capable of autonomously finding and exploiting zero-day vulnerabilities. Its release sparked debate about AI's role in cybersecurity, with vendors quickly marketing solutions. LLMs are increasingly used in vulnerability detection, but their practical impact on everyday security operations is still evolving.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theguardian.com/technology/2026/apr/22/what-is-anthropic-mythos-ai-threat-global-cybersecurity">What is Mythos AI and why could it be a threat to global cybersecurity? | AI (artificial intelligence) | The Guardian</a></li>
<li><a href="https://red.anthropic.com/2026/mythos-preview/">Assessing Claude Mythos Preview’s cybersecurity capabilities \ Anthropic</a></li>
<li><a href="https://github.com/huhusmang/Awesome-LLMs-for-Vulnerability-Detection">GitHub - huhusmang/Awesome-LLMs-for-Vulnerability-Detection: The community's most comprehensive, continuously-updated index of research on Large Language Models for software vulnerability detection — papers across function-level, repository-level, agentic, and smart-contract detection, plus datasets, benchmarks, and surveys.</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed views: some note that LLMs are already effective at finding vulnerabilities (e.g., Deepseek V4 Flash), while others criticize vendor fear-mongering and emphasize that most security issues are due to misconfigurations and human error. One commenter highlights the scale of effort behind finding a BSD vulnerability, putting LLM capabilities in perspective.

**Tags**: `#cybersecurity`, `#Mythos`, `#LLM`, `#vulnerability research`, `#AI security`

---

<a id="item-7"></a>
## [Apple Seeks Exception to Buy RAM from Blacklisted Chinese Supplier CXMT](https://www.theverge.com/tech/958707/apple-ram-buy-memory-blacklisted-china-cxmt) ⭐️ 7.0/10

Apple has requested a U.S. government exception to purchase DRAM chips from ChangXin Memory Technologies (CXMT), a Chinese memory maker blacklisted by the Pentagon for alleged ties to the People's Liberation Army. This move highlights Apple's supply chain vulnerability amid rising memory prices and geopolitical tensions, and could set a precedent for other tech firms seeking to bypass blacklist restrictions. CXMT produces only commodity DRAM, not advanced HBM, so the request poses little threat to major U.S. memory maker Micron. Apple's request comes as RAM and storage prices have skyrocketed, pressuring its supply chain.

rss · The Verge · Jun 27, 17:28

**Background**: The Pentagon maintains a list of Chinese military companies under Section 1260H of the National Defense Authorization Act, restricting U.S. entities from doing business with them without a special license. CXMT was added to this list due to alleged ties to the People's Liberation Army. Apple's request seeks an exception to buy memory from CXMT to ease supply chain constraints.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ChangXin_Memory_Technologies">ChangXin Memory Technologies - Wikipedia</a></li>
<li><a href="https://247wallst.com/investing/2026/06/27/apple-wants-to-buy-blacklisted-chinese-memory-micron-has-nothing-to-worry-about/">Apple Wants to Buy Blacklisted Chinese Memory. - 24/7 Wall St.</a></li>
<li><a href="https://www.bloomberg.com/news/articles/2024-03-09/us-mulls-blacklisting-cxmt-to-further-curb-china-s-chip-advance">US Mulls Blacklisting CXMT to Further Curb... - Bloomberg</a></li>

</ul>
</details>

**Tags**: `#Apple`, `#supply chain`, `#memory`, `#geopolitics`, `#CXMT`

---

<a id="item-8"></a>
## [OpenRA Revives Classic RTS Games with Modern Features](https://www.openra.net/) ⭐️ 6.0/10

OpenRA is an open-source reimplementation of classic RTS games like Red Alert, Command & Conquer, and Dune 2000, offering improved balance, modern features, and cross-platform support. This project keeps beloved classic games alive and accessible on modern systems, with an active community and ongoing development that enhances gameplay and balance. OpenRA is written in C# using SDL, supports Windows, macOS, Linux, and *BSD, and automatically downloads original game files or installs them from discs. The project's next major goal is to add support for Tiberian Sun and other second-generation C&C games.

hackernews · tosh · Jun 27, 12:10 · [Discussion](https://news.ycombinator.com/item?id=48697560)

**Background**: Command & Conquer: Red Alert, released in 1996 by Westwood Studios, is a landmark RTS game set in an alternate history where the Allies battle the Soviet Union. Electronic Arts made the game freeware in 2008. OpenRA is one of several open-source engine recreations that modernize classic games while preserving their original feel.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/OpenRA">OpenRA</a></li>
<li><a href="https://www.openra.net/">OpenRA - Classic strategy games rebuilt for the modern era</a></li>
<li><a href="https://cnc.fandom.com/wiki/OpenRA">OpenRA - Command & Conquer Wiki - covering Tiberium, Red ...</a></li>

</ul>
</details>

**Discussion**: Community comments are overwhelmingly positive, praising OpenRA's improved balance and modern features. One user noted that the player base remains strong, while another mentioned occasional toxicity in online play. The project has been discussed multiple times on Hacker News, indicating sustained interest.

**Tags**: `#open-source`, `#gaming`, `#RTS`, `#game-development`

---

<a id="item-9"></a>
## [TownSquare Adds Ephemeral Presence to Websites](https://cauenapier.com/blog/townsquare_release/) ⭐️ 6.0/10

TownSquare is a lightweight, ephemeral presence layer that lets website visitors see and chat with each other in real-time without accounts or permanent history. It revives the early web's sense of co-presence, offering a non-corporate alternative to social media that prioritizes serendipitous interaction over data collection. The tool is intentionally tiny and forgetful: no accounts, profiles, follower counts, or permanent chat history; messages exist only while people are present.

hackernews · eustoria · Jun 27, 17:11 · [Discussion](https://news.ycombinator.com/item?id=48699928)

**Background**: The IndieWeb movement advocates for personal websites and decentralized social interactions, often using tools like Webmention. TownSquare aligns with this ethos by providing a lightweight, ephemeral social layer that doesn't rely on centralized platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/IndieWeb">IndieWeb</a></li>
<li><a href="https://indieweb.org/">IndieWeb</a></li>

</ul>
</details>

**Discussion**: Comments are mixed: some praise the nostalgic feel and indieweb alignment, while others find the interface confusing or question the value of ephemeral interactions without permanence.

**Tags**: `#web development`, `#social software`, `#real-time`, `#indieweb`, `#ephemeral`

---

<a id="item-10"></a>
## [Fintech Engineering Handbook Criticized for Shallow Advice](https://w.pitula.me/fintech-engineering-handbook/) ⭐️ 6.0/10

A fintech engineering handbook has been published, covering topics like monetary data handling and FX exchange, but the community has criticized it for being shallow and providing questionable advice, such as storing monetary values as floats. This handbook aims to guide fintech engineers, but its mixed reception highlights the need for rigorous, battle-tested best practices in financial software, where errors can have serious financial consequences. The handbook is available online and has generated 147 comments, with users pointing out flaws like using integers for monetary values and the complexity of FX rate handling, while some find it a useful collection of existing knowledge.

hackernews · signa11 · Jun 27, 10:28 · [Discussion](https://news.ycombinator.com/item?id=48696982)

**Background**: Financial software must handle monetary values with precision to avoid rounding errors. Best practices recommend using integers (e.g., cents) or fixed-point arithmetic, not floating-point numbers. FX handling requires careful consideration of rates and timing.

**Discussion**: The community is divided: some criticize the handbook for shallow content and bad advice on monetary storage and FX, while others find it a practical collection of known best practices. A key point of contention is the use of integers vs. floats for monetary values.

**Tags**: `#fintech`, `#software engineering`, `#monetary data`, `#best practices`

---

<a id="item-11"></a>
## [Smart home industry still betting on Matter standard](https://www.theverge.com/tech/958008/matter-unify-conference-csa-apple-google-amazon-samsung-smart-home-interoperability) ⭐️ 6.0/10

The Verge reports from the Matter Unify conference in Amsterdam that the smart home industry, including Apple, Google, Amazon, and Samsung, continues to invest in the Matter interoperability standard despite slow consumer adoption. Matter aims to solve smart home fragmentation by enabling devices from different brands to work together seamlessly, which could simplify the user experience and accelerate IoT adoption. Matter was launched four years ago as an open standard built on existing technologies, but adoption has been slow due to complexity and certification delays. The conference highlights ongoing industry commitment and incremental progress.

rss · The Verge · Jun 27, 13:00

**Background**: Matter is a technical standard for smart home and IoT devices, intended to improve interoperability and security while allowing local control. It originated in 2019 as Project Connected Home over IP (CHIP) by Amazon, Apple, Google, and others, and the first version was released in 2022.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Matter_(standard)">Matter (standard) - Wikipedia matter-handbook | This is the repository for the Matter ... Top Stories Welcome to Matter’s documentation — Matter documentation What Is Matter? We Explain the Smart Home Standard (2025 ... Matter: IoT Interoperability for Smart Homes - arXiv.org Matter Protocol in 2026: The Smart Home Interoperability ...</a></li>
<li><a href="https://matter-smarthome.de/en/">All about the Matter standard | FAQ | News | Product overview</a></li>
<li><a href="https://csa-iot.org/all-solutions/matter/">Build With Matter | Smart Home Device Solution - CSA-IOT</a></li>

</ul>
</details>

**Tags**: `#smart home`, `#Matter`, `#interoperability`, `#IoT`

---

<a id="item-12"></a>
## [PUBG's AI Teammate Ella: Natural Chat, Poor Play](https://www.4gamer.net/games/348/G034868/20260626019/) ⭐️ 6.0/10

PUBG: Battlegrounds has introduced a limited-time AI teammate named Ella, powered by a large language model and NVIDIA ACE, allowing natural conversation and voice commands in the Ally Duo mode available until June 30 on Steam. This marks a significant integration of LLMs into a mainstream multiplayer game, showcasing how AI can enhance cooperative play and potentially reshape player expectations for NPC interactions. Ella can understand map callouts, item names, and execute commands like 'find a vehicle' or 'cover me,' but the report notes she plays poorly, often dying quickly and lacking banter, similar to a random foreign teammate.

rss · 4Gamer.net · Jun 27, 02:00

**Background**: PUBG is a battle royale game where players typically team up with human partners. AI teammates have existed in games before, but Ella uses a large language model (LLM) for more natural communication, powered by NVIDIA ACE technology for real-time AI interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamesn.com/playerunknowns-battlegrounds/ai-teammate">PUBG's new AI teammate is somehow more useless than my friends - PCGamesN</a></li>
<li><a href="https://www.tweaktown.com/news/112250/pubgs-new-ally-duo-game-mode-pairs-you-with-an-ai-teammate-powered-by-nvidia-ace/index.html">PUBG's new Ally Duo game mode pairs you with an AI teammate powered by NVIDIA ACE</a></li>
<li><a href="https://www.gamermarkt.com/blog/pubg-ally-duo-ai-teammate-beta-mode-ella/">PUBG Ally Duo Beta: AI Teammate Ella Explained (2026)</a></li>

</ul>
</details>

**Tags**: `#AI`, `#gaming`, `#LLM`, `#PUBG`

---

<a id="item-13"></a>
## [Browser Ports of Half-Life 2 and Portal via WebAssembly](https://www.pcgamer.com/games/fps/web-port-wizards-produce-browser-versions-of-half-life-2-and-portal/) ⭐️ 6.0/10

Developers have created browser-based ports of Half-Life 2 and Portal using WebAssembly, allowing these classic games to run directly in a web browser without plugins. This demonstrates the growing capability of WebAssembly to handle complex, high-performance applications like AAA games, potentially expanding the reach of gaming to platforms without native installations. The ports leverage Emscripten to compile the original C++ code to WebAssembly, achieving playable frame rates in modern browsers. However, performance may vary depending on hardware and browser optimizations.

rss · PC Gamer · Jun 27, 16:28

**Background**: WebAssembly is a binary instruction format that allows code written in languages like C++ to run in web browsers at near-native speed. Emscripten is a toolchain that compiles C/C++ code to WebAssembly, enabling porting of existing applications to the web. This project follows a trend of porting classic games to the browser, such as Doom and Quake.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/genizy/web-ports">GitHub - genizy/web-ports: a huge collection of games that ...</a></li>
<li><a href="https://markaicode.com/webassembly-games-cpp-engines-browser/">WebAssembly 4.0 for Games: Porting C++ Engines to the Browser</a></li>

</ul>
</details>

**Tags**: `#WebAssembly`, `#game ports`, `#browser technology`, `#Half-Life 2`, `#Portal`

---