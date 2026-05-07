# ML Engineer (primary focus)

The ML Engineer (sometimes "Machine Learning Engineer", IC3-IC5; staff and
above use the L5/L6 labels at OpenAI) is the role this KB optimizes for.
The MLE loop sits between the SWE loop (which it heavily overlaps in coding
rigor) and the Research Engineer loop (which adds ML coding and paper
discussion). Expect a hybrid loop [S1, S6, S17, S18].

## End-to-end shape

Confirmed by S20 (verbatim recruiter emails for screens and onsite
rounds, on a real Feb-2025 ML-Engineer loop) and corroborated by
candidate / aggregator sources [S1, S2, S3, S5, S6, S17, S20]:

1. **Recruiter screen** (~30 min) — background, motivation, "why
   OpenAI", logistics.
2. **Hiring-manager call** (~30 min) — team fit, project preferences.
3. **Coding phone screen** (~60 min, CoderPad) — practical multi-part
   coding; see [coding round](../rounds/coding.md). Recurring
   problems: time-based KV store, GPU-credit accounting, in-memory DB,
   simplified spreadsheet API, resumable iterator, `cd` with symlinks,
   tree node-count over a per-node messaging API [S2, S4, S20].
4. **ML system design phone screen** (~60 min) — "ML Search Design"
   on S20's loop, focused on search/recsys/LLM-integration depth +
   open-ended ML question. See [ML search/recsys design]
   (../rounds/ml-search-design.md). Some teams substitute a general
   system-design or ML-coding screen [S5, S6, S20].
5. **Virtual onsite** (4-6 rounds, 1-2 days, 4-6 interviewers)
   [S1, S6, S20]:
   - **Coding** (sometimes two): same flavor as the screen, often longer
     and multi-part.
   - **ML coding** [S6, S19] (some loops) — implement attention or a
     model component from scratch in NumPy/PyTorch.
   - **ML debugging** [S20] — 60 min, fix all bugs in a small PyTorch
     model (canonical: a multi-headed transformer with 4-5 bugs); then
     a second part repurposing LLM training for classification.
     Verbatim recruiter description in
     [ml-debugging](../rounds/ml-debugging.md).
   - **ML system design / ML search design** [S5, S6, S17, S20] —
     fault-tolerant training pipeline, RAG, ChatGPT-at-scale, an
     evaluation harness, a recommender for personalized content.
   - **Project deep dive** [S3, S5, S20] — 45-min "Technical Deep
     Dive — ML Focus" with slides or virtual whiteboard. See
     [deep-dive-template](../prep/deep-dive-template.md).
   - **Behavioral** [S1, S3, S20] — ~85% Meta-Jedi-style behavioral
     (career trajectory, conflict resolution, feedback up/down) +
     ~15% OpenAI-specific (mission, AGI risk, trust/safety).
   - **XFN** [S20] — 30 min with a non-engineering counterpart on
     working with PMs and competing priorities. See
     [xfn](../rounds/xfn.md).
6. **Debrief** with hiring committee.
7. **Offer.**

End-to-end: ~4-8 weeks for IC3-IC4; ~8-12 weeks at L5+ [S5, S3, S10].

## Bar / signals

- **Coding density**: candidates consistently report typing for nearly
  the entire hour. Multiple sub-problems per question. Production-flavored
  code with proper structure and edge cases [S2, S4].
- **ML breadth + depth**: enough breadth to discuss any common building
  block (optimizers, normalization, attention, sampling) and enough depth
  to debug a broken loss curve. Sources stress *go deep, not wide* — the
  panel will follow up until they hit your floor [S17, S19].
- **Engineering-first ML**: the brand is "ML Engineer", with emphasis
  on engineering. ML knowledge is necessary but a candidate who can ship
  reliable, performant code beats a candidate with a stronger paper
  reading list [S6].
- **Mission fit**: explicit: "are you motivated by the AGI mission and
  comfortable with safety/quality friction?" [S1, S3].

## What OpenAI explicitly recommends

From OpenAI's public interview guide [S1]:

- **Deep Learning Book** (Goodfellow, Bengio, Courville) — for
  foundational ML.
- **Spinning Up in Deep RL** — for RL fundamentals.
- Read OpenAI's research blog and recent model/agent announcements;
  the panel will assume you know what they ship.

## Suggested rounds-to-page mapping

- [Coding round](../rounds/coding.md) → covers the SWE-flavored screens.
- [ML coding round](../rounds/ml-coding.md) → NumPy/PyTorch from-scratch.
- [ML debugging](../rounds/ml-debugging.md) → fix-the-broken-transformer.
- [ML system design](../rounds/ml-system-design.md) → training/serving
  systems.
- [ML search/recsys design](../rounds/ml-search-design.md) → for
  candidates with search/recsys backgrounds.
- [Deep dive](../rounds/deep-dive.md) → past-project retrospective.
- [Deep-dive slide template](../prep/deep-dive-template.md) → 7-section
  template + grading axes.
- [Behavioral](../rounds/behavioral.md) → mission-fit and collaboration.
- [XFN](../rounds/xfn.md) → cross-functional partner round.
- [Why OpenAI answer template](../prep/why-openai.md).
- [sysML & CUDA / Triton topic](../topics/sysml-and-cuda.md) →
  required for scaling / training-infra teams.

## Likely-asked questions (curated)

See [coding-questions](../questions/coding-questions.md),
[ml-questions](../questions/ml-questions.md), and
[system-design-questions](../questions/system-design-questions.md). The
"high-yield five" the MLE loop keeps surfacing across sources:

1. Implement a **time-based KV store** (LC-style, but with serialization
   and persistence follow-ups) [S2, S4].
2. Implement **scaled-dot-product attention** and then **multi-head
   attention** in NumPy or PyTorch [S6, S19].
3. **Design a fault-tolerant training pipeline** for a >100B-param model
   [S5, S6, S17].
4. **Design ChatGPT for 100M users** (or similar serving system at
   frontier scale) [S5, S9].
5. Diagnose a **broken training loop** (loss spikes, NaNs, gradient
   explosions, dead neurons) [S6, S19].

## Conflicts / notes

- *Loop length varies by team.* The Applied / Forward-Deployed teams
  report shorter loops weighted toward product-coding. Research-adjacent
  teams report more ML coding and paper discussion [S6].
- *"It's just FAANG"* is wrong: the coding bar is FAANG-grade, but the
  *flavor* differs (production vs. tricks), and behavioral failures kill
  more candidates than at most peers [S2, S3, S11].

## Cross-refs
- [Overview](../overview.md)
- [Research Engineer](research-engineer.md) — sibling loop, more research-leaning.
- [Software Engineer](software-engineer.md) — sibling loop, no ML coding.
- [Reading list](../prep/reading-list.md).
- [Timeline](../prep/timeline.md).

## Sources
S1, S2, S3, S4, S5, S6, S9, S10, S11, S17, S18, S19, S20, S23
