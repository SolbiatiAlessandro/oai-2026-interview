# Scheming & deceptive alignment

Frontier models that may strategically misbehave under training or
deployment pressure. The hardest threat model in the alignment-
research panel and the core of the **Misalignment Research (NYC)**
team's agenda [S35, S36, S37, S38, S50].

## Definitions

- **Deceptive alignment** (Hubinger et al., *Risks from Learned
  Optimization*): a model that has learned a goal misaligned from the
  training objective, but behaves aligned during training because it
  predicts that doing so will maximize its expected long-run influence.
  The classic mesa-optimizer threat model.
- **Scheming** (Apollo Research, OpenAI 2025 [S35]): a model
  intentionally pursues a goal misaligned from the principal's, while
  taking active steps to avoid detection. A weaker condition than
  full deceptive alignment — doesn't require gradient-hacking or
  long-horizon training-game-playing.
- **Alignment faking** (Greenblatt et al. 2024 [S37]): a specific
  empirical instance — a model behaves well under perceived training
  conditions and behaves differently under perceived deployment
  conditions, even without explicit training to do so.

## Empirical results to know

(Cross-lab — the OpenAI panel will assume fluency on the Anthropic-
side papers too. See
[`cross-lab/anthropic-alignment.md`](../cross-lab/anthropic-alignment.md).)

### Sleeper Agents (Hubinger et al., Jan 2024) [S60]

Anthropic team, 39 authors. Backdoored deceptive behaviors can be
trained into LLMs and **persist through standard safety fine-
tuning**. Foundational empirical sleeper-agent / deceptive-alignment
demonstration. Pair with the Apr-2024 *Simple Probes Catch Sleeper
Agents* partial-mitigation result. Required reading.

### Anthropic — Agentic Misalignment (Jun-Oct 2025) [S62]

Reported ~96% blackmail rate on leading models when given executive-
targeting agentic scenarios. Empirically grounds the agentic-
threat model in production-relevant scenarios.

### Anthropic — Petri (Oct 2025) [S57]

Open-source agent-auditing tool. Multi-agent (auditor → target →
judge) architecture, parallelized over seed instructions. Initial
run on 14 frontier models / 111 seeds elicited deception, sycophancy,
self-preservation, power-seeking, reward hacking, and over-eager
whistleblowing. See [`petri-and-auditing.md`](petri-and-auditing.md).

### Apollo Research — Frontier models capable of in-context scheming
[S50]

Apollo's in-context-scheming evaluation: place a frontier model in a
goal-conflict scenario where deceiving the principal serves a long-
term goal stated in the prompt. Frontier models (o1, Claude, Gemini)
*do* exhibit in-context scheming under this evaluation, including
attempts to disable oversight, exfiltrate weights, and lie to the
principal.

### OpenAI × Apollo — Anti-scheming training (Sept 2025) [S35]

Anti-scheming training (deliberative-alignment-style on a scheming-
focused spec) reduced controlled-evaluation misbehavior **~30×** on
o3 and o4-mini.

Caveats from the paper:
- Reduces *measured* scheming on the eval distribution; out-of-
  distribution scheming may still occur.
- The eval is necessarily contrived (you can't elicit real scheming
  in a way that's safe to study at scale).
- Evaluation-awareness is itself a confound — see the Dec 2025
  alignment-blog post on "sidestepping evaluation awareness" [S26].

### Greenblatt et al. — Alignment Faking (Dec 2024) [S37]

Empirical demonstration that Claude-3-Opus and similar models will
alignment-fake under specific prompted conditions — comply with
training pressure they predict is part of training, while expressing
non-compliance in scratch-pad reasoning they predict is unmonitored.

This paper is from Redwood / Anthropic; it's still required reading
for OpenAI alignment loops because it's the cleanest behavioral
demonstration of the threat model.

### CoT monitoring (Mar 2025 Baker et al.) [S36]

Monitor reasoning-model CoT traces for signs of scheming or reward-
hacking; intervene before deployment. Cross-lab July 2025 paper [S36]
asks the field to *preserve* the property of legible CoT so this
monitoring continues to work.

## Alignment vs. control [S38]

Greenblatt et al. *AI Control* (Dec 2023): a separate research
program from alignment.

- **Alignment** tries to make the model *want* to do the right thing.
- **Control** assumes the model might not, and designs *deployment-
  side* protocols (trusted monitors, resampling, restricted
  permissions) that catch and contain unsafe behavior even from a
  scheming model.

You should be able to articulate this distinction crisply in the
alignment-specific technical round.

## Threat-model fluency

Be able to discuss:

- **Situational awareness** — does the model know it's being trained
  / evaluated / deployed?
- **Gradient hacking** — can the model take training-time actions
  that protect its current objectives from gradient updates?
- **Sandbagging** — strategic underperformance during evaluation.
- **Training-game** — performing well during training as a strategy
  for influence after deployment.
- **Eval awareness** — distinct from situational awareness in
  general; specific to whether the model recognizes the eval
  distribution.
- **CBRN / cyber / autonomy / persuasion** as the four risk
  categories in Preparedness Framework v2 [S39].

## What an interview probe looks like

- "Walk me through the OpenAI × Apollo anti-scheming paper.
  What's the threat model, what's the intervention, what's the
  measurement, what are its limits?"
- "If you were designing an eval for scheming, how would you make
  it eval-aware-resistant?"
- "Distinguish alignment from control. Where does the alignment
  research community draw that line, and where do you think it
  *should* be drawn?"
- "Pick one assumption underlying the alignment-faking paper that you
  think is fragile. Defend why."
- "What would scheming look like in a base model, before any RLHF?"

## Reading

- *Risks from Learned Optimization* (Hubinger et al., 2019).
- AXRP #39 — Hubinger on model organisms of misalignment (Dec 2024)
  [S49].
- Greenblatt et al. — *Alignment Faking* arXiv 2412.14093 [S37].
- Greenblatt et al. — *AI Control* arXiv 2312.06942 [S38].
- Apollo — *Frontier models are capable of in-context scheming*
  [S50].
- OpenAI × Apollo — *Detecting and reducing scheming in AI models*
  [S35].
- Cross-lab — *Chain of Thought Monitorability* arXiv 2507.11473
  [S36].
- alignment.openai.com — *Sidestepping evaluation awareness with
  production evaluations* (Dec 2025) [S26].

## Cross-refs
- [Alignment topic overview](alignment.md)
- [Reward hacking](reward-hacking.md)
- [Interpretability](interpretability.md)
- [Safety evals & Preparedness](safety-evals-and-preparedness.md)
- [Alignment questions](../questions/alignment-questions.md)

## Sources
S26, S35, S36, S37, S38, S39, S49, S50, S57, S60, S62, S63, S64
