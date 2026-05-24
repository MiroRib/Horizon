---
layout: default
title: "Horizon Summary: 2026-05-24 (EN)"
date: 2026-05-24
lang: en
---

> From 72 items, 16 important content pieces were selected

---

1. [16-Byte Windows Executable Pushes Demo Size Limits](#item-1) ⭐️ 9.0/10
2. [Memory Now 63% of AI Chip Component Costs](#item-2) ⭐️ 8.0/10
3. [Constraint Decay: LLM Agents Fail on Backend Code Rules](#item-3) ⭐️ 8.0/10
4. [Microsoft open-sources earliest known DOS source code](#item-4) ⭐️ 8.0/10
5. [Usborne 1980s Computer Books Now Available Online](#item-5) ⭐️ 8.0/10
6. [DeepSeek Makes Permanent 75% Discount on Flagship AI Model](#item-6) ⭐️ 8.0/10
7. [AMD drops Linux support for free Vivado tier](#item-7) ⭐️ 8.0/10
8. [Australia Four-Day Work Week Study Shows Productivity Gains](#item-8) ⭐️ 7.0/10
9. [Go to Rust Migration Guide Sparks Debate](#item-9) ⭐️ 7.0/10
10. [Greg Brockman Interview Criticized for Superficiality](#item-10) ⭐️ 7.0/10
11. [Scammers abuse internal Microsoft account to send spam](#item-11) ⭐️ 7.0/10
12. [Mastering Dyalog APL as Interactive Jupyter Notebooks](#item-12) ⭐️ 6.0/10
13. [Ruby for Good: Maintainers Gather for Social Good](#item-13) ⭐️ 6.0/10
14. [Hackers evolve from simple prompt injection to personality exploits](#item-14) ⭐️ 6.0/10
15. [Beluga Whales Pass the Mirror Test](#item-15) ⭐️ 6.0/10
16. [Godot beats Unity in size, speed, and load times test](#item-16) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [16-Byte Windows Executable Pushes Demo Size Limits](https://hellmood.111mb.de/wake_up_16b_writeup.html) ⭐️ 9.0/10

A 16-byte Windows executable, named 'Wake up! 16b', creates a full-screen demo with both visuals and sound, setting a new record for code size optimization in the demoscene. This achievement demonstrates the extreme limits of algorithmic density, inspiring the demoscene and low-level programming communities to explore what can be done within minimal binary sizes. The executable runs in real-mode DOS compatibility, using video memory as a calculation space to draw a Sierpinski fractal while simultaneously generating sound through PC speaker manipulation.

hackernews · MaximilianEmel · May 24, 00:30 · [Discussion](https://news.ycombinator.com/item?id=48253060)

**Background**: The demoscene is a community focused on creating small, self-contained programs called 'demos' that produce audio-visual presentations. Code golf is the practice of writing the smallest possible program to achieve a given task. This 16-byte demo is an extreme example of both, pushing beyond typical 4K or 64K intro sizes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Demoscene">Demoscene - Wikipedia SizeCoding Exploring the algorithmic density in 16 bytes of x86 assembly Home - Assembly X Demoscene - 30 years of Demoscene by Assembly. Deconstruction of a 16 byte demo - jsalter.tech</a></li>
<li><a href="https://board.flatassembler.net/topic.php?t=24270">flat assembler - 16 byte demo with graphics and sound</a></li>
<li><a href="https://blog.adafruit.com/2026/05/18/explorating-the-algorithmic-density-in-16-bytes-of-x86-assembly/">Exploring the algorithmic density in 16 bytes of x86 assembly</a></li>

</ul>
</details>

**Discussion**: The community expressed awe and admiration, with one commenter noting that a previous 32-byte demo without sound was thought to be the limit. Others shared related work and rabbit holes, such as a Sierpinski triangle built with recursive PowerPoint presentations.

**Tags**: `#demoscene`, `#code golf`, `#low-level programming`, `#executable compression`, `#x86 assembly`

---

<a id="item-2"></a>
## [Memory Now 63% of AI Chip Component Costs](https://epoch.ai/data-insights/ai-chip-component-cost-shares) ⭐️ 8.0/10

High-bandwidth memory (HBM) now accounts for 63% of AI chip component costs, up from 52% in Q1 2024, according to Epoch AI. This cost shift highlights a growing supply-demand imbalance in DRAM, driving up prices and potentially slowing AI hardware cost reductions. DRAM contract prices surged 171.8% year-over-year as of Q3 2025, with some RAM modules seeing up to 619% price increases.

hackernews · intelkishan · May 24, 16:31 · [Discussion](https://news.ycombinator.com/item?id=48258684)

**Background**: AI chips rely heavily on high-bandwidth memory (HBM) for fast data access during training and inference. DRAM manufacturing capacity has struggled to keep pace with surging AI demand, leading to price spikes.

<details><summary>References</summary>
<ul>
<li><a href="https://epoch.ai/data-insights/ai-chip-component-cost-shares">AI Chip Component Costs: Memory at 63% | Epoch AI</a></li>
<li><a href="https://www.tomshardware.com/pc-components/dram/dram-prices-surge-171-percent-year-over-year-ai-demand-drives-a-higher-yoy-price-increase-than-gold">DRAM prices skyrocket 171% year-over-year, outpacing the rate of gold ...</a></li>
<li><a href="https://www.glukhov.org/hardware/memory/ram-price-increase/">RAM Price Surge: Up to 619% in 2025 - glukhov.org</a></li>

</ul>
</details>

**Discussion**: Commenters noted dramatic price increases (e.g., 96GB RAM from $250 to $1200) and expressed concern about consumer affordability. Some suggested that waiting for supply to catch up could yield ~3x hardware cost reduction without innovation.

**Tags**: `#AI hardware`, `#memory costs`, `#DRAM`, `#semiconductors`, `#supply chain`

---

<a id="item-3"></a>
## [Constraint Decay: LLM Agents Fail on Backend Code Rules](https://arxiv.org/abs/2605.06445) ⭐️ 8.0/10

A systematic study reveals that LLM-based coding agents exhibit constraint decay, performing well on unconstrained code generation but dropping significantly in assertion pass rate when required to follow architectural, ORM, and framework constraints in backend development. This finding highlights a critical reliability gap for LLM agents in production backend development, where adherence to structural rules is essential, and suggests that current agents are only suitable for rapid prototyping, not for production-grade code generation. The study observed that on multi-file backend generation, LLM agents dropped approximately 30 percentage points in assertion pass rate as constraints accumulated, with the loss concentrated on convention-heavy frameworks. The paper did not fully test frontier models due to cost constraints.

hackernews · wek · May 24, 12:55 · [Discussion](https://news.ycombinator.com/item?id=48256912)

**Background**: LLM-based coding agents are AI systems that generate code from natural language prompts. In backend development, code must satisfy both functional requirements (correct output) and structural requirements (e.g., architectural patterns, ORM conventions, framework rules). Constraint decay refers to the phenomenon where agents increasingly fail to meet structural constraints as more rules are introduced, even while maintaining functional correctness.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.06445">[2605.06445] Constraint Decay: The Fragility of LLM Agents in Backend Code Generation</a></li>
<li><a href="https://arxiv.org/html/2605.06445">Constraint decay: The Fragility of LLM Agents in Backend Code Generation</a></li>
<li><a href="https://agentpatterns.ai/verification/constraint-decay-backend-agents/">Constraint Decay in Backend Code Generation - AgentPatterns.ai</a></li>

</ul>
</details>

**Discussion**: Commenters noted that the industry already addresses this through ecosystems of skills, rules, tests, and agentic loops, but agreed that LLMs struggle as codebases grow. One commenter introduced the concept of 'calcification,' where patterns in the codebase degrade agent performance over time.

**Tags**: `#LLM agents`, `#code generation`, `#software engineering`, `#AI reliability`, `#backend development`

---

<a id="item-4"></a>
## [Microsoft open-sources earliest known DOS source code](https://arstechnica.com/gadgets/2026/04/microsoft-open-sources-the-earliest-dos-source-code-discovered-to-date/) ⭐️ 8.0/10

Microsoft has open-sourced the earliest known version of MS-DOS source code, painstakingly recovered from paper printouts via OCR by the DOS Disassembly Group. This release preserves a pivotal piece of computing history and offers rare insight into Microsoft's early operating system development, which laid the foundation for the PC revolution. The source code was recovered from paper printouts provided by original developer Tim Paterson, as modern OCR software struggled with the decades-old print quality.

hackernews · DamnInteresting · May 24, 01:21 · [Discussion](https://news.ycombinator.com/item?id=48253386)

**Background**: MS-DOS was the operating system that Microsoft licensed to IBM for the original IBM PC in 1981, becoming the dominant OS for the PC era. The code was written primarily in assembly language and was not stored digitally at the time.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/zacharywhitley/awesome-ocr">GitHub - zacharywhitley/awesome-ocr</a></li>
<li><a href="https://www.ocr4all.org/">OCR4all | Setup guide, user guide, developer documentation and more.</a></li>
<li><a href="https://stackoverflow.com/questions/1888587/need-good-ocr-for-printed-source-code-listing-any-ideas">Need good OCR for printed source code listing, any ideas?</a></li>

</ul>
</details>

**Discussion**: Commenters expressed gratitude to Microsoft for the release, with some noting the historical significance of the accompanying BASIC source code. Others marveled at how a few thousand lines of assembly could launch a successful software company.

**Tags**: `#open source`, `#history`, `#DOS`, `#Microsoft`, `#preservation`

---

<a id="item-5"></a>
## [Usborne 1980s Computer Books Now Available Online](https://usborne.com/us/books/computer-and-coding-books) ⭐️ 8.0/10

Usborne Publishing has made a collection of its 1980s computer books available online for free, allowing a new generation to access the titles that inspired many early programmers. These books played a pivotal role in teaching programming to a generation of children, and their online release preserves a key piece of computing history while making it accessible to modern learners. The collection includes titles such as 'Practice Your BASIC' and 'Write Your Own Adventure Programs', which taught programming concepts through hands-on projects and illustrations.

hackernews · ngram · May 24, 15:43 · [Discussion](https://news.ycombinator.com/item?id=48258194)

**Background**: In the 1980s, home computers like the Commodore 64 and ZX Spectrum were popular, and Usborne's books provided accessible introductions to programming in BASIC. These books were known for their colorful illustrations and step-by-step instructions, making complex topics approachable for children.

**Discussion**: Commenters shared personal stories of how these books inspired their coding careers, with one user recalling learning BASIC from a school library copy in 1989 and another porting BASIC listings to JavaScript in the early 2000s. The sentiment is overwhelmingly nostalgic and grateful, highlighting the books' lasting impact.

**Tags**: `#retro computing`, `#programming education`, `#nostalgia`, `#BASIC`

---

<a id="item-6"></a>
## [DeepSeek Makes Permanent 75% Discount on Flagship AI Model](https://www.bloomberg.com/news/articles/2026-05-23/deepseek-to-make-permanent-75-discount-on-flagship-ai-model) ⭐️ 8.0/10

DeepSeek announced a permanent 75% price reduction on its flagship AI model, V4 Pro, effective immediately. The discount, previously a temporary promotion, is now a permanent pricing change. This aggressive pricing move intensifies competition in the AI model market, potentially forcing rivals like OpenAI and Anthropic to lower prices. It also makes advanced AI more accessible to developers and businesses, accelerating adoption. The discount applies to DeepSeek's V4 Pro model, which is a 671B parameter Mixture-of-Experts model with 37B activated parameters per token. The price cut is permanent and not limited to a promotional period.

hackernews · moh_maya · May 24, 14:09 · [Discussion](https://news.ycombinator.com/item?id=48257410)

**Background**: DeepSeek is a Chinese AI company founded in 2023, known for developing cost-effective large language models. Its V3 model was trained for only $6 million, far less than competitors like GPT-4. The company's open-weight models and efficient training have disrupted the AI industry, often described as a 'Sputnik moment' for the US.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3">deepseek-ai/DeepSeek-V3 · Hugging Face</a></li>
<li><a href="https://github.com/deepseek-ai/DeepSeek-V3">GitHub - deepseek-ai/DeepSeek-V3</a></li>

</ul>
</details>

**Discussion**: The Hacker News community discussed the discount in a related thread, with some users noting the efficiency of DeepSeek's cache system. One commenter shared that using DeepSeek V4 Pro via a bridge resulted in a high cache hit rate (over 95%), reducing costs further.

**Tags**: `#AI`, `#pricing`, `#DeepSeek`, `#industry news`

---

<a id="item-7"></a>
## [AMD drops Linux support for free Vivado tier](https://adaptivesupport.amd.com/s/question/0D5Pd00001YQLdMKAX/why-is-vivado-20261-dropping-linux-support-for-free-tier-?language=en_US) ⭐️ 8.0/10

Starting with Vivado 2026.1, AMD will remove Linux support from the free Basic tier of its Vivado Design Suite, while Windows support remains available. This decision alienates students, hobbyists, and developers who rely on Linux for FPGA development, potentially shrinking the AMD FPGA ecosystem and driving users to competitors like Lattice. The Basic tier remains free but only for Windows; users needing Linux must upgrade to paid tiers. AMD has not provided a clear rationale for the change, despite community backlash.

hackernews · zdw · May 24, 04:14 · [Discussion](https://news.ycombinator.com/item?id=48254309)

**Background**: Vivado is AMD's primary FPGA design suite, used for synthesizing and implementing designs on Xilinx FPGAs. The free Basic tier has historically supported both Windows and Linux, enabling broad access for education and hobbyist use. Linux is preferred in many academic and professional environments for automation and cross-compilation workflows.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-buy.html">AMD Vivado™ Design Suite: Standard & Enterprise Edition</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado.html">AMD Vivado™ Design Suite</a></li>
<li><a href="https://www.amd.com/en/products/software/adaptive-socs-and-fpgas/vivado/vivado-licensing-options.html">AMD Vivado™ Licensing Options | Flexible Subscription & Perpetual Tiers</a></li>

</ul>
</details>

**Discussion**: Community comments express strong frustration, with users criticizing AMD for ignoring real concerns and harming the ecosystem. Some suggest switching to Lattice or Cologne Chip as alternatives, while long-term users note a decline in AMD's engineering focus since the acquisition.

**Tags**: `#FPGA`, `#AMD`, `#Vivado`, `#Linux`, `#hardware design`

---

<a id="item-8"></a>
## [Australia Four-Day Work Week Study Shows Productivity Gains](https://scienceaim.com/australia-just-proved-the-four-day-work-week-works-here-is-what-the-data-actually-says/) ⭐️ 7.0/10

A study on Australia's four-day work week trial reports productivity gains, reigniting debate on work culture and corporate motives. This matters because it provides empirical evidence supporting reduced work hours, challenging traditional five-day work norms and influencing global workplace policy discussions. The study is based on survey data rather than controlled experiments, leading some to criticize its scientific rigor. Australia is also experiencing a 60-year productivity low, which may affect the generalizability of the findings.

hackernews · randycupertino · May 24, 18:56 · [Discussion](https://news.ycombinator.com/item?id=48259990)

**Background**: The four-day work week is a workplace arrangement where employees work fewer days for the same pay, aiming to improve work-life balance and productivity. Proponents argue that technological advances should allow reduced working hours without sacrificing output.

**Discussion**: Commenters express skepticism about corporate motives, with some arguing that productivity gains have historically not led to reduced hours or higher wages. Others question the study's methodology, calling it an opinion survey rather than rigorous science. A few advocate for even shorter work weeks, such as one or three days.

**Tags**: `#work-life balance`, `#productivity`, `#workplace culture`, `#four-day work week`, `#labor economics`

---

<a id="item-9"></a>
## [Go to Rust Migration Guide Sparks Debate](https://corrode.dev/learn/migration-guides/go-to-rust/) ⭐️ 7.0/10

A detailed migration guide from Go to Rust was published on corrode.dev, sparking discussion about the practical trade-offs between the two languages for web back-end development. This discussion highlights the ongoing tension between Go's simplicity and managed runtime versus Rust's performance and safety, helping developers make informed language choices for back-end systems. The guide covers error handling, package management, and the borrow checker, while community comments point out that Go's standard library covers many needs that Rust requires external crates for.

hackernews · jabits · May 24, 18:31 · [Discussion](https://news.ycombinator.com/item?id=48259808)

**Background**: Go and Rust are both modern systems programming languages but with different philosophies: Go prioritizes simplicity and a managed runtime with garbage collection, while Rust offers zero-cost abstractions and memory safety without a garbage collector. The choice often depends on whether a managed runtime is acceptable for the target domain.

**Discussion**: Commenters like Animats and tptacek argue that for web back-end work, Go's managed runtime is often preferable, while others note Rust's package management complexity. A user also pointed out that the document contains stylistic patterns typical of LLM-generated text.

**Tags**: `#Go`, `#Rust`, `#migration`, `#web back-end`, `#programming languages`

---

<a id="item-10"></a>
## [Greg Brockman Interview Criticized for Superficiality](https://fs.blog/knowledge-project-podcast/greg-brockman/) ⭐️ 7.0/10

Greg Brockman, co-founder of OpenAI, gave an interview on The Knowledge Project podcast covering OpenAI's journey and controversies, but the discussion was widely criticized for lacking depth and avoiding key internal conflicts. As a key figure at OpenAI, Brockman's interview could have provided valuable insights into the organization's governance and internal dynamics, but its superficiality disappointed many in the AI community, highlighting a gap in public understanding of OpenAI's challenges. The interview scored 7.0/10, with community comments pointing out that it glossed over major events like the firing and reinstatement of Sam Altman, and the role of Ilya Sutskever. Critics also noted Brockman's personal diary, revealed in a Musk lawsuit, showed financial motivations.

hackernews · prakashqwerty · May 24, 08:29 · [Discussion](https://news.ycombinator.com/item?id=48255593)

**Background**: OpenAI was originally founded as a non-profit AI research organization but later created a capped-profit subsidiary to attract investment. This structure has been controversial, with critics arguing it undermines the non-profit mission. The interview touched on these issues but did not delve into specifics.

**Discussion**: Community comments were largely critical, with users expressing frustration over the interview's lack of depth. One commenter questioned why no one asked about Ilya Sutskever's role in the Altman firing saga, while another criticized the non-profit's shift to for-profit as setting a bad precedent. A user also referenced Brockman's personal diary from a Musk lawsuit, suggesting financial motives.

**Tags**: `#OpenAI`, `#interview`, `#AI governance`, `#non-profit controversy`

---

<a id="item-11"></a>
## [Scammers abuse internal Microsoft account to send spam](https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/) ⭐️ 7.0/10

Scammers have been exploiting a loophole in Microsoft's infrastructure to send spam and phishing emails from an internal Microsoft email address typically used for legitimate account alerts. This abuse undermines user trust in Microsoft's domain management and email security, potentially leading to more successful phishing attacks against Microsoft users. The issue has persisted for months, and the scammers are using an internal Microsoft account to send spam links and fake alerts, raising concerns about Microsoft's ability to secure its own domains.

hackernews · spike021 · May 24, 00:51 · [Discussion](https://news.ycombinator.com/item?id=48253186)

**Background**: Email authentication protocols like SPF, DKIM, and DMARC are designed to prevent domain spoofing and abuse. However, if an internal account is compromised or misused, these protections can be bypassed, making it difficult for recipients to distinguish legitimate emails from spam.

<details><summary>References</summary>
<ul>
<li><a href="https://techcrunch.com/2026/05/21/scammers-are-abusing-an-internal-microsoft-account-to-send-spam/">Scammers are abusing an internal Microsoft account to send spam links | TechCrunch</a></li>
<li><a href="https://techplanet.today/post/microsofts-internal-account-abuse-a-critical-security-failure-that-undermines-user-trust">Microsoft's Internal Account Abuse: A Critical Security Failure That Undermines User Trust | TechPlanet</a></li>
<li><a href="https://powerdmarc.com/what-is-domain-abuse/">What Is Domain Abuse ?</a></li>

</ul>
</details>

**Discussion**: Commenters expressed frustration with Microsoft's domain management, noting that the company's many domains create confusion and make it hard to identify legitimate emails. Some shared personal experiences with Microsoft security issues, while others suggested using subdomains like internal.microsoft.com to simplify domain management.

**Tags**: `#security`, `#phishing`, `#Microsoft`, `#spam`, `#domain abuse`

---

<a id="item-12"></a>
## [Mastering Dyalog APL as Interactive Jupyter Notebooks](https://mastering.dyalog.com/README.html) ⭐️ 6.0/10

The classic book 'Mastering Dyalog APL' has been republished as a set of interactive Jupyter Notebooks, allowing readers to run and modify APL code directly in the browser. This modern format lowers the barrier to learning APL, a powerful but niche array-oriented language, by providing hands-on practice without complex setup. It could help revive interest in APL for data analysis and algorithmic problem-solving. The notebooks are hosted on GitHub and can be run locally or via cloud services like Binder. They cover topics from basic array operations to advanced idioms, mirroring the original book's structure.

hackernews · tosh · May 24, 11:42 · [Discussion](https://news.ycombinator.com/item?id=48256475)

**Background**: APL is a programming language from the 1960s known for its concise, symbolic syntax and powerful array operations. Dyalog APL is the most widely used modern implementation, but it is proprietary and enterprise-licensed. Jupyter Notebooks provide an interactive environment that combines code, text, and visualizations, making them ideal for learning languages like APL.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Dyalog_APL">Dyalog APL</a></li>
<li><a href="https://github.com/Dyalog/dyalog-jupyter-notebooks">Jupyter notebooks for Dyalog APL - GitHub</a></li>

</ul>
</details>

**Discussion**: Commenters generally welcomed the interactive format, noting that hands-on practice is crucial for APL's symbol-heavy syntax. Some expressed concerns about Dyalog's proprietary licensing, while others recommended alternative learning resources like 'Learn APL' by xpqz.

**Tags**: `#APL`, `#programming languages`, `#education`, `#Jupyter`

---

<a id="item-13"></a>
## [Ruby for Good: Maintainers Gather for Social Good](https://ti.to/codeforgood/rubyforgood) ⭐️ 6.0/10

Ruby for Good announced an in-person gathering of open source maintainers to work on existing projects for social good, with early-bird registrations opened early due to community interest. This event highlights a shift from hackathon-style creation to sustained maintenance of social good projects, fostering long-term impact in the open source community. The event is explicitly not a hackathon; it focuses on maintaining existing projects, some over 10 years old, and is organized by Ruby for Good founder Sean Marcia.

hackernews · mooreds · May 24, 15:49 · [Discussion](https://news.ycombinator.com/item?id=48258254)

**Background**: Ruby for Good is a community initiative that brings together Ruby developers to work on projects benefiting social causes. Unlike hackathons that produce new prototypes, this gathering emphasizes ongoing maintenance and support for established open source tools used by nonprofits.

**Discussion**: Community comments are positive, with founder Sean Marcia clarifying it's not a hackathon. Users express interest in sponsors and hope to see follow-up on built projects.

**Tags**: `#Ruby`, `#Open Source`, `#Community`, `#Social Good`

---

<a id="item-14"></a>
## [Hackers evolve from simple prompt injection to personality exploits](https://www.theverge.com/column/935545/hackers-ai-chatbots) ⭐️ 6.0/10

A newsletter reports that hackers are moving beyond basic prompt injection to exploit the 'personalities' of AI chatbots, using more sophisticated attacks that manipulate the chatbot's character and tone to bypass safeguards. This shift highlights the growing sophistication of AI security threats, as attackers target the very features that make chatbots engaging, potentially leading to more effective social engineering and data breaches. Early prompt injection attacks were trivial, but now hackers craft inputs that align with a chatbot's assigned personality to elicit unintended responses, a technique that exploits the model's inability to distinguish between developer instructions and user input.

rss · The Verge · May 24, 12:00

**Background**: Prompt injection is a cybersecurity exploit where malicious inputs cause large language models (LLMs) to behave unintentionally, bypassing safety filters. As chatbots are given distinct personalities to improve user experience, attackers can leverage these personas to craft more convincing and effective attacks.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://xeber.world/en/article/cybercriminals-exploit-ai-chatbot-personalities-in-new-wave-of-jailbreak-attacks-182634">AI Chatbot Jailbreak Attacks: How Hackers Exploit Personalities</a></li>

</ul>
</details>

**Tags**: `#AI security`, `#chatbots`, `#prompt injection`, `#hacking`

---

<a id="item-15"></a>
## [Beluga Whales Pass the Mirror Test](https://arstechnica.com/science/2026/05/belugas-may-pass-the-mirror-test-but-does-the-mirror-test-still-pass/) ⭐️ 6.0/10

Researchers revisited old videotapes and confirmed that beluga whales exhibit behaviors consistent with passing the mirror test for self-recognition, joining a small group of animals like great apes, dolphins, and elephants. This finding adds to the debate about animal self-awareness and the validity of the mirror test itself, which has been criticized for potential biases and limitations in assessing cognition across species. The mirror test, developed by Gordon Gallup Jr. in 1970, involves placing a mark on an animal's body and observing whether it touches the mark while looking in a mirror, indicating self-recognition. Beluga whales are highly intelligent Arctic cetaceans with large brains and advanced communication skills.

rss · Ars Technica · May 24, 11:15

**Background**: The mirror test is a behavioral technique used to determine if an animal can recognize itself in a mirror, which is considered a marker of self-awareness. Only a few species have consistently passed the test, including chimpanzees, dolphins, and elephants. However, the test has been criticized for relying on visual cues, which may not be appropriate for animals that rely more on other senses.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mirror_test">Mirror test - Wikipedia</a></li>
<li><a href="https://www.animalcognition.org/2015/04/15/list-of-animals-that-have-passed-the-mirror-test/">List of Animals That Have Passed the Mirror Test - Animal ...</a></li>
<li><a href="https://arstechnica.com/science/2026/05/belugas-may-pass-the-mirror-test-but-does-the-mirror-test-still-pass/">Whatever the mirror test tells us, beluga whales pass it - Ars Technica</a></li>

</ul>
</details>

**Tags**: `#animal cognition`, `#mirror test`, `#beluga whales`, `#science`

---

<a id="item-16"></a>
## [Godot beats Unity in size, speed, and load times test](https://www.pcgamer.com/gaming-industry/game-development/a-game-developer-compared-godot-and-unity-by-making-the-same-game-in-both-engines-and-hes-found-a-clear-winner/) ⭐️ 6.0/10

Game designer Thomas Grové created the same game in both Godot and Unity, finding Godot to be smaller, faster, and quicker to load. This hands-on comparison provides practical evidence for developers choosing between the two popular engines, potentially influencing indie and small-team decisions. The test involved replicating the same game logic and assets in both engines, with Godot showing advantages in build size, runtime performance, and startup time.

rss · PC Gamer · May 24, 13:00

**Background**: Godot is a free, open-source game engine released under the MIT License, while Unity is a proprietary engine widely used for indie and mobile games. Both support 2D and 3D development across multiple platforms.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Godot_(game_engine)">Godot (game engine)</a></li>
<li><a href="https://en.wikipedia.org/wiki/Unity_(game_engine)">Unity (game engine)</a></li>

</ul>
</details>

**Tags**: `#game development`, `#Godot`, `#Unity`, `#engine comparison`

---