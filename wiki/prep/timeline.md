# Timeline & study plan

Concrete week-by-week prep templates. Choose the variant that matches
your role and starting point.

## Variant A — 4 weeks, ML Engineer / RE (full-time prep)

Modeled on Tomotake Zata's reported plan [S5] and the role-specific
expectations in [ml-engineer](../roles/ml-engineer.md).

### Week 1 — coding foundations

- Day 1-2: Implement LRU cache, time-based KV store, KV
  serialize/deserialize. Practice in CoderPad sandbox [S2, S5, S12].
- Day 3-4: In-memory SQL DB, spreadsheet API with cycle detection
  [S2, S4].
- Day 5-7: Resumable iterator, GPU credit accounting, multithreaded
  web crawler [S2, S4]. End-of-week: full 60-min mock with one of
  the above.

### Week 2 — ML coding & ML breadth

- Day 1-2: Scaled-dot-product attention + multi-head attention from
  scratch in NumPy and PyTorch [S6, S19].
- Day 3: Tiny transformer block; minimal training loop [S6].
- Day 4: ML breadth drills: optimizers, regularization, batch/layer/
  RMS norm, mixed-precision pitfalls [S19].
- Day 5: ML debugging scenarios — NaN losses, frozen training,
  throughput collapse [S6, S19].
- Day 6-7: Skim *Attention Is All You Need*, FlashAttention, vLLM
  paged-attention, ZeRO. Re-implement attention with FlashAttention-
  style tiling on paper [S19].

### Week 3 — system design

- Day 1: Capacity-estimation drill (back-of-envelope math) on 5
  designs.
- Day 2: Design Slack; Design GitHub Actions; Design webhook system
  [S3].
- Day 3: Design ChatGPT for 100M users [S3, S5].
- Day 4: Design fault-tolerant training pipeline at >100B params
  [S5, S6, S17].
- Day 5: Design eval pipeline for a frontier reasoning model;
  Design a RAG system [S6, S17].
- Day 6-7: Two full 45-min mock system-design sessions with a peer.

### Week 4 — deep dive, behavioral, mocks

- Day 1: Pick the deep-dive project; build a 3-slide skeleton; draft
  the trade-off justification [S3, S5].
- Day 2: Behavioral STAR stories — 6 stories spanning disagreement,
  failure, prioritization, quality/safety, mentorship,
  research-eng collab [S1, S3].
- Day 3: "Why OpenAI" — write a non-generic answer [S1, S3].
- Day 4-5: Two full mock loops with a friend (1× coding, 1× ML
  coding, 1× system design, 1× deep dive, 1× behavioral).
- Day 6: Read recent OpenAI launches and one current paper of
  interest [S1, S6].
- Day 7: Light review and rest before the loop.

## Variant B — 8 weeks, working full-time (≈12 hrs/week)

Same content, half-pace:

- Weeks 1-2: coding foundations.
- Weeks 3-4: ML coding + ML breadth.
- Week 5: deep dive + behavioral.
- Weeks 6-7: system design.
- Week 8: full mock loop and review.

## Variant C — Software Engineer (no ML coding)

Drop the ML-coding week from Variant A. Replace with a second coding
week and an extra system-design week:

- Weeks 1-2: coding (extended set: graphs, recursion, concurrency,
  in-memory databases).
- Weeks 3-4: system design.
- Week 5: deep dive + behavioral.
- Week 6: mock loop + review.

## Cross-cutting

### Daily hygiene

- 30 min of typed CoderPad practice (any problem). Build hand-on-
  keyboard fluency [S5].
- 15 min of skim-reading: one OpenAI blog post, one paper abstract.
- One STAR-story rehearsal aloud; record it on day-of-mock.

### Mocks

Two real mocks per week is the cadence repeatedly cited [S5, S13].
Use peers from Pramp / interviewing.io for system design and a
friend for ML coding (peer who'll push back is more useful than a
stranger).

### Day-before and day-of

- Day before: light review of canonical questions, no new content.
- Day of: re-read OpenAI charter, your STAR stories, your deep-dive
  one-pager. Sleep is the highest-EV preparation [S5, S13].

## Cross-refs
- [Reading list](reading-list.md)
- [ML Engineer role](../roles/ml-engineer.md)
- [Software Engineer role](../roles/software-engineer.md)
- [Behavioral round](../rounds/behavioral.md)

## Sources
S1, S2, S3, S4, S5, S6, S12, S13, S17, S19
