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
