<!-- DO NOT EDIT - this file is auto-generated. See CONTRIBUTING.md to add a benchmark. -->
# Awesome Agent Benchmarks

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![@BerkeleyRDI](https://img.shields.io/badge/@BerkeleyRDI-black?logo=x&logoColor=white)](https://x.com/BerkeleyRDI)
[![Discord](https://img.shields.io/discord/1280234300012494859?label=&logo=discord&logoColor=ffffff&color=5865F2&labelColor=4a5568)](https://discord.gg/uqZUta3MYa)

A curated list of agent benchmarks and evaluation frameworks.

## Table of Contents

- [Coding](#coding) (9)
- [Computer Use](#computer-use) (14)
- [Deep Research](#deep-research) (6)
- [Embodied](#embodied) (4)
- [General Capabilities](#general-capabilities) (17)
- [Memory](#memory) (7)
- [Safety](#safety) (6)
- [Scientific Research](#scientific-research) (3)
- [Security](#security) (8)
- [Web](#web) (12)

---

## Coding

- **Commit0** *(Dec 2024)* 📄 29 ⭐ 187\
  [Paper](https://arxiv.org/abs/2412.01769) · [Github](https://github.com/commit-0/commit0) · [Website](https://commit-0.github.io/)
  > Evaluates AI agents on writing complete software libraries from scratch given specification documents and interactive unit test suites.
- **LoCoBench-Agent** *(Nov 2025)* 📄 6 ⭐ 19\
  [Paper](https://arxiv.org/abs/2511.13998) · [Github](https://github.com/SalesforceAIResearch/LoCoBench-Agent)
  > Evaluates LLM agents in realistic long-context software engineering workflows, testing multi-turn conversations, tool usage efficiency, error recovery, and architectural consistency across context lengths from 10K to 1M tokens.
- **MLE-bench** *(Oct 2024)* 📄 194 ⭐ 1.5k\
  [Paper](https://arxiv.org/abs/2410.07095) · [Github](https://github.com/openai/mle-bench) · [Website](https://www.mlebench.com/)
  > Measures agents on machine learning engineering using 75 competitions from Kaggle, testing skills including model training, dataset preparation, and experiment execution.
- 🆕 **ProjDevBench** *(Feb 2026)* 📄 4 ⭐ 15\
  [Paper](https://arxiv.org/abs/2602.01655) · [Github](https://github.com/zsworld6/projdevbench)
  > Evaluates coding agents on end-to-end project development across 20 programming problems in 8 categories, assessing system architecture design, functional correctness, and iterative solution refinement.
- **SciCode** *(Jul 2024)* 📄 100 ⭐ 188\
  [Paper](https://arxiv.org/abs/2407.13168) · [Github](https://github.com/scicode-bench/SciCode)
  > Evaluates agents on generating code to solve 80 real scientific research problems decomposed into 338 subproblems across 16 natural science fields including math, physics, chemistry, biology, and materials science.
- **SWE-bench** *(Oct 2023)* 📄 1.9k ⭐ 4.7k\
  [Paper](https://arxiv.org/abs/2310.06770) · [Github](https://github.com/SWE-bench/SWE-bench) · [Website](https://www.swebench.com)
  > Evaluates agents' ability to resolve real GitHub issues by editing codebases, drawn from 2,294 issues across 12 Python repositories.
- **SWE-EVO** *(Dec 2025)* 📄 9\
  [Paper](https://arxiv.org/abs/2512.18470)
  > Evaluates coding agents on 48 long-horizon software evolution tasks requiring multi-step modifications spanning an average of 21 files, drawn from version histories of 7 mature open-source Python projects.
- **SWE-rebench** *(May 2025)* 📄 50\
  [Paper](https://arxiv.org/abs/2505.20411) · [Website](https://swe-rebench.com)
  > A continuously refreshed benchmark of 21,000+ interactive Python-based software engineering tasks extracted from GitHub repositories, designed to prevent evaluation contamination.
- **USACO** *(Apr 2024)* 📄 67 ⭐ 123\
  [Paper](https://arxiv.org/abs/2404.10952) · [Github](https://github.com/princeton-nlp/USACO) · [Website](https://princeton-nlp.github.io/USACOBench/)
  > Evaluates agents on 307 competitive programming problems from the USA Computing Olympiad, requiring complex algorithmic reasoning, puzzle solving, and efficient code generation.

## Computer Use

- **AndroidWorld** *(May 2024)* 📄 260 ⭐ 729\
  [Paper](https://arxiv.org/abs/2405.14573) · [Github](https://github.com/google-research/android_world)
  > A dynamic benchmarking environment for autonomous agents on 116 programmatic tasks across 20 real-world Android apps, with tasks parameterized and expressed in natural language.
- **CRAB** *(Jul 2024)* 📄 34 ⭐ 416\
  [Paper](https://arxiv.org/abs/2407.01511) · [Github](https://github.com/camel-ai/crab) · [Website](https://crab.camel-ai.org/)
  > Evaluates multimodal agents on 120 tasks across computer desktop and mobile phone environments using a graph-based fine-grained evaluation method.
- **MobileWorld** *(Dec 2025)* 📄 17\
  [Paper](https://arxiv.org/abs/2512.19432)
  > Evaluates autonomous mobile agents on 201 tasks across 20 applications in agent-user interactive and MCP-augmented environments, emphasizing long-horizon cross-application workflows.
- **OmniACT** *(Feb 2024)* 📄 133\
  [Paper](https://arxiv.org/abs/2402.17553) · [Dataset](https://huggingface.co/datasets/Writer/omniact)
  > Evaluates agents on generating executable programs to complete computer tasks across desktop and web applications, using both text and visual UI understanding.
- **OSUniverse** *(May 2025)* 📄 7 ⭐ 24\
  [Paper](https://arxiv.org/abs/2505.03570) · [Github](https://github.com/agentsea/osuniverse) · [Website](https://agentsea.github.io/osuniverse/)
  > Evaluates agents on complex multimodal desktop tasks of increasing difficulty, from basic UI interactions to multistep workflows requiring spatial reasoning and dexterity.
- **OSWorld** *(Apr 2024)* 📄 576 ⭐ 2.8k\
  [Paper](https://arxiv.org/abs/2404.07972) · [Github](https://github.com/xlang-ai/OSWorld) · [Website](https://os-world.github.io)
  > Evaluates multimodal agents on 369 real-world computer tasks across OS, web, and desktop apps.
- **OSWorld-MCP** *(Oct 2025)* 📄 8 ⭐ 222\
  [Paper](https://arxiv.org/abs/2510.24563) · [Github](https://github.com/X-PLUG/OSWorld-MCP) · [Website](https://osworld-mcp.github.io)
  > Evaluates computer-use agents on 158 tasks combining MCP tool invocation and GUI operations across 7 common applications in a real-world environment.
- **SCUBA** *(Sep 2025)* 📄 4 ⭐ 8\
  [Paper](https://arxiv.org/abs/2509.26506) · [Github](https://github.com/SalesforceAIResearch/SCUBA) · [Website](https://sfrcua.github.io/SCUBA/)
  > Evaluates computer-use agents on CRM workflows within Salesforce across 300 tasks spanning three personas - platform administrators, sales representatives, and service agents.
- **Spider2-V** *(Jul 2024)* 📄 49 ⭐ 151\
  [Paper](https://arxiv.org/abs/2407.10956) · [Github](https://github.com/xlang-ai/Spider2-V) · [Website](https://spider2-v.github.io)
  > Evaluates multimodal agents on 494 real-world data science and engineering tasks across 20 enterprise applications, requiring SQL queries, Python code, and GUI operations.
- **Terminal-Bench 1.0** ⭐ 2.0k\
  [Github](https://github.com/harbor-framework/terminal-bench) · [Website](https://www.tbench.ai)
  > Evaluates agents' ability to use a computer terminal on ~100 tasks.
- **Terminal-Bench 2.0** *(Jan 2026)* 📄 57 ⭐ 188\
  [Paper](https://arxiv.org/abs/2601.11868) · [Github](https://github.com/harbor-framework/terminal-bench-2) · [Website](https://www.tbench.ai) · [Agentbeats](https://agentbeats.dev/jngan00/terminal-bench-2-0-green-agent)
  > Curated hard benchmark of 89 tasks in computer terminal environments, spanning software engineering, ML, security, and data science.
- **UI-CUBE** *(Nov 2025)* 📄 2\
  [Paper](https://arxiv.org/abs/2511.17131) · [Github](https://github.com/UiPath/uipath_enterprise_benchmark) · [Website](https://www.uipath.com/ai/research/ui-cube-benchmark)
  > Evaluates enterprise computer use agents on 226 tasks spanning simple UI interactions and complex workflows in enterprise applications, with multi-resolution testing and automated validation.
- **WorkArena** *(Mar 2024)* 📄 177 ⭐ 244\
  [Paper](https://arxiv.org/abs/2403.07718) · [Github](https://github.com/ServiceNow/WorkArena) · [Website](https://servicenow.github.io/WorkArena/)
  > Evaluates agents on 33 knowledge worker tasks using the ServiceNow enterprise platform, measuring ability to handle realistic workplace software workflows.
- **WorkArena++** *(Jul 2024)* 📄 45 ⭐ 244\
  [Paper](https://arxiv.org/abs/2407.05291) · [Github](https://github.com/ServiceNow/WorkArena) · [Website](https://www.servicenow.com/research/publication/leo-boisvert-work-neurips-datasets2024.html)
  > Evaluates LLMs and vision-language models on 682 realistic enterprise workflow tasks requiring planning, problem-solving, logical reasoning, retrieval, and contextual understanding within ServiceNow.

## Deep Research

- **BrowseComp-Plus** *(Aug 2025)* 📄 84 ⭐ 247\
  [Paper](https://arxiv.org/abs/2508.06600) · [Github](https://github.com/texttron/BrowseComp-Plus) · [Website](https://texttron.github.io/BrowseComp-Plus/)
  > Evaluates deep-research agents using a fixed curated document corpus, enabling controlled experiments on retrieval methods, citation accuracy, and context engineering.
- **DeepResearch Bench** *(Jun 2025)* 📄 119 ⭐ 685\
  [Paper](https://arxiv.org/abs/2506.11763) · [Github](https://github.com/Ayanami0730/deep_research_bench) · [Website](https://deepresearch-bench.github.io/)
  > Evaluates deep research agents on 100 PhD-level research tasks across 22 fields crafted by domain experts, assessing report quality and information retrieval effectiveness.
- **DeepScholar-Bench** *(Aug 2025)* 📄 15 ⭐ 236\
  [Paper](https://arxiv.org/abs/2508.20033) · [Github](https://github.com/guestrin-lab/deepscholar-bench) · [Website](https://sky.cs.berkeley.edu/project/deepscholar-bench/)
  > A live benchmark for generative research synthesis evaluating systems that retrieve from the live web and produce long-form cited reports, assessed on knowledge synthesis, retrieval quality, and verifiability.
- **MMDeepResearch-Bench** *(Jan 2026)* 📄 5 ⭐ 26\
  [Paper](https://arxiv.org/abs/2601.12346) · [Github](https://github.com/AIoT-MLSys-Lab/MMDeepResearch-Bench) · [Website](https://mmdeepresearch-bench.github.io/)
  > Evaluates multimodal deep research agents on 140 expert-crafted tasks across 21 domains, assessing citation-rich report synthesis where models must connect visual artifacts to sourced claims.
- **PaperArena** *(Oct 2025)* 📄 5 ⭐ 14\
  [Paper](https://arxiv.org/abs/2510.10909) · [Github](https://github.com/Melmaphother/PaperArena) · [Website](https://paperarena-ai.github.io/)
  > Evaluates LLM-based agents on questions requiring multi-paper information integration using external tools, with agents achieving only 38.78% average accuracy.
- **WideSearch** *(Aug 2025)* 📄 33 ⭐ 132\
  [Paper](https://arxiv.org/abs/2508.07999) · [Github](https://github.com/ByteDance-Seed/WideSearch) · [Website](https://widesearch-seed.github.io)
  > Evaluates agent reliability on large-scale information collection through 200 manually curated questions across 15+ domains requiring agents to gather and organize atomic verifiable information.

## Embodied

- **ALFWorld** *(Oct 2020)* 📄 775 ⭐ 717\
  [Paper](https://arxiv.org/abs/2010.03768) · [Github](https://github.com/alfworld/alfworld) · [Website](https://alfworld.github.io)
  > A benchmark and simulator bridging abstract text-based planning with embodied visual task execution, enabling agents to learn policies in TextWorld and transfer them to ALFRED visual environments.
- **BEHAVIOR-1K** *(Mar 2024)* 📄 119 ⭐ 1.4k\
  [Paper](https://arxiv.org/abs/2403.09227) · [Github](https://github.com/StanfordVL/BEHAVIOR-1K) · [Website](https://behavior.stanford.edu)
  > A comprehensive simulation benchmark for human-centered robotics agents covering 1,000 everyday activities across 50 realistic scenes with over 9,000 annotated objects.
- **MineAnyBuild** *(May 2025)* 📄 1 ⭐ 13\
  [Paper](https://arxiv.org/abs/2505.20148) · [Github](https://github.com/MineAnyBuild/MineAnyBuild)
  > Evaluates agents on spatial planning in Minecraft across 4,000 curated tasks covering spatial understanding, reasoning, creativity, and commonsense, requiring generation of executable architecture building plans.
- **Robotouille** *(Feb 2025)* 📄 23 ⭐ 40\
  [Paper](https://arxiv.org/abs/2502.05227) · [Github](https://github.com/portal-cornell/robotouille) · [Website](https://portal.cs.cornell.edu/robotouille/)
  > Evaluates LLM agents on long-horizon asynchronous kitchen planning scenarios, testing their capacity to manage overlapping tasks, interruptions, and parallel execution.

## General Capabilities

- **AgencyBench** *(Jan 2026)* 📄 7 ⭐ 75\
  [Paper](https://arxiv.org/abs/2601.11044) · [Github](https://github.com/GAIR-NLP/AgencyBench) · [Website](https://agencybench.opensii.ai/)
  > Evaluates autonomous agents on 6 core agentic capabilities across 32 real-world scenarios comprising 138 tasks, each requiring approximately 90 tool calls and 1 million tokens.
- **API-Bank** *(Apr 2023)* 📄 389\
  [Paper](https://arxiv.org/abs/2304.08244) · [Github](https://github.com/AlibabaResearch/DAMO-ConvAI/tree/main/api-bank)
  > Evaluates LLMs on planning, retrieving, and calling APIs across 73 tools and 314 annotated tool-use dialogues containing 753 API calls.
- **AppWorld** *(Jul 2024)* 📄 136 ⭐ 407\
  [Paper](https://arxiv.org/abs/2407.18901) · [Github](https://github.com/StonyBrookNLP/appworld) · [Website](https://appworld.dev/)
  > Evaluates autonomous agents on 750 tasks requiring rich interactive code generation across 9 everyday applications accessible through 457 APIs, testing multi-app coordination and avoidance of unintended side effects.
- **CRMArena** *(Nov 2024)* 📄 40 ⭐ 136\
  [Paper](https://arxiv.org/abs/2411.02305) · [Github](https://github.com/SalesforceAIResearch/CRMArena)
  > Evaluates AI agents on realistic customer service tasks across 9 task types and 3 personas using 16 industrial CRM objects with interconnected data simulating enterprise environments.
- 🆕 **DeepPlanning** *(Jan 2026)* 📄 7\
  [Paper](https://arxiv.org/abs/2601.18137) · [Website](https://qwenlm.github.io/Qwen-Agent/en/benchmarks/deepplanning/)
  > Evaluates LLM agents on long-horizon planning through multi-day travel planning and shopping tasks requiring proactive information acquisition, local constrained reasoning, and global constrained optimization.
- **GAIA** *(Nov 2023)* 📄 669\
  [Paper](https://arxiv.org/abs/2311.12983) · [Website](https://huggingface.co/gaia-benchmark)
  > Evaluates general AI assistants on 466 real-world questions requiring reasoning, multi-modality handling, web browsing, and tool-use proficiency, with humans scoring 92% vs. 15% for GPT-4 with plugins.
- **Gaia2** *(Sep 2025)* 📄 14 ⭐ 478\
  [Paper](https://arxiv.org/abs/2509.17158) · [Github](https://github.com/facebookresearch/meta-agents-research-environments) · [Website](https://facebookresearch.github.io/meta-agents-research-environments/)
  > Measures general agent capabilities in dynamic, asynchronous environments requiring agents to handle ambiguities, adapt to noise, collaborate with other agents, and operate under temporal constraints.
- **GTA** *(Jul 2024)* 📄 65 ⭐ 141\
  [Paper](https://arxiv.org/abs/2407.08713) · [Github](https://github.com/open-compass/GTA) · [Website](https://open-compass.github.io/GTA/)
  > Evaluates LLMs on real-world tool use with 229 tasks using human-written queries, real deployed tools, and authentic multimodal inputs such as images, screenshots, and code files.
- **HCAST** *(Mar 2025)* 📄 9 ⭐ 19\
  [Paper](https://arxiv.org/abs/2503.17354) · [Github](https://github.com/METR/hcast-public)
  > Evaluates AI agents on 189 tasks across ML engineering, cybersecurity, software engineering, and general reasoning, using human baselines collected over 1,500+ hours to calibrate difficulty.
- **MCP-Bench** *(Aug 2025)* 📄 45 ⭐ 473\
  [Paper](https://arxiv.org/abs/2508.20453) · [Github](https://github.com/Accenture/mcp-bench) · [Website](https://mcpbench.ai/)
  > Evaluates LLMs on realistic multi-step tasks requiring tool use and cross-tool coordination through 28 MCP servers spanning 250 tools across finance, travel, scientific computing, and academic search.
- **MCP-Universe** *(Aug 2025)* 📄 61 ⭐ 580\
  [Paper](https://arxiv.org/abs/2508.14704) · [Github](https://github.com/SalesforceAIResearch/MCP-Universe) · [Website](https://mcp-universe.github.io)
  > Evaluates LLMs on realistic tasks through 11 real-world MCP servers across 6 domains including location navigation, repository management, financial analysis, 3D design, browser automation, and web search.
- **REALM-Bench** *(Feb 2025)* 📄 7 ⭐ 37\
  [Paper](https://arxiv.org/abs/2502.18836) · [Github](https://github.com/genglongling/REALM-Bench)
  > Evaluates multi-agent systems on 14 progressively complex real-world planning and scheduling problems featuring multi-agent coordination, inter-dependencies, and dynamic disruptions.
- **tau-bench** *(Jun 2024)* 📄 468 ⭐ 1.2k\
  [Paper](https://arxiv.org/abs/2406.12045) · [Github](https://github.com/sierra-research/tau-bench)
  > Evaluates agents on dynamic conversations with a simulated user in real-world domains, providing domain-specific API tools and policy guidelines across retail and airline scenarios.
- **Tool Decathlon** *(Oct 2025)* 📄 26 ⭐ 317\
  [Paper](https://arxiv.org/abs/2510.25726) · [Github](https://github.com/hkust-nlp/Toolathlon) · [Website](https://toolathlon.xyz/)
  > Evaluates language agents across 108 tasks spanning 32 software applications and 604 tools, requiring multi-app workflows over approximately 20 interaction turns.
- **ToolComp** *(Jan 2025)* 📄 7 ⭐ 4\
  [Paper](https://arxiv.org/abs/2501.01290) · [Github](https://github.com/vaskar-nath/toolcomp)
  > Evaluates multi-step tool-use reasoning with process supervision labels, enabling assessment of both final outcomes and intermediate reasoning steps.
- **UltraHorizon** *(Sep 2025)* 📄 11 ⭐ 22\
  [Paper](https://arxiv.org/abs/2509.21766) · [Github](https://github.com/StarDewXXX/UltraHorizon)
  > Measures foundational agent capabilities for long-horizon partially observable tasks, with standard configurations involving 35K+ tokens and 60+ tool calls across exploration environments.
- **τ²-bench** *(Jun 2025)* 📄 181 ⭐ 1.0k\
  [Paper](https://arxiv.org/abs/2506.07982) · [Github](https://github.com/sierra-research/tau2-bench) · [Website](https://taubench.com) · [Agentbeats](https://agentbeats.dev/agentbeater/tau2-bench)
  > Evaluates agents in dual-control settings where both the agent and user modify shared state, exposing coordination and communication failures.

## Memory

- **Evo-Memory** *(Nov 2025)* 📄 42\
  [Paper](https://arxiv.org/abs/2511.20857)
  > A streaming benchmark for evaluating self-evolving memory in LLM agents across 10 diverse datasets, requiring agents to search, adapt, and update memory after each interaction.
- **LoCoMo** *(Feb 2024)* 📄 362 ⭐ 785\
  [Paper](https://arxiv.org/abs/2402.17753) · [Github](https://github.com/snap-research/locomo) · [Website](https://snap-research.github.io/locomo/)
  > Benchmarks long-term memory in language models across question answering, event summarization, and multimodal dialogue tasks using conversations spanning up to 35 sessions and 9K tokens on average.
- 🆕 **LoCoMo-Plus** *(Feb 2026)* 📄 1 ⭐ 20\
  [Paper](https://arxiv.org/abs/2602.10715) · [Github](https://github.com/xjtuleeyf/Locomo-Plus)
  > Benchmarks cognitive memory in LLM agents under cue-trigger semantic disconnect, testing agents on retaining and applying implicit constraints across long conversational contexts.
- **LongMemEval** *(Oct 2024)* 📄 212 ⭐ 691\
  [Paper](https://arxiv.org/abs/2410.10813) · [Github](https://github.com/xiaowu0162/LongMemEval) · [Website](https://web.cs.ucla.edu/~kwchang/bibliography/wu2025longmemeval/)
  > Benchmarks chat assistants on five long-term memory abilities - information extraction, multi-session reasoning, temporal reasoning, knowledge updates, and abstention - using 500 questions embedded in scalable chat histories.
- **Mem2ActBench** *(Jan 2026)* 📄 2\
  [Paper](https://arxiv.org/abs/2601.19935)
  > Evaluates whether agents can proactively leverage long-term memory to execute tool-based actions, covering 2,029 sessions across 400 tool-use tasks.
- 🆕 **MemoryArena** *(Feb 2026)* 📄 6\
  [Paper](https://arxiv.org/abs/2602.16313) · [Website](https://memoryarena.github.io/)
  > Evaluates agent memory in multi-session loops across web navigation, preference-constrained planning, progressive information search, and sequential formal reasoning.
- **MEMTRACK** *(Oct 2025)* 📄 6\
  [Paper](https://arxiv.org/abs/2510.01353)
  > Evaluates long-term memory and state tracking in multi-platform agent environments, testing memory acquisition, selection, and conflict resolution across realistic organizational workflows spanning Slack, Linear, and Git.

## Safety

- **Agent-SafetyBench** *(Dec 2024)* 📄 144 ⭐ 126\
  [Paper](https://arxiv.org/abs/2412.14470) · [Github](https://github.com/thu-coai/Agent-SafetyBench) · [Dataset](https://huggingface.co/datasets/thu-coai/Agent-SafetyBench)
  > Evaluates the safety of LLM agents across 8 categories of safety risks and 10 failure modes, covering 349 interaction environments and 2,000 test cases.
- **AgentAuditor** *(May 2025)* 📄 31 ⭐ 3\
  [Paper](https://arxiv.org/abs/2506.00641) · [Github](https://github.com/Astarojth/AgentAuditor)
  > Benchmarks LLM-based evaluators on detecting safety risks and security threats in agent interactions, covering 2,293 annotated records across 15 risk types and 29 application scenarios.
- **MCP-SafetyBench** *(Dec 2025)* 📄 10 ⭐ 17\
  [Paper](https://arxiv.org/abs/2512.15163) · [Github](https://github.com/xjzzzzzzzz/MCPSafety) · [Website](https://xjzzzzzzzz.github.io/mcpsafety.github.io/)
  > Evaluates safety of LLMs using the Model Context Protocol across 5 domains with a taxonomy of 20 MCP attack types spanning server, host, and user sides.
- 🆕 **MT-AgentRisk** *(Feb 2026)* 📄 2 ⭐ 17\
  [Paper](https://arxiv.org/abs/2602.13379) · [Github](https://github.com/CHATS-lab/ToolShield) · [Website](https://unsafer-in-many-turns.github.io/)
  > Evaluates multi-turn tool-using agent safety, revealing that attack success rates increase by approximately 16% in multi-turn settings compared to single-turn baselines.
- **OpenAgentSafety** *(Jul 2025)* 📄 28 ⭐ 32\
  [Paper](https://arxiv.org/abs/2507.06134) · [Github](https://github.com/sani903/OpenAgentSafety) · [Dataset](https://huggingface.co/datasets/sani903/openagentsafety)
  > Evaluates agent behavior across 8 critical risk categories using real tools including web browsers, code execution, file systems, and bash shells across 350+ multi-turn tasks with both benign and adversarial intents.
- **OS-Harm** *(Jun 2025)* 📄 40 ⭐ 63\
  [Paper](https://arxiv.org/abs/2506.14866) · [Github](https://github.com/tml-epfl/os-harm)
  > Evaluates safety of computer use agents on 150 tasks spanning three harm categories - deliberate user misuse, prompt injection attacks, and model misbehavior.

## Scientific Research

- **AstaBench** *(Oct 2025)* 📄 7 ⭐ 98\
  [Paper](https://arxiv.org/abs/2510.21652) · [Github](https://github.com/allenai/asta-bench)
  > Evaluates agents on 2,400+ problems spanning the full scientific discovery process across multiple domains, including literature review, experiment replication, data analysis, and research direction proposals.
- **InnovatorBench** *(Oct 2025)* 📄 7 ⭐ 17\
  [Paper](https://arxiv.org/abs/2510.27598) · [Github](https://github.com/GAIR-NLP/InnovatorBench) · [Website](https://ai-innovator.opensii.ai/)
  > Evaluates agents on 20 code-driven LLM research tasks spanning data construction, filtering, augmentation, and model design, paired with the ResearchGym execution environment.
- **RE-Bench** *(Nov 2024)* 📄 79 ⭐ 135\
  [Paper](https://arxiv.org/abs/2411.15114) · [Github](https://github.com/METR/RE-Bench)
  > Evaluates AI agents on 7 challenging open-ended ML research engineering tasks, benchmarking against human experts across 1,500+ hours of collected human baselines.

## Security

- **Agent Security Bench** *(Oct 2024)* 📄 172 ⭐ 219\
  [Paper](https://arxiv.org/abs/2410.02644) · [Github](https://github.com/agiresearch/ASB) · [Website](https://luckfort.github.io/ASBench/)
  > Evaluates attacks and defenses of LLM-based agents across 10 scenarios, 10 agent types, over 400 tools, and 27 attack and defense methods.
- **CAIBench** *(Oct 2025)* 📄 12\
  [Paper](https://arxiv.org/abs/2510.24317) · [Github](https://github.com/aliasrobotics/cai/tree/main/benchmarks)
  > A modular meta-benchmark for evaluating LLMs and agents across offensive and defensive cybersecurity domains, integrating over 10,000 instances across Jeopardy CTFs, Attack-Defense CTFs, Cyber Range exercises, and knowledge assessments.
- **CVE-Bench** *(Mar 2025)* 📄 57 ⭐ 199\
  [Paper](https://arxiv.org/abs/2503.17332) · [Github](https://github.com/uiuc-kang-lab/cve-bench)
  > Evaluates LLM agents on exploiting real-world web application vulnerabilities based on critical-severity CVEs, with state-of-the-art agents resolving approximately 13% of vulnerabilities.
- **CyberGym** *(Jun 2025)* 📄 11 ⭐ 245\
  [Paper](https://arxiv.org/abs/2506.02548) · [Github](https://github.com/sunblaze-ucb/cybergym) · [Website](https://www.cybergym.io/)
  > Evaluates agents on real-world vulnerability analysis by tasking them with generating proof-of-concept tests for known vulnerabilities given a natural language description and codebase. Covers 1,507 vulnerabilities across 188 open-source projects.
- **DoomArena** *(Apr 2025)* 📄 22 ⭐ 57\
  [Paper](https://arxiv.org/abs/2504.14064) · [Github](https://github.com/ServiceNow/DoomArena)
  > A security evaluation framework for AI agents that tests vulnerabilities across configurable threat models including malicious user and malicious environment scenarios, integrated with BrowserGym and tau-bench.
- **ExCyTIn-Bench** *(Jul 2025)* 📄 7 ⭐ 119\
  [Paper](https://arxiv.org/abs/2507.14201) · [Github](https://github.com/microsoft/SecRL) · [Website](https://www.microsoft.com/en-us/security/blog/2025/10/14/microsoft-raises-the-bar-a-smarter-way-to-measure-ai-for-cybersecurity/)
  > Evaluates LLM agents on cyber threat investigation through 589 security questions derived from investigation graphs built from 8 simulated attacks across 57 log tables in an Azure environment.
- **SEC-bench** *(Jun 2025)* 📄 25 ⭐ 67\
  [Paper](https://arxiv.org/abs/2506.11791) · [Github](https://github.com/SEC-bench/SEC-bench)
  > Evaluates LLM agents on authentic security engineering tasks - proof-of-concept generation and vulnerability patching - using an automated pipeline that constructs repositories, reproduces vulnerabilities, and generates gold patches.
- **WASP** *(Apr 2025)* 📄 73 ⭐ 82\
  [Paper](https://arxiv.org/abs/2504.18575) · [Github](https://github.com/facebookresearch/wasp)
  > Evaluates end-to-end security of web agents against prompt injection attacks in realistic scenarios, with attacks partially succeeding in up to 86% of cases.

## Web

- **AssistantBench** *(Jul 2024)* 📄 102 ⭐ 70\
  [Paper](https://arxiv.org/abs/2407.15711) · [Github](https://github.com/oriyor/assistantbench) · [Website](https://assistantbench.github.io/)
  > Evaluates web agents on 214 realistic time-consuming tasks that can be automatically evaluated across different scenarios and domains, with no model exceeding 26% accuracy.
- **BrowseComp** *(Apr 2025)* 📄 350 ⭐ 4.4k\
  [Paper](https://arxiv.org/abs/2504.12516) · [Github](https://github.com/openai/simple-evals)
  > Evaluates web browsing agents on 1,266 questions requiring persistent navigation to find entangled hard-to-locate information with short, verifiable answers.
- **BrowserArena** *(Oct 2025)* 📄 6 ⭐ 4\
  [Paper](https://arxiv.org/abs/2510.02418) · [Github](https://github.com/sagnikanupam/browserarena)
  > A live open-web agent evaluation platform that collects user-submitted tasks and runs Arena-style head-to-head comparisons with step-level human feedback for LLM web agents.
- **Mind2Web** *(Jun 2023)* 📄 972 ⭐ 978\
  [Paper](https://arxiv.org/abs/2306.06070) · [Github](https://github.com/OSU-NLP-Group/Mind2Web) · [Website](https://osu-nlp-group.github.io/Mind2Web)
  > Evaluates generalist web agents on 2,000+ tasks across 137 websites and 31 domains.
- **Mind2Web 2** *(Jun 2025)* 📄 33 ⭐ 108\
  [Paper](https://arxiv.org/abs/2506.21506) · [Github](https://github.com/OSU-NLP-Group/Mind2Web-2) · [Website](https://osu-nlp-group.github.io/Mind2Web-2/)
  > Evaluates agentic search systems on 130 long-horizon tasks requiring real-time web browsing, information synthesis, and citation-backed answers, using an Agent-as-a-Judge framework.
- **Online-Mind2Web** *(Apr 2025)* 📄 89 ⭐ 170\
  [Paper](https://arxiv.org/abs/2504.01382) · [Github](https://github.com/OSU-NLP-Group/Online-Mind2Web) · [Leaderboard](https://huggingface.co/spaces/osunlp/Online_Mind2Web_Leaderboard)
  > Evaluates web agents on 300 diverse realistic tasks spanning 136 websites under conditions that approximate real user settings.
- **VisualWebArena** *(Jan 2024)* ⭐ 461\
  [Paper](https://arxiv.org/abs/2401.13649) · [Github](https://github.com/web-arena-x/visualwebarena) · [Website](https://jykoh.com/vwa)
  > Evaluates multimodal web agents on realistic visually grounded web tasks, requiring agents to process image-text inputs and execute actions on websites.
- **WebArena** *(Jul 2023)* 📄 1.1k ⭐ 1.4k\
  [Paper](https://arxiv.org/abs/2307.13854) · [Github](https://github.com/web-arena-x/webarena) · [Website](https://webarena.dev/og/)
  > Evaluates agents on realistic web tasks spanning e-commerce, forums, collaborative software dev, and content management.
- 🆕 **WebArena-Infinity** *(Mar 2026)* ⭐ 40\
  [Github](https://github.com/web-arena-x/webarena-infinity) · [Website](https://webarena.dev/webarena-infinity/)
  > Generates realistic browser environments with verifiable tasks at scale using a multi-agent pipeline that builds, audits, and hardens web applications from static artifacts such as user manuals and recorded workflows. The initial release includes 10 environments, 1,260 verifiable tasks, and 2,070 successful browser-agent trajectories.
- **WebArena-Verified** ⭐ 36\
  [Github](https://github.com/ServiceNow/webarena-verified) · [Website](https://servicenow.github.io/webarena-verified/)
  > A curated, version-controlled set of 812 web agent tasks with deterministic evaluators supporting offline evaluation via network trace replay, eliminating LLM-based judging.
- **WebChoreArena** *(Jun 2025)* 📄 19 ⭐ 34\
  [Paper](https://arxiv.org/abs/2506.01952) · [Github](https://github.com/WebChoreArena/WebChoreArena) · [Website](https://webchorearena.github.io/)
  > Evaluates web browsing agents on 532 tedious real-world tasks focusing on massive memory requirements, mathematical calculations, and long-term memory across multiple webpages.
- **WebShop** *(Jul 2022)* 📄 923 ⭐ 520\
  [Paper](https://arxiv.org/abs/2207.01206) · [Github](https://github.com/princeton-nlp/webshop) · [Website](https://webshop-pnlp.github.io)
  > Evaluates agents on navigating and shopping in a simulated e-commerce environment with 1.18 million real-world products and 12,087 crowd-sourced text instructions.

