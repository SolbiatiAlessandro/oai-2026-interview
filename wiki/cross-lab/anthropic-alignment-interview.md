# Anthropic Alignment Researcher / MTS – interview loop

Cross-lab page documenting Anthropic's alignment-research interview
process. Useful for the candidate even though primary target is
OpenAI: (a) the loops differ in important ways and the comparison
itself is a behavioral probe, (b) Anthropic publishes more on its
hiring criteria than OpenAI, (c) the **Goncharov first-person
account** [S71] is the cleanest first-person AI-safety-lab loop
writeup publicly available. [S56]

## Loop snapshot (composite, 2025-26)

7 stages. Triangulated across IGotAnOffer, interviewing.io,
InterviewQuery, Goncharov FP, Glassdoor, 1Point3Acres, Anthropic
careers [S56, S71, S77, S80].

1. **Recruiter screen** (30-45 min). Background, "why Anthropic", how
   your work maps to Alignment Science focus areas.
2. **Online coding** (90 min CodeSignal) **OR** 60-min live coding.
   Tiny problem bank (~6 problems). Style: pure problem-solving,
   concurrency recurring. Goncharov reports an automated API-
   implementation challenge with **four progressive levels**, scored
   on speed > optimality.
3. **Hiring-manager / face-to-face technical** (60 min). LeetCode-
   medium in some loops; on alignment-track often substituted with a
   research deep-dive.
4. **Research presentation / deep-dive** (60-90 min). Present own
   work or analyze a recent Anthropic paper. Panel grills on
   hypothesis formation, experimental design, ablations, broader-
   safety implications. Successful candidates show **independent
   thought + acknowledge limitations**, not recitation [S77].
5. **Take-home** (sometimes; Fellowship variant ~5 hours). Goncharov
   reports a 5-hour API-exploration take-home on the Fellowship
   track; assessed for *creativity*, not just correctness. Anthropic's
   candidate-AI-guidance page [S75] explicitly says: do NOT use
   Claude on take-homes unless told otherwise.
6. **Virtual onsite — 4-5 sessions, ~1 hour each.** Composition
   varies by team but typically:
   - Coding / pair-programming.
   - ML system design (training systems, eval design).
   - ML theory / safety research round.
   - **Research brainstorm** (15-30 min on-the-spot ideation with a
     senior alignment scientist or head of alignment — **Goncharov's
     reported failure mode**).
   - **Values / culture-fit final round** — reported as the **#1
     single-source of failures** [S77].
7. **References — heavy.** Both written and live calls. Multiple
   sources call this stage "not a formality".

End-to-end: 3-5 weeks (SWE avg ~19 days; alignment longer due to
panel scheduling).

## Goncharov first-person account [S71]

The clearest first-person AI-safety-lab loop writeup publicly
available, even though it's a *failure* report (which is precisely
why it's high signal — successful-candidate writeups are rarer and
self-curated).

Stages he reports:

- Recruiter screen.
- Automated coding challenge: **four progressive levels** of API
  implementation; scored on speed > optimality.
- 5-hour take-home for the Fellowship track: API exploration, marked
  on creativity.
- Virtual onsite: research brainstorm + values/culture round.

**His failure mode**: research brainstorm with the head of alignment
— 15-30 min on-the-spot ideation, framed as "given problem X, what
research would you do?". He went too deep on one direction and didn't
demonstrate range.

**Lesson**: rehearse rapid research brainstorms. Practice "given
this open problem, here are 3 directions ranked by tractability and
expected value, and here's the falsification I'd run for #1 first."

## Distinctively probed topics

(Beyond what's on the OpenAI alignment loop — see
`wiki/roles/alignment-researcher.md`.)

- **Mech interp depth** — well above OpenAI's bar [S56, S67]. SAEs,
  superposition, monosemanticity, crosscoders, induction heads.
  May show a circuit and ask you to interpret. Reading:
  `transformer-circuits.pub` end-to-end.
- **Auditing methodology / model-organisms** — given Hidden
  Objectives [S64], Auditing Game replication, and Petri [S57],
  expect "design an audit for behavior X". Bowman's *many largely-
  independent lines of defense* framing [S68] is canonical.
- **Agentic / threat-model** — Frontier Red Team scenarios:
  "Claude has access to a corporate email server, what evals run
  before deploy?". SHADE-Arena-style sabotage detection [S63].
  Agentic-misalignment results [S62].
- **Constitutional AI / RLAIF** [S61] — be ready for "what would
  you change about CAI" and trade-offs vs RLHF.
- **Sycophancy / sandbagging / scheming** — Sharma sycophancy
  paper [S66]; *Automated Researchers Can Subtly Sandbag* [S58];
  *Alignment Faking* [S37].
- **Many-shot jailbreaking** [S65] — adversarial-robustness
  regime; pairs with OpenAI Instruction Hierarchy [S32].
- **Model welfare** [S74] — emerging; expect at least one question
  on whether you'd take it seriously.
- **"Why Anthropic vs OpenAI vs DeepMind"** — see
  [openai-vs-anthropic](openai-vs-anthropic.md). Critical:
  candidates are expected to **disagree** with parts of Anthropic's
  strategy, not just praise it [S77].

## Hiring-criteria public signals

- **Sam Bowman's FAQ + Checklist** [S68] — canonical "what does
  Anthropic look for / what does success look like" reference.
- **Anthropic Recommended Directions** [S58] — tasting menu of open
  problems candidates engage with.
- **Anthropic Fellows Program 2026** [S72] — May & July cohorts;
  $3,850/wk + $15k/mo compute; no PhD required.
- **Ethan Perez's project-selection + empirical-tips essays** [S69].
- **Anthropic candidate AI guidance** [S75] — explicit policy on AI
  use in interviews.

## Comp band (Levels.fyi 4/27/2026) [S76]

- Research Scientist median ~$746K, top reported $1.05M (single
  self-report).
- SF-specific bands $555K-$741K+.
- 2-year retention reported ~80% (Signalfire); higher than OpenAI's
  reported ~67%. Note: Signalfire-only, not independently audited.
- Press: Fortune Aug 4 2025 covers Dario refusing Meta $100M
  poaching match.

## Reading priority (Anthropic-specific)

Tier 1 — non-negotiable:

1. Bowman's FAQ + *The Checklist* [S68].
2. Anthropic Recommended Directions [S58].
3. Sleeper Agents [S60] + Alignment Faking [S37].
4. Constitutional AI [S61].
5. The interpretability canon: Toy Models of Superposition →
   Towards Monosemanticity → Scaling Monosemanticity → Crosscoders
   [S67].
6. Petri release post + tech report [S57].
7. Auditing LMs for Hidden Objectives [S64].
8. SHADE-Arena [S63].
9. Agentic Misalignment [S62].
10. Cross-lab safety eval [S43].

Tier 2:

- Ethan Perez essays [S69].
- Hubinger's Alignment Stress-Testing intro [S70].
- AXRP #39 (Hubinger, model organisms) [S49].
- Sycophancy [S66] + Many-Shot Jailbreaking [S65].
- Goncharov's failure writeup [S71] — for loop calibration.
- Dwarkesh × Sholto + Trenton episodes [S78].

## Cross-refs
- [Anthropic alignment overview](anthropic-alignment.md)
- [OpenAI vs Anthropic comparison](openai-vs-anthropic.md)
- [Petri & auditing](../topics/petri-and-auditing.md)
- [Researcher, Alignment role (OpenAI)](../roles/alignment-researcher.md)
- [Why OpenAI answer template](../prep/why-openai.md)
- [Alignment questions bank](../questions/alignment-questions.md)

## Sources
S32, S37, S43, S49, S56-S58, S60-S78, S80
