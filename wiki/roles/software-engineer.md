# Software Engineer

The pure SWE loop at OpenAI (backend, infra, product, security) is
FAANG-scale rigor with an OpenAI-specific flavor: practical, production-
oriented coding instead of LeetCode-tricks; system design with
ML-system overtones; and a behavioral round with strong mission-fit
weight [S1, S2, S3, S5, S12].

## Loop shape

Aggregated from candidate write-ups [S2, S3, S5, S13]:

1. **Recruiter screen** (~30 min).
2. **Hiring-manager call** (~30 min) — for some teams.
3. **Coding phone screen** (~60 min, CoderPad) — one practical problem
   with multiple sub-parts. See [coding round](../rounds/coding.md).
4. **System design phone screen** (~45-60 min) — open-ended; "Design
   X" prompt; trade-offs and probing follow-ups. See
   [system design round](../rounds/system-design.md).
5. **Virtual onsite** (4-6 rounds, 1-2 days):
   - 1-2× **coding** (often a different question than the screen,
     longer, more sub-parts).
   - 1× **system design**.
   - 1× **deep dive** (project retrospective; staff levels: a 30-min
     **technical project presentation** with slides) [S3, S13].
   - 1-2× **behavioral / mission-fit** (at L5+ split into
     **leadership** and **collaboration**) [S3].
   - Optional **domain-specific** round (e.g., security, ML infra,
     distributed systems) [S3].
6. **Debrief and decision.**
7. **Offer.**

End-to-end: ~4-8 weeks at IC3-IC4; can stretch to 8-12 weeks at L5+
[S3, S5, S10].

## Coding bar [S2, S3, S4, S5, S12]

- 60-75 min per coding interview. Time management critical: many
  questions decompose into 3-5 sub-problems and time pressure is
  intentional.
- "Won't pass with 2/4 or low 3/4 on coding even if you ace everything
  else" — repeatedly reported on Blind and aggregator sites [S3, S11].
- Production-quality matters more than algorithmic elegance:
  invariants, error paths, edge cases, tests-on-the-side.
- LRU cache is canonical [S5, S12]. So is the time-based KV store and
  the simplified-SQL / in-memory-database family [S2, S4].

## System design bar [S3, S9]

- Open-ended prompts: Design Slack, Design Online Chess, Design
  GitHub Actions, Design a Payment System, Design ChatGPT.
- The first 5-10 min: clarify scale, read/write patterns, consistency
  needs. *Drive* the conversation.
- Trade-offs over name-drops: explain *why* a choice, not *which*
  technology.
- For ML-product teams the design will tilt toward serving infra,
  retrieval, evaluation, and feedback loops.

## What OpenAI explicitly recommends [S1]

The official guide tells SWE candidates:

- Be fluent in your strongest language, especially Python.
- Practice in CoderPad-style shared editors before the screen.
- Read the OpenAI engineering and research blogs.
- Expect "more code than a typical FAANG round".

## Cross-refs
- [Coding round](../rounds/coding.md)
- [System design round](../rounds/system-design.md)
- [Deep dive](../rounds/deep-dive.md)
- [Technical project presentation](../rounds/technical-project-presentation.md)
- [Behavioral](../rounds/behavioral.md)
- [Coding questions](../questions/coding-questions.md)
- [System-design questions](../questions/system-design-questions.md)

## Sources
S1, S2, S3, S4, S5, S9, S10, S11, S12, S13
