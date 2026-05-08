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
