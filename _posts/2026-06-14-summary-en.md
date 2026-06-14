---
layout: default
title: "Horizon Summary: 2026-06-14 (EN)"
date: 2026-06-14
lang: en
---

> From 36 items, 10 important content pieces were selected

---

1. [Rio's homegrown LLM found to be a merge of existing models](#item-1) ⭐️ 8.0/10
2. [Jane Street on Formal Methods and AI Code Verification](#item-2) ⭐️ 8.0/10
3. [2014 Talk Predicted JavaScript's Rise and Fall](#item-3) ⭐️ 8.0/10
4. [Kage: Archive websites into a single offline binary](#item-4) ⭐️ 7.0/10
5. [AI Adoption Not as Widespread as Hype Suggests](#item-5) ⭐️ 7.0/10
6. [FBI Builds Fake Town for Cyberattack Training](#item-6) ⭐️ 7.0/10
7. [China may have accessed Anthropic's Mythos AI model](#item-7) ⭐️ 7.0/10
8. [Zeroserve Boosts Caddy Compatibility with 3x Throughput](#item-8) ⭐️ 6.0/10
9. [Paul Graham on Building Billion-Dollar Startups](#item-9) ⭐️ 6.0/10
10. [Veteran Dev: Theme Park MMOs No Longer Viable](#item-10) ⭐️ 6.0/10

---

<a id="item-1"></a>
## [Rio's homegrown LLM found to be a merge of existing models](https://github.com/nex-agi/Nex-N2/issues/4) ⭐️ 8.0/10

An investigation reveals that Rio de Janeiro's claimed homegrown LLM, Rio-3.5-Open-397B, is actually a weighted merge of approximately 60% Nex-N2 Pro and 40% Qwen3.5-397B-A17B, with no evidence of additional training. This raises serious concerns about transparency and attribution in AI development, as a city government presented a merged model as a homegrown innovation, potentially misleading the public and the AI community. Weight tensor analysis showed that every weight tensor in Rio's model is, to thousands of standard deviations, the same 0.6/0.4 blend of Nex and Qwen across all 60 layers and components, a pattern not seen in typical fine-tunes.

hackernews · unrvl22 · Jun 14, 15:37 · [Discussion](https://news.ycombinator.com/item?id=48528371)

**Background**: Model merging is a technique that combines the weights of multiple trained models into a single model without additional training, often using linear interpolation. It has become a mainstream approach in LLM development, but proper attribution of base models is expected in open-source practices.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/arcee-ai/mergekit">GitHub - arcee-ai/mergekit: Tools for merging pretrained large language ...</a></li>
<li><a href="https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/">An Introduction to Model Merging for LLMs - NVIDIA Developer</a></li>

</ul>
</details>

**Discussion**: The community is divided: some defend the developers, suggesting the uploaded model may have lacked distillation steps, while others criticize the lack of attribution. One commenter noted the robustness of deep learning models where a simple linear combination can enhance performance.

**Tags**: `#LLM`, `#AI ethics`, `#model merging`, `#open source`, `#transparency`

---

<a id="item-2"></a>
## [Jane Street on Formal Methods and AI Code Verification](https://blog.janestreet.com/formal-methods-at-jane-street-index/?from_theconsensus=1) ⭐️ 8.0/10

Jane Street published a blog post discussing the practical use of formal methods in programming and their potential to verify AI-generated code, sparking a community discussion with 165 points and 52 comments. As AI generates more code, formal methods could shift human value from writing code to verifying it, improving reliability and safety in software engineering. The post highlights that formal methods have evolved from early theorem provers like Boyer-Moore to modern type systems in Scala 3, and that they can help prevent issues like 'noun accretion' in AI-generated code.

hackernews · eatonphil · Jun 14, 12:35 · [Discussion](https://news.ycombinator.com/item?id=48526633)

**Background**: Formal methods are mathematically rigorous techniques for specifying and verifying software and hardware systems. They include theorem proving, model checking, and type systems. Historically, they required significant human effort to guide proofs, but modern tools and AI are making them more practical.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Formal_methods">Formal methods - Wikipedia</a></li>
<li><a href="https://web.mit.edu/16.35/www/lecturenotes/FormalMethods.pdf">Introducing Formal Methods - MIT</a></li>
<li><a href="https://formal.epfl.ch/">Formal Methods Portal</a></li>

</ul>
</details>

**Discussion**: Commenters shared diverse perspectives: some recalled early proof automation with SAT solvers, others praised expressive types in Scala 3 for compile-time proofs, and a few questioned whether formal specs are just 'tests written differently' and can suffer from the same bugs.

**Tags**: `#formal methods`, `#programming`, `#verification`, `#AI`, `#software engineering`

---

<a id="item-3"></a>
## [2014 Talk Predicted JavaScript's Rise and Fall](https://www.destroyallsoftware.com/talks/the-birth-and-death-of-javascript) ⭐️ 8.0/10

A 2014 talk by Gary Bernhardt humorously predicted JavaScript's dominance as a compilation target and its eventual replacement, which has proven prescient with the rise of WebAssembly and TypeScript. The talk's accurate foresight about JavaScript's evolution and the emergence of compilation targets like WebAssembly remains highly relevant, influencing how developers think about the future of web technologies. The talk specifically mentioned asm.js as a compilation target, which was later deprecated in favor of WebAssembly, and correctly anticipated that JavaScript would become a universal intermediate language.

hackernews · subset · Jun 14, 12:38 · [Discussion](https://news.ycombinator.com/item?id=48526661)

**Background**: A compilation target is a language that other languages are compiled into, such as machine code or bytecode. JavaScript, originally a scripting language for browsers, has become a popular compilation target for languages like TypeScript and C++ via WebAssembly.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebAssembly">WebAssembly</a></li>
<li><a href="https://softwareengineering.stackexchange.com/questions/344599/what-exactly-is-a-compile-target">compiler - What exactly is a compile target? - Software ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Compiler">Compiler - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters noted the talk's eerie accuracy, with one joking that it predicted a global disaster between 2020-2025 but got the type wrong. Others discussed WebAssembly's limitations, such as lack of DOM access, and the continued reliance on JavaScript as glue code.

**Tags**: `#JavaScript`, `#WebAssembly`, `#compilation target`, `#programming languages`, `#tech talk`

---

<a id="item-4"></a>
## [Kage: Archive websites into a single offline binary](https://github.com/tamnd/kage) ⭐️ 7.0/10

Kage is a new open-source tool that clones any website into a folder for offline browsing, stripping all scripts, and can optionally glue the archive onto a copy of itself to produce a single executable that serves the site offline. This tool simplifies offline access to websites, making it easy to distribute entire sites as a single binary without dependencies, which is especially useful for documentation, wikis, or any content needed in areas without internet connectivity. The tool uses the `--format binary` flag to create a single executable that bundles the archived site with a built-in server; the resulting binary can be run with `kage serve` to serve the static content.

hackernews · tamnd · Jun 14, 17:25 · [Discussion](https://news.ycombinator.com/item?id=48529990)

**Background**: Website archiving tools like HTTrack and SingleFile have long existed, but they typically produce folders or single HTML files. Kage's approach of packaging an entire site into a single binary with a built-in server is novel, leveraging Go's ability to create standalone executables.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/tamnd/kage">GitHub - tamnd/ kage : Shadow any website for offline viewing, with the...</a></li>

</ul>
</details>

**Discussion**: Commenters noted the tool's potential for offline wikis and documentation, but some questioned the need for a server when a static HTML file could suffice, and others pointed to alternatives like SingleFile or HTTrack as more robust for certain use cases.

**Tags**: `#offline`, `#archiving`, `#static-site`, `#tool`, `#open-source`

---

<a id="item-5"></a>
## [AI Adoption Not as Widespread as Hype Suggests](https://gabrielweinberg.com/p/people-are-consuming-ai-like-they) ⭐️ 7.0/10

Gabriel Weinberg argues that despite the AI hype, a significant portion of people use AI infrequently, and true adoption will come from embedding AI into existing software rather than standalone chat interfaces. This challenges the prevailing narrative that everyone is using AI, highlighting a gap between perception and reality that could affect investment and product strategy in the AI industry. The article cites a study showing over 50% of people use AI less than once per week, and suggests that AI adoption will grow through integration into existing tools rather than through dedicated chat interfaces.

hackernews · yegg · Jun 14, 14:44 · [Discussion](https://news.ycombinator.com/item?id=48527700)

**Background**: Since the launch of ChatGPT in late 2022, there has been widespread media coverage suggesting that AI is being adopted rapidly across all sectors. However, actual usage data shows a more nuanced picture, with many people trying AI but not incorporating it into their daily routines.

**Discussion**: Commenters discuss the challenges of answering AI usage questions in job interviews, with some noting that AI code generation still requires significant human oversight. Others agree that embedding AI into existing software is the key to broader adoption, while a few report not using AI at all.

**Tags**: `#AI adoption`, `#LLMs`, `#software engineering`, `#technology trends`, `#community discussion`

---

<a id="item-6"></a>
## [FBI Builds Fake Town for Cyberattack Training](https://www.theverge.com/tech/949648/fbi-fake-town-cyberattacks-kinetic-cyber-range) ⭐️ 7.0/10

The FBI opened a 22,000-square-foot Cyber Range in Huntsville, Alabama, that physically replicates a small town with buildings like a convenience store, gas station, and hospital to simulate cyberattacks for training. This facility provides a unique, immersive environment for FBI agents to practice responding to cyber threats in realistic settings, bridging the gap between digital and physical security training. The range, called the Kinetic Cyber Range, is located on the FBI's North Campus at Redstone Arsenal and is operated by the Bureau's Operational Technology Division.

rss · The Verge · Jun 14, 20:35

**Background**: The FBI has long used physical mock towns like Hogan's Alley for tactical training. The Kinetic Cyber Range extends this concept to cybersecurity, allowing agents to train on cyberattacks that affect physical infrastructure.

<details><summary>References</summary>
<ul>
<li><a href="https://www.fbi.gov/news/stories/inside-the-fbis-kinetic-cyber-range">Inside the FBI's Kinetic Cyber Range — FBI</a></li>
<li><a href="https://www.hstoday.us/subject-matter-areas/law-enforcement-and-public-safety/inside-the-fbis-massive-kinetic-cyber-range-in-huntsville/">Inside the FBI's Massive Kinetic Cyber Range in Huntsville</a></li>

</ul>
</details>

**Tags**: `#cybersecurity`, `#FBI`, `#training`, `#simulation`

---

<a id="item-7"></a>
## [China may have accessed Anthropic's Mythos AI model](https://www.theverge.com/ai-artificial-intelligence/949644/china-white-house-anthropic-mythos) ⭐️ 7.0/10

A Semafor report indicates that the White House's decision to impose export restrictions on Anthropic's Mythos AI model was partly due to fears that a China-linked group had accessed it. If confirmed, this access could give China advanced AI capabilities, posing serious national security risks and accelerating the AI arms race between the US and China. The report specifically mentions Mythos 5 or Fable 5, which are Anthropic's most advanced models; Fable 5 is a safety-tuned version of Mythos 5, while Mythos 5 is restricted to limited release through Project Glasswing.

rss · The Verge · Jun 14, 18:27

**Background**: Anthropic is an AI safety company that develops large language models like Claude. Mythos is their most powerful model, considered too dangerous for public release due to its advanced capabilities in cybersecurity and other sensitive domains. Export restrictions aim to prevent adversaries from obtaining such technology.

<details><summary>References</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-fable-5-mythos-5">Claude Fable 5 and Claude Mythos 5 \ Anthropic</a></li>
<li><a href="https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5">Introducing Claude Fable 5 and Claude Mythos 5 - Claude API Docs</a></li>

</ul>
</details>

**Tags**: `#AI`, `#national security`, `#export controls`, `#Anthropic`

---

<a id="item-8"></a>
## [Zeroserve Boosts Caddy Compatibility with 3x Throughput](https://su3.io/posts/zeroserve-caddy-compat) ⭐️ 6.0/10

Zeroserve, an io_uring-based HTTPS server, now claims Caddy compatibility, achieving 3x throughput and 70% lower latency compared to standard Caddy. This performance leap could attract users seeking high-speed web serving, but the lack of ACME and plugin support limits its practical adoption for production environments. The compatibility is partial: zeroserve can compile and serve a Caddy config, but it does not support ACME automatic HTTPS or Caddy plugins, which are core features for many users.

hackernews · losfair · Jun 14, 13:43 · [Discussion](https://news.ycombinator.com/item?id=48527145)

**Background**: Caddy is a popular web server known for its automatic HTTPS via ACME and extensive plugin ecosystem. Zeroserve is a newer, high-performance server built on Linux's io_uring asynchronous I/O interface, aiming for zero-configuration and eBPF scripting. io_uring provides low-overhead, zero-copy I/O operations, which can significantly boost throughput and reduce latency.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/losfair/zeroserve">GitHub - losfair/zeroserve: Zero-config, fast `io_uring`-based HTTPS server. · GitHub</a></li>
<li><a href="https://su3.io/posts/introducing-zeroserve">zeroserve: a zero-config web server you can script with eBPF</a></li>
<li><a href="https://en.wikipedia.org/wiki/Io_uring">io_uring - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some users find the missing ACME and plugin support a dealbreaker, while others are impressed by the performance numbers. There is also a technical discussion about the safety of using io_uring for web servers, with concerns about cybersecurity.

**Tags**: `#web server`, `#performance`, `#Caddy`, `#io_uring`, `#Rust`

---

<a id="item-9"></a>
## [Paul Graham on Building Billion-Dollar Startups](https://paulgraham.com/earn.html) ⭐️ 6.0/10

Paul Graham published an essay titled 'How to earn a billion dollars' outlining strategies for building billion-dollar startups, emphasizing creating and capturing value. This essay provides a framework for wealth creation that could influence aspiring entrepreneurs and investors, sparking debate on the ethics of extreme wealth accumulation. The essay argues that billion-dollar fortunes come from creating new value rather than extracting it, but critics in the comments dispute this, citing examples like Uber's disruption of taxi drivers.

hackernews · kingstoned · Jun 14, 11:50 · [Discussion](https://news.ycombinator.com/item?id=48526360)

**Background**: Paul Graham is a well-known venture capitalist and co-founder of Y Combinator, a startup accelerator. His essays on startups and entrepreneurship are widely read in the tech community.

**Discussion**: Comments are mixed: some praise the essay's insights, while others criticize it as justifying wealth extraction and ignoring negative externalities like creative destruction.

**Tags**: `#startups`, `#wealth`, `#entrepreneurship`, `#Paul Graham`

---

<a id="item-10"></a>
## [Veteran Dev: Theme Park MMOs No Longer Viable](https://www.pcgamer.com/games/mmo/ultima-online-and-star-wars-galaxies-vet-tells-me-the-theme-park-assembly-line-mmo-just-isnt-viable-anymore-especially-as-dev-costs-spike-we-hit-the-wall/) ⭐️ 6.0/10

A veteran developer of Ultima Online and Star Wars Galaxies argues that traditional theme park MMOs are no longer viable due to soaring development costs and player dissatisfaction with monetization. This commentary highlights a critical shift in the MMO industry, where rising costs and changing player expectations are making the classic theme park model unsustainable, potentially influencing future game design and business strategies. The developer notes that the MMO audience feels 'underserved and overmonetized,' and that the industry has 'hit the wall' with the theme park assembly-line approach. Development costs for MMOs have skyrocketed, with examples like Amazon's New World costing hundreds of millions.

rss · PC Gamer · Jun 14, 15:00

**Background**: Theme park MMOs are games that guide players through a series of predefined attractions or quests, similar to a real-world theme park. This contrasts with sandbox MMOs, which offer more freedom and emergent gameplay. The genre has faced increasing development costs and competition from other entertainment forms.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/amazon-axes-mmos-pivots-to-ai-party-games-in-gaming-shakeup">Amazon axes MMOs, pivots to AI party games in... | The Tech Buzz</a></li>
<li><a href="https://forums.mmorpg.com/discussion/315163/sandbox-vs-theme-park-style-mmos">Sandbox vs Theme Park style MMOs — MMORPG.com Forums</a></li>

</ul>
</details>

**Tags**: `#MMO`, `#game development`, `#industry trends`, `#monetization`

---