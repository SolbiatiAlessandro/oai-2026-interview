# Mechanistic interpretability

Reverse-engineer features and circuits inside trained models. Useful
for debugging misaligned behavior, validating training procedures, and
spotting deceptive reasoning that doesn't show up in behavioral evals.
[S33, S26, S48]

## The OpenAI-specific contribution

### Scaling sparse autoencoders to GPT-4 (Gao et al., 2024) [S33]

Train a sparse autoencoder on activations from a frozen GPT-4. Each
SAE latent corresponds to a (claimed) interpretable concept. The
paper scales to **16M latents** and reports clean concept separation
on many of them.

Variants you should know:

- **Top-k SAEs** — enforce sparsity by zeroing all but the top-k
  activations per token.
- **JumpReLU SAEs** — learnable thresholds; better dead-feature rate.
- **Gated SAEs** — separate the "is this feature active" decision
  from the "by how much" decision; reduces shrinkage bias.

### Dec 2025 alignment-blog post: SAE latent attribution [S26]

"Debugging misaligned completions with sparse-autoencoder latent
attribution" — given a misaligned completion, attribute it to specific
SAE latents and show which residual-stream features were responsible.
This is the operational use of mech interp inside OpenAI's alignment
pipeline.

### Dec 2025 alignment-blog post: helpful-assistant features
suppress emergent misalignment [S26, S54]

A structural finding: certain features in the residual stream that
correspond to "being a helpful assistant" suppress reward-hacking-
induced misalignment. Editing them up reduces emergent misalignment
on the Anthropic-style "natural emergent misalignment from production
RL" [S54] distribution.

## Background you must own — the Anthropic interpretability canon

The OpenAI panel assumes you've read this in full. Anthropic publishes
substantially more interpretability output than OpenAI does, and it's
all on `transformer-circuits.pub`. Full registry at [S67]; full
context in [`cross-lab/anthropic-alignment.md`](../cross-lab/anthropic-alignment.md).

- **Toy models of superposition** (Elhage / Olah, Sep 2022) [S67] —
  why neural networks compress more features than they have neurons,
  and what that does to interpretability.
- **Towards Monosemanticity** (Bricken / Olah, Oct 2023) [S67] —
  first big SAE result on a small model.
- **Scaling Monosemanticity** on Sonnet 3 (Templeton et al., May
  2024) [S67] — first big SAE result on a production-scale model.
- **Crosscoder Model Diffing** (Bricken / Olah, 2025) [S67] — diff
  features across model checkpoints / fine-tunes.
- **Influence Functions** (Grosse + 16, Aug 2023) [S67] — EK-FAC on
  52B-param models; alternative to SAEs for tracing model behavior
  to training data.
- **Evaluating Feature Steering** (Anthropic, 2024) [S67] —
  causal-style evaluation of editing SAE latents.
- **Engineering Challenges of Scaling Interpretability** (Anthropic,
  2024) [S67] — the infra story behind running SAEs at production
  scale.
- *(Older, still useful)* **Scaling monosemanticity** / **Towards Monosemanticity** (Anthropic
  2024) — first big result of SAEs on a production-scale model.
- **Circuits** — the older Olah et al. line of work; "induction
  heads" as a canonical mechanistic finding.
- **Activation patching** / **path patching** — causal-style
  interventions to localize a behavior to specific weights or
  activations.

## Practical track

(Following Neel Nanda's guides [S48].)

1. *Concrete steps* — Nanda's getting-started guide on
   `neelnanda.io/mechanistic-interpretability/getting-started`.
2. *Prereqs* — linear algebra, probability, transformers. Nanda's
   prereq guide is the standard reference.
3. **ARENA curriculum** — multi-week structured course; widely
   considered the canonical hands-on practical track.
4. Implement a tiny SAE on GPT-2 small activations; reproduce
   clean feature recovery.
5. Read OpenAI's Scaling SAEs paper [S33] and the alignment-blog SAE
   posts [S26].

## What an interview probe looks like

- "Walk me through how you'd train a SAE on GPT-4 activations from
  scratch. What's the loss? What sparsity penalty? How do you handle
  dead features?"
- "Given a SAE feature you suspect is 'sycophancy', design a study
  to test whether it's causally responsible for sycophantic
  behavior."
- "Critique the use of SAE-latent attribution as an alignment debugging
  tool. What does it miss?"
- "Why is superposition a problem? How do SAEs sidestep it?"

## Failure modes

- **Feature splitting / merging** — a "true" feature appears as
  multiple SAE latents at one width and merges at another.
- **Reconstruction-fidelity vs. sparsity** trade-off; you can pick
  any point on the curve.
- **Causal fidelity** — high reconstruction does not imply that
  individual features are causally meaningful.
- **Dead features** — a fraction of latents never activate. Top-k and
  JumpReLU partly address this.
- **Distribution shift** — features trained on one corpus may not
  generalize to a different prompt distribution.

## Cross-refs
- [Alignment topic overview](alignment.md)
- [Scheming & deceptive alignment](scheming-and-deceptive-alignment.md)
- [Reward hacking](reward-hacking.md)
- [Alignment reading list](../prep/alignment-reading-list.md)

## Sources
S24, S26, S33, S48, S54, S67
