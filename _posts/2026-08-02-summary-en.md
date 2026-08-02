---
layout: default
title: "Horizon Summary: 2026-08-02 (EN)"
date: 2026-08-02
lang: en
---

> From 39 items, 10 important content pieces were selected

---

1. [Kakehashi: Running macOS Binaries on Linux ARM](#item-1) ⭐️ 8.0/10
2. [Fuse: A New Statically Typed Functional Language with GRIN Backend](#item-2) ⭐️ 8.0/10
3. [Karpathy's Pelican Benchmark Sparks Debate on AI Physical World Understanding](#item-3) ⭐️ 7.0/10
4. [F*: A Proof-Oriented Language for Verified Software](#item-4) ⭐️ 7.0/10
5. [eBay Harassment Campaign Leads to $56M Payout and Prison Sentences](#item-5) ⭐️ 7.0/10
6. [How Essential English Vocabulary for Learners Has Shifted Since 1953](#item-6) ⭐️ 7.0/10
7. [Bor 0.8: Open-Source Linux Desktop Policy Management with Real-Time Streaming](#item-7) ⭐️ 7.0/10
8. [RISC OS Open Marks 20 Years of Niche OS Development](#item-8) ⭐️ 6.0/10
9. [Meshdiff: Client-Side STL Comparison Tool in Browser](#item-9) ⭐️ 6.0/10
10. [Royalties Alone Won't Sway Artists on AI Training](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Kakehashi: Running macOS Binaries on Linux ARM](https://github.com/wie-project/kakehashi) ⭐️ 8.0/10

Kakehashi, an experimental userspace translation layer written in Rust, successfully runs macOS CLI binaries on Linux ARM64. Working prototypes include 7-Zip, curl, and Xcode Tools Git, with 7-Zip passing multi-threaded compression tests and curl passing over 200 commands. This project addresses a significant technical challenge and could reduce CI/CD costs by enabling macOS binaries to run on cheaper Linux ARM runners. It also opens possibilities for running macOS applications on Linux, similar to Wine/Proton for Windows. The project is at an early stage; 7-Zip is currently ~5.2x slower than native Linux execution, but the author has an optimization plan. It focuses on CLI binaries and uses a userspace approach without full hardware emulation.

hackernews · vlad_kalinkin · Aug 2, 16:26 · [Discussion](https://news.ycombinator.com/item?id=49145937)

**Background**: macOS binaries use the Mach-O format, which differs from Linux's ELF format, and they rely on macOS system libraries. Running them on Linux typically requires emulation or a compatibility layer. Kakehashi aims to translate system calls and library calls in userspace, similar to Darling, which is a long-term project for macOS compatibility on Linux.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/wie-project/kakehashi">GitHub - wie-project/kakehashi: Userspace macOS translation ...</a></li>
<li><a href="https://news.mcan.sh/item/49145937">Show HN: Kakehashi – Experimental userspace to run macOS ...</a></li>
<li><a href="https://ecosistemastartup.com/kakehashi-reduce-costos-ci-cd-con-binarios-macos-en-linux/">Kakehashi reduce costos CI/CD con binarios macOS en Linux</a></li>

</ul>
</details>

**Discussion**: The community shows strong interest, with users referencing the Darling project and suggesting potential collaboration. Some express cautious optimism, noting the project is early-stage, while others envision applications like running Audio Unit plugins on Linux via a bridge similar to yabridge.

**Tags**: `#macOS`, `#Linux`, `#ARM`, `#binary compatibility`, `#userspace`

---

<a id="item-2"></a>
## [Fuse: A New Statically Typed Functional Language with GRIN Backend](https://fuselang.org/) ⭐️ 8.0/10

Fuse, a statically typed purely functional programming language developed over five years by a solo developer, has been showcased on Hacker News. It compiles via the GRIN whole-program optimizer to LLVM native code, supporting higher-kinded types, ad-hoc polymorphism, ADTs, traits, and pattern matching. Fuse represents a significant contribution to the functional programming ecosystem, offering a modern language that combines Rust-like features with pure functional semantics. Its use of GRIN as a backend could inspire further adoption of whole-program optimization techniques in functional language compilers. The language is implemented in Scala, starting from System F as described in TAPL, and extends it with bidirectional type checking and higher-rank polymorphism. The standard library's string type is not Unicode-aware, a limitation noted by the community.

hackernews · the_unproven · Aug 2, 11:23 · [Discussion](https://news.ycombinator.com/item?id=49143412)

**Background**: GRIN (Graph Reduction Intermediate Notation) is a compiler framework and intermediate representation for lazy and strict functional languages, enabling whole-program optimization. Higher-kinded types allow abstraction over type constructors, while ad-hoc polymorphism enables function overloading based on types. Fuse aims to provide a purely functional language with features familiar from Rust, Haskell, and Scala.

<details><summary>References</summary>
<ul>
<li><a href="https://grin-compiler.github.io/">GRIN Compiler - Overview</a></li>
<li><a href="https://github.com/grin-compiler/grin">GitHub - grin-compiler/grin: GRIN is a compiler back-end for ... A Modern Look at GRIN, an Optimizing Functional Language Back ... A modern look at GRIN, an optimizing functional language back ... A modern look at GRIN, an optimizing functional language back ... [PDF] A Modern Look at GRIN, an Optimizing Functional ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Higher-kinded_type">Higher-kinded type</a></li>
<li><a href="https://en.wikipedia.org/wiki/Ad_hoc_polymorphism">Ad hoc polymorphism</a></li>

</ul>
</details>

**Discussion**: The Hacker News community responded positively, praising the use of GRIN and the language's design. Comments included questions about trait syntax for non-type-dependent members, suggestions for adding performance benchmarks and compiler metrics, and notes on Unicode support in the standard library.

**Tags**: `#programming language`, `#functional programming`, `#type theory`, `#GRIN`, `#LLVM`

---

<a id="item-3"></a>
## [Karpathy's Pelican Benchmark Sparks Debate on AI Physical World Understanding](https://twitter.com/karpathy/status/2083749667410727319) ⭐️ 7.0/10

Andrej Karpathy highlighted 'Pelican' as a new benchmark for evaluating AI models' physical world understanding, specifically through generating SVGs of a pelican on a bicycle. This sparked a debate on Hacker News with 280 comments discussing the validity and implications of such benchmarks. This matters because it shifts focus from image generation quality to deeper physical world understanding, which is crucial for embodied AI and robotics. The debate highlights the need for better evaluation methods as models advance beyond simple generation tasks. The benchmark involves generating SVGs of a pelican on a bicycle, with 18 trajectories and 4 views, as seen in the GitHub repository. Some argue that models like Anthropic's may be specifically trained to generate three.js code, questioning the benchmark's indicative value. A statistical study by Dylan Castillo tested 7 models across 48 animal-vehicle SVG combos and found no significant evidence of 'pelicanmaxxing' (training specifically for the benchmark).

hackernews · delichon · Aug 2, 04:05 · [Discussion](https://news.ycombinator.com/item?id=49140998)

**Background**: Pelican is a benchmark that evaluates AI models' understanding of the physical world by asking them to generate SVGs of a pelican on a bicycle. This task requires spatial reasoning, object interaction, and physical plausibility, going beyond simple image generation. The benchmark is part of a broader trend in AI evaluation to test models' embodied intelligence and world models, as seen in related projects like Pelican-VL and Pelican-Unified.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/jlebensold/pelican-benchmark">GitHub - jlebensold/ pelican - benchmark : Pelican -on-Bicycle SVG...</a></li>
<li><a href="https://explainx.ai/blog/are-ai-labs-pelicanmaxxing-study-july-2026">Are AI Labs Pelicanmaxxing? A Statistical Study | explainx.ai</a></li>
<li><a href="https://simonwillison.net/2026/Jun/9/andrej-karpathy/">A quote from Andrej Karpathy | Simon Willison’s Weblog</a></li>

</ul>
</details>

**Discussion**: The community discussion shows mixed sentiments. Some, like YmiYugy, express concern that the author implies the 'pelican on a bicycle' problem is solved, while noting that AI content has raised expectations for speed but lowered quality. Others, like jmugan, argue that the benchmark's purpose is to expose physical world understanding, not just produce polished outputs. Some commenters share practical experiences, like bredren using LLMs for 3D animations, and others question whether models are specifically trained for three.js code, as HarHarVeryFunny suggests.

**Tags**: `#AI`, `#benchmarking`, `#Karpathy`, `#physical world understanding`, `#model evaluation`

---

<a id="item-4"></a>
## [F*: A Proof-Oriented Language for Verified Software](https://fstar-lang.org/) ⭐️ 7.0/10

F* is a general-purpose proof-oriented programming language that combines dependent types with SMT-based proof automation, and it has gained attention in the community for its ability to incrementally migrate existing C codebases to a verified environment. The language compiles to OCaml by default and supports extraction to F#, C, or Wasm. F* matters because it enables developers to formally verify software properties, such as functional correctness, which is critical for high-assurance systems. Its incremental C migration capability offers a practical path for adopting formal verification in existing codebases, potentially improving software reliability across industries. F* supports both purely functional and effectful programming, and its proof automation relies on SMT solving and tactic-based interactive theorem proving. The language is actively developed on GitHub, with an online book 'Proof-Oriented Programming in F*' and a tutorial available, but community feedback highlights a lack of accessible syntax examples on the homepage.

hackernews · ducktective · Aug 2, 12:31 · [Discussion](https://news.ycombinator.com/item?id=49143925)

**Background**: F* (pronounced F star) is a high-level, multi-paradigm programming language inspired by ML, Caml, and OCaml, designed for program verification. It is a dependently typed language and proof assistant, meaning it can express precise specifications and prove properties about programs. The language is part of a broader trend in formal verification, where tools like Frama-C and Rust-based approaches are also being used to verify and migrate legacy code.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/F*_(programming_language)">F* (programming language) - Wikipedia</a></li>
<li><a href="https://fstar-lang.org/">F*: A Proof-Oriented Programming Language</a></li>
<li><a href="https://github.com/FStarLang/FStar">GitHub - FStarLang/FStar: A Proof-oriented Programming ... F* (programming language) - Wikipedia Proof-oriented Programming in F* - fstar-lang.org F*: A Proof-oriented Programming Language - GitHub Proof-Oriented Programming in F* - mtzguido.github.io Internships on the F proof-oriented programming language</a></li>

</ul>
</details>

**Discussion**: Community comments show mixed reactions: some praise F* for its solid support in incrementally migrating C codebases, while others criticize the lack of accessible syntax examples on the homepage, making it hard for newcomers to quickly understand the language. There is also curiosity about its industry usage and a humorous remark about side effects in responsive stylesheets.

**Tags**: `#formal verification`, `#programming language`, `#proof-oriented`, `#functional programming`, `#software verification`

---

<a id="item-5"></a>
## [eBay Harassment Campaign Leads to $56M Payout and Prison Sentences](https://www.ft.com/content/06ec1b03-d4af-40cf-b12a-4ba5a410f6d2) ⭐️ 7.0/10

eBay has agreed to pay $56 million to David and Ina Steiner, a couple targeted by a harassment campaign orchestrated by eBay's former security executives. Several former employees, including Senior Director Jim Baugh, received prison sentences for their roles in the intimidation scheme. This case highlights the severe consequences of corporate misconduct and the abuse of power by security personnel, reinforcing the importance of accountability at the highest levels. It serves as a warning to companies about the legal and financial risks of retaliating against critics. The harassment campaign included sending disturbing deliveries, surveillance, and threats, targeting the Steiners after they published critical articles about eBay. Seven members of eBay's security team, including former police captains, were involved; Jim Baugh received a 57-month prison sentence, while Brian Gilbert was sentenced to time served and a $20,000 fine.

hackernews · JumpCrisscross · Aug 2, 19:19 · [Discussion](https://news.ycombinator.com/item?id=49147435)

**Background**: eBay is a major online marketplace where users buy and sell goods. The Steiners operated a newsletter that criticized eBay's business practices, prompting the company's security team to retaliate. This case underscores the potential for corporate security departments to overstep ethical and legal boundaries when targeting perceived threats.

**Discussion**: Commenters expressed skepticism that the harassment was limited to the Steiners, questioning whether other critics were targeted. Some noted the involvement of former police captains and called for broader investigations, while others drew parallels to other corporate misconduct cases and discussed eBay's high seller fees.

**Tags**: `#corporate accountability`, `#legal`, `#harassment`, `#eBay`, `#security`

---

<a id="item-6"></a>
## [How Essential English Vocabulary for Learners Has Shifted Since 1953](https://pudding.cool/2026/07/essential-words/) ⭐️ 7.0/10

The Pudding published a data-driven analysis showing how the essential vocabulary taught to English language learners has changed from 1953 to 2023, with a shift from interpersonal words like 'humble' and 'loyalty' to identity- and community-related terms like 'community' and 'identity'. This analysis reveals how cultural and societal shifts over 70 years are reflected in language education, impacting what learners prioritize and how they connect with English-speaking communities. It also sparks discussion about teaching priorities and the role of vocabulary in shaping social identity. The 'Social-Communicative' category remained similar in size, but nearly a quarter of the 1953 words were replaced, and 39% of the 2023 words are new. The shift indicates a move from words for close personal relationships to those for broader belonging and identity.

hackernews · c-oreills · Aug 2, 15:41 · [Discussion](https://news.ycombinator.com/item?id=49145590)

**Background**: The analysis is based on comparing essential word lists for English learners from 1953 and 2023, likely using frequency data from corpora or educational materials. Vocabulary lists are fundamental to language teaching, as they guide curriculum design and learner focus. The observed shift mirrors broader societal trends toward emphasizing identity and community in public discourse.

**Discussion**: Commenters discussed the difficulty of creating such lists, with one noting the lack of a 'right' answer depending on learner goals. Another linked the vocabulary shift to rising inequality and tribalization. Some criticized the article's presentation as a scrolljacker, while others shared personal experiences about language change.

**Tags**: `#linguistics`, `#education`, `#data-analysis`, `#language-learning`, `#societal-change`

---

<a id="item-7"></a>
## [Bor 0.8: Open-Source Linux Desktop Policy Management with Real-Time Streaming](https://getbor.dev/blog/2026-08-02-bor-v080-release/) ⭐️ 7.0/10

Bor, an open-source centralized Linux desktop management system, released version 0.8, adding new policy types for Thunderbird, Microsoft Edge for Business, and FirewallD zones. The system uses a Go agent and server with real-time policy streaming over mTLS/gRPC, eliminating polling. This addresses a significant gap in Linux desktop management, offering a modern alternative to manual configuration or existing tools. Its real-time streaming architecture could improve policy enforcement efficiency and responsiveness for organizations managing Linux workstations. The 0.8 release introduces policy types for Thunderbird, Microsoft Edge for Business, and FirewallD zones, alongside improvements and fixes. The architecture uses mTLS for secure authentication and gRPC for bidirectional streaming, ensuring policies are pushed in real time without polling.

hackernews · eniac111 · Aug 2, 09:06 · [Discussion](https://news.ycombinator.com/item?id=49142569)

**Background**: Linux desktop management often relies on manual configuration or tools like Ansible, which use pull-based models. Bor's push-based approach with mTLS/gRPC streaming offers a novel alternative, potentially reducing configuration drift and improving scalability. The project targets organizations needing centralized control over Firefox, Chrome, KDE, dconf, polkit, and package management.

<details><summary>References</summary>
<ul>
<li><a href="https://firewalld.org/documentation/zone/">Documentation - Zone | firewalld</a></li>
<li><a href="https://en.wikipedia.org/wiki/Dconf">dconf - Wikipedia</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-08-grpc-mtls-mutual-tls/view">How to Add mTLS (Mutual TLS) to gRPC Services</a></li>

</ul>
</details>

**Discussion**: Community members expressed strong interest, with one user noting it closely matches their needs for managing non-profit laptops. Questions focused on architecture choices (mTLS vs SSH), comparisons to existing tools, custom script execution, user mapping, and handling of configuration drift without polling.

**Tags**: `#Linux`, `#desktop management`, `#policy`, `#open-source`, `#gRPC`

---

<a id="item-8"></a>
## [RISC OS Open Marks 20 Years of Niche OS Development](https://www.riscosopen.org/news/articles/2026/06/20/twenty-years-of-risc-os-open) ⭐️ 6.0/10

RISC OS Open (ROOL) celebrated its 20th anniversary on June 20, 2026, marking two decades of managing the open-source release and continued development of RISC OS. The milestone highlights the project's persistence in maintaining a niche operating system originally created by Acorn Computers. This anniversary underscores the enduring viability of a community-driven, open-source operating system in a landscape dominated by mainstream platforms. It matters to retro-computing enthusiasts and open-source advocates, demonstrating how a dedicated community can sustain a legacy system long after its original vendor ceased operations. RISC OS Open was founded by former Pace staff, who acquired RISC OS after Acorn's demise, and it oversees the publication of RISC OS source code. The open-sourcing of RISC OS 5.0 occurred in 2018, and the OS is known for its fast boot times on hardware like the Raspberry Pi.

hackernews · AlexeyBrin · Aug 2, 12:36 · [Discussion](https://news.ycombinator.com/item?id=49143967)

**Background**: RISC OS is a modular operating system originally developed by Acorn Computers for ARM-based machines like the Archimedes and Risc PC. Despite Acorn's closure, the OS has survived through community efforts, with RISC OS Open managing its open-source development. The system is lightweight and efficient, designed for RISC architectures, and continues to receive updates from a small but active community.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS">RISC OS - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/RISC_OS_Open">RISC OS Open - Wikipedia</a></li>
<li><a href="https://www.riscosopen.org/content/">RISC OS Open: Welcome</a></li>

</ul>
</details>

**Discussion**: Commenters shared personal anecdotes and technical insights, with one recalling developing software for RISC OS and another noting the surprising persistence of the project. Some highlighted the OS's fast boot on Raspberry Pi, while others pointed to notable applications like Sibelius that originated on RISC OS.

**Tags**: `#RISC OS`, `#Open Source`, `#Retro Computing`, `#Operating Systems`

---

<a id="item-9"></a>
## [Meshdiff: Client-Side STL Comparison Tool in Browser](https://meshdiff.com/) ⭐️ 6.0/10

Meshdiff is a new browser-based tool that allows users to visually compare two STL file versions entirely on the client side, without uploading files to a server. It provides three viewports for side-by-side and overlay comparisons, and the community has suggested features like synchronized view rotation and GitHub integration. This tool addresses a practical need in 3D printing and CAD workflows, where comparing file versions is common. Its client-side approach enhances privacy and speed, and the positive community response suggests it could become a useful utility for designers and engineers. Meshdiff runs entirely in the browser, likely using WebGL or Three.js for rendering, and supports STL files, which are common in 3D printing. The tool currently offers three viewports, and community members have requested synchronized camera controls and integration with GitHub for automated comparisons in pull requests.

hackernews · projscope · Aug 2, 11:34 · [Discussion](https://news.ycombinator.com/item?id=49143479)

**Background**: STL is a file format used for 3D printing and CAD, representing surface geometry as a triangulated mesh without color or texture. Client-side processing means files are handled locally in the browser, improving privacy and reducing server load. Tools like Meshdiff leverage modern web technologies such as WebGL and WebAssembly to enable complex 3D visualization in the browser.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/STL_(file_format)">STL (file format)</a></li>
<li><a href="https://www.adobe.com/creativecloud/file-types/image/vector/stl-file.html">STL files explained | Learn about the STL file format | Adobe</a></li>

</ul>
</details>

**Discussion**: The community response is positive, with users praising the tool's utility and client-side emphasis. Suggestions include synchronized viewport rotation, locked views, and embedding as a GitHub PR trigger for 3D files. One user initially confused STL with the C++ Standard Template Library, but others clarified the context.

**Tags**: `#3D`, `#STL`, `#browser-tool`, `#visualization`, `#CAD`

---

<a id="item-10"></a>
## [Royalties Alone Won't Sway Artists on AI Training](https://www.theverge.com/ai-artificial-intelligence/974018/pippa-seedance-artist-royalties) ⭐️ 6.0/10

The Verge article examines whether paying artists royalties is sufficient to address their objections to generative AI models training on their work without permission. It highlights that despite compensation proposals, many artists remain unconvinced, viewing the practice as fundamentally exploitative. This debate is central to the future of generative AI and copyright law, affecting artists, AI companies, and policymakers. The outcome could set precedents for how AI training data is sourced and compensated, influencing the ethical and legal landscape of the industry. The article references ongoing legal battles and artist protests, such as the October 2024 statement signed by over 10,500 creatives condemning unauthorized AI training. It also notes that some proposals, like India's mandatory royalty system, are emerging but face practical challenges.

rss · The Verge · Aug 2, 13:00

**Background**: Generative AI models like GPT-4 and Stable Diffusion are trained on vast datasets scraped from the internet, often including copyrighted works. Artists argue this constitutes theft, while AI companies claim fair use or text-and-data-mining exceptions. Legal frameworks vary by jurisdiction, with the US relying on fair use and Europe on TDM exceptions.

<details><summary>References</summary>
<ul>
<li><a href="https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-3-Generative-AI-Training-Report-Pre-Publication-Version.pdf">Copyright and Artificial Intelligence, Part 3: Generative AI ...</a></li>
<li><a href="https://arxiv.org/pdf/2502.15858">Generative AI Training and Copyright Law</a></li>
<li><a href="https://www.technologyreview.com/2023/10/23/1082189/data-poisoning-artists-fight-generative-ai/">This new data poisoning tool lets artists fight back against ... Artists Fight Back Against Unethical AI Training The Ethics of Using Artists' Work Without Consent to Train AI ... AI Training and Copyright: The Fight for Creative Consent</a></li>

</ul>
</details>

**Discussion**: No community comments were provided for this news item.

**Tags**: `#AI ethics`, `#generative AI`, `#copyright`, `#artists`, `#compensation`

---