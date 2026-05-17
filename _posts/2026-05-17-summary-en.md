---
layout: default
title: "Horizon Summary: 2026-05-17 (EN)"
date: 2026-05-17
lang: en
---

> From 41 items, 11 important content pieces were selected

---

1. [Native UI Fails at Text: WebKit Wins for Markdown](#item-1) ⭐️ 8.0/10
2. [CAR T Cell Therapy Shows Promise for Autoimmune Diseases](#item-2) ⭐️ 8.0/10
3. [Turning $80 Android Tablet into Debian Workstation](#item-3) ⭐️ 7.0/10
4. [AI Won't Speed Up Software Processes, Says Blog](#item-4) ⭐️ 7.0/10
5. [AI Is a Technology, Not a Product](#item-5) ⭐️ 7.0/10
6. [Apple Silicon Local LLM Cost vs OpenRouter API](#item-6) ⭐️ 7.0/10
7. [Mozilla Defends VPNs Against UK Age-Gating Proposals](#item-7) ⭐️ 7.0/10
8. [Tesla Solar Roof on Life Support as Company Pivots to Panels](#item-8) ⭐️ 7.0/10
9. [GitHub List of CUDA Books Sparks Community Debate](#item-9) ⭐️ 6.0/10
10. [Hosting a Website on an 8-bit Microcontroller](#item-10) ⭐️ 6.0/10
11. [Students Boo Eric Schmidt's AI Cheerleading at Commencement](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Native UI Fails at Text: WebKit Wins for Markdown](https://justsitandgrin.im/posts/native-all-the-way-until-you-need-text/) ⭐️ 8.0/10

A developer building a text editor found that native frameworks like SwiftUI and TextKit cannot efficiently render complex Markdown with text selection, so they switched to WebKit for the Markdown view. This highlights a growing trend where web rendering engines outperform native UI for text-heavy tasks, challenging the assumption that native is always faster. The developer reported that SwiftUI's AttributedString lacks proper text selection for Markdown, and TextKit 2 struggles with performance on large files, while WebKit handles both smoothly.

hackernews · dive · May 17, 11:49 · [Discussion](https://news.ycombinator.com/item?id=48168058)

**Background**: Native UI frameworks like SwiftUI and TextKit are designed for standard app interfaces, but complex text rendering—especially Markdown with inline styles and selection—remains challenging. WebKit, though a web engine, is a native macOS/iOS framework that excels at text layout and selection.

<details><summary>References</summary>
<ul>
<li><a href="https://developer.apple.com/documentation/webkit">WebKit | Apple Developer Documentation</a></li>
<li><a href="https://developer.apple.com/documentation/swiftui/text">Text | Apple Developer Documentation</a></li>
<li><a href="https://fatbobman.com/en/posts/a-deep-dive-into-swiftui-rich-text-layout/">A Deep Dive into SwiftUI Rich Text Layout: Beyond AttributedString ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the trade-offs: some argued WebKit is a native framework on macOS, making it a logical choice for Markdown; others pointed to existing SwiftUI Markdown libraries that work well. One developer shared their success with TextKit 2, achieving sub-8ms keystroke restyling.

**Tags**: `#text rendering`, `#native vs web`, `#SwiftUI`, `#WebKit`, `#performance`

---

<a id="item-2"></a>
## [CAR T Cell Therapy Shows Promise for Autoimmune Diseases](https://arstechnica.com/science/2026/05/a-revolutionary-cancer-treatment-could-transform-autoimmune-disease/) ⭐️ 8.0/10

Researchers are testing CAR T cell therapy, originally developed for cancer, as a way to reset the immune system and treat autoimmune diseases. This could represent a paradigm shift in treating autoimmune diseases, offering a potential long-term remission or cure for millions of patients who currently rely on lifelong immunosuppression. CAR T cells are engineered to target and destroy specific immune cells that drive autoimmunity, effectively resetting the immune system. Early case reports show patients with multiple autoimmune diseases entering remission.

rss · Ars Technica · May 17, 11:00

**Background**: CAR T cell therapy involves genetically modifying a patient's T cells to express chimeric antigen receptors (CARs) that recognize specific antigens. Originally approved for blood cancers, the therapy has shown remarkable success in eliminating malignant B cells. Researchers now believe the same approach can be used to deplete autoreactive B cells that cause autoimmune diseases, allowing the immune system to regenerate a healthy balance.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CAR_T_cell_therapy">CAR T cell therapy</a></li>
<li><a href="https://www.sciencealert.com/woman-with-3-autoimmune-diseases-enters-remission-after-immune-reset&">Woman With 3 Autoimmune Diseases Enters... : ScienceAlert</a></li>

</ul>
</details>

**Tags**: `#CAR T cell therapy`, `#autoimmune disease`, `#immunotherapy`, `#medical research`

---

<a id="item-3"></a>
## [Turning $80 Android Tablet into Debian Workstation](https://github.com/tech4bot/rk3562deb) ⭐️ 7.0/10

A guide on GitHub details how to convert an $80 RK3562 Android tablet into a functional Debian Linux workstation, with most devices fully working. This demonstrates the potential to repurpose cheap Android hardware for Linux, expanding access to desktop-class computing and reducing e-waste. The RK3562 is an octa-core ARM processor with PowerVR graphics and 4K video support; the tablet has 4 GB RAM, which may limit multitasking but is adequate for lightweight development.

hackernews · tech4bot · May 17, 13:16 · [Discussion](https://news.ycombinator.com/item?id=48168668)

**Background**: Android is built on the Linux kernel, but running a full Linux distribution like Debian on Android hardware typically requires custom bootloaders or chroot environments. This guide likely uses a method to boot Debian directly, leveraging the RK3562's support for mainline Linux.

<details><summary>References</summary>
<ul>
<li><a href="https://sesamedisk.com/rk3562-android-tablet-into-debian-workstation-2026/">How I Turned $80 RK3562 Android Tablet into Full Debian Linux ...</a></li>
<li><a href="https://rockchips.net/product/rk3562/">RK3562 - Rockchips.net</a></li>
<li><a href="https://www.cpubenchmark.net/cpu.php?id=5674&cpu=Rockchip+RK3562">Rockchip RK3562 Benchmark</a></li>

</ul>
</details>

**Discussion**: Commenters discussed the usability of 4 GB RAM for web browsing and development, with some suggesting lightweight desktop environments or terminal-based setups. Others noted that AI-assisted reverse engineering could simplify porting Linux to new devices, and expressed concern that such breakthroughs might drive up prices of cheap tablets.

**Tags**: `#Linux`, `#embedded systems`, `#hardware hacking`, `#Debian`, `#single-board computer`

---

<a id="item-4"></a>
## [AI Won't Speed Up Software Processes, Says Blog](https://frederickvanbrabant.com/blog/2026-05-15-i-dont-think-ai-will-make-your-processes-go-faster/) ⭐️ 7.0/10

A blog post argues that AI will not accelerate software development processes because the main bottleneck is unclear requirements, which AI cannot fix without precise specifications. This contrarian perspective challenges the prevailing optimism about AI's productivity gains in software engineering, highlighting that vague requirements remain a fundamental human-centric bottleneck. The post emphasizes that software engineering inherently involves clarifying ambiguous feature requests, and AI cannot replace this human interpretation step. It suggests that AI's impact is limited to later stages like coding and deployment, not the initial requirements gathering.

hackernews · TheEdonian · May 17, 12:13 · [Discussion](https://news.ycombinator.com/item?id=48168221)

**Background**: In software development, requirements gathering is often the most time-consuming and error-prone phase. AI tools like large language models have been widely adopted for code generation, but they still rely on clear, detailed input to produce useful output. The blog argues that without solving the requirements problem, AI cannot dramatically speed up the overall process.

**Discussion**: Commenters largely agree with the premise, sharing anecdotes of vague requirements like 'get data and give it to the user.' Some counter that AI can help with ideation, documentation, and deployment, not just coding. Others express frustration that this point has been made repeatedly without convincing leadership.

**Tags**: `#AI`, `#software engineering`, `#requirements`, `#productivity`

---

<a id="item-5"></a>
## [AI Is a Technology, Not a Product](https://daringfireball.net/2026/05/ai_is_technology_not_a_product) ⭐️ 7.0/10

John Gruber argues that AI should be treated as a foundational technology integrated into user experiences, like Apple's Siri, rather than marketed as a standalone product. This perspective challenges the current AI industry trend of packaging AI as separate products, and suggests that the most successful AI implementations will be invisible, embedded features that enhance existing tools. The article draws a parallel to the 'Dropbox is a feature, not a product' argument, noting that AI companies are trying to build ecosystems to avoid becoming disposable. Gruber specifically points to Apple's approach as an example of treating AI as infrastructure.

hackernews · ch_sm · May 17, 13:11 · [Discussion](https://news.ycombinator.com/item?id=48168626)

**Background**: AI has rapidly evolved from research to commercial products, with companies like OpenAI and Anthropic offering standalone AI services. However, historically, transformative technologies like the internet or GPS became most impactful when integrated into other products rather than sold separately.

**Discussion**: Commenters largely agree, with one noting that Apple's ideal AI implementation would simply make Siri work reliably. Another draws a parallel to Steve Jobs' philosophy of working backwards from customer experience. A dissenting comment suggests AI can be a product for companies like Anthropic selling to enterprises.

**Tags**: `#AI`, `#product strategy`, `#Apple`, `#technology trends`, `#user experience`

---

<a id="item-6"></a>
## [Apple Silicon Local LLM Cost vs OpenRouter API](https://www.williamangel.net/blog/2026/05/17/offline-llm-energy-use.html) ⭐️ 7.0/10

A blog post argues that running LLMs locally on Apple Silicon is more expensive than using cloud APIs like OpenRouter, based on a cost analysis that includes hardware amortization and electricity. This analysis challenges the common assumption that local inference is cheaper, but the community debate reveals flaws in the methodology, highlighting the need for nuanced total cost of ownership comparisons. The author rounds up electricity costs by 10% and uses the high end of a power range that is double the low end, while also assuming a newly purchased Mac runs at full capacity 24/7 for inference only.

hackernews · datadrivenangel · May 17, 12:09 · [Discussion](https://news.ycombinator.com/item?id=48168198)

**Background**: Running large language models locally requires powerful hardware like Apple Silicon Macs, which have unified memory suitable for large models. Cloud APIs like OpenRouter charge per token, often subsidized by venture capital, making direct cost comparisons tricky.

<details><summary>References</summary>
<ul>
<li><a href="https://openrouter.ai/pricing">Pricing - OpenRouter</a></li>
<li><a href="https://mljourney.com/full-local-llm-setup-guide-cpu-vs-gpu-vs-apple-silicon/">Full Local LLM Setup Guide: CPU vs GPU vs Apple Silicon</a></li>
<li><a href="https://2acrestudios.com/guides/local-llm-hardware/">Local LLM Hardware Guide 2026: 2 Acre Studios</a></li>

</ul>
</details>

**Discussion**: Commenters criticize the analysis for rounding up costs and ignoring that a laptop has dual-use value beyond inference. Some note that frontier AI companies sell at a loss, so local inference may still be cheaper if hardware is already owned.

**Tags**: `#LLM`, `#Apple Silicon`, `#cost analysis`, `#local inference`, `#API pricing`

---

<a id="item-7"></a>
## [Mozilla Defends VPNs Against UK Age-Gating Proposals](https://blog.mozilla.org/netpolicy/2026/05/15/mozilla-to-uk-regulators-vpns-are-essential-privacy-and-security-tools-and-should-not-be-undermined/) ⭐️ 7.0/10

Mozilla submitted a response to a UK government consultation arguing that VPNs are essential privacy and security tools and should not be age-gated or undermined by regulation. If adopted, the UK's proposal could set a precedent for restricting VPN access, threatening online privacy and security for all users, not just minors. The UK government's consultation, titled 'Growing up in the online world', includes a question about age-gating VPNs, and the House of Lords has already passed amendments banning VPNs for under-18s.

hackernews · WithinReason · May 17, 06:17 · [Discussion](https://news.ycombinator.com/item?id=48166459)

**Background**: VPNs (Virtual Private Networks) encrypt internet traffic and hide users' IP addresses, protecting privacy and security online. The UK government is considering age-gating VPNs to prevent children from bypassing online safety measures, but critics argue this would undermine fundamental privacy rights and break the internet.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techradar.com/vpn/vpn-privacy-security/uk-government-says-it-may-age-restrict-or-limit-childrens-vpn-use-following-new-consultation">UK government may 'age restrict or limit children’s VPN use ...</a></li>
<li><a href="https://www.theregister.com/security/2026/05/06/uk-age-gating-plans-risk-breaking-the-internet-privacy-groups-warn/5230732">UK age-gating plans risk breaking the internet, privacy ...</a></li>
<li><a href="https://stateofsurveillance.org/articles/government/uk-lords-vpn-ban-surveillance-software-2026/">UK Lords Vote to Ban VPNs for Minors, Mandate Device ...</a></li>

</ul>
</details>

**Discussion**: Commenters generally support Mozilla's stance, with some noting that the Australian government actually recommends VPN usage. Others question how platforms can be held accountable without age verification, while a user points out the proposal is still just a consultation and encourages people to respond.

**Tags**: `#privacy`, `#VPN`, `#regulation`, `#Mozilla`, `#UK`

---

<a id="item-8"></a>
## [Tesla Solar Roof on Life Support as Company Pivots to Panels](https://electrek.co/2026/05/14/tesla-solar-roof-promise-vs-reality-pivot-panels/) ⭐️ 7.0/10

Tesla's Solar Roof is effectively on life support, with the company pivoting back to traditional solar panels due to high costs and poor economics. This shift signals a major retreat from Tesla's ambitious integrated solar product, impacting the broader solar industry's perception of building-integrated photovoltaics. An average Tesla Solar Roof costs about $106,000 before incentives, compared to $60,000 for a traditional roof plus solar panels, with a payback period of 15-25 years versus 7-12 years.

hackernews · celsoazevedo · May 17, 04:09 · [Discussion](https://news.ycombinator.com/item?id=48165980)

**Background**: Tesla's Solar Roof was introduced as a premium product that integrates solar cells into roof tiles, aiming to replace traditional roofing while generating electricity. However, high installation costs and complex logistics have hindered adoption, leading to the pivot back to conventional solar panels.

**Discussion**: Commenters expressed skepticism, with some noting the product's high cost and long payback period, while others appreciated its aesthetics but acknowledged the poor economics. One commenter suggested the Solar Roof was introduced to pump the stock.

**Tags**: `#Tesla`, `#Solar Energy`, `#Renewable Energy`, `#Business Strategy`, `#Economics`

---

<a id="item-9"></a>
## [GitHub List of CUDA Books Sparks Community Debate](https://github.com/alternbits/awesome-cuda-books) ⭐️ 6.0/10

A GitHub repository titled 'awesome-cuda-books' curates a list of books for learning CUDA programming, and the community has actively discussed the quality and relevance of these resources. This curated list helps learners navigate the vast landscape of CUDA resources, and the community feedback provides valuable insights into which books are most effective for mastering GPU parallel computing. The repository includes books ranging from introductory to advanced topics, and community comments highlight specific titles like 'CUDA Programming: A Developer's Guide' as a strong intro, while criticizing 'Massively Parallel Processors' for errors.

hackernews · dariubs · May 17, 12:52 · [Discussion](https://news.ycombinator.com/item?id=48168485)

**Background**: CUDA is a parallel computing platform and programming model developed by NVIDIA that allows developers to use GPUs for general-purpose processing. Learning CUDA typically involves understanding GPU architecture, thread hierarchy, and memory management, which these books aim to teach.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.nvidia.com/cuda/cuda-programming-guide/">CUDA Programming Guide - NVIDIA Documentation Hub</a></li>
<li><a href="https://www.digitalocean.com/community/tutorials/parallel-computing-gpu-vs-cpu-with-cuda">Understanding Parallel Computing: GPUs vs CPUs Explained ...</a></li>
<li><a href="https://www.atlantic.net/gpu-server-hosting/gpu-parallel-computing-techniques-challenges-and-best-practices/">GPU Parallel Computing: Techniques, Challenges, and Best ...</a></li>

</ul>
</details>

**Discussion**: Commenters debated the best CUDA books, with some recommending 'CUDA Programming: A Developer's Guide' and others suggesting newer tools like Warp for Python users. A few noted that NVIDIA insiders now advise against writing custom CUDA kernels unless it's a full-time role.

**Tags**: `#CUDA`, `#GPU programming`, `#books`, `#parallel computing`

---

<a id="item-10"></a>
## [Hosting a Website on an 8-bit Microcontroller](https://maurycyz.com/projects/mcusite/) ⭐️ 6.0/10

Maurycy's blog demonstrates hosting a website on an AVR64DD32 8-bit microcontroller, using a VPS proxy to serve the site under a subpath. This project showcases the feasibility of running a web server on extremely resource-constrained hardware, highlighting the versatility of modern 8-bit microcontrollers for IoT and embedded applications. The microcontroller does not have its own IP address; instead, a VPS proxies requests under /mcu to the MCU via a local address block. The setup uses a simple TCP/IP stack and serves static HTML.

hackernews · zdw · May 17, 01:25 · [Discussion](https://news.ycombinator.com/item?id=48165295)

**Background**: 8-bit microcontrollers like the AVR series are low-power, low-cost chips commonly used in embedded systems. Hosting a web server on such devices typically requires external networking hardware or a full TCP/IP stack, but this project achieves it with minimal resources.

<details><summary>References</summary>
<ul>
<li><a href="https://maurycyz.com/projects/mcusite/">Hosting a website on an 8-bit microcontroller. (Maurycy's blog)</a></li>
<li><a href="https://www.edn.com/compact-web-server-runs-on-8-bit-microcontroller/">Compact Web server runs on 8 - bit microcontroller - EDN</a></li>
<li><a href="https://cybermediacreations.com/hosting-a-website-on-an-8-bit-microcontroller/">Hosting a website on an 8 - bit microcontroller - Cyber Media Creations</a></li>

</ul>
</details>

**Discussion**: Commenters noted historical precedents, such as the 'smallest web server' contest from 25 years ago using an ACE1101 microcontroller. Some expressed concern about Microchip's new PIC32 CM making AVR DD series obsolete, while others reminisced about the nostalgic experience of seeing HTML stream in real-time.

**Tags**: `#embedded systems`, `#microcontrollers`, `#web server`, `#retro computing`

---

<a id="item-11"></a>
## [Students Boo Eric Schmidt's AI Cheerleading at Commencement](https://www.theverge.com/ai-artificial-intelligence/932203/university-of-arizona-students-boo-eric-schmidt-ai-commencement) ⭐️ 6.0/10

During his commencement speech at the University of Arizona, former Google CEO Eric Schmidt was repeatedly booed by students when he promoted AI. This incident highlights growing public anxiety about AI's impact on jobs, especially among graduates entering a tough labor market. The booing occurred specifically when Schmidt's speech turned to AI topics, reflecting strong negative sentiment among the student audience.

rss · The Verge · May 17, 17:22

**Background**: Eric Schmidt is a prominent tech figure who led Google for many years. AI has become a contentious issue due to fears of job displacement and ethical concerns.

**Tags**: `#AI`, `#public sentiment`, `#education`, `#job market`

---