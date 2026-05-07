# Research Engineer (RE)

The Research Engineer is the role most candidates conflate with "ML
Engineer". At OpenAI in 2026, the RE role is the **research-adjacent
engineering hybrid**: you sit on a research team, write production-quality
code that runs experiments at scale, and co-own results with research
scientists [S6].

## Loop shape

Reported / aggregated [S1, S6, S19]:

1. **Recruiter screen** (~30 min).
2. **Hiring-manager call** with the research-team lead.
3. **2-hour initial screening** sometimes used: 1× ML design + 1× pandas/
   numpy-flavored coding [S6, S19].
4. **Onsite (4-6 rounds)**:
   - **Coding** — practical, production-quality (overlaps SWE round).
   - **ML coding** — implement a model component from scratch (attention
     is the canonical example) [S6, S19].
   - **ML debugging** — fix a broken training loop or eval; transformer-
     centered [S6].
   - **Deep dive** — your most impactful research/engineering project.
   - **Behavioral / mission-fit**.
5. **Optional domain-specific round** for ML infra / distributed
   systems / AI safety teams [S3].

## Where it sits relative to siblings

- **vs. ML Engineer**: more research-deep-dive and paper discussion,
  similar coding density. The MLE loop is more product-shaped.
- **vs. ML Researcher / MTS-R**: more coding rigor, less "research
  vision", similar ML breadth.
- **vs. SWE**: adds ML coding and ML debugging; subtracts at most one
  pure-SWE coding round.

## Sundeep Teki's framing of OpenAI vs. peers [S6]

- **OpenAI**: "pragmatic scalers" — coding-heavy, ship-fast,
  "engineering efficiency" is the dominant cultural theme.
- **Anthropic**: more safety/research framing; longer paper discussions.
- **DeepMind**: more theoretical depth; mathier interviews.

This is one researcher's framing, not gospel — but multiple secondary
sources echo the OpenAI "ship fast" framing [S5, S13].

## Bar / signals

- Implement a transformer block in <30 minutes without an internet lookup [S6, S19].
- Diagnose a misbehaving training loop with limited info [S6].
- Discuss your research at a level a peer scientist will probe — defend
  metric choices, ablations, and limitations [S5].
- Production-grade code: tests, edge cases, no hand-waving [S2, S6].

## Cross-refs
- [ML Researcher](ml-researcher.md)
- [ML Engineer](ml-engineer.md)
- [ML coding round](../rounds/ml-coding.md)
- [Transformers topic](../topics/transformers.md)
- [Reading list](../prep/reading-list.md)

## Sources
S1, S2, S3, S5, S6, S13, S19
