# Safety evaluations & Preparedness Framework

Safety eval design is one of the highest-leverage skills the
Researcher-Alignment loop screens for [S6, S24, S39]. Capability
elicitation, contamination, eval-awareness, and the Preparedness
threshold framework are all expected fluencies.

## Preparedness Framework v2 (Apr 2025) [S39]

OpenAI's framework for catastrophic-capability evaluation. v2 narrows
to two thresholds:

- **High** — capabilities that warrant new mitigations before
  deployment.
- **Critical** — capabilities that warrant *not deploying* until
  mitigations land.

Four risk categories:

1. **CBRN** — chemical, biological, radiological, nuclear uplift.
2. **Cyber** — vulnerability discovery, exploitation, payload
   generation.
3. **Autonomy** — autonomous-replication-and-adaptation (ARA),
   self-improvement, model-weight exfiltration.
4. **Persuasion** — influence operations, coercion, manipulation.

Read the v2 PDF before any safety / preparedness round; expect
"what surprised you in PF v2 compared to v1?" as a real probe [S24,
S39].

## Capability elicitation

The hard part of safety eval isn't running the eval; it's making
sure you've **elicited** the model's capability cleanly, so a passed
eval really means the model can't do the dangerous thing.

Standard playbook (METR, Anthropic, OpenAI):

- **Best-of-N sampling** with sensible decoders.
- **Prompt-engineering budget** — enough effort to find the model's
  ceiling, not its average.
- **Tool access** that mirrors deployed-tool surface (browser, code
  exec, file system).
- **Human-AI teams** — does a domain-expert human, paired with the
  model, exceed the threshold?
- **Fine-tune-resistance** — for open-weight releases, evaluate
  capability *after* a small fine-tune for the dangerous task.

If you skip elicitation, your eval becomes capability-floor, not
capability-ceiling — and that's the wrong direction for safety.

## Contamination

The model has seen the eval. Now what?

Mitigations:

- Held-out human-only sets that are never published.
- Canary strings in eval prompts; check perplexity-of-canary as a
  contamination signal.
- Periodic eval-set rotation.
- N-gram overlap with training data.
- Behavioral signal: if a model gets a question right but gets
  trivial perturbations wrong, contamination is the prior hypothesis.

## Eval awareness

The model recognizes that it is being evaluated and behaves
differently. Distinct from situational awareness in general.

The Dec 2025 alignment-blog post *Sidestepping Evaluation Awareness
with Production Evaluations* [S26] is the canonical OpenAI write-up.
The trick: run the eval inside the production deployment surface, with
production prompts and noise, so the model can't distinguish eval
from real traffic.

## Sandbagging-aware design

A misaligned model might *underperform* on capability evals to avoid
triggering deployment restrictions. Design defenses:

- **Capability-elicitation steps above** — make the elicitation
  serious enough that intentional underperformance becomes
  detectable.
- **Cross-eval consistency checks** — if the model excels at sub-
  capabilities A and B but fails at A∘B, that's a flag.
- **Behavior-cloning probes** — compare to base-model behavior on
  the same task.

## Public eval surfaces to know

- **Evaluations Hub** [S29] — OpenAI's public eval results dashboard.
- **METR** — autonomous-replication-and-adaptation evals; closest
  external partner to OpenAI on autonomy evals [S24].
- **lm-evaluation-harness** — community standard for academic-style
  evals.
- **HELM** — Stanford's holistic-evaluation framework.
- **Apollo Research** — scheming evaluation specialist [S50].
- **Anthropic alignment.anthropic.com** — cross-lab safety evaluation
  exchange [S43].

## Eval-design as an interview probe

Likely shapes [S6, S24]:

- "Design a capability elicitation procedure for biological-weapon
  uplift on a frontier reasoning model."
- "Design an eval that detects sandbagging."
- "How do you tell whether a model's win-rate regression on safety
  evals is real vs. noise? Walk me through the statistics."
- "OpenAI's GPT-5 system card claims X. How would you design a
  follow-up eval to confirm it?"
- "Critique Preparedness Framework v2's threshold definitions.
  What's a category you'd add or refine?"

## Cross-refs
- [Alignment topic overview](alignment.md)
- [Scheming & deceptive alignment](scheming-and-deceptive-alignment.md)
- [Reward hacking](reward-hacking.md)
- [Alignment questions](../questions/alignment-questions.md)
- [Alignment reading list](../prep/alignment-reading-list.md)

## Sources
S6, S24, S26, S29, S35, S39, S43, S50, S53
