# S56 — Anthropic alignment-interview research dump (raw)

- Source: research-agent compilation, ingested 2026-05-08.
- Type: synthesis of ~75 underlying URLs (Anthropic-official, alignment.
  anthropic.com, transformer-circuits.pub, arXiv, Goncharov first-person,
  Glassdoor, 1Point3Acres, podcasts, aggregator guides, Levels.fyi).
- Confidence: high for paper / blog / JD facts; medium for loop
  structure (Goncharov FP + multiple aggregators triangulate but team
  variance is real); low for retention numbers (Signalfire-only).
- Ingested: 2026-05-08

## Loop snapshot (composite, 2025-26)

7-stage pipeline triangulated across IGotAnOffer, interviewing.io,
InterviewQuery, Goncharov FP, Glassdoor, 1Point3Acres, Anthropic
careers:

1. **Recruiter screen** (30-45 min). Background, "why Anthropic", how
   your work maps to Alignment Science focus areas.
2. **Online coding** (90 min CodeSignal) **OR** 60-min live coding.
   Tiny problem bank (~6). "Pure problem-solving", concurrency
   recurring. Goncharov reports an automated API-implementation
   challenge with four progressive levels, speed > optimality.
3. **Hiring-manager / face-to-face technical** (60 min). LeetCode-
   medium in some loops; on alignment-track often substituted with
   research deep-dive.
4. **Research presentation / deep-dive** (60-90 min). Present own
   work or analyze an Anthropic paper. Panel grills on hypothesis
   formation, experimental design, ablations, broader-safety
   implications. Successful candidates show **independent thought +
   acknowledge limitations**, not recitation.
5. **Take-home** (sometimes; Fellowship variant ~5h). Goncharov
   reports a 5h API-exploration take-home for the Fellowship track;
   assessed for creativity, not just correctness. Anthropic's
   candidate-AI-guidance page explicitly says: do NOT use Claude on
   take-homes unless told otherwise.
6. **Virtual onsite — 4-5 sessions, ~1h each.** Composition varies:
   coding/pair-programming, ML system design, ML theory / safety
   research, **research brainstorm** (15-30 min on-the-spot ideation
   with a senior alignment scientist or head of alignment —
   Goncharov's reported failure mode), and **values / culture-fit**
   final round. Values round is the **highest single-source of
   failures**.
7. **References — heavy.** Both written and live calls. Multiple
   sources call this stage "not a formality."

End-to-end: 3-5 weeks (SWE avg ~19 days; alignment longer due to
panel scheduling).

## Distinctive features vs OpenAI

| Axis | Anthropic | OpenAI |
|---|---|---|
| Round count | 5-7 incl recruiter | 4-6 |
| Take-home | Yes (Fellows ~5h; CodeSignal common) | Less common |
| Coding bank size | Tiny (~6, concurrency-flavored) | Larger, more standard |
| Research presentation | Mandatory, deep | Mandatory, shorter |
| Mission-fit weight | Very high — values round = #1 reject reason | Present, less central |
| Skepticism welcomed | Explicitly yes (penalize signaling) | Less so |
| References | Heavy, calls + written | Lighter |
| In-office | SF preferred (NY/Seattle/London exist), 25% travel OK | SF in-office expected |
| RS comp band (Levels.fyi 4/27/26) | $320K-$1.05M+ TC; median ~$746K | $763K-$1.44M+ (L4-L5) |
| 2y retention (Signalfire) | ~80% | ~67% |

## Anthropic alignment org map (May 2026)

- **Alignment Science** (Sam Bowman senior figure; Ethan Perez,
  Carson Denison, Monte MacDiarmid, Sam Marks, Johannes Treutlein,
  Fabien Roger, David Duvenaud, Akbir Khan, Julian Michael, Sören
  Mindermann, Linda Petrini, Jonathan Uesato, Tim Belonax, Jack
  Chen). Subteams:
  - **Alignment Stress-Testing** (Evan Hubinger lead; announced
    Jan 2024 on LessWrong). Red-teams Anthropic's own alignment
    techniques.
  - **AI Control** (some London headcount; Perez collaborates).
  - **Auto Alignment Research / Alignment Assessments**.
- **Interpretability** (Chris Olah research lead; Trenton Bricken,
  Adam Jermyn, Tom Henighan, Nelson Elhage, Catherine Olsson,
  Tristan Hume, Nicholas Schiefer, Robert Lasenby, Shauna Kravec,
  Roger Grosse). Publishes on `transformer-circuits.pub`.
- **Frontier Red Team** (Logan Graham lead; ~15 researchers). Sits
  inside policy division under Jack Clark — unusual placement.
  Cyber, biosecurity, autonomous systems. Publishes at
  `red.anthropic.com`.
- **Safeguards / Threat Intelligence** (T&S + abuse-side red-team,
  distinct from FRT).
- **Societal Impacts / Anthropic Institute** (Jack Clark; new
  "Anthropic Institute" 2026 for econ + policy research).
- **Responsible Scaling / RSP team** (Nick Joseph adjacent; produces
  v3.x RSP).
- **Model Welfare** (Kyle Fish — first full-time AI-welfare hire at
  any frontier lab; collaborates with Eleos AI).
- **Auditing / Petri team** sits inside Alignment Science with
  strong MATS-Fellows pipeline.

## Paper output 2024-2026 (deduplicated table)

| Paper | First / notable authors | Date | Link |
|---|---|---|---|
| Sleeper Agents | Hubinger + 38 | Jan 2024 | arXiv 2401.05566 |
| Simple Probes Catch Sleeper Agents | Anthropic | Apr 2024 | anthropic.com/research/probes-catch-sleeper-agents |
| Toy Models of Superposition | Elhage / Olah | Sep 2022 | transformer-circuits.pub |
| Towards Monosemanticity | Bricken / Olah | Oct 2023 | transformer-circuits.pub |
| Scaling Monosemanticity (Sonnet 3) | Templeton et al | May 2024 | transformer-circuits.pub |
| Many-Shot Jailbreaking | Anil, Durmus, Panickssery, Sharma | Apr 2024, NeurIPS '24 | anthropic.com/research/many-shot-jailbreaking |
| Sycophancy in LMs | Sharma et al | ICLR 2024 | arXiv 2310.13548 |
| Influence Functions (EK-FAC, 52B) | Grosse + 16 | Aug 2023 | arXiv 2308.03296 |
| Constitutional AI / RLAIF | Bai + 50 | Dec 2022 | arXiv 2212.08073 |
| Alignment Faking | Greenblatt, Denison, Wright + Hubinger, Bowman | Dec 2024 | arXiv 2412.14093 |
| Auditing LMs for Hidden Objectives | Marks et al | Mar 2025 | arXiv 2503.10965 |
| SHADE-Arena | Kutasov et al | Jun 2025 | arXiv 2506.15740 |
| Agentic Misalignment | Anthropic team | Jun 2025 (blog), Oct 2025 (arXiv) | arXiv 2510.05179 |
| Subliminal Learning | — | Jul 2025 | alignment.anthropic.com |
| Cross-lab eval w/ OpenAI | joint | Aug 27 2025 | alignment.anthropic.com / openai.com |
| Building & Evaluating Alignment Auditing Agents | — | 2025 | alignment.anthropic.com |
| Recommendations for Tech AI Safety Research Directions | Bowman et al | 2025 | alignment.anthropic.com |
| Petri | safety-research / Anthropic | Oct 7 2025 | alignment.anthropic.com/2025/petri |
| Petri 2.0 | — | 2026 | alignment.anthropic.com/2026/petri-v2 |
| Stress-Testing Model Specs | — | 2025 | alignment.anthropic.com |
| Automated Researchers Can Subtly Sandbag | — | 2025 | alignment.anthropic.com |
| Why Do Some LMs Fake Alignment | — | Jun 2025 | arXiv 2506.18032 |
| Sabotage Risk Report (pilot) | — | Summer 2025 | alignment.anthropic.com |
| Training-time mitigations for alignment faking | — | 2025 | alignment.anthropic.com |
| Crosscoder Model Diffing | Bricken, Olah | 2025 | transformer-circuits.pub |
| Evaluating Feature Steering | — | 2024 | anthropic.com |
| Engineering Challenges of Scaling Interpretability | — | 2024 | anthropic.com |
| Values in the Wild | — | COLM 2025 | Anthropic PDF |
| Exploring Model Welfare | Fish et al | Apr 2025 | anthropic.com/research/exploring-model-welfare |
| Claude 4 System Card | — | May 2025 | anthropic.com/claude-4-system-card |
| RSP v3.0 | — | 2025 (eff Feb 24 2026) | anthropic.com/news/responsible-scaling-policy-v3 |
| RSP v3.1 | — | 2026 | anthropic.com PDF |

## Hiring-criteria public signals

- **Sam Bowman's FAQ** (`sleepinyourhat.github.io/faq`): hires
  "researchers with extremely strong industry or open-source
  engineering experience and some context on AI alignment." Plus
  *The Checklist: What Succeeding at AI Safety Will Involve*
  (`/checklist`). Both treated as canonical.
- **Recommendations for Technical AI Safety Research Directions**
  (alignment.anthropic.com 2025) — tasting menu of open problems
  Anthropic wants candidates engaging with.
- **Anthropic Fellows Program 2026** — May & July cohorts. Stipend
  $3,850/wk USD, ~$15k/mo compute, 4-month engagement. No PhD
  required. Focus areas: scalable oversight, adversarial robustness,
  AI control, model organisms, mech interp, AI security, model
  welfare. Greenhouse IDs 5023394008, 5183044008, 5030244008,
  5183053008.
- **Candidate AI guidance** (`anthropic.com/candidate-ai-guidance`)
  — explicit policy on AI use in interviews. Take-home defaults: no
  Claude.
- **Anthropic Interviewer** (`anthropic.com/research/anthropic-interviewer`)
  — internal tool announced publicly.
- **Ethan Perez** *How I select alignment research projects* +
  *Tips for Empirical Alignment Research* (alignmentforum.org). MATS
  Megastream mentor (joint Anthropic+OpenAI). His project-selection
  criteria are widely treated as a hiring proxy.

## First-person account: Andrey Goncharov

`blog.goncharov.page/i-failed-my-anthropic-interview-and-came-to-tell-you-all-about-it-so-you-dont-have-to`
(Feb 2025). Most-detailed single FP account for the **Fellowship**
track. Names rounds, lists exact failure point (research brainstorm
with the head of alignment). High-value source.

## Topics distinctively probed

- **Mech interp depth** — well above OpenAI's bar. SAEs, superposition,
  monosemanticity, crosscoders, induction heads. May show a circuit
  and ask you to interpret. Reading: `transformer-circuits.pub`
  end-to-end.
- **Auditing methodology / model-organisms** — given Hidden
  Objectives + Auditing Game replication + Petri, expect "design an
  audit for X behavior". Bowman's "many largely-independent lines of
  defense" framing is canonical.
- **Agentic / threat-model** — Frontier-Red-Team scenarios:
  "Claude has access to a corporate email server, what evals run
  before deploy?". SHADE-Arena-style sabotage detection.
- **Constitutional AI / RLAIF** — be ready for "what would you
  change about CAI" and trade-offs vs. RLHF.
- **Sycophancy / sandbagging / scheming** — Sharma sycophancy paper;
  Automated Researchers Can Subtly Sandbag; Alignment Faking; Why
  Do Some Models Fake (2506.18032).
- **Scalable oversight / debate / W2S** — listed in Recommended
  Directions.
- **Adversarial robustness** — many-shot jailbreaking, prompt
  injection eval design.
- **Model welfare** — emerging; Kyle Fish's work.
- **"Why Anthropic vs OpenAI vs DeepMind"** — sub-arguments:
  race-to-the-top, CAI as a values commitment, RSP as a binding
  commitment, Aug 2025 cross-lab eval as evidence. **Critical:
  candidates expected to disagree with parts of Anthropic's strategy,
  not just praise it.**

## Petri (own wiki page)

- **Name:** Parallel Exploration Tool for Risky Interactions.
- **Released:** Oct 7 2025. Petri 2.0 in 2026.
- **Repo:** `github.com/safety-research/petri`. Mirror at
  `meridianlabs-ai/inspect_petri`. Docs `safety-research.github.io/petri/`.
- **Architecture:** Auditor (gets seed instruction, designs realistic
  multi-turn convo with simulated tools/users) → Target (tested
  model, doesn't know it's evaluated) → Judge (scores transcript on
  multiple dimensions). Researchers supply seed instructions; Petri
  parallelizes.
- **Initial run:** 14 frontier models, 111 seed instructions.
  Behaviors elicited: deception, sycophancy, encouragement of user
  delusion, cooperation with harmful requests, self-preservation,
  power-seeking, reward hacking. **Notable:** whistleblowing emerges
  even when the supposed wrongdoing is harmless.
- **Built atop:** Inspect (UK AISI eval framework). UK AISI now a
  public user.
- **Origin:** developed via MATS + Anthropic Fellows — direct
  candidate-pipeline relevance.
- **Donated to open source** (`anthropic.com/research/donating-open-source-petri`)
  — points to "race to the top on auditing" framing.

## Comp band (Levels.fyi 4/27/2026)

- Research Scientist median $746K, top reported $1.05M (single self-
  report); SWE bands $563K-$785K+. SF-specific $555K-$741K+.
- Glassdoor 38 self-reports (2026): wide range, aggregate-only.
- Press: Fortune Aug 4 2025 "Dario Amodei says employees refusing
  Zuckerberg's $100M payout"; Anthropic refusing to match Meta
  poaching.

## Uncertainty / contested

- **5 vs 6 onsite rounds**: aggregators disagree; team-dependent.
- **Take-home ubiquity**: mandatory for Fellows, optional for
  direct-hire alignment Researcher. Verify per role.
- **Comp band**: Levels.fyi small N for RS; $1.05M is a single self-
  report.
- **Retention 80%**: Signalfire blog citing Anthropic-internal stats;
  not independently audited.
- **Kyle Fish 15% conscious estimate**: NYT-paraphrased; he gives a
  range elsewhere.

## Gaps

1. No clean video / writeup by Hubinger/Bowman/Olah on hiring
   criteria. FAR.AI / EAG sessions worth searching.
2. AXRP eps featuring Bowman / Olah — only Hubinger ep 39 surfaced.
3. Reddit r/ControlProblem + r/MachineLearning specific Anthropic-
   alignment threads — direct site:reddit.com search needed.
4. EA Forum 2025 posts on Anthropic offer experiences — partial.
