# S24 — Alignment Researcher research dump (raw)

- Source: research-agent compilation, ingested 2026-05-08.
- Type: synthesis of ~40 underlying URLs (official OpenAI, arXiv, news,
  podcasts, LessWrong/Alignment Forum, candidate-experience aggregators,
  Levels.fyi).
- Confidence: high for paper / blog / job-posting facts; **low for the
  alignment-loop-specific structure** — no clean first-person
  Alignment Researcher loop writeup exists publicly as of May 2026.
- Ingested: 2026-05-08

## Loop (synthesized — flag low confidence on structure)

No first-person Alignment Researcher writeup was found on Glassdoor,
Blind, 1Point3Acres, LessWrong, Alignment Forum, or Substack as of
May 2026. The reconstructed loop is built from (a) the official job
description, (b) general OpenAI Researcher loop reporting (S1-S20),
and (c) candidate accounts of adjacent ML-Researcher / Research
Engineer loops.

Reconstructed:

1. **Recruiter screen** (30-45 min). "Why OpenAI / why alignment" is
   probed harder than for SWE/MLE.
2. **Hiring-manager screen** with the team lead. As of Feb 2026, this
   is now typically Post-Training / Safety Systems / Misalignment
   Research / Alignment Science / Alignment Training, since *Mission
   Alignment* was disbanded.
3. **Coding screen** in CoderPad (same gated production-coding format
   used elsewhere — confirms across S2/S3/S20).
4. **ML coding / ML breadth** — implementing transformer / attention /
   RLHF or DPO loss / scalable-oversight loop from scratch.
5. **Research / paper presentation** (45-60 min) — present a prior
   alignment / ML project; expect probing on choices, ablations,
   alternatives, "what would you do next?".
6. **Alignment-specific technical** — discussion / whiteboard. Likely
   shapes: design an evaluation, critique a recent alignment paper,
   propose a research direction, walk through a threat model.
7. **Behavioral / mission-fit** — heavier than for SWE. Reported
   prompts include "why OpenAI vs Anthropic / SSI", "what would you
   do if you found a model behaving in a misaligned way during
   training?".
8. Some loops include a **48-hour take-home** — more often for
   engineering than research tracks.

End-to-end: 4-8 weeks. Onsite: 4-6 hours over 1-2 days. Tooling:
CoderPad standard.

## Org map (May 2026)

Two organizational shocks that reshape the team layout:

- **May 2024** — Superalignment dissolved after Sutskever and Leike
  resigned. (cnbc.com / axios coverage.)
- **Feb 11, 2026** — *Mission Alignment* (~7 people, headed by
  Joshua Achiam, formed late-2024) disbanded. Achiam → **Chief
  Futurist** with Jason Pruet. (TechCrunch, Platformer, Business
  Today, WinBuzzer.)

Where alignment work lives now (May 2026), reconstructed from the
public job postings:

- **Researcher, Alignment** (the candidate's role). Training-time
  alignment of frontier models; ships into post-training. Boaz Barak
  (Harvard, part-time at OpenAI since Fall 2025) is associated with
  this work; co-author on Deliberative Alignment.
- **Researcher, Alignment Science** — separate posting; ran the
  December 2025 launch of `alignment.openai.com`.
- **Researcher, Alignment Training** — separate posting; post-
  training-flavored.
- **Researcher, Misalignment Research (NYC)** — model-organisms-style
  work; partners with Apollo Research.
- **Safety Systems** — operational deployed safety stack
  (red-teaming, deployment evals, refusal training). Lilian Weng was
  VP until Nov 2024.
- **Preparedness** — catastrophic-capability evals (CBRN, cyber,
  autonomy, persuasion). Aleksander Mądry led; transitioned out
  July 2024. Preparedness Framework v2 published April 2025.
  **Head of Preparedness role open as of Dec 2025**, comp ~$555K
  reported.
- **Model Behavior** — Joanne Jang, founding lead, owned the Model
  Spec until Sept 2025 reorg. Folded into Post-Training under Max
  Schwarzer; Jang departed early 2026 to launch OAI Labs.

## Flagship alignment papers / posts (2024-2026)

(Full URLs in `sources/sources.md` under S30-S55.)

- **Weak-to-strong generalization** — Burns et al., Dec 2023, arXiv
  2312.09390. Authors: Burns, Leike, Aschenbrenner, Wu, Izmailov, Gao,
  Baker, Kirchner. Foundational.
- **Deliberative alignment** — Guan et al., arXiv 2412.16339,
  Dec 2024. The o-series alignment paradigm: train the model to reason
  over a written safety spec at inference time.
- **Safe completions (GPT-5)** — Aug 2025. Output-centric reward
  replaces refusal training; widely viewed as the successor to
  deliberative alignment for the GPT-5 series.
- **Instruction Hierarchy** — Wallace et al., arXiv 2404.13208,
  Apr 2024 (ICLR 2025). Privileged-instruction policy that hardens
  models against prompt injection.
- **Sparse autoencoders / scaling SAEs on GPT-4** — Gao et al.,
  arXiv 2406.04093, Jun 2024. 16M-latent SAE on GPT-4.
- **CriticGPT** — McAleese et al., arXiv 2407.00215. Scalable-
  oversight result for code review.
- **Detecting and reducing scheming** — Sept 2025 OpenAI × Apollo
  Research. Anti-scheming training reduced misbehavior ~30× on
  o3/o4-mini. arXiv 2509.15541.
- **CoT monitoring** — arXiv 2503.11926 (Bowen Baker et al., Mar
  2025). Cross-lab "Chain of Thought Monitorability" arXiv
  2507.11473 signed by OpenAI/Anthropic/DeepMind.
- **Sycophancy in GPT-4o** — April 2025 incident + retrospective.
- **Alignment Faking** — Greenblatt et al. arXiv 2412.14093.
- **AI Control** — Greenblatt et al. arXiv 2312.06942.
- **System cards (safety sections):** o1 (Dec 2024), o3-mini
  (Jan 31 2025), GPT-4.5 (Feb 27 2025), o3/o4-mini (Apr 16 2025),
  GPT-5 (Aug 13 2025), gpt-oss (Aug 5 2025).
- **Anthropic ↔ OpenAI cross-lab safety eval** — Aug 2025 pilot.
- **alignment.openai.com blog** — launched Dec 1 2025 ("Hello
  World"). Dec 2025 posts: "Helpful assistant features suppress
  emergent misalignment", "Sidestepping Evaluation Awareness…",
  "Debugging misaligned completions with sparse-autoencoder latent
  attribution", "A Practical Approach to Verifying Code at Scale".
- **Collective alignment / Model Spec public input** (Aug 2025).
  Latest Model Spec: 2025-12-18.
- **Updated Preparedness Framework v2** (Apr 2025).
- **Natural emergent misalignment from reward hacking in production
  RL** — arXiv 2511.18397.

## Topical depth expected (synthesis)

- **Post-training**: SFT → RLHF (PPO + KL) → DPO → GRPO; KTO/DAPO at
  the level of "what problem they solve". Derive DPO from RLHF
  objective. Why GRPO drops the critic and uses group-relative
  advantages.
- **Reward hacking** — Goodhart, length bias, sycophancy as reward
  hacking. Lilian Weng's Nov 2024 "Reward Hacking in RL" post still
  cited inside OpenAI as the canonical writeup.
- **Scalable oversight** — debate, recursive reward modeling, weak-to-
  strong, CriticGPT.
- **Mechanistic interpretability** — superposition, features, sparse
  autoencoders (k-sparse, top-k, JumpReLU), circuits, activation
  patching. Neel Nanda's prereq guide and "Concrete Steps to Get
  Started" + ARENA curriculum are canonical.
- **Eval design for safety** — capability elicitation, METR's ARA,
  agentic evals, contamination, sandbagging-aware design.
- **AI control** (Greenblatt) — distinguish *alignment* from
  *control*; trusted/untrusted-model setup, monitoring, resampling.
- **Deceptive alignment / scheming** — Hubinger "Risks from Learned
  Optimization"; Greenblatt "Alignment faking"; Apollo "Frontier
  models capable of in-context scheming"; OpenAI Sept 2025 anti-
  scheming.
- **Threat models** — situational awareness, gradient hacking,
  sandbagging, training-game; Preparedness CBRN/cyber/autonomy/
  persuasion.

## People (publicly visible alignment-side at OpenAI)

- **Boaz Barak** — Harvard / OpenAI part-time. Active on X. Most
  visible academic-ish alignment hire post-Superalignment.
- **Joshua Achiam** — Chief Futurist (since Feb 2026); previously
  ran Mission Alignment.
- **Bowen Baker** — first author "Detecting misbehavior in frontier
  reasoning models"; CoT-monitoring agenda.
- **Jeff Wu** — co-author Weak-to-Strong; long-tenure alignment
  team.
- **Leo Gao** — sparse-autoencoder lead; LessWrong / Alignment Forum
  presence.
- **Nat McAleese** — first-author CriticGPT.
- **Pavel Izmailov, Jan Hendrik Kirchner, Collin Burns** — W2S paper
  authors still relevant.
- **Jakub Pachocki** — Chief Scientist (post-Sutskever).

Departed but still cited in the room: Sutskever (SSI), Leike
(Anthropic), Lilian Weng, John Schulman (Anthropic → Thinking
Machines), Mira Murati, Aschenbrenner, Mądry.

## Comp band (Levels.fyi, May 2026)

- Research Scientist L4 ~$771K total comp.
- L5 ~$1.0-1.47M (median ~$1.0M).
- "Alignment Researcher" specifically not broken out — assume RS
  band. PPU valuation moves the headline number.

## Gaps / uncertainty

- **No clean first-person Alignment Researcher loop writeup**.
  Highest gap.
- **Org chart is unstable** — Mission Alignment Feb 2026; Model
  Behavior Sept 2025; Preparedness head vacant. Any definitive map is
  stale within months.
- Aggregator pages (Linkjob, Apex Interviewer) likely partially
  synthesized.
- Salary band not separately reported.

## Sources surfaced (primary URLs ingested as S25-S55)

Captured in `sources/sources.md` as S25-S55. The four flagship
ingest-priorities: W2S (S30), Deliberative Alignment (S31),
Instruction Hierarchy (S32), Scaling SAEs (S33). Plus
`alignment.openai.com` (S29).
