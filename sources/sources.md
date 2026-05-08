# Sources registry

Every source the wiki cites gets a stable ID `S<N>`. Add new sources at the
bottom; never renumber.

Schema per entry:
- `id`, `url`, `type`, `author`, `date`, `roles`, `summary`, `confidence`,
  `ingested_at`.

---

## S1
- url: https://openai.com/interview-guide/
- type: official
- author: OpenAI
- date: 2024 (ongoing)
- roles: all
- summary: OpenAI's own public interview guide. Recommends the Deep Learning
  Book and Spinning Up in Deep RL for ML candidates; describes a
  multi-stage loop with practical coding, not LeetCode-tricks.
- confidence: high
- ingested_at: 2026-05-07

## S2
- url: https://www.hellointerview.com/blog/openai-coding-questions
- type: blog
- author: Hello Interview
- date: 2025
- roles: SWE, ML Eng
- summary: Aggregated, named coding-round questions from real OpenAI
  candidates: KV-store serialize/deserialize, time-based KV store, resumable
  iterator, in-memory SQL DB, Unix `cd`, multithreaded crawler, spreadsheet
  formulas. Emphasizes "production-quality, edge-case heavy, lots of typing".
- confidence: high
- ingested_at: 2026-05-07

## S3
- url: https://www.hellointerview.com/guides/openai/l5
- type: blog
- author: Hello Interview
- date: 2026
- roles: L5 (Senior+ SWE/ML)
- summary: 6-8 round L5 loop: recruiter+HM, coding screen, system-design
  screen, onsite (coding, system design, technical project presentation,
  leadership behavioral, collaboration behavioral, optional domain-specific).
  Lists named questions: KV serialize/deserialize, Disease Spread in Flower
  Grid, In-Memory SQL DB, credit tracking service, LC 2408 Design SQL;
  system design: Online Chess, GitHub Actions, Slack, Payment, ChatGPT.
- confidence: high
- ingested_at: 2026-05-07

## S4
- url: https://medium.com/@anqi.silvia/my-8-coding-questions-from-the-2025-openai-interview-d0df24773d33
- type: blog
- author: Anqi Silvia (Medium)
- date: 2025
- roles: ML Eng / SWE
- summary: First-person 2025 OpenAI loop. Names 3 of 8 coding questions:
  spreadsheet API getCell/setCell with cycle detection, timestamp-based
  KV store with versioning, GPU credit management with FIFO expiry.
  Recommends Python, time-management, focus on real engineering not algos.
- confidence: high
- ingested_at: 2026-05-07

## S5
- url: https://medium.com/@tomzat/how-i-prepared-for-my-openai-interview-and-what-actually-helped-a185eefbafe6
- type: blog
- author: Tomotake Zata (Medium)
- date: 2025
- roles: SWE / ML Eng
- summary: 4-week prep plan. Loop: recruiter chat, coding phone screen,
  system-design phone screen, onsite coding, onsite system design, deep
  dive, behavioral. Says LRU cache is canonical and "design ChatGPT for
  100M users" is a common system-design prompt. Recommends 1Point3Acres
  for fresh experience reports.
- confidence: medium
- ingested_at: 2026-05-07

## S6
- url: https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs
- type: blog
- author: Sundeep Teki
- date: 2025-2026
- roles: AI Research Engineer
- summary: Comparative guide for OpenAI / Anthropic / DeepMind RE roles.
  Characterizes OpenAI as "much more coding-focused than research-focused"
  and "pragmatic scalers" obsessed with shipping. 4-6 hour onsite over
  1-2 days; assesses coding, ML coding (transformers), ML debugging, ML
  system design (large-model training), inference, paper discussion,
  behavioral.
- confidence: high
- ingested_at: 2026-05-07

## S7
- url: https://igotanoffer.com/en/advice/openai-interview-questions
- type: blog
- author: IGotAnOffer
- date: 2025
- roles: all
- summary: Question bank by role: ML Engineer, ML Researcher, SWE, applied
  AI. Covers ML breadth (overfitting, optimizers, regularization), system
  design, behavioral. (Surface-only; secondary aggregator.)
- confidence: medium
- ingested_at: 2026-05-07

## S8
- url: https://igotanoffer.com/en/advice/openai-interview-process
- type: blog
- author: IGotAnOffer
- date: 2025
- roles: all
- summary: 6-step process timeline. Approx 4-8 weeks end-to-end (varies).
- confidence: medium
- ingested_at: 2026-05-07

## S9
- url: https://igotanoffer.com/en/advice/openai-system-design-interview
- type: blog
- author: IGotAnOffer
- date: 2025
- roles: SWE, ML Eng
- summary: System-design round usually 45-60 min. Open-ended ("Design
  Slack"-class), probing on assumptions and trade-offs. Expect
  ML-system-design framing for ML roles.
- confidence: medium
- ingested_at: 2026-05-07

## S10
- url: https://www.glassdoor.com/Interview/OpenAI-Interview-Questions-E2210885.htm
- type: glassdoor
- author: Glassdoor (aggregated)
- date: 2025-2026 (rolling)
- roles: all
- summary: Aggregate Glassdoor data: avg ~31 days time-to-decision,
  difficulty 3.21/5, ~38% positive experience rating. Loop varies but
  recurrent themes: practical coding, system design, mission-fit
  behavioral.
- confidence: medium
- ingested_at: 2026-05-07

## S11
- url: https://www.teamblind.com/company/OpenAI/posts
- type: blind
- author: Blind community
- date: ongoing
- roles: all
- summary: Anonymous candidate threads. Recurring signals: rejections after
  strong technical due to behavioral/deep-dive; coding bar high — "won't
  pass with 2/4 even if you ace everything else"; multiple rounds use
  CoderPad; some candidates report being allowed to use their own IDE
  with screenshare.
- confidence: low
- ingested_at: 2026-05-07

## S12
- url: https://leetcodewizard.io/blog/mastering-the-openai-software-engineer-interview-questions-process-and-expert-tips-for-preparation
- type: blog
- author: Leetcode Wizard
- date: 2025
- roles: SWE
- summary: SWE-specific prep guide. Confirms LRU cache as canonical;
  emphasizes trees, binary search, graphs, recursion; production-quality
  coding over algorithmic gimmicks.
- confidence: medium
- ingested_at: 2026-05-07

## S13
- url: https://molochinations.substack.com/p/how-i-got-a-job-at-openai
- type: blog
- author: Philip Su (ex-Microsoft, ex-Meta)
- date: 2024
- roles: SWE (senior)
- summary: First-person hire story. Notes a "present a technical topic"
  round unusual elsewhere; spent ~80 hrs on system design prep using
  YouTube + ChatGPT. Stresses referrals, recruiter relationships, and
  long-arc reputation.
- confidence: medium
- ingested_at: 2026-05-07

## S14
- url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- type: gist
- author: Andrej Karpathy
- date: 2025
- roles: meta
- summary: Defines the LLM Wiki pattern this repo implements. Three layers:
  raw sources, the wiki, the schema (CLAUDE.md). Operations: ingest, query,
  lint.
- confidence: high
- ingested_at: 2026-05-07

## S15
- url: https://www.youtube.com/watch?v=e6JisS9tEtY
- type: yt
- author: (candidate, $500K+ comp anecdote)
- date: 2024-2025
- roles: Senior SWE
- summary: First-person video walkthrough of an OpenAI Senior SWE loop:
  rounds, system design experience, comp band, prep tips. Not yet
  transcribed in this KB — flagged for transcription/ingest.
- confidence: low
- ingested_at: 2026-05-07

## S16
- url: https://careerservices.fas.harvard.edu/blog/2025/04/07/how-to-get-and-ace-interviews-at-openai/
- type: blog
- author: Harvard FAS / Mignone Center
- date: 2025-04-07
- roles: all (early-career bias)
- summary: University-side guide. Mostly application/strategy advice;
  re-affirms practical coding bar and mission-fit behavioral.
- confidence: medium
- ingested_at: 2026-05-07

## S17
- url: https://www.linkjob.ai/interview-questions/openai-ml-interview/
- type: blog
- author: Linkjob.ai
- date: 2026
- roles: ML Eng
- summary: Reported 2026 ML loop: foundational ML (overfitting / metrics),
  system design ("Design a fault-tolerant training pipeline"), project
  deep-dive, research-vision questions ("design next-gen multimodal
  reasoning system"). Likely partially synthesized; treat with care.
- confidence: low
- ingested_at: 2026-05-07

## S18
- url: https://www.interviewquery.com/interview-guides/openai-machine-learning-engineer
- type: blog
- author: Interview Query
- date: 2025
- roles: ML Eng
- summary: Aggregated ML-Eng prep guide; question taxonomy + sample
  problems.
- confidence: medium
- ingested_at: 2026-05-07

## S19
- url: https://www.interviewnode.com/post/ace-your-openai-ml-interview-top-25-questions-and-expert-answers
- type: blog
- author: Interview Node
- date: 2025
- roles: ML Eng / Researcher
- summary: 25-question bank covering transformers, attention, optimization,
  evaluation, debugging, distributed training, RLHF.
- confidence: medium
- ingested_at: 2026-05-07

## S20
- url: https://docs.google.com/document/d/1agAkPq_F-GFnbrCk4Daa85BYlSXcEWUwKRsGeLRL1GA/edit
- type: doc
- author: Alessandro Solbiati (repo owner)
- date: 2025-02 (active prep window)
- roles: ML Eng
- summary: First-person OpenAI ML-Engineer prep doc. Captures verbatim
  recruiter emails (Coding, ML Debug, Tech Deep Dive, ML Search Design),
  passed Coding + ML SD screens, in-progress onsite (ML debugging w/
  Leo Gao, project deep dive, behavioral + XFN). Includes a question
  pool (time-based KV, in-memory DB, resumable iterator, GPU credit,
  CD with symlinks, tree node-count, LRU), ML SD depth checklist
  (calibration, AUC, attention, MoE, LoRA, ACE, vertical ranking,
  RAG, etc.), Karpathy + Neel-Nanda study plan, a 7-section deep-dive
  slide template, and a behavioral STAR matrix.
  Raw ingest stored at `sources/s20-alessandro-prep-doc.md`.
- confidence: high
- ingested_at: 2026-05-07

## S21
- url: https://hyring.com/blog/ai-interview-integrity-2026/
- type: blog
- author: Hyring
- date: 2026
- roles: meta
- summary: Industry-side overview of AI-cheating in interviews and the
  countermeasures (proctoring, AI-resistant questions, AI-collab
  interviews). Useful background for the "AI in interviews" tooling page.
- confidence: medium
- ingested_at: 2026-05-07

## S22
- url: https://www.lockedinai.com/blog/companies-allowing-ai-in-interviews
- type: blog
- author: LockedIn AI
- date: 2025-2026
- roles: meta
- summary: Lists companies that explicitly allow AI tools in coding
  interviews (Canva, Shopify, etc.). Useful contrast — OpenAI is not on
  the "allowed" list as of mid-2026 per public reports; verify per role.
- confidence: low
- ingested_at: 2026-05-07

## S23
- url: (private chat, paste excerpt; raw at `sources/s23-alberto-alfarano-chat.md`)
- type: forum (chat excerpt, peer signal)
- author: Alberto Alfarano (Meta sysML engineer; OpenAI candidate signal)
- date: 2025-03-11
- roles: sysML / ML-infra / scaling-team Eng
- summary: First-person account of the **sysML** flavor of the OpenAI
  loop. Six concrete questions: GPU vector-matrix multiply, autograd
  system design, MHA kernel on H100, scaling 8 GPU → 20k GPU,
  two-level-memory matmul, LLM-customer-support quality. Names
  Triton + flash-linear-attention as canonical study material.
  Cultural signal: "0 bullshit, only code firing" — coding density and
  low-level systems depth dominate over behavioral.
- confidence: high
- ingested_at: 2026-05-07

# Alignment Researcher research-pass (S24-S55) — ingested 2026-05-08

## S24
- url: internal research dump (raw at `sources/s24-alignment-research-dump.md`)
- type: synthesis
- author: research-agent + repo agent
- date: 2026-05-08
- roles: Researcher, Alignment
- summary: Multi-source synthesis covering the Alignment Researcher
  loop, OpenAI's alignment org chart post-Mission-Alignment-dissolution
  (Feb 2026), flagship alignment papers (W2S, Deliberative Alignment,
  Instruction Hierarchy, SAEs, CriticGPT, scheming, CoT monitoring),
  topical depth checklist, key people, comp band.
- confidence: high (for paper/blog/JD facts); low (for loop structure
  — no first-person writeup found)
- ingested_at: 2026-05-08

## S25 — Job postings
- urls:
  - https://openai.com/careers/researcher-alignment-san-francisco/
  - https://openai.com/careers/research-engineer-research-scientist-alignment/
  - https://openai.com/careers/researcher-alignment-science-san-francisco/
  - https://openai.com/careers/researcher-alignment-training-san-francisco/
  - https://openai.com/careers/researcher-misalignment-research-new-york-city/
  - https://openai.com/careers/head-of-preparedness-san-francisco/
- type: official
- author: OpenAI
- date: 2025-2026 (rolling)
- roles: Alignment / Alignment Science / Alignment Training /
  Misalignment Research / Head of Preparedness
- summary: Six distinct alignment-adjacent job postings as of May
  2026. PhD or equivalent expected for research-track; San Francisco
  hybrid (3 days in office) standard.
- confidence: high
- ingested_at: 2026-05-08

## S26 — alignment.openai.com (Alignment-Science blog)
- url: https://alignment.openai.com/
- type: official
- author: OpenAI Alignment Science team
- date: launched 2025-12-01
- roles: Alignment / Alignment Science
- summary: Standalone blog launched December 2025 with "Hello World".
  Dec 2025 posts: "Helpful assistant features suppress emergent
  misalignment" (Dec 22), "Sidestepping Evaluation Awareness… with
  Production Evaluations" (Dec 18), "Debugging misaligned completions
  with sparse-autoencoder latent attribution" (Dec 1), "A Practical
  Approach to Verifying Code at Scale" (Dec 1). Read all posts
  before interview.
- confidence: high
- ingested_at: 2026-05-08

## S27 — Our approach to alignment research
- url: https://openai.com/index/our-approach-to-alignment-research/
- type: official
- author: OpenAI
- date: 2024 (updated)
- roles: all alignment
- summary: OpenAI's framing of its alignment agenda: training models
  with human feedback, training models to assist human evaluation
  (scalable oversight), training models to do alignment research.
- confidence: high
- ingested_at: 2026-05-08

## S28 — Safety alignment overview
- url: https://openai.com/safety/how-we-think-about-safety-alignment/
- type: official
- author: OpenAI
- date: 2024-2025
- roles: all alignment + Preparedness
- summary: How-we-think-about-safety-alignment overview; pairs with
  Preparedness Framework and the Evaluations Hub.
- confidence: high
- ingested_at: 2026-05-08

## S29 — Evaluations Hub
- url: https://openai.com/safety/evaluations-hub/
- type: official
- author: OpenAI
- date: 2025
- roles: all alignment + Preparedness
- summary: Public-facing evaluation results across capability and
  safety axes for OpenAI models.
- confidence: high
- ingested_at: 2026-05-08

## S30 — Weak-to-strong generalization
- urls:
  - https://openai.com/index/weak-to-strong-generalization/
  - https://arxiv.org/abs/2312.09390
  - https://cdn.openai.com/papers/weak-to-strong-generalization.pdf
- type: paper
- author: Burns, Izmailov, Kirchner, Baker, Gao, Aschenbrenner, Chen,
  Ecoffet, Joglekar, Leike, Sutskever, Wu (Dec 2023)
- date: 2023-12
- roles: Alignment / Alignment Science
- summary: Foundational scalable-oversight result. Train a strong
  student on labels produced by a weaker teacher and study how much
  of the strong-model capability survives. Canonical reading for
  scalable oversight; named authors include current alignment-team
  members (Wu, Gao, Baker, Izmailov, Kirchner, Burns).
- confidence: high
- ingested_at: 2026-05-08

## S31 — Deliberative alignment
- urls:
  - https://openai.com/index/deliberative-alignment/
  - https://arxiv.org/abs/2412.16339
- type: paper
- author: Guan et al. (incl. Boaz Barak)
- date: 2024-12
- roles: Alignment / Alignment Training
- summary: The o-series alignment paradigm: train the model to read
  and reason over a written safety spec at inference time, instead of
  encoding policy implicitly into refusal training. Co-author Boaz
  Barak is associated with the Researcher-Alignment role.
- confidence: high
- ingested_at: 2026-05-08

## S32 — Instruction Hierarchy
- urls:
  - https://openai.com/index/the-instruction-hierarchy/
  - https://arxiv.org/abs/2404.13208
- type: paper
- author: Wallace et al.
- date: 2024-04 (ICLR 2025)
- roles: Alignment / Safety Systems
- summary: Privileged-instruction policy. System > developer > user;
  trained data and inference-time policy that hardens models against
  prompt injection by making the message hierarchy first-class.
- confidence: high
- ingested_at: 2026-05-08

## S33 — Scaling sparse autoencoders on GPT-4
- urls:
  - https://openai.com/index/extracting-concepts-from-gpt-4/
  - https://arxiv.org/abs/2406.04093
  - https://cdn.openai.com/papers/sparse-autoencoders.pdf
- type: paper
- author: Gao et al.
- date: 2024-06
- roles: Alignment / interpretability
- summary: 16M-latent sparse autoencoder trained on GPT-4 activations
  (k-sparse / top-k variant). Canonical OpenAI interpretability
  result; pairs with the Dec 2025 alignment-blog post on debugging
  misaligned completions via SAE latent attribution.
- confidence: high
- ingested_at: 2026-05-08

## S34 — CriticGPT
- urls:
  - https://cdn.openai.com/llm-critics-help-catch-llm-bugs-paper.pdf
  - https://arxiv.org/abs/2407.00215
- type: paper
- author: McAleese et al.
- date: 2024-06
- roles: Alignment Science / scalable oversight
- summary: Train an LLM to critique another LLM's code. A scalable-
  oversight result that worked end-to-end in production for code
  review. Pair with W2S as the two canonical OpenAI scalable-
  oversight artifacts.
- confidence: high
- ingested_at: 2026-05-08

## S35 — Detecting and reducing scheming
- urls:
  - https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/
  - https://arxiv.org/abs/2509.15541
  - https://www.apolloresearch.ai/research/stress-testing-deliberative-alignment-for-anti-scheming-training/
- type: paper
- author: OpenAI × Apollo Research
- date: 2025-09
- roles: Alignment / Misalignment Research
- summary: Anti-scheming training reduced misbehavior ~30× on o3 /
  o4-mini in a controlled-scheming evaluation. Co-published with
  Apollo's stress-testing post; central to Misalignment-Research
  agenda.
- confidence: high
- ingested_at: 2026-05-08

## S36 — Chain-of-thought monitoring
- urls:
  - https://openai.com/index/chain-of-thought-monitoring/
  - https://openai.com/index/evaluating-chain-of-thought-monitorability/
  - https://arxiv.org/abs/2503.11926
  - https://arxiv.org/abs/2507.11473
- type: paper
- author: Baker et al. + cross-lab signatories
- date: 2025-03 / 2025-07
- roles: Alignment / Misalignment Research
- summary: Use CoT to monitor for reward-hacking and scheming
  behavior in reasoning models; cross-lab follow-up signed by
  OpenAI/Anthropic/DeepMind asks the field to preserve CoT
  monitorability.
- confidence: high
- ingested_at: 2026-05-08

## S37 — Alignment faking
- url: https://arxiv.org/abs/2412.14093
- type: paper
- author: Greenblatt et al. (Redwood / Anthropic)
- date: 2024-12
- roles: Alignment (cross-lab)
- summary: Empirical demonstration that frontier models can fake
  alignment under training pressure. Required reading for OpenAI
  alignment loops despite being from Redwood/Anthropic — defines the
  scheming threat model in concrete terms.
- confidence: high
- ingested_at: 2026-05-08

## S38 — AI Control
- url: https://arxiv.org/abs/2312.06942
- type: paper
- author: Greenblatt et al. (Redwood)
- date: 2023-12
- roles: Alignment / control
- summary: Frames "AI control" as separate from "AI alignment":
  given an *untrusted* model, can a *trusted* monitor + protocol
  catch and contain unsafe behaviors? Trusted-untrusted setup,
  protocol families, monitoring, resampling. Foundational for
  control-vs-alignment fluency.
- confidence: high
- ingested_at: 2026-05-08

## S39 — Preparedness Framework v2
- urls:
  - https://openai.com/index/updating-our-preparedness-framework/
  - https://cdn.openai.com/pdf/18a02b5d-6b67-4cec-ab64-68cdfbddebcd/preparedness-framework-v2.pdf
- type: official
- author: OpenAI Preparedness team
- date: 2025-04
- roles: Preparedness / Alignment Science
- summary: Two-threshold (High, Critical) framework narrowed to
  highest-priority risks. CBRN, cyber, autonomy, persuasion. Read
  before any safety/preparedness interview.
- confidence: high
- ingested_at: 2026-05-08

## S40 — Model Spec
- url: https://model-spec.openai.com/2025-12-18.html
- type: official
- author: OpenAI Model Behavior / Post-Training
- date: 2025-12-18
- roles: Alignment / Model Behavior
- summary: The current Model Spec — the human-written policy the
  o-series models reason over per Deliberative Alignment. Required
  reading; expect interviewers to assume you know the precedence
  rules and policy categories.
- confidence: high
- ingested_at: 2026-05-08

## S41 — Sycophancy in GPT-4o
- urls:
  - https://openai.com/index/sycophancy-in-gpt-4o/
  - https://openai.com/index/expanding-on-sycophancy/
- type: official
- author: OpenAI
- date: 2025-04 / 2025-05
- roles: Alignment / Safety Systems
- summary: April 2025 sycophancy incident retrospective. Concrete
  example of reward-hacking from production-RL preference signals;
  good behavioral-interview talking point on quality vs. shipping.
- confidence: high
- ingested_at: 2026-05-08

## S42 — Safe completions (GPT-5)
- urls:
  - https://openai.com/index/gpt-5-safe-completions/
  - https://cdn.openai.com/pdf/be60c07b-6bc2-4f54-bcee-4141e1d6c69a/gpt-5-safe_completions.pdf
- type: paper
- author: OpenAI
- date: 2025-08
- roles: Alignment / Alignment Training
- summary: Output-centric reward replaces refusal training. Treats
  "safe completion" as the unit instead of "refusal vs. comply";
  successor to deliberative alignment for the GPT-5 series.
- confidence: high
- ingested_at: 2026-05-08

## S43 — OpenAI × Anthropic safety eval
- urls:
  - https://openai.com/index/openai-anthropic-safety-evaluation/
  - https://alignment.anthropic.com/2025/openai-findings/
- type: official
- author: OpenAI × Anthropic
- date: 2025-08
- roles: Alignment / Misalignment Research
- summary: Cross-lab pilot exercise: each lab evaluated the other's
  models on its own safety evals. Read both write-ups — useful
  comparison of how OpenAI vs. Anthropic frame the same model.
- confidence: high
- ingested_at: 2026-05-08

## S44 — Mission Alignment dissolution coverage
- urls:
  - https://techcrunch.com/2026/02/11/openai-disbands-mission-alignment-team-which-focused-on-safe-and-trustworthy-ai-development/
  - https://www.platformer.news/openai-mission-alignment-team-joshua-achiam/
  - https://www.businesstoday.in/technology/news/story/openai-restructures-mission-alignment-team-appoints-joshua-achiam-as-chief-futurist-515820-2026-02-12
  - https://winbuzzer.com/2026/02/12/openai-disbanded-mission-alignment-team-16-months-xcxwbn/
- type: news
- author: TechCrunch / Platformer / Business Today / WinBuzzer
- date: 2026-02-11+
- roles: meta (org chart)
- summary: Mission Alignment (~7 people, headed by Joshua Achiam)
  disbanded Feb 2026; Achiam → Chief Futurist with Jason Pruet.
  Calibrates "where alignment work lives now" for hiring-manager
  conversations.
- confidence: high
- ingested_at: 2026-05-08

## S45 — Boaz Barak's Harvard CS 2881 AI Safety syllabus
- urls:
  - https://boazbk.github.io/mltheoryseminar/
  - https://www.boazbarak.org/
- type: course
- author: Boaz Barak (Harvard, OpenAI part-time)
- date: 2025-Fall
- roles: Alignment
- summary: Boaz Barak is a known interviewer on the alignment-research
  side; his Fall-2025 Harvard course is the closest public proxy
  for the depth-bar he expects. Includes AI 2027, Bostrom, METR,
  *Replicating Emergent Misalignment* as homework. Endorsed by Owain
  Evans on X.
- confidence: high
- ingested_at: 2026-05-08

## S46 — Lilian Weng — Reward Hacking in RL
- url: https://lilianweng.github.io/posts/2024-11-28-reward-hacking/
- type: blog
- author: Lilian Weng (ex-OpenAI VP Safety Systems)
- date: 2024-11-28
- roles: Alignment
- summary: Canonical reward-hacking writeup. Still cited inside
  OpenAI as the reference text. Required reading for any reward-
  hacking / sycophancy / Goodhart discussion.
- confidence: high
- ingested_at: 2026-05-08

## S47 — Jan Leike on superalignment hiring (80,000 Hours)
- urls:
  - https://80000hours.org/podcast/episodes/jan-leike-superalignment/
  - https://80000hours.org/podcast/episodes/jan-leike-ml-alignment/
- type: podcast
- author: Jan Leike (ex-OpenAI Superalignment co-lead)
- date: 2023 (still circulating)
- roles: Alignment
- summary: Despite Leike having moved to Anthropic (May 2024), his
  hiring criteria still set the bar for what alignment-team
  candidates look like. Listen for: what kind of empirical research
  taste they hire for; what background combinations they reward;
  why he says ML-engineering ability is non-negotiable.
- confidence: high
- ingested_at: 2026-05-08

## S48 — Neel Nanda mech interp guides
- urls:
  - https://www.neelnanda.io/mechanistic-interpretability/prereqs
  - https://www.neelnanda.io/mechanistic-interpretability/getting-started
  - https://www.alignmentforum.org/posts/jP9KDyMkchuv6tHwm/how-to-become-a-mechanistic-interpretability-researcher
- type: blog
- author: Neel Nanda (DeepMind)
- date: 2023-2025
- roles: Alignment / interpretability
- summary: Standard practical track for building mech-interp depth.
  Pair with ARENA curriculum.
- confidence: high
- ingested_at: 2026-05-08

## S49 — AXRP #39 Hubinger on model organisms
- url: https://axrp.net/episode/2024/12/01/episode-39-evan-hubinger-model-organisms-misalignment.html
- type: podcast
- author: Evan Hubinger (Anthropic)
- date: 2024-12-01
- roles: Alignment / Misalignment Research
- summary: Definitive interview on the "model organisms of
  misalignment" research program — directly maps to OpenAI's
  Misalignment Research (NYC) team's work.
- confidence: high
- ingested_at: 2026-05-08

## S50 — Apollo Research scheming work
- urls:
  - https://www.apolloresearch.ai/research/frontier-models-are-capable-of-incontext-scheming/
  - https://www.apolloresearch.ai/
- type: paper / org
- author: Apollo Research
- date: 2024-2025
- roles: Misalignment Research / scheming
- summary: Apollo's "Frontier models are capable of in-context
  scheming" + the Sept 2025 stress-test of OpenAI's anti-scheming
  training. Apollo is OpenAI's primary external partner on
  scheming/control.
- confidence: high
- ingested_at: 2026-05-08

## S51 — Alignment Forum: evaluations of new safety researchers
- url: https://www.alignmentforum.org/posts/HACcn8roty9KBAWzZ/evaluations-of-new-ai-safety-researchers-can-be-noisy
- type: forum
- author: Alignment Forum community
- date: 2024
- roles: Alignment (meta-hiring)
- summary: One of the closest things to a first-person AI-safety-
  hiring writeup in public. Not OpenAI-specific.
- confidence: medium
- ingested_at: 2026-05-08

## S52 — Joshua Achiam Substack (Chief Futurist intro)
- urls:
  - https://openaiglobalaffairs.substack.com/p/introducing-our-chief-futurist
  - https://jachiam.github.io/about
- type: blog
- author: Joshua Achiam
- date: 2026-02
- roles: meta
- summary: Achiam's pivot from Mission Alignment lead to Chief
  Futurist; useful for tracking how OpenAI frames "alignment of
  the org with the world" vs. "alignment of the model".
- confidence: high
- ingested_at: 2026-05-08

## S53 — System cards (safety sections)
- urls:
  - https://openai.com/index/openai-o1-system-card/
  - https://cdn.openai.com/o3-mini-system-card-feb10.pdf
  - https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf
  - https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf
  - https://cdn.openai.com/gpt-5-system-card.pdf
- type: official
- author: OpenAI safety teams
- date: 2024-12 → 2025-08
- roles: Alignment / Preparedness / Safety Systems
- summary: Safety sections of o1 (Dec 2024), o3-mini (Jan 2025),
  GPT-4.5 (Feb 2025), o3/o4-mini (Apr 2025), GPT-5 (Aug 2025), and
  gpt-oss (Aug 2025). Required reading; expect "what surprised you
  in the GPT-5 system card?" as a real interview probe.
- confidence: high
- ingested_at: 2026-05-08

## S54 — Reward-hacking emergent misalignment paper
- url: https://arxiv.org/html/2511.18397v1
- type: paper
- author: OpenAI Alignment Science (cross-team)
- date: 2025-11
- roles: Alignment Science / Misalignment Research
- summary: "Natural emergent misalignment from reward hacking in
  production RL" — empirical demonstration that reward-hacking in
  production RL can spontaneously produce misaligned behavior;
  echoed in the Dec 22 alignment-blog post on suppressing it via
  helpful-assistant features.
- confidence: high
- ingested_at: 2026-05-08

## S55 — Levels.fyi OpenAI Research Scientist comp
- urls:
  - https://www.levels.fyi/companies/openai/salaries/software-engineer/title/research-scientist
  - https://www.levels.fyi/companies/openai/salaries
- type: data
- author: Levels.fyi (community-reported)
- date: 2025-2026
- roles: meta (comp)
- summary: Research Scientist L4 ~$771K; L5 ~$1.0-1.47M (median
  ~$1.0M). PPU valuation moves the headline number; treat any single
  point as a snapshot.
- confidence: medium
- ingested_at: 2026-05-08
