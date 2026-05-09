# Log

Append-only chronological log of ingests, edits, lints. Newest at the bottom.

---

## 2026-05-07 — repo bootstrap
- Created repository skeleton per CLAUDE.md / Karpathy LLM-Wiki pattern.
- Wrote README.md, CLAUDE.md (schema), index.md, this log, sources registry.
- Ingested S1–S22 (initial corpus from public OpenAI interview write-ups,
  Hello Interview, IGotAnOffer, Medium candidate posts, Sundeep Teki's
  research-engineer guide, Glassdoor, Blind, OpenAI's own interview-guide
  page, Karpathy's gist).
- Created wiki pages:
  - `wiki/overview.md`
  - `wiki/roles/{ml-engineer,ml-researcher,research-engineer,software-engineer}.md`
  - `wiki/rounds/{recruiter,coding,ml-coding,system-design,ml-system-design,deep-dive,behavioral,technical-project-presentation}.md`
  - `wiki/questions/{coding,ml,system-design,behavioral}-questions.md`
  - `wiki/topics/transformers.md`
  - `wiki/tooling/coderpad-and-ai-tools.md`
  - `wiki/prep/{reading-list,timeline}.md`

## 2026-05-07 — S20 + S23 ingest (primary-source upgrade)
- **S20**: ingested the repo owner's full prep doc (first-person,
  contains verbatim recruiter emails for Coding, ML Debug, ML Search
  Design, Tech Deep Dive). Promoted from `confidence: pending` to
  `confidence: high`. Raw ingest at
  `sources/s20-alessandro-prep-doc.md`.
- **S23**: ingested Alberto Alfarano (Meta sysML peer) chat — six
  concrete sysML / Triton / scaling-track questions, recommended
  reading (`fla-org/flash-linear-attention`), cultural signal ("0
  bullshit, only code firing"). Raw ingest at
  `sources/s23-alberto-alfarano-chat.md`.
- New wiki pages added:
  - `wiki/rounds/ml-debugging.md` (canonical fix-the-broken-transformer
    round, 60 min, with verbatim recruiter email).
  - `wiki/rounds/ml-search-design.md` (search/recsys-flavor of ML SD,
    with verbatim Young Cha description).
  - `wiki/rounds/xfn.md` (cross-functional partner round).
  - `wiki/topics/sysml-and-cuda.md` (parallelism, GPU kernels, Triton,
    autograd-system design — calibrated by S23).
  - `wiki/prep/deep-dive-template.md` (7-section project-deep-dive
    template with grading-axes mapping).
  - `wiki/prep/why-openai.md` (4-ingredient answer-construction
    template).
- Updated:
  - `wiki/roles/ml-engineer.md` — replaced inferred loop with
    S20-confirmed loop; added pointers to all new round/topic pages.
  - `wiki/rounds/coding.md` — added verbatim OpenAI recruiter email +
    evaluation criteria.
  - `wiki/rounds/behavioral.md` — added 85/15 Meta-Jedi vs.
    OpenAI-specific mix from S20.
  - `wiki/questions/coding-questions.md` — added GPU credit class
    signature, time-based KV follow-ups, tree node-count, `cd` with
    symlinks.
  - `wiki/questions/ml-questions.md` — added ML-search/recsys
    questions and sysML/scaling-track questions.
  - `wiki/questions/system-design-questions.md` — added sysML
    scaling-track table.
  - `index.md` updated to list new pages and raw-source files.
- Open follow-ups:
  - S15 (YouTube Senior SWE loop video) still needs transcription.
  - Compensation page deferred (volatile; needs Levels.fyi + Blind).
  - Per-team pages (Applied, Safety, Scaling, Post-training) deferred.
  - Add a `wiki/people/` directory once we have ≥3 named interviewers
    (currently: Leo Gao, Young Cha — both via S20).

## 2026-05-08 — Alignment Researcher pivot
- User confirmed the role they're interviewing for is **Researcher,
  Alignment**. KB primary focus shifted to that loop.
- Spawned a research agent for a thorough sweep on alignment loop +
  papers + people + comp; raw output saved as `S24` at
  `sources/s24-alignment-research-dump.md`.
- Registered S25-S55 in `sources/sources.md`:
  - S25: alignment-related job postings (6 distinct postings).
  - S26: alignment.openai.com (Alignment-Science blog, Dec 2025
    launch + Dec 2025 posts).
  - S27-S29: official "Our approach to alignment", "How we think
    about safety alignment", Evaluations Hub.
  - S30-S38: paper canon — W2S, Deliberative Alignment, Instruction
    Hierarchy, Scaling SAEs, CriticGPT, Anti-scheming, CoT
    monitoring, Alignment Faking, AI Control.
  - S39-S43: Preparedness Framework v2, Model Spec, Sycophancy
    retrospectives, Safe Completions, OpenAI×Anthropic cross-lab.
  - S44: Mission Alignment dissolution coverage (Feb 2026).
  - S45: Boaz Barak Harvard CS 2881 syllabus.
  - S46: Lilian Weng Reward-Hacking-in-RL post.
  - S47-S50: Leike 80kh, Neel Nanda mech interp, AXRP #39 Hubinger,
    Apollo Research scheming.
  - S51-S55: Alignment-Forum hiring-noisy post, Achiam Substack,
    system cards, emergent-misalignment paper, Levels.fyi.
- New wiki pages added:
  - `wiki/roles/alignment-researcher.md` (PRIMARY).
  - `wiki/topics/alignment.md` (topic overview, paper arc).
  - `wiki/topics/openai-alignment-org.md` (May-2026 org map).
  - `wiki/topics/rlhf-and-post-training.md` (RLHF → DPO → GRPO →
    safe completions; reward hacking).
  - `wiki/topics/scalable-oversight.md` (W2S, CriticGPT, debate).
  - `wiki/topics/interpretability.md` (SAEs, OpenAI's specific
    contributions).
  - `wiki/topics/reward-hacking.md` (Goodhart, sycophancy, emergent
    misalignment).
  - `wiki/topics/scheming-and-deceptive-alignment.md` (Apollo,
    OpenAI×Apollo, alignment-faking, AI control).
  - `wiki/topics/safety-evals-and-preparedness.md` (PF v2,
    capability elicitation, contamination, eval awareness,
    sandbagging).
  - `wiki/prep/alignment-reading-list.md` (3-tier prioritized list).
  - `wiki/prep/alignment-timeline.md` (4-week + 8-week + role-
    variant study plans).
  - `wiki/questions/alignment-questions.md` (probe-shaped question
    bank).
- Updated:
  - `CLAUDE.md` — Mission section now flags Researcher, Alignment as
    primary focus.
  - `wiki/overview.md` — added the alignment-primary banner.
  - `index.md` — full re-generation with new pages.
- Open follow-ups for the next research-pass:
  - **Highest priority**: any first-person OpenAI Alignment Researcher
    loop writeup (Glassdoor, Blind, LessWrong, podcast, Substack) —
    currently the largest gap in the KB [S24].
  - Per-team pages: Alignment Science, Alignment Training,
    Misalignment Research, Preparedness, Safety Systems.
  - `wiki/people/` directory — add Boaz Barak, Bowen Baker, Leo Gao,
    Jeff Wu, Nat McAleese, Joshua Achiam profiles.
  - alignment.openai.com posts after Dec 2025 (the blog should grow
    monthly; ingest each new post as it lands).
  - Levels.fyi snapshot for "Alignment Researcher" specifically if
    it ever gets broken out.

## 2026-05-08 — Anthropic alignment + Petri ingest (cross-lab pivot)
- User requested expansion to Anthropic alignment interviews +
  Anthropic's Petri auditing framework.
- Spawned a research agent (background) for thorough Anthropic-loop
  sweep; agent returned ~75 URLs grouped by source type. Raw output
  saved as `S56` at `sources/s56-anthropic-research-dump.md`.
- Direct WebFetch on Anthropic's Petri page captured architecture,
  authors, behaviors audited, repo URL.
- Registered S56-S80 in `sources/sources.md`:
  - S56: Anthropic research-pass synthesis (raw).
  - S57: Petri (multi-URL: anthropic page + alignment.anthropic.com +
    GitHub repo + Petri 2.0 + donate-to-OSS post).
  - S58: alignment.anthropic.com blog (multi-post: Recommended
    Directions, automated auditing, MO replication, red-team strength,
    subliminal learning, sandbagging, sabotage risk, alignment-faking
    mitigations, stress-testing model specs, activation oracles, bloom).
  - S59: Anthropic core views + RSP v3 + Claude 4 system card.
  - S60: Sleeper Agents (Hubinger et al. + Simple Probes mitigation).
  - S61: Constitutional AI / RLAIF.
  - S62: Agentic Misalignment.
  - S63: SHADE-Arena.
  - S64: Auditing LMs for Hidden Objectives (Marks et al.).
  - S65: Many-Shot Jailbreaking.
  - S66: Sycophancy in LMs (Sharma et al.).
  - S67: Anthropic interpretability canon (Toy Models, Towards
    Monosemanticity, Scaling Monosemanticity, Crosscoders, Influence
    Functions, feature steering, engineering challenges).
  - S68: Sam Bowman public writing (FAQ + Checklist).
  - S69: Ethan Perez essays (project selection + empirical tips).
  - S70: Hubinger introducing Alignment Stress-Testing.
  - S71: **Andrey Goncharov "I failed my Anthropic interview"** —
    HIGH value first-person account, closes the FP gap that S24
    flagged.
  - S72: Anthropic Fellows Program 2026 + Greenhouse postings.
  - S73: Anthropic Frontier Red Team.
  - S74: Kyle Fish + model welfare + 80kh ep.
  - S75: Anthropic candidate AI guidance + Anthropic Interviewer.
  - S76: Levels.fyi + Glassdoor + Signalfire (comp + retention).
  - S77: Aggregator Anthropic interview guides (IGotAnOffer + interviewing.io
    + InterviewQuery + Jobright).
  - S78: Dwarkesh × Sholto + Trenton + Dario eps.
  - S79: Lex × Dario.
  - S80: 1Point3Acres Anthropic threads.
- New wiki pages added:
  - `wiki/topics/petri-and-auditing.md`.
  - `wiki/cross-lab/anthropic-alignment.md` (org + paper canon).
  - `wiki/cross-lab/anthropic-alignment-interview.md` (loop + Goncharov FP).
  - `wiki/cross-lab/openai-vs-anthropic.md` (comparison matrix for
    "why OpenAI" probe).
- Updated:
  - `wiki/topics/scheming-and-deceptive-alignment.md` — added
    Sleeper Agents, Agentic Misalignment, Petri sub-sections; cross-
    refs the new cross-lab page.
  - `wiki/topics/interpretability.md` — replaced thin "from
    Anthropic, but assumed knowledge" section with full canon
    (Crosscoders, Influence Functions, feature steering, engineering
    challenges) under S67.
  - `wiki/prep/why-openai.md` — added "Why OpenAI vs Anthropic"
    sub-section with three-step structure pointing at the cross-lab
    comparison page.
  - `wiki/prep/alignment-reading-list.md` — Tier-2 expanded with the
    Anthropic canon (Sleeper Agents, CAI, interp canon, Hidden
    Objectives, Petri, SHADE-Arena, Agentic Misalignment, sycophancy,
    many-shot jailbreaking, Recommended Directions, Bowman's writing,
    Perez essays, Hubinger stress-testing intro, FRT).
  - `wiki/questions/alignment-questions.md` — added "Cross-lab
    probes (Anthropic-comparison)" section with 7 specific question
    shapes; updated behavioral probes to point at cross-lab page.
  - `CLAUDE.md` — Mission updated to cover cross-lab framing;
    directory layout adds `wiki/cross-lab/`.
  - `index.md` — adds Topics: Petri & auditing; new Cross-lab
    section; raw-source list adds S56.
- Open follow-ups for next pass:
  - **Highest priority**: search YouTube directly for AXRP eps with
    Bowman / Olah, FAR.AI / EAG sessions on hiring criteria; the
    public-talks gap noted in S56 remains.
  - Reddit r/ControlProblem + r/MachineLearning Anthropic threads —
    direct site:reddit.com search.
  - EA Forum 2025 posts on Anthropic-offer experiences.
  - Ingest each new alignment.anthropic.com post as it lands.
  - DeepMind alignment loop — the comparison set should expand to
    GDM (Sundeep Teki [S6] covers it briefly; needs depth pass).
  - People profile pages: Bowman, Hubinger, Olah, Perez, Bricken,
    Fish — useful for individual-interviewer prep.
