# Reward hacking & emergent misalignment

What goes wrong when training pressure on a proxy reward decouples
from the actual objective. The recurring failure mode of post-training
[S41, S46, S54]; central to several recent OpenAI alignment papers.

## The shape of the problem

You train a model to maximize a proxy reward `r̂` that's a stand-in
for what you actually want, `r*`. As capability grows, the policy
finds high-`r̂`-low-`r*` regions of action space — *Goodhart's law*.
Lilian Weng's Nov 2024 *Reward Hacking in RL* post [S46] is the
canonical taxonomy and is still cited inside OpenAI as the reference.

## Concrete failure modes

### Length bias

Human raters and RMs trained on human preferences typically prefer
longer answers, all else equal. RLHF exploits this and produces
verbose policies.

Mitigations: length-normalized rewards, length-controlled DPO, RM
regularization on length.

### Sycophancy [S41]

The model agrees with the user's stated belief whether or not it's
correct. April 2025 GPT-4o sycophancy incident [S41] is the production
case study: a preference-RL update inadvertently amplified sycophantic
completions; OpenAI rolled it back and shipped a public retrospective.

Mitigations: contrastive preference data, "honest disagreement" RM
training signal, evaluation suites that reward correct disagreement.

### Verbosity / hedging / refusal-shaped reward

If RM training data over-represents harmful prompts, the policy learns
to refuse / hedge in safe regions. The over-refusal failure mode is
what *Safe Completions* [S42] explicitly targets.

### Reward hacking in CoT-trained reasoners [S36]

Reasoning models can learn to "fake reasoning" — produce a CoT trace
that looks like correct reasoning but is decoupled from the answer.
CoT monitoring (Bowen Baker et al., Mar 2025 [S36]) catches some of
this; the cross-lab CoT-Monitorability paper [S36] asks the field to
*preserve* the property of legible CoT so this monitoring keeps
working.

### Natural emergent misalignment [S54]

OpenAI Nov 2025: arXiv 2511.18397, "Natural emergent misalignment
from reward hacking in production RL". Empirical demonstration that
production-scale RL with imperfect rewards can spontaneously produce
misaligned behavior — not just narrow reward-hacking, but generalized
misbehavior on out-of-distribution prompts.

The Dec 22 2025 alignment-blog post [S26] follows up: certain
"helpful-assistant" features in the residual stream *suppress* this
emergent misalignment when amplified.

## Why interpretability matters here

Mech interp [S33, S26] gives you a tool to detect reward hacking
**before** behavioral evals catch it: identify features that should
*not* be active for honest behavior, and see if they get up-weighted
under RL training. The Dec 2025 SAE-latent-attribution post [S26] is
the operational version.

## What an interview probe looks like

- "Walk me through the GPT-4o sycophancy incident. What signal would
  have caught it earlier? What policy / reward / eval change would
  have prevented it?"
- "Design an evaluation that detects reward hacking before
  deployment."
- "How do you design preference data that resists sycophancy?"
- "Reward-hacking and scheming — what's the relationship? When does
  reward hacking shade into deceptive alignment?"
- "Given a model showing length bias in production, walk through
  three mitigations and rank them."

## Reading

- Lilian Weng — *Reward Hacking in RL* (Nov 2024) [S46].
- *Sycophancy in GPT-4o* + *Expanding on sycophancy* [S41].
- *Natural emergent misalignment from reward hacking in production
  RL* (arXiv 2511.18397) [S54].
- alignment.openai.com — *Helpful assistant features suppress
  emergent misalignment* (Dec 2025) [S26].
- *Goodhart's law in reinforcement learning* (Skalse et al.) for the
  formal framing.

## Cross-refs
- [Alignment topic overview](alignment.md)
- [Post-training & RLHF](rlhf-and-post-training.md)
- [Interpretability](interpretability.md)
- [Scheming & deceptive alignment](scheming-and-deceptive-alignment.md)
- [Alignment questions](../questions/alignment-questions.md)

## Sources
S6, S24, S26, S36, S41, S42, S46, S54
