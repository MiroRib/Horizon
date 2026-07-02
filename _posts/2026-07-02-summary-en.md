---
layout: default
title: "Horizon Summary: 2026-07-02 (EN)"
date: 2026-07-02
lang: en
---

> From 161 items, 26 important content pieces were selected

---

1. [Virginia Bans Sale of Geolocation Data](#item-1) ⭐️ 8.0/10
2. [Linux 6.9 LUKS Suspend Fails to Wipe Encryption Keys](#item-2) ⭐️ 8.0/10
3. [Podman v6.0.0 Released with Major Networking Improvements](#item-3) ⭐️ 8.0/10
4. [Immich 3.0 Major Release Sparks Community Debate](#item-4) ⭐️ 8.0/10
5. [Artificial cells achieve limited rounds of cell division](#item-5) ⭐️ 8.0/10
6. [Google loses final appeal of record €4.3B EU antitrust fine](#item-6) ⭐️ 8.0/10
7. [Google's AI buildout drove 37% electricity use increase in 2025](#item-7) ⭐️ 8.0/10
8. [PeerTube: Decentralized Video Platform Gains Traction](#item-8) ⭐️ 7.0/10
9. [How to Ask Strangers for Help Effectively](#item-9) ⭐️ 7.0/10
10. [Spain Blacklists Palantir Over National Security](#item-10) ⭐️ 7.0/10
11. [Tesla driver charged with manslaughter after FSD crash kills woman](#item-11) ⭐️ 7.0/10
12. [PamStealer: New macOS Malware Validates Passwords via PAM](#item-12) ⭐️ 7.0/10
13. [FAA Proposes Quiet Supersonic Flights Over US Cities](#item-13) ⭐️ 7.0/10
14. [Privacy Advocates Warn FTC Over Musk's X Risks](#item-14) ⭐️ 7.0/10
15. [Editorial: Scientists Must Speak Up Against Politicized Science Rule](#item-15) ⭐️ 7.0/10
16. [California's Manure Methane Math Doesn't Add Up](#item-16) ⭐️ 7.0/10
17. [Hidden costs inflate gas plant prices by 30%](#item-17) ⭐️ 7.0/10
18. [Crypto at a Turning Point: From Web3 for Web3 to Real Finance](#item-18) ⭐️ 7.0/10
19. [Ex-Call of Duty dev launches studio with open-source pledge](#item-19) ⭐️ 7.0/10
20. [Google's Electricity Consumption Soars Due to GenAI](#item-20) ⭐️ 7.0/10
21. [Anthropic SDK Python v0.116.0 Adds Agent Memory Beta Header](#item-21) ⭐️ 6.0/10
22. [Exapunks: A Retrospective on Zachtronics' Programming Puzzle Game](#item-22) ⭐️ 6.0/10
23. [AI Moves from Chatbots to Critical Industrial Infrastructure](#item-23) ⭐️ 6.0/10
24. [Startup Springboards Tackles AI Groupthink with Flint LLM](#item-24) ⭐️ 6.0/10
25. [Analysts Predict Rising PPA Prices as Clean Energy Tax Credits Expire](#item-25) ⭐️ 6.0/10
26. [Union Workers Launch Hardship Fund for Laid-Off Game Devs](#item-26) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Virginia Bans Sale of Geolocation Data](https://www.hunton.com/privacy-and-cybersecurity-law-blog/virginia-bans-sale-of-geolocation-data) ⭐️ 8.0/10

Virginia Governor Abigail Spanberger signed SB 338 on April 13, 2024, amending the Virginia Consumer Data Protection Act to prohibit the sale of precise geolocation data, effective July 1, 2024. This ban sets a precedent for state-level privacy protections, limiting data brokers and tech companies from monetizing location data without consent, and follows similar actions in Maryland and Oregon. The ban defines precise geolocation data as information that identifies a person's location within 1,750 feet, and prohibits the sale or offering for sale of such data, with enforcement by the Virginia Attorney General.

hackernews · toomuchtodo · Jul 2, 21:03 · [Discussion](https://news.ycombinator.com/item?id=48767347)

**Background**: The Virginia Consumer Data Protection Act (VCDPA), enacted in 2021 and effective January 1, 2023, is the second comprehensive state privacy law in the U.S. after California's CCPA. Geolocation data is increasingly collected by apps and devices, and its sale has been linked to abuses such as tracking visits to reproductive health clinics.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cybereyeq.com/p/is-your-geolocation-data-ready-for-virginia-s-ban">Is Your Geolocation Data Ready for Virginia 's Ban?</a></li>
<li><a href="https://www.gblock.app/articles/virginia-geolocation-data-sale-ban">Virginia Banned the Sale of Your Location Data —Six More States...</a></li>
<li><a href="https://modernorange.io/item/48767347">US State of Virginia Bans Sale of Geolocation Data | Modern Orange</a></li>

</ul>
</details>

**Discussion**: Commenters generally support the ban, citing real-world abuses like tracking Planned Parenthood visits for anti-abortion ads. Some raise enforcement concerns, such as how to handle out-of-state companies or data processed in Virginia data centers.

**Tags**: `#privacy`, `#geolocation`, `#regulation`, `#data protection`, `#Virginia`

---

<a id="item-2"></a>
## [Linux 6.9 LUKS Suspend Fails to Wipe Encryption Keys](https://mathstodon.xyz/@iblech/116769502749142438) ⭐️ 8.0/10

A regression in Linux kernel 6.9 caused the LUKS suspend operation to stop wiping disk-encryption keys from memory, leaving them vulnerable to cold boot attacks. A fix has been proposed. This security regression could expose full-disk encryption keys during suspend-to-RAM, undermining the protection of sensitive data. It highlights the difficulty of testing security-critical kernel features. The bug affects the cryptsetup luksSuspend command, which is used to temporarily lock LUKS devices before suspend. The issue was introduced in Linux 6.9 and has been fixed in a proposed patch.

hackernews · IngoBlechschmid · Jul 2, 15:25 · [Discussion](https://news.ycombinator.com/item?id=48763035)

**Background**: LUKS (Linux Unified Key Setup) is a disk encryption specification that stores encryption keys in kernel memory during operation. When suspending to RAM, the system normally wipes these keys to prevent cold boot attacks, but the regression broke that behavior.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48763035">Since Linux 6.9, LUKS suspend stopped wiping disk - encryption keys ...</a></li>
<li><a href="https://github.com/nailfarmer/debian-luks-suspend">GitHub - nailfarmer/debian- luks - suspend : Lock encrypted root volume...</a></li>
<li><a href="https://askubuntu.com/questions/95625/suspend-to-ram-and-encrypted-partitions">encryption - Suspend to RAM and encrypted partitions - Ask Ubuntu</a></li>

</ul>
</details>

**Discussion**: Some commenters noted that luksSuspend is not officially supported and may only affect Debian, while others argued that security bugs like this are easy to miss because everything still works. There was also debate about whether the risk is significant for typical users.

**Tags**: `#Linux`, `#security`, `#LUKS`, `#kernel`, `#encryption`

---

<a id="item-3"></a>
## [Podman v6.0.0 Released with Major Networking Improvements](https://blog.podman.io/2026/07/introducing-podman-v6-0-0/) ⭐️ 8.0/10

Podman v6.0.0, a major version release of the daemonless container engine, introduces significant networking improvements and continues to gain traction as a Docker alternative. This release strengthens Podman's position as a leading Docker alternative, offering enhanced networking capabilities that benefit users migrating from Docker or running rootless containers in production. The release focuses on networking improvements, though specific technical details were not provided in the summary. Users report seamless compatibility with docker-compose.yml files, requiring zero changes to switch from Docker.

hackernews · soheilpro · Jul 2, 14:23 · [Discussion](https://news.ycombinator.com/item?id=48762098)

**Background**: Podman is a daemonless, rootless, open-source container engine developed by Red Hat. Unlike Docker, it does not require a central daemon, enhancing security and system integration. Rootless containers allow non-root users to run containers, reducing security risks.

<details><summary>References</summary>
<ul>
<li><a href="https://podman.io/">Podman</a></li>
<li><a href="https://docs.podman.io/">What is Podman? — Podman documentation</a></li>
<li><a href="https://www.redhat.com/en/topics/containers/what-is-podman">What is Podman? - Red Hat</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely positive, with users praising Podman's ease of migration from Docker and the Quadlet feature for systemd integration. Some users discuss performance comparisons with OrbStack on macOS and note minor UI contrast issues.

**Tags**: `#Podman`, `#containers`, `#Docker alternative`, `#networking`, `#open source`

---

<a id="item-4"></a>
## [Immich 3.0 Major Release Sparks Community Debate](https://github.com/immich-app/immich/discussions/29439) ⭐️ 8.0/10

Immich 3.0, a major update to the open-source self-hosted photo management platform, has been released, bringing significant improvements and sparking community discussion. This release solidifies Immich as a leading open-source alternative to Google Photos and Apple Photos, giving users full control over their data and privacy. The update includes improvements to iOS sync, which has been a pain point for users with large photo libraries, and addresses encryption trade-offs compared to alternatives like Ente.

hackernews · hashier · Jul 2, 14:13 · [Discussion](https://news.ycombinator.com/item?id=48761944)

**Background**: Immich is a high-performance, self-hosted photo and video management solution that offers features like face recognition, geolocation, and mobile syncing. It is often compared to Google Photos and Apple Photos, but with the advantage of complete data ownership and privacy.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/immich-app/immich">GitHub - immich-app/immich: High performance self-hosted photo and video management solution. · GitHub</a></li>
<li><a href="https://www.howtogeek.com/self-hosted-alternatives-to-google-photos/">3 Self-Hosted Alternatives to Google Photos - How-To Geek</a></li>
<li><a href="https://blog.elest.io/immich-free-open-source-photo-and-video-management-platform/">Immich: Free Open Source Photo and Video Management Platform</a></li>

</ul>
</details>

**Discussion**: Community members praised Immich as a 'no-brainer replacement' for Apple Photos or Google Photos when combined with a VPN like Tailscale. However, some users reported issues with iOS sync for large libraries, and others chose Ente for its end-to-end encryption, highlighting trade-offs between polish and privacy.

**Tags**: `#self-hosting`, `#photo management`, `#open-source`, `#privacy`, `#immich`

---

<a id="item-5"></a>
## [Artificial cells achieve limited rounds of cell division](https://arstechnica.com/science/2026/07/artificial-cell-manages-a-few-rounds-of-cell-division/) ⭐️ 8.0/10

Researchers have created artificial cells that can undergo a few rounds of cell division, a milestone in synthetic biology, though the process requires extensive externally added materials. This achievement brings us closer to creating self-replicating synthetic life, which could revolutionize biotechnology, drug delivery, and our understanding of the origin of life. The artificial cells only manage a few divisions before stopping, and they rely on a supply of added materials such as membrane components and energy sources to divide.

rss · Ars Technica · Jul 2, 16:21

**Background**: Cell division is a fundamental process for life, enabling growth and reproduction. Synthetic biology aims to build minimal cells from scratch to understand life's principles and create useful bio-systems. Previous attempts have achieved artificial cell growth but not division.

<details><summary>References</summary>
<ul>
<li><a href="https://www.quantamagazine.org/for-the-first-time-a-cell-built-from-scratch-grows-and-divides-20260701/">For the First Time, a Cell Built From Scratch Grows and Divides | Quanta Magazine</a></li>
<li><a href="https://link.springer.com/article/10.1186/s12915-019-0665-1">Synthetic cell division via membrane-transforming molecular assemblies | BMC Biology | Springer Nature Link</a></li>

</ul>
</details>

**Tags**: `#synthetic biology`, `#artificial cells`, `#cell division`, `#biotechnology`

---

<a id="item-6"></a>
## [Google loses final appeal of record €4.3B EU antitrust fine](https://arstechnica.com/gadgets/2026/07/google-loses-long-running-appeal-of-record-eu-fine-will-have-to-cough-up-4-7-billion/) ⭐️ 8.0/10

The European Court of Justice upheld a €4.3 billion fine against Google for abusing its market dominance by bundling its search and Chrome apps with Android, rejecting Google's final appeal. This landmark ruling sets a strong precedent that bundling free apps can still be an antitrust violation, potentially reshaping how tech giants distribute software on mobile platforms globally. The fine, originally imposed in 2018, is the largest ever levied by the EU. Google had argued that Android is open-source and that bundling was necessary to monetize the platform.

rss · Ars Technica · Jul 2, 16:15

**Background**: Since 2010, the European Commission has investigated Google for antitrust violations, resulting in three major fines totaling over €8 billion. The Android case focused on Google requiring manufacturers to pre-install Google Search and Chrome as a condition for licensing the Play Store.

<details><summary>References</summary>
<ul>
<li><a href="https://cryptobriefing.com/google-loses-eu-antitrust-fine-appeal/">Google loses appeal against €4B EU antitrust fine over Android bundling</a></li>
<li><a href="https://en.wikipedia.org/wiki/Antitrust_cases_against_Google_by_the_European_Union">Antitrust cases against Google by the European Union - Wikipedia</a></li>
<li><a href="https://www.theverge.com/2018/10/18/17996640/google-eu-android-antitrust-ruling-app-unbundling-european-commission-chrome-search">Google is unbundling Android apps: all the news about the EU’s antitrust ruling | The Verge</a></li>

</ul>
</details>

**Tags**: `#antitrust`, `#Google`, `#EU regulation`, `#Android`, `#tech policy`

---

<a id="item-7"></a>
## [Google's AI buildout drove 37% electricity use increase in 2025](https://arstechnica.com/ai/2026/07/googles-ai-buildout-drove-37-increase-in-electricity-use-in-2025/) ⭐️ 8.0/10

Google's total electricity consumption rose by 37% in 2025, driven primarily by the expansion of AI data centers, according to its latest environmental report. This surge highlights the growing tension between AI infrastructure growth and corporate clean energy commitments, potentially influencing industry practices and energy policy. Google's electricity demand more than doubled from 2020 to 2024, and despite signing agreements for over 12 GW of new clean energy in 2025, the company's carbon-free energy goal remains challenging.

rss · Ars Technica · Jul 2, 11:15

**Background**: AI model training and deployment require massive computational resources, leading to rapid growth in data center electricity use. Google has set a goal of operating on 24/7 carbon-free energy by 2030, but rising AI demand is making this target harder to achieve.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pewresearch.org/short-reads/2025/10/24/what-we-know-about-energy-use-at-us-data-centers-amid-the-ai-boom/">US data centers’ energy use amid the artificial intelligence ...</a></li>
<li><a href="https://www.technologyreview.com/2025/11/13/1127896/google-energy-goals/">Google is still aiming for its “moonshot” 2030 energy goals | MIT Technology Review</a></li>
<li><a href="https://blog.google/company-news/outreach-and-initiatives/sustainability/2026-environmental-report/">Read Google’s 2026 Environmental Report</a></li>

</ul>
</details>

**Tags**: `#AI`, `#energy`, `#sustainability`, `#Google`, `#data centers`

---

<a id="item-8"></a>
## [PeerTube: Decentralized Video Platform Gains Traction](https://github.com/Chocobozzz/PeerTube) ⭐️ 7.0/10

PeerTube is a free, open-source, decentralized video platform that uses ActivityPub federation and peer-to-peer technology to distribute playout load among viewers, reducing server strain for popular videos. PeerTube offers a viable alternative to centralized platforms like YouTube, giving content creators and communities more control over their data and reducing reliance on big tech infrastructure. PeerTube primarily handles playout (data distribution) and hosting, but lacks built-in monetization and content discovery features, which are major challenges for professional creators.

hackernews · doener · Jul 2, 11:17 · [Discussion](https://news.ycombinator.com/item?id=48759634)

**Background**: PeerTube is built on the ActivityPub protocol, enabling federation across instances, similar to Mastodon. It uses WebTorrent for peer-to-peer streaming, distributing the load among viewers' browsers when a video goes viral.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/PeerTube">PeerTube - Wikipedia</a></li>
<li><a href="https://github.com/Chocobozzz/PeerTube">GitHub - Chocobozzz/PeerTube: ActivityPub-federated video streaming platform using P2P directly in your web browser · GitHub</a></li>
<li><a href="https://joinpeertube.org/">What is PeerTube? | JoinPeerTube</a></li>

</ul>
</details>

**Discussion**: Community comments highlight that PeerTube lacks monetization options, making it difficult for professional YouTubers to sustain high-quality production. Some users appreciate its federated nature for open-source projects but note limited content discovery and audience reach.

**Tags**: `#decentralization`, `#video hosting`, `#federation`, `#open source`, `#PeerTube`

---

<a id="item-9"></a>
## [How to Ask Strangers for Help Effectively](https://pradyuprasad.com/writings/how-to-ask-for-help/) ⭐️ 7.0/10

A practical guide on requesting assistance from strangers, emphasizing proof of work, brevity, and understanding the recipient's perspective, has been published and widely discussed. This advice addresses a universal skill that many people struggle with, and the community validation (344 points, 53 comments) shows its high relevance and impact. Key points include showing proof of work upfront, keeping requests brief, and tailoring the ask to the recipient's context. The article is tagged under communication, career-advice, soft-skills, and networking.

hackernews · FigurativeVoid · Jul 2, 13:19 · [Discussion](https://news.ycombinator.com/item?id=48761118)

**Background**: Asking for help from strangers is a common but challenging task in professional and personal contexts. Many people fail because they do not respect the recipient's time or fail to demonstrate their own effort. This guide synthesizes best practices from experienced individuals.

**Discussion**: Commenters generally agree with the advice, adding personal experiences and nuances. Some emphasize that proof of work must be genuine and deep, not superficial, and that understanding the recipient's baseline request frequency is crucial.

**Tags**: `#communication`, `#career-advice`, `#soft-skills`, `#networking`

---

<a id="item-10"></a>
## [Spain Blacklists Palantir Over National Security](https://clashreport.com/world/articles/spain-orders-blacklist-of-us-tech-giant-palantir-from-public-and-private-companies-fsnc2z17gjv) ⭐️ 7.0/10

Spain has ordered a blacklist of Palantir, the US data analytics giant, from both public and private companies due to national security concerns. This move signals growing European skepticism toward US tech firms handling sensitive data, potentially reshaping transatlantic data sovereignty and geopolitical trust. The decision stems from official concern over potential misuse of classified information linked to national security, though specific concerns have not been detailed.

hackernews · mgh2 · Jul 2, 15:02 · [Discussion](https://news.ycombinator.com/item?id=48762725)

**Background**: Palantir is an American company known for its data integration and analytics software used by intelligence agencies and militaries. Data sovereignty refers to the principle that data generated within a country is subject to its laws. Spain's action reflects broader European efforts to protect data sovereignty and reduce reliance on foreign tech providers.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Palantir_Technologies">Palantir Technologies</a></li>
<li><a href="https://en.wikipedia.org/wiki/Data_sovereignty">Data sovereignty - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Comments are divided: some praise Spain's direction on data sovereignty, while others suspect the decision is politically motivated, noting Spain's recent contracts with Huawei's equivalent. Critics argue that trusting Chinese firms over Palantir is misguided given China's authoritarian nature.

**Tags**: `#Palantir`, `#Spain`, `#data sovereignty`, `#national security`, `#geopolitics`

---

<a id="item-11"></a>
## [Tesla driver charged with manslaughter after FSD crash kills woman](https://www.theverge.com/transportation/961161/tesla-fsd-katy-tx-manslaughter-charges) ⭐️ 7.0/10

Michael Butler, 44, was arrested and charged with manslaughter after his Tesla Model 3, allegedly using Full Self-Driving (FSD), crashed into a Texas home, killing a woman inside. This case could set a legal precedent for holding drivers accountable when using advanced driver-assistance systems, potentially influencing regulations and public trust in autonomous driving technology. The crash occurred last month in Katy, Texas, and Butler claimed the vehicle was in FSD mode at the time. Tesla's FSD is a Level 2 driver-assist system that requires active driver supervision.

rss · The Verge · Jul 2, 22:09

**Background**: Tesla's Full Self-Driving (FSD) is an advanced driver-assistance system (ADAS) that automates steering, acceleration, and braking but still requires the driver to remain attentive and ready to take control. Despite its name, FSD is not fully autonomous; it is classified as Level 2 on the SAE automation scale. This incident highlights the ongoing debate over the safety and legal responsibility of such systems.

<details><summary>References</summary>
<ul>
<li><a href="https://www.msn.com/en-us/autos/self-driving-cars/tesla-driver-charged-with-manslaughter-after-woman-killed-in-crash-sheriff/ar-AA274Thv">Tesla driver charged with manslaughter after woman killed in ...</a></li>
<li><a href="https://www.tesla.com/fsd">Full Self - Driving (Supervised) | Tesla</a></li>

</ul>
</details>

**Tags**: `#Tesla`, `#autonomous driving`, `#legal`, `#FSD`, `#crash`

---

<a id="item-12"></a>
## [PamStealer: New macOS Malware Validates Passwords via PAM](https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/) ⭐️ 7.0/10

Researchers at Jamf Threat Labs discovered PamStealer, a Rust-based macOS infostealer that uses the Pluggable Authentication Modules (PAM) interface to locally validate stolen login passwords before exfiltrating sensitive data. This discovery highlights the increasing sophistication of macOS infostealers, as PamStealer's password validation technique reduces false positives and makes detection harder, signaling a worrying trend for Mac security. PamStealer uses a self-contained JXA dropper and a Rust-based second stage, and it validates credentials locally through PAM before harvesting them, distinguishing it from typical infostealers that blindly steal data.

rss · Ars Technica · Jul 2, 19:38

**Background**: macOS infostealers are malware designed to steal sensitive data like passwords and credentials from Mac systems. Recent campaigns have used social engineering tactics such as ClickFix prompts and malicious DMG installers to deploy stealers like AMOS, MacSync, and DigitStealer. PamStealer represents an evolution by adding password validation to ensure stolen credentials are correct before exfiltration.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/new-pamstealer-macos-malware-uses-clever-tradecraft-to-remain-stealthy/">Newly discovered PamStealer isn’t your typical macOS malware</a></li>
<li><a href="https://www.idropnews.com/news/pamstealer-macos-malware-password-verification/265878/">New PamStealer Mac Malware Pre-verifies Stolen Passwords</a></li>
<li><a href="https://appleworld.today/2026/07/pamstealer-is-a-rust-based-macos-infostealer-that-validates-credentials-through-pam/">PamStealer is a Rust-based macOS infostealer that validates ...</a></li>

</ul>
</details>

**Tags**: `#macOS`, `#malware`, `#security`, `#infostealer`

---

<a id="item-13"></a>
## [FAA Proposes Quiet Supersonic Flights Over US Cities](https://arstechnica.com/gadgets/2026/07/faa-proposal-supersonic-airliners-can-fly-over-us-cities-if-theyre-quiet/) ⭐️ 7.0/10

The FAA has proposed new rules that would legalize quiet supersonic flights over US cities, provided the aircraft do not produce a disruptive sonic boom. This regulatory change could enable a new generation of supersonic airliners to operate over land. This proposal could revitalize supersonic air travel by removing the long-standing ban on overland supersonic flights, which was a major factor in the retirement of the Concorde. If adopted, it would open up lucrative transcontinental routes for supersonic aircraft, potentially reducing flight times significantly. The proposal is based on advancements in quiet supersonic technology, such as NASA's X-59 Quesst, which is designed to produce a low 75 EPNdB thump instead of a loud sonic boom. The rule would set a noise standard that supersonic aircraft must meet to be allowed overland flights.

rss · Ars Technica · Jul 2, 17:29

**Background**: Supersonic flight over land has been banned in the US since 1973 due to the disruptive sonic booms generated by aircraft exceeding Mach 1. The Concorde, the most famous supersonic airliner, was limited to overwater routes, which contributed to its commercial failure. NASA and Lockheed Martin have been developing the X-59 Quesst to demonstrate that supersonic aircraft can be designed to produce a much quieter sound, potentially paving the way for regulatory changes.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Quiet_Supersonic_Technology">Quiet Supersonic Technology</a></li>
<li><a href="https://www.nasa.gov/centers-and-facilities/armstrong/nasa-prepares-to-go-public-with-quiet-supersonic-tech/">NASA Prepares to Go Public with Quiet Supersonic Tech</a></li>
<li><a href="https://www.nasa.gov/centers-and-facilities/armstrong/supersonic-technologies/">Supersonic Technologies - NASA</a></li>

</ul>
</details>

**Tags**: `#aviation`, `#regulation`, `#supersonic`, `#technology`, `#FAA`

---

<a id="item-14"></a>
## [Privacy Advocates Warn FTC Over Musk's X Risks](https://arstechnica.com/tech-policy/2026/07/musks-x-poses-serious-risk-to-americans-privacy-advocates-warn-ftc/) ⭐️ 7.0/10

Privacy advocates have urged the U.S. Federal Trade Commission (FTC) to reject Elon Musk's attempt to end the agency's monitoring of X (formerly Twitter), warning that the platform poses a serious risk to Americans' privacy and AI-related concerns. This matters because X is a major social media platform with hundreds of millions of users, and ending FTC oversight could lead to lax data protection and increased AI-driven privacy violations, setting a dangerous precedent for tech regulation. The FTC consent decree currently requires X to maintain a data governance team and monitor outbound traffic to prevent data breaches; advocates claim that team has been dismantled under Musk's leadership, violating the decree.

rss · Ars Technica · Jul 2, 14:39

**Background**: X (formerly Twitter) has been under an FTC consent decree since 2022 due to previous privacy violations. The decree mandates independent monitoring of the platform's data practices. Elon Musk acquired Twitter in 2022 and has since made significant changes, including layoffs that reportedly affected the compliance team. Privacy advocates fear that ending the decree would allow X to misuse user data for AI training without adequate safeguards.

<details><summary>References</summary>
<ul>
<li><a href="https://www.citizen.org/article/twitters-potential-violations-of-the-ftc-consent-decree/">Twitter's Potential Violations of the FTC Consent Decree - Public Citizen</a></li>
<li><a href="https://www.hoganlovells.com/en/publications/ftc-consent-decree-requires-monitoring-and-filtering-of-outbound-computer-traffic-to-block-export-of-sensitive-information">FTC Consent Decree Requires Monitoring and Filtering of Outbound...</a></li>

</ul>
</details>

**Tags**: `#privacy`, `#AI`, `#regulation`, `#social media`, `#Elon Musk`

---

<a id="item-15"></a>
## [Editorial: Scientists Must Speak Up Against Politicized Science Rule](https://arstechnica.com/science/2026/07/editorial-the-most-important-thing-you-can-do-to-protect-science/) ⭐️ 7.0/10

An editorial on Ars Technica urges scientists to submit public comments on a proposed rule that would allow political appointees to override scientific decisions. This rule threatens the integrity of science-based policymaking, and public comments are a critical avenue for scientists to defend evidence-based governance. The editorial emphasizes that individual comments can make a difference, as agencies are required to consider public feedback before finalizing rules.

rss · Ars Technica · Jul 2, 10:00

**Background**: In the U.S., federal agencies often seek public comment on proposed regulations. This particular rule would give political officials authority to alter or reject scientific findings, raising concerns about political interference in science.

**Tags**: `#science policy`, `#editorial`, `#advocacy`

---

<a id="item-16"></a>
## [California's Manure Methane Math Doesn't Add Up](https://www.technologyreview.com/2026/07/02/1139981/why-californias-carbon-manure-math-doesnt-add-up/) ⭐️ 7.0/10

An investigation reveals that California's program incentivizing methane capture from cattle manure may be counterproductive due to flawed carbon accounting. This exposes a critical flaw in California's climate policy, potentially undermining the effectiveness of renewable energy incentives and carbon offset markets. The program pays farmers to convert manure methane into natural gas, but the accounting may overestimate emission reductions, leading to net increases in greenhouse gases.

rss · MIT Technology Review · Jul 2, 09:00

**Background**: California's Low Carbon Fuel Standard (LCFS) incentivizes low-carbon transportation fuels, including biomethane from manure. However, critics argue that the methodology for calculating carbon intensity fails to account for leakage and other indirect effects.

<details><summary>References</summary>
<ul>
<li><a href="https://blog.ucs.org/jeremy-martin/something-stinks-california-must-end-manure-biomethane-accounting-gimmicks-in-its-low-carbon-fuel-standard/">Something Stinks: California Must End Manure Biomethane...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0013935124021765">Methodological study on carbon sequestration accounting for ...</a></li>
<li><a href="https://www.nature.com/articles/s41598-025-27609-2">Reduced life cycle climate impact from manure through ...</a></li>

</ul>
</details>

**Tags**: `#climate policy`, `#methane`, `#carbon accounting`, `#renewable energy`, `#agriculture`

---

<a id="item-17"></a>
## [Hidden costs inflate gas plant prices by 30%](https://www.utilitydive.com/news/sticker-shock-gas-power-plants-pipeline-gridlab/824061/) ⭐️ 7.0/10

GridLab and Current Energy Group released a report revealing that pipeline, fuel, and storage costs add about 30% to the total cost of new gas-fired power plants, costs often ignored by regulators. This analysis challenges the economic competitiveness of gas plants compared to cleaner energy resources, potentially influencing energy policy and infrastructure planning decisions. The hidden costs include mandatory long-term contracts for firm pipeline transportation, gas storage, and gas processing equipment, which can significantly alter a project's true cost to consumers.

rss · Utility Dive · Jul 2, 13:04

**Background**: When utilities propose new gas plants, regulators typically review only the upfront construction costs. However, gas plants require extensive supporting infrastructure—pipelines, storage, and fuel supply contracts—that add substantial ongoing costs. GridLab's report quantifies these overlooked expenses, showing they can inflate total project costs by roughly 30%.

<details><summary>References</summary>
<ul>
<li><a href="https://gridlab.org/the-hidden-costs-of-gas-press-release/">The Hidden Costs of Gas Press Release - GridLab</a></li>
<li><a href="https://gridlab.org/hidden-cost-of-gas/">Beyond the Power Plant: The Hidden Costs of Gas-Fired ...</a></li>
<li><a href="https://www.utilitydive.com/news/sticker-shock-gas-power-plants-pipeline-gridlab/824061/">Why the true cost of new gas plants is much higher than the sticker price | Utility Dive</a></li>

</ul>
</details>

**Tags**: `#energy`, `#infrastructure`, `#policy`, `#gas plants`, `#cost analysis`

---

<a id="item-18"></a>
## [Crypto at a Turning Point: From Web3 for Web3 to Real Finance](https://www.4gamer.net/games/991/G999104/20260702015/) ⭐️ 7.0/10

At IVS2026, IVC partners J.T. Law and Ann Chien declared that the era of 'Web3 for Web3' is over, and crypto is shifting toward practical financial infrastructure, citing Bitcoin cycles, institutional entry, stablecoin types, and Japan's regulatory impact on VC investment. This signals a maturation of the crypto industry, moving from speculative hype to real-world utility, which could attract more institutional capital and regulatory clarity, ultimately benefiting the broader financial ecosystem. The keynote distinguished between yield-bearing stablecoins and utility stablecoins, and noted that Japan's regulatory framework has shifted VC investment criteria. The discussion also covered Bitcoin's four-year cycle and institutional investor participation.

rss · 4Gamer.net · Jul 2, 06:32

**Background**: Web3 refers to a decentralized internet built on blockchain technology, but many projects have focused on speculation rather than real-world applications. Stablecoins are cryptocurrencies pegged to stable assets like the US dollar, and they come in different types: yield-bearing (earning interest) and utility (used for transactions). Japan has been a notable regulatory pioneer in crypto, influencing global investment patterns.

<details><summary>References</summary>
<ul>
<li><a href="https://chain.link/article/yield-bearing-stablecoins-explained">Yield-Bearing Stablecoins: Generating Onchain Yield | Chainlink</a></li>
<li><a href="https://www.bitgo.com/resources/blog/stablecoin-yield-explained/">Understanding Stablecoin Yield Sources and Variability | BitGo</a></li>

</ul>
</details>

**Tags**: `#cryptocurrency`, `#Web3`, `#financial infrastructure`, `#regulation`, `#institutional investment`

---

<a id="item-19"></a>
## [Ex-Call of Duty dev launches studio with open-source pledge](https://www.pcgamer.com/gaming-industry/former-call-of-duty-frontman-launches-new-studio-with-a-stop-killing-games-style-mission-statement-if-the-game-bombs-it-goes-open-source/) ⭐️ 7.0/10

Former Call of Duty developer Robert Bowling has founded a new game studio that pledges to release its games as open source if they fail commercially, aligning with the 'Stop Killing Games' movement. This initiative directly addresses the growing concern over game preservation, where publishers often abandon online-only games, rendering them unplayable. If successful, it could set a precedent for other studios to adopt similar open-source fallback plans. The studio's mission statement explicitly states that if a game 'bombs,' it will be made open source, allowing the community to keep it alive. This comes after Bowling's previous studio, Midnight Society, shut down in January 2025 following controversies involving co-founder Dr Disrespect.

rss · PC Gamer · Jul 2, 17:19

**Background**: The 'Stop Killing Games' movement, started in 2024 by YouTuber Ross Scott, campaigns against publishers permanently destroying games by shutting down servers without providing offline modes. The movement gained traction after Ubisoft shut down The Crew, a primarily single-player game that required constant internet. Open-sourcing a failed game would allow players to host their own servers and continue playing.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stop_Killing_Games">Stop Killing Games - Wikipedia</a></li>
<li><a href="https://www.stopkillinggames.com/en">Stop Killing Games — They Kill Games. We Fight Back.</a></li>
<li><a href="https://www.ign.com/articles/midnight-society-dr-disrepsect-game-studio-closes-cancels-game-deadrop">Midnight Society, Game Studio Co-Founded by Dr Disrespect, Closes Shop, Cancels Game - IGN</a></li>

</ul>
</details>

**Tags**: `#game preservation`, `#open source`, `#gaming industry`, `#software engineering`

---

<a id="item-20"></a>
## [Google's Electricity Consumption Soars Due to GenAI](https://www.pcgamer.com/software/ai/a-wild-testament-to-the-obscene-bloat-and-waste-of-genai-googles-electricity-consumption-is-exponentially-increasing/) ⭐️ 7.0/10

Google's electricity consumption has risen exponentially, surpassing the total annual power usage of entire countries like Slovakia, Ecuador, Ireland, and Nigeria, largely driven by the energy demands of generative AI (GenAI). This highlights the severe environmental cost of GenAI, raising urgent questions about sustainability and resource allocation in the tech industry as AI adoption accelerates. Training large GenAI models like GPT-4 is a major energy drain, and Google's power demand now exceeds that of several countries, underscoring the scale of the issue.

rss · PC Gamer · Jul 2, 12:15

**Background**: Generative AI (GenAI) is a type of artificial intelligence that creates new content such as text, images, or code. Training these models requires massive computational resources, leading to high electricity consumption. Google's growing use of GenAI services has significantly increased its energy footprint.

<details><summary>References</summary>
<ul>
<li><a href="https://www.pcgamer.com/software/ai/a-wild-testament-to-the-obscene-bloat-and-waste-of-genai-googles-electricity-consumption-is-exponentially-increasing/">'A wild testament to the obscene bloat and waste of GenAI ... | PC Gamer</a></li>
<li><a href="https://www.ohio.edu/news/2024/11/ais-increasing-energy-appetite">AI’s increasing energy appetite | OHIO Today</a></li>
<li><a href="https://en.wikipedia.org/wiki/Generative_AI">Generative AI - Wikipedia</a></li>

</ul>
</details>

**Tags**: `#GenAI`, `#energy consumption`, `#sustainability`, `#environmental impact`

---

<a id="item-21"></a>
## [Anthropic SDK Python v0.116.0 Adds Agent Memory Beta Header](https://github.com/anthropics/anthropic-sdk-python/releases/tag/v0.116.0) ⭐️ 6.0/10

Anthropic released version 0.116.0 of its Python SDK, which adds a beta header for the agent memory API, specifically 'agent-memory-2026-07-22'. This update allows developers to access the experimental agent memory feature, enabling agents to retain information across conversations, which is crucial for building more context-aware and persistent AI applications. The beta header is required to use the agent memory API, which is currently in beta and subject to change. The memory tool is generally available on Claude 4 and later models without a beta header, but the agent memory API for more advanced memory management requires this header.

github · stainless-app[bot] · Jul 2, 19:07

**Background**: Beta headers in the Anthropic API allow developers to access experimental features before they become part of the standard API. The agent memory API is designed to give AI agents persistent memory across sessions, improving their ability to handle long-running tasks and maintain context. This is part of Anthropic's broader effort to enhance agent capabilities, following the launch of Claude Skills in October 2025.

<details><summary>References</summary>
<ul>
<li><a href="https://platform.claude.com/docs/en/api/beta-headers">Beta headers - Claude Platform Docs</a></li>
<li><a href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool">Memory tool - Claude Platform Docs</a></li>
<li><a href="https://aiwiki.ai/wiki/anthropic_api">Anthropic API | AI Wiki</a></li>

</ul>
</details>

**Tags**: `#Anthropic`, `#SDK`, `#Python`, `#API`

---

<a id="item-22"></a>
## [Exapunks: A Retrospective on Zachtronics' Programming Puzzle Game](https://www.zachtronics.com/exapunks/) ⭐️ 6.0/10

A Hacker News post discusses the 2018 programming puzzle game Exapunks, highlighting its design and community appreciation, along with updates on the creator's new studio Coincidence Games and their latest game UVS Nirmana. Exapunks is a beloved title among programming puzzle enthusiasts, and the discussion reflects the lasting impact of Zachtronics' games on learning low-level programming concepts. The mention of the creator's new project shows continued innovation in the genre. Exapunks was released in early access on August 9, 2018, and fully launched on October 22, 2018. The game features a custom puzzle creation tool called Axiom VirtualNetwork+, which uses JavaScript to define hosts, files, and registers.

hackernews · yu3zhou4 · Jul 2, 18:41 · [Discussion](https://news.ycombinator.com/item?id=48765663)

**Background**: Exapunks is a programming puzzle game by Zachtronics, a studio known for engineering-focused puzzle games like TIS-100 and Shenzhen I/O. Players write assembly-like code to hack virtual networks, solving puzzles by controlling EXAs (executable agents). The game is set in a cyberpunk world where players read fictional zines for tutorials and lore.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Exapunks">Exapunks - Wikipedia</a></li>
<li><a href="https://www.zachtronics.com/exapunks/">EXAPUNKS - Zachtronics</a></li>
<li><a href="https://store.steampowered.com/app/716490/EXAPUNKS/">Save 50% on EXAPUNKS on Steam Exapunks - Wikipedia EXAPUNKS - Zachtronics EXAPUNKS by Zachtronics Steam Community :: Guide :: Dan's Exapunks Solutions -50% EXAPUNKS on GOG.com Exapunks Review - by Felix Roth - Corerunner</a></li>

</ul>
</details>

**Discussion**: Commenters praised Exapunks and Shenzhen I/O for capturing the fun of programming, with one noting the futility of pre-optimizing solutions. Another user shared that Exapunks and TIS-100 influenced their career by demystifying assembly language. A comment also pointed out that Zachtronics founder Zach Barth is now at Coincidence Games, which released UVS Nirmana, a spacecraft engineering puzzle game.

**Tags**: `#gaming`, `#programming`, `#puzzle`, `#zachtronics`

---

<a id="item-23"></a>
## [AI Moves from Chatbots to Critical Industrial Infrastructure](https://www.technologyreview.com/2026/07/02/1138433/teaching-ai-to-run-with-the-turbines/) ⭐️ 6.0/10

An article from MIT Technology Review highlights that AI is increasingly deployed in industrial settings for operational continuity and safety, moving beyond consumer applications like chatbots and image generators. This shift demonstrates AI's growing role in critical infrastructure, where failures can have severe consequences, and signals a maturation of AI beyond hype into high-stakes operational technology. The article discusses how AI is becoming a core operating layer in industries with sprawling physical systems, but does not provide specific technical details or case studies.

rss · MIT Technology Review · Jul 2, 12:51

**Background**: Operational technology (OT) refers to hardware and software that monitors and controls physical devices and processes in industries like energy, manufacturing, and transportation. AI integration into OT aims to improve efficiency, predictive maintenance, and safety, but also introduces new cybersecurity challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/02/1140045/achieving-operational-excellence-with-ai/">Achieving operational excellence with AI - MIT Technology Review</a></li>
<li><a href="https://blogs.nvidia.com/blog/ai-cybersecurity-operational-technology-industrial-control-systems/">NVIDIA Brings AI-Powered Cybersecurity to World’s Critical Infrastructure | NVIDIA Blog</a></li>

</ul>
</details>

**Tags**: `#AI`, `#industrial AI`, `#infrastructure`, `#operational technology`

---

<a id="item-24"></a>
## [Startup Springboards Tackles AI Groupthink with Flint LLM](https://www.technologyreview.com/2026/07/02/1140027/the-download-ai-groupthink-llms/) ⭐️ 6.0/10

Australian startup Springboards has developed an LLM called Flint, trained to produce more diverse responses to open-ended questions, addressing the groupthink problem where major LLMs like ChatGPT, Claude, and Gemini give strikingly similar answers. This matters because AI groupthink limits creativity and usefulness in applications like brainstorming, travel planning, and creative writing, and a solution could restore output diversity and user trust in LLMs. Flint was specifically trained to generate a wider variety of responses to open-ended prompts such as 'Where should I go in Europe?' and 'Give me a random number between 1 and 10,' where mainstream LLMs often default to the same answer (e.g., '7').

rss · MIT Technology Review · Jul 2, 12:10

**Background**: Large language models (LLMs) like GPT-4, Claude, and Gemini are trained on vast internet data, which can lead to convergence in responses due to common training data and reinforcement learning from human feedback (RLHF). This 'groupthink' effect reduces output diversity, especially for open-ended questions. The startup Springboards aims to break this pattern by training Flint to prioritize variety.

<details><summary>References</summary>
<ul>
<li><a href="https://www.technologyreview.com/2026/07/01/1140003/llms-are-stuck-in-a-groupthink-rut-this-startup-is-trying-to-get-them-out/">LLMs are stuck in a groupthink groove. This startup is trying ...</a></li>

</ul>
</details>

**Tags**: `#AI`, `#LLMs`, `#startup`, `#groupthink`

---

<a id="item-25"></a>
## [Analysts Predict Rising PPA Prices as Clean Energy Tax Credits Expire](https://www.utilitydive.com/news/rising-ppa-prices-anticipated-as-clean-energy-tax-credits-phase-out/824386/) ⭐️ 6.0/10

Analysts expect power purchase agreement (PPA) prices to rise as clean energy tax credits phase out, according to a report from Utility Dive. Josh Price of Crux noted that the missing tax credit revenue will likely be compensated through higher PPA prices. This shift could increase costs for corporate and utility buyers of renewable energy, potentially slowing clean energy adoption. It highlights the economic impact of policy changes on the renewable energy market. The phase-out includes the Clean Electricity Investment Credit replacing the Energy Investment Tax Credit after 2024, with residential credits beginning to phase out in 2033. PPAs are long-term contracts typically lasting 10-25 years between generators and customers.

rss · Utility Dive · Jul 2, 17:17

**Background**: A power purchase agreement (PPA) is a long-term contract between an electricity generator and a customer, such as a utility or company, to buy energy at a pre-negotiated price. Clean energy tax credits, like the Investment Tax Credit, have historically reduced project costs, and their phase-out removes this financial incentive, potentially raising PPA prices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Power_purchase_agreement">Power purchase agreement - Wikipedia</a></li>
<li><a href="https://www.irs.gov/credits-deductions/residential-clean-energy-credit">Residential Clean Energy Credit | Internal Revenue Service</a></li>

</ul>
</details>

**Tags**: `#clean energy`, `#PPA`, `#tax credits`, `#renewable energy`

---

<a id="item-26"></a>
## [Union Workers Launch Hardship Fund for Laid-Off Game Devs](https://www.gamedeveloper.com/business/union-workers-establish-hardship-fund-to-support-devs-impacted-by-layoffs) ⭐️ 6.0/10

Union workers have established a hardship fund that offers up to $5,000 for game developers affected by layoffs in the United States and Canada. This initiative provides direct financial relief to game developers facing job loss, addressing a critical need in an industry hit by widespread layoffs. The fund is available to game developers in the US and Canada, with each eligible individual able to request up to $5,000.

rss · Game Developer (Gamasutra) · Jul 2, 10:20

**Background**: The game development industry has experienced significant layoffs in recent years, leaving many workers without financial support. Union-organized hardship funds are a common way to provide emergency aid to members during crises.

**Tags**: `#game development`, `#layoffs`, `#union`, `#hardship fund`

---