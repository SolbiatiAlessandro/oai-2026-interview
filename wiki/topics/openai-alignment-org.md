# OpenAI alignment org map (May 2026)

Where alignment work lives at OpenAI, who's on it, and what each team
ships. Critically unstable — re-check before each interview.

## Org-level shocks shaping the current map

- **May 2024** — Superalignment dissolved after Sutskever and Leike
  resigned. The 20% compute commitment was effectively cancelled.
  [cnbc.com / axios.com 2024-05-17 coverage; via S24]
- **Sept 2025** — Model Behavior team folded into Post-Training under
  Max Schwarzer; founding lead Joanne Jang departed early 2026 to
  launch OAI Labs. [theaiinsider.tech 2025-09-09; via S24]
- **Feb 11, 2026** — *Mission Alignment* (~7 people, headed by Joshua
  Achiam since late-2024) disbanded; Achiam → Chief Futurist with
  Jason Pruet [S44, S52].

Implication: anyone telling you the alignment org map is "stable" is
working from old info. Confirm with your recruiter.

## Teams that own alignment work today

### Alignment (the role)

The team behind the public **Researcher, Alignment** posting [S25].
Training-time alignment of frontier models; ships into post-training.
Boaz Barak (Harvard, OpenAI part-time since Fall 2025) is associated
with this work and co-authored Deliberative Alignment [S31, S45].

### Alignment Science

Separate posting [S25]. Ran the December 2025 launch of
`alignment.openai.com` [S26]. Authors recent posts on emergent-
misalignment suppression and eval-awareness sidestepping.

### Alignment Training

Separate posting [S25]. Post-training-flavored — closer to the RLHF /
DPO / GRPO / safe-completions production stack [S42, S46].

### Misalignment Research (NYC)

Separate posting [S25]. Model-organisms-style work; partners with
Apollo Research; co-authored Sept 2025 anti-scheming results [S35,
S50].

### Safety Systems

Operational deployed safety stack: red-teaming, deployment evals,
refusal training, classifier pipeline. Lilian Weng was VP through
Nov 2024 [S46]; no public successor in identical title.

### Preparedness

Catastrophic-capability evals — CBRN, cyber, autonomy, persuasion.
Aleksander Mądry led until July 2024; **Head of Preparedness role
open** as of Dec 2025, reported comp ~$555K [S25, S39]. Owns the
Preparedness Framework v2 and the Evaluations Hub.

### Model Behavior (folded)

Owned the Model Spec until Sept 2025 reorg. Folded into Post-Training
under Max Schwarzer; Joanne Jang departed early 2026. Latest Model
Spec snapshot is dated 2025-12-18 [S40].

## Public-facing people on the alignment side

(High-signal follows for the candidate.)

| Person | Role / org | Why follow |
|---|---|---|
| Boaz Barak | Harvard / OpenAI part-time | Co-author Deliberative Alignment [S31]; Harvard CS 2881 syllabus is closest public proxy for the depth bar [S45]. Active on X. |
| Joshua Achiam | Chief Futurist | Ran Mission Alignment until Feb 2026 [S44, S52]. |
| Bowen Baker | OpenAI | First author "Detecting misbehavior in frontier reasoning models" [S36]. |
| Jeff Wu | OpenAI | Co-author Weak-to-Strong [S30]; long-tenure alignment team. |
| Leo Gao | OpenAI | Sparse-autoencoder lead; first author Scaling SAEs [S33]. LessWrong / Alignment Forum presence. |
| Nat McAleese | OpenAI | First-author CriticGPT [S34]. |
| Pavel Izmailov | OpenAI | Co-author Weak-to-Strong [S30]. |
| Jan Hendrik Kirchner | OpenAI | Co-author Weak-to-Strong [S30]. |
| Collin Burns | OpenAI | Lead author Weak-to-Strong [S30]. |
| Jakub Pachocki | Chief Scientist | Sets the high-level safety / science direction. |
| Wojciech Zaremba | OpenAI co-founder | Tweets occasionally on safety. |

## Departed but still cited

- **Ilya Sutskever** — SSI. Nov 2025 Dwarkesh interview discusses SSI
  alignment philosophy [S24].
- **Jan Leike** — Anthropic. 80,000 Hours episodes still calibrate
  hiring criteria [S47].
- **Lilian Weng** — Reward-Hacking-in-RL post still canonical
  reference [S46].
- **John Schulman** — Anthropic → Mira Murati's Thinking Machines.
- **Mira Murati** — Thinking Machines.
- **Aleksander Mądry** — back to MIT.
- **Leopold Aschenbrenner** — co-author W2S, then *Situational
  Awareness*.

## What this implies for an interview loop

- Your hiring manager will be on Alignment, Alignment Science,
  Alignment Training, or Misalignment Research [S25].
- The alignment-specific technical round is shaped by *which* team
  the role is for. Misalignment-Research candidates should be deepest
  on scheming and Apollo's work [S35, S50]; Alignment-Science
  candidates on the alignment.openai.com posts [S26]; Alignment-
  Training candidates on safe-completions and the post-training stack
  [S42, S46]; Alignment candidates on Deliberative Alignment and the
  Model Spec [S31, S40].
- The behavioral round will probe how you'd react to org instability
  ("how do you do alignment research at a company where the alignment
  team has been reshuffled twice?") [S24, S44].

## Cross-refs
- [Researcher, Alignment role](../roles/alignment-researcher.md)
- [Alignment topic overview](alignment.md)
- [Why OpenAI answer template](../prep/why-openai.md)

## Sources
S24, S25, S26, S27, S28, S31, S33, S34, S35, S36, S39, S40, S42, S44,
S45, S46, S47, S50, S52
