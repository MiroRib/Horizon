---
layout: default
title: "Horizon Summary: 2026-07-03 (EN)"
date: 2026-07-03
lang: en
---

> From 128 items, 20 important content pieces were selected

---

1. [MEP Investigating Spyware Hacked with Pegasus](#item-1) ⭐️ 8.0/10
2. [Ubicloud advocates strict memory overcommit for PostgreSQL](#item-2) ⭐️ 8.0/10
3. [Startup's Smart Oven Fails Due to Lack of Domain Expertise](#item-3) ⭐️ 8.0/10
4. [Device Revives Donor Eyes, Paving Way for Transplants](#item-4) ⭐️ 8.0/10
5. [Guide to Running SOTA LLMs Locally](#item-5) ⭐️ 7.0/10
6. [Costco's Warehouse Model Avoids Amazon's Last-Mile Woes](#item-6) ⭐️ 7.0/10
7. [Factories Are Just Rooms: Demystifying Manufacturing](#item-7) ⭐️ 7.0/10
8. [Wordgard: New Rich-Text Editor from ProseMirror Creator](#item-8) ⭐️ 7.0/10
9. [Valve open-sources Steam Machine e-ink screen for DIY](#item-9) ⭐️ 7.0/10
10. [LLM Cost Hack: Convert Code to Images for Cheaper OCR Tokens](#item-10) ⭐️ 7.0/10
11. [Hacker News explores novel LLM coding workflows](#item-11) ⭐️ 7.0/10
12. [Screwworm's Fall and Rise: A Cautionary Tale](#item-12) ⭐️ 7.0/10
13. [US data centers consume more power than any other country](#item-13) ⭐️ 7.0/10
14. [EVE Online Studio Fenris Open-Sources Carbon Engine](#item-14) ⭐️ 7.0/10
15. [Google Loses Antitrust Case, Fined €4.1 Billion](#item-15) ⭐️ 7.0/10
16. [Meta's custom chip enables DDR4 in DDR5 servers](#item-16) ⭐️ 7.0/10
17. [Anthropic Launches Claude Science for Drug Development](#item-17) ⭐️ 6.0/10
18. [Gaming Industry Roundup: Labor, Discs, and Price Fixing](#item-18) ⭐️ 6.0/10
19. [The Five-Layer AI Stack and Japan's Sovereign AI Role](#item-19) ⭐️ 6.0/10
20. [Palantir CEO blasts AI token pricing as 'effing insane'](#item-20) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [MEP Investigating Spyware Hacked with Pegasus](https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/) ⭐️ 8.0/10

Citizen Lab found with high confidence that European Parliament member Stelios Kouloglou, who served on the committee investigating spyware abuses, had his iPhone infected with Pegasus spyware on at least three occasions in 2022 and 2023. This incident demonstrates that even those tasked with investigating surveillance abuses are not safe from state-sponsored spyware, highlighting severe security gaps in European institutions and the ongoing threat of commercial spyware like Pegasus. The infections occurred on October 21, 2022, and March 6–7, 2023, while Kouloglou was a member of the PEGA committee. Citizen Lab noted that a Pegasus customer with authorization to spy in multiple European countries is likely responsible.

hackernews · ledoge · Jul 3, 20:38 · [Discussion](https://news.ycombinator.com/item?id=48779683)

**Background**: Pegasus is a powerful spyware developed by Israel's NSO Group, capable of remotely compromising mobile devices and extracting data, messages, and recordings. It has been widely abused by governments to target journalists, activists, and political opponents. The European Parliament established the PEGA committee in 2022 to investigate the use of Pegasus and similar spyware in Europe.

<details><summary>References</summary>
<ul>
<li><a href="https://citizenlab.ca/research/member-of-committee-investigating-spyware-hacked-with-pegasus/">Espionage Against the European Parliament: Member of ...</a></li>
<li><a href="https://www.theguardian.com/world/2026/jul/03/spyware-used-against-mep-investigating-pegasus-abuses-report-finds">Spyware used against MEP investigating Pegasus abuses, report ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Pegasus_(spyware)">Pegasus (spyware)</a></li>

</ul>
</details>

**Discussion**: Commenters expressed concern that the same phone contained both personal medical information and confidential government documents, questioning the lack of device separation policies. Some noted that using more secure phones like GrapheneOS could have prevented the attack, while others pointed to broader state-sponsored spyware scandals in Greece and Italy, suggesting the attack may be linked to domestic surveillance rather than a direct attack on the European Parliament.

**Tags**: `#cybersecurity`, `#spyware`, `#Pegasus`, `#surveillance`, `#European Parliament`

---

<a id="item-2"></a>
## [Ubicloud advocates strict memory overcommit for PostgreSQL](https://www.ubicloud.com/blog/postgresql-and-the-oom-killer-why-we-use-strict-memory-overcommit) ⭐️ 8.0/10

Ubicloud published a blog post explaining why they use strict memory overcommit (vm.overcommit_memory=2) for PostgreSQL to avoid OOM killer disruptions, and the community discussion highlights trade-offs and operational cautions. This matters because PostgreSQL is sensitive to memory pressure, and the default Linux overcommit behavior can lead to OOM killer killing Postgres, causing downtime. The discussion provides practical insights for database operators considering similar changes. Strict overcommit (mode 2) prevents the kernel from overcommitting memory, reducing OOM killer risk, but can cause fork failures if overcommit ratio is not tuned. The author recommends testing in QA environments and using dynamic sysctl changes during deployment.

hackernews · furkansahin · Jul 3, 13:00 · [Discussion](https://news.ycombinator.com/item?id=48774509)

**Background**: Linux memory overcommit allows processes to allocate more virtual memory than physical RAM available. When memory is exhausted, the OOM killer terminates a process to free memory. PostgreSQL often becomes a victim due to its large memory usage, causing database outages.

<details><summary>References</summary>
<ul>
<li><a href="https://www.baeldung.com/linux/memory-overcommitment-oom-killer">Linux Memory Overcommitment and the OOM Killer - Baeldung</a></li>
<li><a href="https://www.baeldung.com/linux/overcommit-modes">Linux Overcommit Modes - Baeldung</a></li>
<li><a href="https://linuxhandbook.com/oom-killer/">What is Out of Memory Killer (OOM Killer) in Linux?</a></li>

</ul>
</details>

**Discussion**: Commenters note that Linux default memory management is problematic, and caution that mode 2 can prevent forks if not tested. Ubicloud's Ozgun acknowledges the blog's strong tone and agrees strict overcommit is not suitable for all scenarios.

**Tags**: `#PostgreSQL`, `#Linux`, `#memory management`, `#OOM killer`, `#database operations`

---

<a id="item-3"></a>
## [Startup's Smart Oven Fails Due to Lack of Domain Expertise](https://weli.dev/blog/half-baked-product/) ⭐️ 8.0/10

A startup founder attempted to build a smart oven without any domain expertise, resulting in a half-baked product that failed to meet market needs. This story highlights the critical importance of domain expertise in product development, serving as a cautionary tale for founders and engineers about the pitfalls of entering unfamiliar industries. The founder's primary motivation was wealth, not solving a real problem, leading to a mismatch between vision and technical feasibility. The article and 361 comments discuss common startup failures like lack of customer understanding and over-reliance on fundraising.

hackernews · weli · Jul 3, 08:23 · [Discussion](https://news.ycombinator.com/item?id=48772388)

**Background**: Domain expertise refers to deep knowledge and experience in a specific field, which is crucial for identifying real customer needs and feasible technical solutions. Many startups fail because founders prioritize market trends over genuine expertise, as seen in this smart oven case.

**Discussion**: Commenters generally agree that the founder's lack of domain expertise and focus on wealth were root causes. Some note this pattern is common across industries, while others humorously compare it to their own startup attempts in unrelated fields.

**Tags**: `#startups`, `#product development`, `#domain expertise`, `#entrepreneurship`

---

<a id="item-4"></a>
## [Device Revives Donor Eyes, Paving Way for Transplants](https://www.technologyreview.com/2026/07/03/1140148/a-device-that-revives-eyeballs-from-dead-donors-could-make-eye-transplants-possible/) ⭐️ 8.0/10

Researchers have developed a device that preserves and revives eyeballs from deceased donors, potentially overcoming a key barrier to whole-eye transplantation. Whole-eye transplants could restore sight for millions of blind individuals, but rapid tissue degeneration after death has made them impossible until now. This device could enable the first successful sight-restoring eye transplants. The device maintains the eye's viability by supplying nutrients and oxygen, preventing degeneration after removal from the donor. It addresses the critical issue of retinal survival and optic nerve preservation.

rss · MIT Technology Review · Jul 3, 17:34

**Background**: Whole-eye transplantation faces three major challenges: retinal survival, immune rejection, and optic nerve regeneration. Previous attempts, such as the world's first whole-eye and partial-face transplant in 2023, resulted in a viable eye but no vision restoration. The new device specifically targets the first challenge by keeping the eye alive outside the body.

<details><summary>References</summary>
<ul>
<li><a href="https://www.aao.org/eyenet/article/eyes-on-the-prize-whole-eye-transplant">Eyes on the Prize: The Quest to Restore Vision With Whole Eye Transplant - American Academy of Ophthalmology</a></li>
<li><a href="https://nyulangone.org/news/worlds-first-whole-eye-partial-face-transplant-recipient-achieves-remarkable-recovery-viable-eye-one-year-after-landmark-surgery">The World’s First Whole-Eye & Partial-Face Transplant Recipient Achieves Remarkable Recovery, with Viable Eye One Year After Landmark Surgery | NYU Langone News</a></li>
<li><a href="https://wyss.harvard.edu/news/vision-for-whole-eye-transplant/">Vision for whole eye transplant - Wyss Institute</a></li>

</ul>
</details>

**Tags**: `#biotechnology`, `#medical devices`, `#transplantation`, `#ophthalmology`

---

<a id="item-5"></a>
## [Guide to Running SOTA LLMs Locally](https://github.com/jamesob/local-llm) ⭐️ 7.0/10

Jamesob published a comprehensive guide on GitHub detailing how to build and run state-of-the-art large language models locally, with hardware recommendations ranging from budget setups to a $40K+ high-end configuration. This guide helps developers and enthusiasts understand the real costs and trade-offs of local LLM inference, sparking debate on whether local setups are cost-effective compared to cloud subscriptions. The high-end build includes 4 GPUs at $12K each, totaling around $50-55K, and relies on quantization to run models like those approaching Claude Opus quality.

hackernews · livestyle · Jul 3, 15:03 · [Discussion](https://news.ycombinator.com/item?id=48775921)

**Background**: Running large language models locally requires significant GPU VRAM; for example, a 70B parameter model may need 48GB or more. Quantization reduces memory requirements but can lower output quality. Cloud services like ChatGPT offer easier access but raise privacy and cost concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/aanoskov/local_llms_quantized">GitHub - aanoskov/ local _llms_quantized: This repository demonstrates...</a></li>
<li><a href="https://specpicks.com/reviews/best-budget-gpu-local-llm-inference-2026">Best Budget GPU for Local LLM Inference in 2026 | SpecPicks</a></li>
<li><a href="https://www.hivenet.com/post/best-7-gpus-for-llm-inference-and-fine-tuning">Best GPUs for LLM inference and fine-tuning in 2026 | Hivenet</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the $40K build actually costs $50-55K, and that $40K could cover 16.8 years of Claude Opus subscription. Some suggested alternatives like unified memory architectures (e.g., M5 MacBook Pro with 48GB) or cloud hosting as cheaper options.

**Tags**: `#LLM`, `#local inference`, `#hardware`, `#deep learning`, `#open source`

---

<a id="item-6"></a>
## [Costco's Warehouse Model Avoids Amazon's Last-Mile Woes](https://phenomenalworld.org/analysis/the-anti-amazon/) ⭐️ 7.0/10

An analysis argues that Costco's warehouse club model inherently avoids the logistical complexity and social costs of Amazon's last-mile delivery system, highlighting a fundamental strategic divergence in retail. This comparison matters because it challenges the assumption that e-commerce delivery is always superior, revealing trade-offs in convenience, cost, and societal impact that affect consumers, retailers, and urban planners. Costco's model relies on customers driving to warehouses and transporting goods themselves, avoiding the per-package delivery cost and traffic congestion associated with last-mile logistics. However, Costco also partners with Instacart for same-day delivery, offering a hybrid option.

hackernews · bookofjoe · Jul 3, 15:14 · [Discussion](https://news.ycombinator.com/item?id=48776044)

**Background**: Last-mile delivery is the final step of the supply chain where goods are transported from a distribution center to the customer's door. It is often the most expensive and inefficient part of logistics due to low drop sizes and multiple stops. Costco's warehouse model, in contrast, uses bulk shipments to centralized locations where customers pick up items themselves, reducing per-unit logistics costs.

<details><summary>References</summary>
<ul>
<li><a href="https://www.gofo.com/us/track">Last - Mile Delivery for E-Commerce Parcel Logistics Network | GOFO</a></li>
<li><a href="https://www.solbox.it/how-last-mile-delivery-logistics-has-evolved-in-food-logistics/">How Last Mile Delivery Logistics Has Evolved in Food... - SolBox</a></li>

</ul>
</details>

**Discussion**: Commenters praised the engineering wisdom of avoiding the last-mile problem, with one quoting a proverb: 'A clever person solves a problem; a wise person avoids it.' Others noted Costco's international presence and non-food offerings, while some pointed out that Costco now offers delivery via Instacart, partially bridging the gap.

**Tags**: `#logistics`, `#retail`, `#business strategy`, `#engineering`, `#e-commerce`

---

<a id="item-7"></a>
## [Factories Are Just Rooms: Demystifying Manufacturing](https://interconnected.org/home/2026/07/03/factories) ⭐️ 7.0/10

An article argues that factories are fundamentally just rooms where things are made, challenging the mystique of industrial production and encouraging a more accessible view of manufacturing. This perspective could democratize manufacturing by reducing the perceived barriers to entry, inspiring more people to start small-scale production and fostering a culture of making. The article, published on interconnected.org, has sparked high engagement on Hacker News with 170 points and 71 comments, indicating strong community interest in rethinking manufacturing.

hackernews · arbesman · Jul 3, 15:13 · [Discussion](https://news.ycombinator.com/item?id=48776035)

**Background**: Manufacturing is often seen as complex and capital-intensive, requiring specialized machinery and large facilities. The article challenges this notion by suggesting that a simple room with basic tools can serve as a factory, emphasizing that the essence of production is the act of making, not the environment.

**Discussion**: Commenters shared personal experiences, with one noting how a small UK factory with hand assembly was enjoyable, while another pointed out that a 'just a room' approach may not sustain consistent business. The discussion reflects a mix of admiration for simplicity and recognition of practical challenges.

**Tags**: `#manufacturing`, `#philosophy of technology`, `#making`, `#industrial design`

---

<a id="item-8"></a>
## [Wordgard: New Rich-Text Editor from ProseMirror Creator](https://wordgard.net/) ⭐️ 7.0/10

Wordgard 0.1.0, a new in-browser rich-text editor, has been released by the creator of ProseMirror. It shares many concepts with ProseMirror but offers a fresh approach with no upgrade path. Wordgard introduces a new design for rich-text editing on the web, potentially influencing future editor development. Developers using ProseMirror or similar libraries will need to evaluate whether to adopt this new system. Wordgard is not an upgrade from ProseMirror; switching requires significant rework. It is designed for modern web applications and emphasizes a different internal architecture.

hackernews · indy · Jul 3, 08:50 · [Discussion](https://news.ycombinator.com/item?id=48772573)

**Background**: ProseMirror is a widely-used, battle-tested rich-text editor framework with a steep learning curve. Wordgard is a new system by the same author, aiming to address some limitations of ProseMirror while maintaining similar concepts.

<details><summary>References</summary>
<ul>
<li><a href="https://discuss.prosemirror.net/t/wordgard-0-1-0/9035">Wordgard 0.1.0 - Announce - discuss.ProseMirror</a></li>
<li><a href="https://prosemirror.net/">ProseMirror</a></li>

</ul>
</details>

**Discussion**: The community expressed interest in understanding the 'why' behind Wordgard and noted the lack of an upgrade path. Some developers found the design validating for their own approaches, while others highlighted the need for statically-typed document representations.

**Tags**: `#rich-text editor`, `#ProseMirror`, `#web development`, `#open source`, `#WYSIWYG`

---

<a id="item-9"></a>
## [Valve open-sources Steam Machine e-ink screen for DIY](https://www.gamingonlinux.com/2026/07/valve-open-source-the-steam-machine-e-ink-screen-so-you-can-make-your-own/) ⭐️ 7.0/10

Valve has released the open-source designs for the e-ink screen used in the Steam Machine, allowing anyone to build their own compatible display. The screen is based on a standard Adafruit 5.83-inch e-ink panel. This move empowers the community to customize and innovate on Steam Machine hardware, reinforcing Valve's reputation for openness. It could inspire similar DIY projects for other devices like the Framework Desktop. The e-ink screen displays system stats and uses proprietary waveforms for high refresh rates and color contrast without full screen resets. Valve will not manufacture the display themselves, but third parties like Jsaux are working on compatible versions.

hackernews · ahlCVA · Jul 3, 13:01 · [Discussion](https://news.ycombinator.com/item?id=48774518)

**Background**: The Steam Machine is Valve's living room gaming console running SteamOS. The e-ink screen is an optional front-panel display that shows system information like CPU/GPU usage and game art. Valve has a history of open-source contributions, including funding the FEX emulator and Mesa3D Turnip driver.

<details><summary>References</summary>
<ul>
<li><a href="https://www.theverge.com/games/961242/valve-just-open-sourced-its-e-ink-screen-for-the-steam-machine">Valve just open-sourced its e-ink screen for the Steam Machine.</a></li>
<li><a href="https://www.gamingonlinux.com/2025/11/igalia-detail-their-open-source-work-for-valves-steam-frame-and-steam-machine/">Igalia detail their open source work for Valve's Steam Frame and Steam Machine | GamingOnLinux</a></li>

</ul>
</details>

**Discussion**: Commenters praised Valve's openness, with one wishing more companies would follow suit. Some discussed using the design with Framework Desktop, while others debated the business benefits of Valve's goodwill. A technical question about larger e-ink screens with HDMI input also arose.

**Tags**: `#open-source`, `#hardware`, `#valve`, `#e-ink`, `#steam-machine`

---

<a id="item-10"></a>
## [LLM Cost Hack: Convert Code to Images for Cheaper OCR Tokens](https://github.com/teamchong/pxpipe) ⭐️ 7.0/10

A technique called pxpipe reduces LLM API costs by converting text-based code into images and then using OCR to extract the text, exploiting the fact that image tokens are often priced lower than text tokens. This hack could significantly cut API costs for developers who process large amounts of code or text, but it may be a temporary loophole that providers could close by adjusting token pricing. The approach reportedly reduces prompt tokens by up to 60%, but may increase completion tokens, potentially making it slower and more expensive overall, as noted by a previous attempt with OpenAI models.

hackernews · dimitropoulos · Jul 3, 15:50 · [Discussion](https://news.ycombinator.com/item?id=48776464)

**Background**: LLM APIs charge based on token usage, with separate pricing for input and output tokens. Image tokens are sometimes cheaper than text tokens, creating an arbitrage opportunity. OCR (Optical Character Recognition) is used to extract text from images, but the model may still process the image as an image, leading to potential token accounting loopholes.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/">The unified interface for LLMs. Find the best models & prices for your...</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that this is likely a token accounting loophole that may be closed, and that similar attempts with OpenAI resulted in higher overall costs due to increased completion tokens. Some also note that this technique is essentially rediscovering compressed binary formats for efficiency.

**Tags**: `#LLM`, `#cost optimization`, `#OCR`, `#hack`

---

<a id="item-11"></a>
## [Hacker News explores novel LLM coding workflows](https://news.ycombinator.com/item?id=48771515) ⭐️ 7.0/10

A Hacker News discussion highlights experiments with alternative LLM coding paradigms, including tab models, hermetic agents, and heterogeneous LLM swarms, moving beyond the standard prompt-response loop. These experiments could lead to more seamless AI-assisted coding workflows, helping developers achieve flow state and improve code quality by reducing confirmation bias and enabling collaborative multi-model systems. The tab model offers inline completions rather than chat-based interaction, while hermetic agents sandbox code and test writers separately to avoid bias. Heterogeneous LLM swarms leverage multiple models across networked hardware for collaborative inference.

hackernews · yehiaabdelm · Jul 3, 06:21

**Background**: Current LLM coding tools like Claude Code and Codex rely on a prompt-response loop, which can disrupt flow state. The tab model, inspired by autocomplete, aims to provide continuous suggestions. Hermetic agents and LLM swarms are emerging approaches to improve code quality and leverage distributed resources.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/jovan_chan_9500711396d4e6/best-local-coding-llm-in-2026-qwen25-coder-vs-deepseek-coder-v2-vs-codestral-45g8">Best Local Coding LLM in 2026: Qwen2.5- Coder vs... - DEV Community</a></li>
<li><a href="https://github.com/anyscale/hermetic">GitHub - anyscale/hermetic: Hermetic is a library for developing, deploying and refining LLM Applications · GitHub</a></li>
<li><a href="https://arxiv.org/html/2606.14711">SWARM - LLM : Collaborative Inference for Edge-based Small...</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal experiments: one user built a heterogeneous swarm from old GPUs, another advocated for hermetic agents to avoid confirmation bias, and others noted the loss of flow state but offered alternative workflows like reviewing AI-generated code.

**Tags**: `#LLM`, `#coding`, `#AI-assisted development`, `#workflow`, `#experimentation`

---

<a id="item-12"></a>
## [Screwworm's Fall and Rise: A Cautionary Tale](https://www.construction-physics.com/p/the-fall-and-rise-of-screwworm) ⭐️ 7.0/10

An article on Construction Physics traces the history of screwworm eradication using sterile insect technique and its recent resurgence, with confirmed cases in South Texas in 2026. This story highlights the fragility of past agricultural victories and the ongoing threat of screwworm to livestock and wildlife, underscoring the need for sustained vigilance and international cooperation. The screwworm (Cochliomyia hominivorax) is a parasitic fly whose larvae feed on living tissue; eradication relied on releasing radiation-sterilized males to suppress reproduction, a method pioneered in the 1950s.

hackernews · crescit_eundo · Jul 3, 12:58 · [Discussion](https://news.ycombinator.com/item?id=48774492)

**Background**: Screwworm infestations cause severe wounds and death in warm-blooded animals, costing the livestock industry billions. The sterile insect technique (SIT) successfully eradicated screwworm from the US and Central America, but a permanent barrier at the Darién Gap has been difficult to maintain, leading to recent incursions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cochliomyia_hominivorax">Cochliomyia hominivorax - Wikipedia</a></li>
<li><a href="https://www.nal.usda.gov/exhibits/speccoll/exhibits/show/stop-screwworms--selections-fr/introduction">Introduction · STOP Screwworms : Selections from the Screwworm ...</a></li>
<li><a href="https://publichealth.jhu.edu/2026/what-to-know-about-new-world-screwworm">What to Know About New World Screwworm | Johns Hopkins</a></li>

</ul>
</details>

**Discussion**: Commenters noted the evolutionary paradox of a parasite that kills its host, and questioned whether maintaining a barrier is cost-effective compared to continent-wide eradication. Others lamented that the original research would be impossible today due to ethical constraints.

**Tags**: `#ecology`, `#agriculture`, `#pest control`, `#science history`, `#public health`

---

<a id="item-13"></a>
## [US data centers consume more power than any other country](https://www.canarymedia.com/articles/data-centers/data-centers-use-more-power-in-the-us-than-anywhere-else) ⭐️ 7.0/10

In 2025, nearly 40% of global data center electricity demand came from the United States, making it the largest consumer of data center power worldwide, according to the Statistical Review of World Energy. This highlights the immense energy footprint of US data centers, which has significant implications for energy policy, grid infrastructure, and the tech industry's sustainability goals as demand continues to surge. The data comes from the 2025 Statistical Review of World Energy, which tracks global energy statistics. US data centers alone account for nearly 40% of global data center power demand, surpassing even China.

rss · Latitude Media (Canary Media) · Jul 3, 07:30

**Background**: Data centers are facilities that house computer systems and associated components, such as telecommunications and storage systems. They consume vast amounts of electricity to power servers and cooling systems. The Statistical Review of World Energy is an annual report that provides comprehensive data on global energy production and consumption.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Statistical_Review_of_World_Energy">Statistical Review of World Energy</a></li>
<li><a href="https://www.energyinst.org/statistical-review/about">energyinst.org/ statistical - review /about</a></li>
<li><a href="https://kpmg.com/xx/en/our-insights/esg/statistical-review-of-world-energy.html">Energy Institute Statistical Review of World Energy</a></li>

</ul>
</details>

**Tags**: `#data centers`, `#energy consumption`, `#US`, `#technology`, `#infrastructure`

---

<a id="item-14"></a>
## [EVE Online Studio Fenris Open-Sources Carbon Engine](https://www.pcgamer.com/games/mmo/eve-online-studio-fenris-follows-through-on-yearslong-promise-to-make-its-in-house-game-engine-fully-open-source/) ⭐️ 7.0/10

Fenris Creations, the studio behind EVE Online, has fully open-sourced its in-house Carbon game engine framework on GitHub as of July 1, 2026. This move enables community contributions, transparency, and potential reuse of a proven MMO engine, setting a precedent for other studios to follow. The open-source release includes over two dozen modular components from the Carbon engine, which powers both EVE Online and EVE Frontier.

rss · PC Gamer · Jul 3, 17:18

**Background**: Fenris Creations (formerly CCP Games) first promised to open-source the Carbon engine in 2024. Carbon is a cross-platform game engine framework that has been developed in-house for years, supporting the massive single-shard universe of EVE Online.

<details><summary>References</summary>
<ul>
<li><a href="https://www.opensourceforu.com/2026/07/fenris-creations-carbon-game-engine-goes-open-source-on-github/">Fenris Creations' Carbon Game Engine Goes Open-Source On GitHub - Open Source For You</a></li>
<li><a href="https://www.gamesindustry.biz/eve-onlines-carbon-engine-is-now-open-source-fenris-creations-explains-why">Eve Online's Carbon engine is now open source: Fenris Creations explains why | GamesIndustry.biz</a></li>
<li><a href="https://massivelyop.com/2026/07/01/eve-onlines-fenris-creations-just-open-sourced-the-carbon-engine-framework-its-built-on/">EVE Online’s Fenris Creations just open-sourced the Carbon engine framework it’s built on | Massively Overpowered</a></li>

</ul>
</details>

**Discussion**: Community reactions are largely positive, with many praising the transparency and potential for modding. Some discussions note the distinction between the Carbon framework and blockchain-related features, expressing cautious optimism.

**Tags**: `#open source`, `#game engine`, `#EVE Online`, `#Fenris`

---

<a id="item-15"></a>
## [Google Loses Antitrust Case, Fined €4.1 Billion](https://www.pcgamer.com/hardware/google-loses-protracted-antitrust-fight-and-will-have-to-pay-record-breaking-eur4-1-billion-fine-equivalent-to-less-than-3-percent-of-alphabets-annual-profit/) ⭐️ 7.0/10

Google has lost a protracted antitrust fight and will pay a record-breaking €4.1 billion fine, which is less than 3% of Alphabet's annual profit. This ruling sets a significant precedent for antitrust enforcement against big tech companies, potentially leading to stricter regulations and more scrutiny of Google's business practices. The fine is the largest ever imposed by the European Union in an antitrust case, yet it represents only a small fraction of Alphabet's annual profit, highlighting the limited financial impact on the company.

rss · PC Gamer · Jul 3, 15:29

**Background**: Antitrust laws are designed to promote competition and prevent monopolistic behavior. The European Commission has been investigating Google's practices in areas such as search and advertising for years, leading to multiple fines.

**Tags**: `#antitrust`, `#Google`, `#regulation`, `#tech industry`, `#legal`

---

<a id="item-16"></a>
## [Meta's custom chip enables DDR4 in DDR5 servers](https://www.pcgamer.com/hardware/memory/metas-solution-to-the-global-memory-shortage-is-to-use-ddr4-in-a-ddr5-server-with-a-custom-chip-making-the-impossible-possible/) ⭐️ 7.0/10

Meta developed a custom chip that allows DDR4 memory modules to be used in servers designed for DDR5, addressing memory shortages by repurposing older RAM. This innovation helps Meta overcome global memory shortages and reduce e-waste by extending the life of DDR4 modules, though it is not applicable to consumer PCs. The custom chip manages the DDR4 sticks as a separate, slower memory pool alongside the main DDR5 pool, enabling hybrid memory configurations in servers.

rss · PC Gamer · Jul 3, 12:59

**Background**: DDR4 and DDR5 are different generations of RAM with incompatible physical and electrical interfaces, so they cannot be mixed on standard motherboards. Meta's solution uses a custom chip to bridge this gap, allowing older DDR4 modules to supplement DDR5 in servers.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/hardware/memory/metas-solution-to-the-global-memory-shortage-is-to-use-ddr4-in-a-ddr5-server-with-a-custom-chip-making-the-impossible-possible/">Meta 's solution to the global memory shortage is to use... | PC Gamer</a></li>

</ul>
</details>

**Tags**: `#hardware`, `#memory`, `#Meta`, `#server`, `#innovation`

---

<a id="item-17"></a>
## [Anthropic Launches Claude Science for Drug Development](https://www.theverge.com/ai-artificial-intelligence/961311/anthropic-claude-science-ai-drug-development) ⭐️ 6.0/10

Anthropic announced Claude Science, an AI workbench for scientists that integrates fragmented tools and datasets into one environment, enabling researchers to generate figures and visuals. The launch was framed around drug development at the 'AI for Science' event. Claude Science could accelerate scientific research, particularly drug discovery, by reducing time spent on tool integration and allowing researchers to focus on core science. It positions Anthropic to compete in the growing AI-for-science market alongside other tech giants. Claude Science is a desktop app available in beta on macOS and Linux, integrating commonly used research tools and packages. It produces auditable artifacts and provides flexible access to computing resources.

rss · The Verge · Jul 3, 13:56

**Background**: Anthropic is known for its Claude AI models and coding tools. The company launched an 'AI for Science' program in May 2025 to accelerate research through API access. Claude Science is the latest product under this initiative, targeting scientists who need streamlined workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-science-ai-workbench">Claude Science, an AI workbench for scientists \ Anthropic</a></li>
<li><a href="https://claude.com/product/claude-science">Claude Science beta | Claude by Anthropic</a></li>
<li><a href="https://claude.com/docs/claude-science/overview">Claude Science - Claude.ai Documentation</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Anthropic`, `#science`, `#drug development`, `#tools`

---

<a id="item-18"></a>
## [Gaming Industry Roundup: Labor, Discs, and Price Fixing](https://www.gamedeveloper.com/business/rockstar-workers-hit-back-playstation-ditches-physical-discs-and-chipmakers-accused-of-price-fixing-patch-notes-58) ⭐️ 6.0/10

Rockstar Games fired QA testers who were attempting to unionize, leading to protests outside their Edinburgh office. Sony announced it will phase out physical disc production for PlayStation games by 2028, moving to an all-digital future. A class-action lawsuit accused Samsung, SK Hynix, and Micron of fixing RAM prices. These events highlight major shifts in the gaming industry: labor rights conflicts, the end of physical media, and potential hardware cost inflation due to alleged price fixing. They affect developers, gamers, and the broader tech ecosystem. Rockstar accused the fired testers of gross misconduct and leaking secrets, while the workers claim retaliation for union organizing. Sony's disc-less transition begins in 2028, ending trade-ins and lending. The RAM price-fixing lawsuit references a past 2002 DRAM scandal.

rss · Game Developer (Gamasutra) · Jul 3, 10:36

**Background**: The gaming industry has seen increasing labor activism, with QA workers often facing poor conditions and job insecurity. Physical game discs have been declining due to digital distribution, but Sony's move signals a definitive end. RAM price-fixing has historical precedent, with major chipmakers previously convicted.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/games/grand-theft-auto/all-you-had-to-do-was-follow-the-damn-law-rockstar-workers-are-protesting-outside-take-two-after-gta-6-devs-alleged-ruthless-union-busting/">'All you had to do was follow the damn law, Rockstar !': Workers are...</a></li>
<li><a href="https://www.msn.com/en-us/entertainment/gaming/playstation-s-disc-less-future-could-heavily-influence-xbox-and-nintendo-former-sony-boss-says/ar-AA279L9e">PlayStation's disc-less future could heavily influence Xbox ...</a></li>
<li><a href="https://www.dualshockers.com/ram-price-fixing-lawsuit-explained/">RAM Price-Fixing Lawsuit Explained: Samsung, SK Hynix, and ...</a></li>

</ul>
</details>

**Tags**: `#gaming`, `#industry news`, `#labor`, `#hardware`, `#legal`

---

<a id="item-19"></a>
## [The Five-Layer AI Stack and Japan's Sovereign AI Role](https://www.4gamer.net/games/991/G999110/20260703032/) ⭐️ 6.0/10

At IVS2026, a session titled 'The New AI Stack' introduced a five-layer model of AI infrastructure—spanning energy, data centers, networking, GPU servers, and applications—and highlighted Japan's strategic position as a hub for sovereign AI and large-scale AI factories, exemplified by a facility in Kagoshima. This framework provides a clear, layered understanding of the physical and digital infrastructure underpinning modern AI, helping stakeholders identify bottlenecks and investment opportunities. Japan's emphasis on sovereign AI and domestic AI factories could reduce reliance on foreign technologies and strengthen national AI autonomy. The five layers are: Energy (power generation and distribution), Data Center (facilities housing compute), Network (connectivity including submarine cables), GPU Servers (compute hardware), and Applications (user-facing AI services). The Kagoshima AI factory is cited as a concrete example of Japan's investment in large-scale AI infrastructure.

rss · 4Gamer.net · Jul 3, 10:22

**Background**: Sovereign AI refers to a nation's ability to produce AI using its own infrastructure, data, workforce, and business networks, aligning with its own rules and values. The AI stack concept helps demystify the complex layers required to deliver AI services, from raw power to end-user applications. IVS2026 is Japan's largest startup conference, held in Kyoto.

<details><summary>References</summary>
<ul>
<li><a href="https://medium.com/@ThinkingLoop/the-new-ai-stack-explained-in-5-layers-74fea810df8d">The New AI Stack, Explained in 5 Layers - Medium</a></li>
<li><a href="https://www.linkedin.com/pulse/5-layer-ai-stack-why-understanding-every-layer-your-secret-naik-nguhc">The 5-Layer AI Stack: Why Understanding Every Layer Is Your ...</a></li>
<li><a href="https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-sovereign-ai">What is sovereign AI? | McKinsey</a></li>

</ul>
</details>

**Tags**: `#AI infrastructure`, `#sovereign AI`, `#Japan`, `#GPU`, `#conference`

---

<a id="item-20"></a>
## [Palantir CEO blasts AI token pricing as 'effing insane'](https://www.pcgamer.com/software/ai/something-has-gone-completely-wrong-palantir-ceo-rants-on-live-television-about-his-problems-with-the-ai-business-model-why-are-they-charging-for-tokens-if-its-so-valuable/) ⭐️ 6.0/10

Palantir CEO Alex Karp went on CNBC to denounce the token-based pricing model used by leading AI labs like OpenAI and Anthropic, calling it an 'effing insane' business model that imposes a 'wealth tax' on enterprises. Karp's criticism highlights growing enterprise frustration with AI pricing, potentially pushing the industry toward alternative models like flat fees or outcome-based pricing, which could reshape how AI services are commercialized. Karp specifically argued that charging per token for AI usage is flawed because it penalizes heavy users and fails to align costs with value delivered, while also risking enterprise data being used to improve competitors' models.

rss · PC Gamer · Jul 3, 10:04

**Background**: Most major AI companies, including OpenAI and Anthropic, charge developers based on the number of tokens processed (input and output). This model has become standard for API access, but critics argue it creates unpredictable costs and disincentivizes widespread adoption. Palantir, a data analytics firm, builds custom AI solutions for government and enterprise clients, making it sensitive to pricing inefficiencies.

<details><summary>References</summary>
<ul>
<li><a href="https://www.forbes.com/sites/tylerroush/2026/07/01/palantir-billionaire-alex-karp-calls-ai-industry-effing-insane-in-heated-interview/">Palantir Billionaire Karp Blasts AI Industry As ‘Effing Insane’</a></li>
<li><a href="https://cryptobriefing.com/palantir-karp-criticizes-ai-token-chasers/">Palantir CEO criticizes AI labs for 'tokenmaxxing,' backs enterprise.....</a></li>
<li><a href="https://www.alexjoneslive.com/2026/07/02/something-has-gone-completely-wrong-palantirs-alex-karp-goes-ballistic-on-openai-anthropic/">'Something Has Gone Completely Wrong': Palantir 's Alex Karp Goes....</a></li>

</ul>
</details>

**Tags**: `#AI`, `#business model`, `#Palantir`, `#industry commentary`

---