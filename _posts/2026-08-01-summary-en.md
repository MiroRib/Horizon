---
layout: default
title: "Horizon Summary: 2026-08-01 (EN)"
date: 2026-08-01
lang: en
---

> From 54 items, 11 important content pieces were selected

---

1. [Ripgrep musl binaries segfault in large searches due to mallocng allocator bug](#item-1) ⭐️ 8.0/10
2. [Canada Signs UN Cybercrime Convention, Raising Surveillance Concerns](#item-2) ⭐️ 8.0/10
3. [Google's Role in the Decline of RSS Feeds](#item-3) ⭐️ 7.0/10
4. [Comprehensive 800-Page Book on 64-bit Assembly Sparks Debate](#item-4) ⭐️ 7.0/10
5. [NetBSD 11.0 Released with MICROVM Kernel and Firewall Enhancements](#item-5) ⭐️ 7.0/10
6. [Microsoft's Flint: A New Visualization Language for AI Agents](#item-6) ⭐️ 7.0/10
7. [Silicon Valley Founder's Financial Ruin: A Cautionary Tale](#item-7) ⭐️ 7.0/10
8. [Cursor Accidentally Removes Cost Data from Usage Page and CSV Export](#item-8) ⭐️ 6.0/10
9. [Reddit CEO Questions Google AI Overviews Value as Stock Falls](#item-9) ⭐️ 6.0/10
10. [Defcon Badge Doubles as Open-Source Security Key](#item-10) ⭐️ 6.0/10
11. [How Fruit Flies Navigate Turbulent Odor Plumes Using Memory and Direction](#item-11) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Ripgrep musl binaries segfault in large searches due to mallocng allocator bug](https://github.com/BurntSushi/ripgrep/issues/3494) ⭐️ 8.0/10

Ripgrep's musl binaries occasionally segfault during very-large searches, as reported in issue #3494. The root cause is traced to musl's mallocng allocator, which has a bug that triggers under high memory contention. This bug affects users who rely on ripgrep's static musl builds for performance-critical large-scale searches, potentially causing crashes and data loss. It highlights the importance of allocator choice in multithreaded applications and sparks discussion on kernel-level memory management issues. The issue involves ripgrep 15.2.0 with x86_64-unknown-linux-musl, static linking, and jemalloc as Rust's global allocator, while musl 1.2.5 services C-allocator calls (notably calloc from opendir). The analysis suggests a suspected memory-management race in Linux 7.0, with a detailed write-up available in the ripgrep-3494-analysis repository.

hackernews · throwaway2037 · Aug 1, 12:34 · [Discussion](https://news.ycombinator.com/item?id=49133889)

**Background**: musl is a lightweight libc implementation commonly used for static binaries, and its mallocng allocator (introduced in v1.2.1) focuses on hardening against memory errors. However, it has known performance issues under multithreaded contention. Ripgrep is a popular fast search tool that offers musl builds for portability, but this bug reveals a trade-off between performance and stability.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/dfoxfranke/ripgrep-3494-analysis">dfoxfranke/ ripgrep -3494-analysis: Analysis of one crazy segfault in...</a></li>
<li><a href="https://elsolitario.org/en/2026/08/01/ripgrep-musl-segfault-mallocng-heap-en/">Musl Segfault : mallocng Bug Hits Ripgrep 15.2</a></li>
<li><a href="https://sourcefeed.dev/a/that-ripgrep-segfault-is-probably-a-kernel-bug">That ripgrep Segfault Is Probably a Kernel Bug — SourceFeed</a></li>

</ul>
</details>

**Discussion**: The community discussion includes expert commentary on allocator performance, with one user noting that mallocng is bad at handling multithreaded contention and suggesting replacing it. Another user points out that the kernel patch may be the real culprit, linking to a detailed analysis. There is also a comment about HPC workflows being unsuitable for ripgrep on cluster filesystems due to high small I/O.

**Tags**: `#ripgrep`, `#musl`, `#allocator`, `#bug`, `#performance`

---

<a id="item-2"></a>
## [Canada Signs UN Cybercrime Convention, Raising Surveillance Concerns](https://www.michaelgeist.ca/2026/07/a-surveillance-treaty-in-disguise-the-trouble-with-canadas-quiet-decision-to-sign-the-un-cybercrime-convention/) ⭐️ 8.0/10

Canada quietly signed the United Nations Convention against Cybercrime, also known as the Hanoi Convention, in 2026, despite previously opposing the treaty. The signing has drawn criticism from privacy advocates who view it as a surveillance treaty in disguise. This move could expand government surveillance powers and undermine privacy and civil liberties in Canada and globally. It also signals a shift in Canada's stance on international cybercrime cooperation, potentially setting a precedent for other nations. The treaty, proposed by Russia in 2017 and adopted by the UN General Assembly in December 2024, aims to strengthen international cooperation in combating cybercrime and sharing electronic evidence. As of May 2026, 76 participants have signed, but ratification is required for full effect; Canada has not yet ratified it.

hackernews · iamnothere · Aug 1, 14:19 · [Discussion](https://news.ycombinator.com/item?id=49134694)

**Background**: The UN Cybercrime Convention is the first comprehensive global treaty on cybercrime, providing measures for prevention and combat, as well as international cooperation. Human rights organizations have resisted it due to concerns about surveillance and potential abuse. Canada initially opposed the treaty, highlighting threats to human rights during negotiations.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/United_Nations_Convention_against_Cybercrime">United Nations Convention against Cybercrime - Wikipedia</a></li>
<li><a href="https://www.unodc.org/unodc/en/cybercrime/convention/home.html">United Nations Convention against Cybercrime</a></li>
<li><a href="https://ccla.org/privacy/ccla-distrubed-as-canada-signs-global-surveillance-treaty/">CCLA distrubed as Canada signs global surveillance treaty - CCLA</a></li>

</ul>
</details>

**Discussion**: Commenters expressed mixed views: some praised Michael Geist's long-standing work on privacy issues, while others noted that signing is common for Canada and that ratification is the critical step. One commenter highlighted the performative nature of international politics, questioning the seriousness of such commitments.

**Tags**: `#surveillance`, `#cybercrime`, `#privacy`, `#Canada`, `#UN treaty`

---

<a id="item-3"></a>
## [Google's Role in the Decline of RSS Feeds](https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds) ⭐️ 7.0/10

An article published on Open RSS argues that Google's decision to shut down Google Reader in 2013 significantly contributed to the decline of RSS adoption. The piece highlights how this action, along with other tech companies' moves, eroded the open web ecosystem. This matters because RSS is a fundamental open standard that empowers users to control their content consumption, and its decline has led to a more centralized, ad-driven web dominated by walled gardens. Understanding Google's role helps contextualize the broader loss of open web principles and informs discussions about preserving digital openness. The article specifically criticizes Google's excuse of 'declining usage' for killing Reader, noting it coincided with the promotion of Google+, which had low adoption. It also references Mozilla's removal of RSS features in Firefox 64, such as Live Bookmarks, as another contributing factor.

hackernews · pudgywalsh · Aug 1, 18:07 · [Discussion](https://news.ycombinator.com/item?id=49136821)

**Background**: RSS (Really Simple Syndication) is a web feed format that allows users to subscribe to content updates from websites. In the early 2000s, RSS was widely used, and Google Reader became the most popular RSS reader, but its shutdown in 2013 left a void that many argue accelerated RSS's decline. Social media platforms like Twitter and Facebook, which offered their own feeds, also reduced or removed RSS support, further marginalizing the technology.

<details><summary>References</summary>
<ul>
<li><a href="https://openrss.org/blog/how-google-helped-destroy-adoption-of-rss-feeds">How Google helped destroy adoption of RSS feeds - Open RSS</a></li>
<li><a href="https://news.ycombinator.com/item?id=16722260">> When did RSS go out of style anyway? It went away when Google killed Reader. R... | Hacker News</a></li>
<li><a href="https://en.wikipedia.org/wiki/RSS">RSS - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters expressed nostalgia for the early internet and frustration with Google's decision, with one noting that Google's excuse was 'obviously fake' as they were pushing Google+ at the time. Another pointed out Mozilla's removal of RSS features, while others lamented that Google Reader's shutdown felt like 'the beginning of the end' of the internet as they knew it.

**Tags**: `#RSS`, `#Google`, `#Web History`, `#Open Standards`, `#Internet Culture`

---

<a id="item-4"></a>
## [Comprehensive 800-Page Book on 64-bit Assembly Sparks Debate](https://nostarch.com/art-64-bit-assembly-v2) ⭐️ 7.0/10

No Starch Press has released 'The Art of 64-bit Assembly', an 800-page book focusing on x86-64 assembly programming using MASM on Windows. The book aims to provide a thorough resource for low-level programmers. This book is significant as it offers a comprehensive, modern treatment of assembly language, a topic often overlooked in contemporary development. It serves as a valuable resource for those interested in low-level programming, performance optimization, and understanding computer architecture. The book is nearly 800 pages long and specifically targets x86-64 architecture using the Microsoft Macro Assembler (MASM) on Windows. It includes coverage of macro language features such as looping, arithmetic, and string processing, which are advantages of MASM over other assemblers like GAS.

hackernews · 0x54MUR41 · Aug 1, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49134599)

**Background**: Assembly language is a low-level programming language closely tied to a processor's machine code, allowing precise control over hardware. It is commonly used in real-time embedded systems, operating-system kernels, and device drivers where performance and efficiency are critical. The x86-64 architecture is widely used in modern computers, and MASM is a mature assembler that has been available since 1981, with a 64-bit version (ml64.exe) included in Visual Studio.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/X86_assembly_language">x86 assembly language - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Microsoft_Macro_Assembler">Microsoft Macro Assembler - Wikipedia</a></li>
<li><a href="https://learn.microsoft.com/en-us/cpp/assembler/masm/masm-for-x64-ml64-exe?view=msvc-170">MASM for x64 (ml64.exe) | Microsoft Learn</a></li>

</ul>
</details>

**Discussion**: The Hacker News discussion is active with 76 comments. Some users express appreciation for the book's depth and the continued relevance of assembly, while others criticize the marketing copy and the use of AI-generated text. There are also comments about the choice of MASM and Windows, with some asking for a Linux equivalent.

**Tags**: `#assembly`, `#low-level programming`, `#book`, `#x86-64`, `#MASM`

---

<a id="item-5"></a>
## [NetBSD 11.0 Released with MICROVM Kernel and Firewall Enhancements](https://blog.netbsd.org/tnf/entry/netbsd_11_0_released) ⭐️ 7.0/10

NetBSD 11.0 has been officially released, introducing a new MICROVM kernel for x86 that can boot in about 10 milliseconds, along with improvements to the npf(7) firewall including layer 2 and user/group filtering. This release demonstrates NetBSD's continued evolution, particularly in virtualization and security, which could attract users interested in lightweight, fast-booting systems. The MICROVM kernel opens possibilities for microservices and edge computing, while firewall improvements enhance security for existing users. The MICROVM kernel leverages PVH boot and VirtIO MMIO, and is available for both i386 and amd64. The npf firewall now supports layer 2 filtering and filtering based on user and group IDs, which are notable additions for network security management.

hackernews · jaypatelani · Aug 1, 17:56 · [Discussion](https://news.ycombinator.com/item?id=49136736)

**Background**: NetBSD is a free, open-source Unix-like operating system known for its portability and clean design. It is one of the major BSD variants, alongside FreeBSD and OpenBSD. The MICROVM kernel is designed for extremely fast virtual machine boot, making it suitable for scenarios like microservices where rapid startup is critical. The npf firewall is NetBSD's packet filter, which has been enhanced to provide more granular control.

<details><summary>References</summary>
<ul>
<li><a href="https://www.netbsd.org/releases/formal-11/NetBSD-11.0.html">Announcing NetBSD 11.0 RC7 (July 21, 2026)</a></li>
<li><a href="https://www.phoronix.com/news/smolBSD">smolBSD Builds On The NetBSD-MicroVM Kernel For Booting To Service VMs In Milliseconds - Phoronix</a></li>
<li><a href="https://wiki.netbsd.org/users/imil/microvm/">microvm</a></li>

</ul>
</details>

**Discussion**: Community comments reflect curiosity about BSD relevance and software compatibility. One user asked about Wine support on NetBSD for running Windows-only software, while another pondered the current status and usage of BSDs compared to Linux. Others highlighted the value of the firewall improvements and the MICROVM kernel's fast boot time, noting the release announcement provides more details.

**Tags**: `#NetBSD`, `#BSD`, `#operating systems`, `#release`, `#virtualization`

---

<a id="item-6"></a>
## [Microsoft's Flint: A New Visualization Language for AI Agents](https://microsoft.github.io/flint-chart/) ⭐️ 7.0/10

Microsoft has introduced Flint, an open-source visualization intermediate language designed to let AI agents create expressive, polished charts from compact, human-editable specifications. The project is available on GitHub and was announced via Microsoft Research's blog. Flint addresses the growing need for efficient and reliable chart generation in AI-driven applications, potentially simplifying how large language models produce visualizations. It could influence the ecosystem by offering a middle ground between low-level charting libraries and high-level grammar, though its adoption depends on community acceptance and demonstrated advantages over existing methods. Flint is an intermediate language that can render to multiple charting backends, aiming to be token-efficient for LLMs. However, community feedback suggests that direct Vega-Lite generation may offer more flexibility for complex customizations, and the necessity of a new language is questioned when LLMs can already write backend code.

hackernews · vinhnx · Aug 1, 02:45 · [Discussion](https://news.ycombinator.com/item?id=49130604)

**Background**: Visualization languages like Vega-Lite and ggplot2 provide high-level grammars for statistical graphics, allowing users to specify charts declaratively. In the AI era, large language models are increasingly used to generate visualizations from natural language, but they often struggle with the verbosity and complexity of existing specifications. Flint aims to bridge this gap by offering a compact, human-editable intermediate representation that AI agents can produce and edit efficiently.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/research/blog/flint-a-visualization-language-for-the-ai-era/">Flint : A visualization language for the AI era - Microsoft Research</a></li>
<li><a href="https://github.com/microsoft/flint-chart">GitHub - microsoft / flint -chart: 🪄 Flint is a visualization language ...</a></li>
<li><a href="https://vega.github.io/vega-lite/examples/">Example Gallery | Vega-Lite</a></li>

</ul>
</details>

**Discussion**: Community comments express mixed sentiment: some praise the concept but question its advantages over direct Vega-Lite generation, citing flexibility issues for custom visualizations. Others wonder why not simply have AI write backend code directly, and some note that existing APIs like ggplot2 remain strong. Overall, the discussion reflects thoughtful critique and engagement with the project's value proposition.

**Tags**: `#visualization`, `#AI`, `#Microsoft`, `#charting`, `#LLM`

---

<a id="item-7"></a>
## [Silicon Valley Founder's Financial Ruin: A Cautionary Tale](https://zaksa.zip/blog/silicon-valley-founder-meat-grinder/) ⭐️ 7.0/10

A personal story details how a founder, referred to as Jim, pursued startup wealth and risk-taking, leading to financial ruin. The article uses his experience to critique the money-driven culture of Silicon Valley. This story resonates with many in the tech community, highlighting the dangers of prioritizing wealth over genuine passion and the high variance of startup outcomes. It sparks reflection on the cultural shift in Silicon Valley from building things to chasing money. The article mentions Jim's financial recklessness, including an example of getting into home brewing, which one commenter noted is actually a cheap hobby. The story underscores the psychological trap of wanting to be a 'founder' rather than doing the actual work.

hackernews · Kaizeras · Aug 1, 20:20 · [Discussion](https://news.ycombinator.com/item?id=49138045)

**Background**: Startup culture often glorifies risk-taking and wealth, but this can lead to personal financial disaster. The Bay Area tech scene has shifted over the years, with some observers noting a move from a focus on building products to a focus on making money, especially after the rise of bitcoin.

**Discussion**: Commenters expressed sympathy for the founder's story and critiqued the money-driven culture. Some shared personal anecdotes of persistence leading to success, while others noted the difference between wanting to be a founder and actually doing the work. One commenter pointed out that home brewing is a cheap hobby, questioning the author's example.

**Tags**: `#startup culture`, `#entrepreneurship`, `#financial risk`, `#tech industry`, `#personal story`

---

<a id="item-8"></a>
## [Cursor Accidentally Removes Cost Data from Usage Page and CSV Export](https://forum.cursor.com/t/usage-page-to-token-amount-what/167153) ⭐️ 6.0/10

Cursor removed cost information from its usage page and CSV export, but a Cursor employee clarified it was accidental and the CSV export has been fixed. The removal was due to cleaning up an old feature flag that showed a dollar usage graph to some self-serve users. This change affects users who rely on Cursor's usage page and CSV export for cost tracking and internal chargeback, especially teams. It highlights the importance of transparency in token usage and billing, and the community's sensitivity to any changes in cost visibility. The Cursor employee stated that the CSV export is fixed, but the dollar usage graph was intentionally removed because it showed included plan usage as dollars, which could be confused with actual spend. The Spending page still shows billing information. Some users reported discrepancies between dashboard UI, CSV export, and API cost totals.

hackernews · EugeneOZ · Aug 1, 15:25 · [Discussion](https://news.ycombinator.com/item?id=49135257)

**Background**: Cursor is an AI-powered code editor that uses tokens for billing, with on-demand usage charged separately from included plan usage. Users often track token usage and costs via the dashboard and CSV exports for budgeting and chargeback. The community discussion also touches on token efficiency differences between AI coding agents and the ease of switching back to VS Code.

<details><summary>References</summary>
<ul>
<li><a href="https://forum.cursor.com/t/dashboard-export-usage-events-csv-no-longer-exports-cost/167193">Dashboard export-usage-events-csv no longer exports cost! - Bug Reports - Cursor - Community Forum</a></li>
<li><a href="https://forum.cursor.com/t/question-about-discrepancies-between-dashboard-ui-csv-export-and-teams-filtered-usage-events-cost-totals/157091">Question about discrepancies between Dashboard UI, CSV export, and /teams/filtered-usage-events cost totals - Help - Cursor - Community Forum</a></li>
<li><a href="https://en.wikipedia.org/wiki/Cursor_(company)">Cursor (company) - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community members expressed mixed sentiments: some recommended measuring token efficiency across different harnesses, while others questioned Cursor's value in 2026, preferring CLI tools like Claude Code and Codex. A Cursor employee clarified the accidental removal and fix, and one user joked about token-based pricing in the future. Another noted Cursor's easy migration from VS Code is a double-edged sword.

**Tags**: `#Cursor`, `#AI coding tools`, `#usage tracking`, `#token efficiency`, `#product update`

---

<a id="item-9"></a>
## [Reddit CEO Questions Google AI Overviews Value as Stock Falls](https://arstechnica.com/ai/2026/08/reddit-ceo-on-ai-overviews-were-still-looking-for-that-win-win/) ⭐️ 6.0/10

Reddit's CEO has publicly questioned the value of Google's AI Overviews feature, suggesting the company may reconsider its licensing deal with Google as Reddit's stock price declines. This development highlights the growing tension between content providers and AI-powered search features that may reduce traffic to original sources. It could influence how Reddit and other platforms negotiate future AI data licensing deals. Reddit signed a licensing deal with Google in February 2024, reportedly worth about $60 million per year, granting Google access to Reddit's data for AI training and grounding. The CEO's comments suggest the deal's value is being reassessed amid stock declines.

rss · Ars Technica · Aug 1, 12:30

**Background**: Google AI Overviews is an AI feature integrated into Google Search that generates AI responses at the top of search results. It has faced criticism for inaccuracies, hallucinations, and reducing web traffic to original sources, which may affect content providers like Reddit.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Google_AI_Overviews">Google AI Overviews</a></li>
<li><a href="https://mentionova.com/research/why-reddit-runs-the-ai-answer">Why Reddit Runs the AI Answer — How One Forum... — Mentionova</a></li>
<li><a href="https://marketvantage.com/blog/the-google-reddit-deal-nine-months-in/">The Google - Reddit Deal Nine Months In | Market Vantage</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Reddit`, `#Google`, `#business`, `#licensing`

---

<a id="item-10"></a>
## [Defcon Badge Doubles as Open-Source Security Key](https://arstechnica.com/security/2026/08/defcons-new-badge-is-a-security-key-you-can-see-inside/) ⭐️ 6.0/10

Defcon's 2026 badge, created by Andrew 'bunnie' Huang, includes a removable, transparent core module called Baochip-1x that functions as an open-source hardware security token. Attendees can inspect the chip's design and continue using it as a security key after the conference. This badge pushes the boundaries of hardware security and transparency, demonstrating how open-source designs can build trust in cryptographic hardware. It could inspire broader adoption of verifiable security keys in consumer devices and security conferences. The Baochip-1x is an open-source chip whose security is verifiable, and it can be used as a hardware security token. The badge's removable core module is transparent, allowing hackers to physically inspect the chip and its connections.

rss · Ars Technica · Aug 1, 10:05

**Background**: Defcon is one of the world's largest and most famous hacking conferences, known for its unique electronic badges that often feature challenges and collectible designs. Hardware security tokens, such as YubiKeys, provide cryptographic authentication, but their internal designs are typically proprietary. By making the chip open-source, Defcon aims to demonstrate that security can be transparent and verifiable.

<details><summary>References</summary>
<ul>
<li><a href="https://www.wired.com/story/defcon-34-badge-baochip-andrew-bunnie-huang/">The New Defcon Badges Pack a Unique Open Source Chip That Doubles as a Security Key | WIRED</a></li>
<li><a href="https://iplogger.org/blog/the-new-defcon-badges-pack-a-unique-open-source-chip-that-doubles-as-a-security-key/">Defcon's Open-Source Badge: A Hardware Root of Trust ...</a></li>
<li><a href="https://www.techmeme.com/260801/p10">Techmeme: This year's Defcon badges include Baochip-1x, an ...</a></li>

</ul>
</details>

**Tags**: `#security`, `#hardware`, `#Defcon`, `#badge`, `#hacking`

---

<a id="item-11"></a>
## [How Fruit Flies Navigate Turbulent Odor Plumes Using Memory and Direction](https://arstechnica.com/science/2026/08/how-fruit-flies-chase-invisible-ribbons-of-smell-to-get-to-their-source/) ⭐️ 6.0/10

The article explains how fruit flies track invisible odor ribbons in turbulent air by combining memory of past encounters with directional sensing, rather than relying on concentration gradients. This research provides new insights into biological olfaction and navigation strategies. Understanding how fruit flies navigate odor plumes could inspire more efficient robotic olfactory systems and improve algorithms for autonomous agents searching for chemical sources. It also deepens our understanding of sensory processing and memory in simple nervous systems. The article likely discusses experiments that track fruit fly behavior in controlled wind tunnels with turbulent odor plumes, revealing that flies use a combination of upwind surges and crosswind casts, modulated by memory of recent odor encounters. The research may also involve computational models or neural imaging to identify underlying mechanisms.

rss · Ars Technica · Aug 1, 10:00

**Background**: Odor plumes in natural environments are turbulent and break into irregular filaments, so they do not provide a smooth concentration gradient for navigation. Insects like fruit flies must use intermittent odor encounters and wind direction to locate sources. This research builds on previous studies of insect navigation and has implications for robotics and artificial olfaction.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/abs/2605.21329">Smart strategies to navigate turbulent odor plumes ...</a></li>
<li><a href="https://arxiv.org/html/2605.21329v2">Smart strategies to navigate turbulent odor plumes ...</a></li>
<li><a href="https://elifesciences.org/articles/72196">Learning to predict target location with turbulent odor plumes</a></li>

</ul>
</details>

**Tags**: `#biology`, `#olfaction`, `#fruit flies`, `#neuroscience`, `#robotics`

---