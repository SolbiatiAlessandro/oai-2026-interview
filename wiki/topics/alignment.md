# Alignment (topic overview)

What "alignment" means at OpenAI in 2026, the research agenda, and the
shortest path through it. Use this page as the reading-comprehension
backbone for the [alignment-researcher role](../roles/alignment-researcher.md).

## The agenda

OpenAI's public framing [S27, S28]:

- Train models with human feedback (RLHF and successors).
- Train models to **assist human evaluation** (scalable oversight).
- Train models to **do alignment research** themselves.

Cross-cutting:

- **Capability elicitation and evaluation** to know what current models
  can do — Preparedness Framework v2 [S39].
- **Behavioral specification** — the Model Spec [S40] codifies what
  models should and shouldn't do.
- **Inference-time policy** — Deliberative Alignment [S31] / Safe
  Completions [S42] make the model reason over the spec at runtime.

## Five sub-fields you should be fluent in

Each gets a dedicated topic page; this section is the map.

### 1. Post-training (RLHF → DPO → GRPO → safe-completions)

The vehicle for getting a model from "base" to "aligned with the spec".
Required fluency: derive DPO from the RLHF objective; explain GRPO's
group-relative advantage; understand reward-model design and KL-
regularization. [S31, S34, S42, S46] — see
[rlhf-and-post-training](rlhf-and-post-training.md).

### 2. Scalable oversight

How to supervise a model that is more capable than its supervisors.
Canonical pieces: weak-to-strong generalization [S30], CriticGPT [S34],
debate / recursive reward modeling. — see
[scalable-oversight](scalable-oversight.md).

### 3. Mechanistic interpretability

Reverse-engineer features and circuits inside trained models. OpenAI's
specific contribution: scaling sparse autoencoders to GPT-4 [S33] and
the Dec 2025 alignment-blog post on debugging misaligned completions
via SAE latent attribution [S26]. — see
[interpretability](interpretability.md).

### 4. Reward hacking & emergent misalignment

What goes wrong when training pressure is misspecified. Sycophancy
[S41] is the production case study; reward-hacking-as-emergent-
misalignment [S54] is the formal result; "helpful assistant features
suppress emergent misalignment" [S26] is the latest mitigation. — see
[reward-hacking](reward-hacking.md).

### 5. Scheming & deceptive alignment

Frontier models that may strategically misbehave under training
pressure. OpenAI × Apollo's anti-scheming training [S35], cross-lab
CoT monitorability [S36], Greenblatt's alignment-faking paper [S37],
Apollo's in-context-scheming results [S50]. — see
[scheming-and-deceptive-alignment](scheming-and-deceptive-alignment.md).

## The arc to internalize

A common interview probe is "walk me through the arc of OpenAI's
alignment work from RLHF to today" [S6, S24]. The clean version:

1. **InstructGPT** (2022): SFT + RLHF gets a base model to follow
   instructions.
2. **CriticGPT** (2024) [S34]: train a critic to find bugs in another
   model's code — an empirical scalable-oversight result.
3. **Weak-to-strong** (2023) [S30]: study whether a strong student
   can exceed its weak teacher's capability ceiling, as a stand-in
   for the human → superhuman supervision gap.
4. **Instruction Hierarchy** (2024) [S32]: privilege system >
   developer > user instructions; harden against prompt injection.
5. **Scaling SAEs** (2024) [S33]: the interpretability lever — open
   the model up.
6. **Deliberative Alignment** (Dec 2024) [S31]: o-series models read
   and reason over a written safety spec at inference.
7. **Sycophancy retrospective** (Apr 2025) [S41]: production reward-
   hacking incident; lesson updates feed into the next iteration.
8. **Anti-scheming + CoT monitoring** (Mar-Sep 2025) [S35, S36]:
   active monitoring of CoT traces; anti-scheming training that
   reduces controlled-evaluation misbehavior ~30×.
9. **Safe Completions** (Aug 2025) [S42]: output-centric reward
   replaces refusal-vs-comply binary.
10. **alignment.openai.com launch** (Dec 2025) [S26]: standalone
    blog with public alignment-science output. Recent posts on
    suppressing emergent misalignment, sidestepping eval awareness,
    SAE latent attribution.

## Common confusions to avoid

- **Alignment ≠ control** [S38]. Alignment tries to make the model
  *want* to do the right thing; control assumes it might not, and
  designs deployment protocols that catch and contain unsafe
  behavior. They're complementary research programs, not the same
  thing.
- **Scalable oversight ≠ scaling laws.** Different fields, different
  authors, different problems.
- **Capability eval ≠ alignment eval.** A model can ace MMLU and
  still scheme; a model can refuse helpful requests and still be
  capability-limited. Preparedness Framework [S39] focuses on
  capability evals; alignment evals are a separate beast.
- **CoT monitoring is not a guarantee.** It works as long as models
  use legible CoT for the reasoning they want monitored — a regime
  the cross-lab CoT-monitorability paper [S36] explicitly asks the
  field to preserve.

## Cross-refs
- [Researcher, Alignment role](../roles/alignment-researcher.md)
- [OpenAI alignment org map](openai-alignment-org.md)
- [Post-training & RLHF](rlhf-and-post-training.md)
- [Scalable oversight](scalable-oversight.md)
- [Interpretability](interpretability.md)
- [Reward hacking](reward-hacking.md)
- [Scheming & deceptive alignment](scheming-and-deceptive-alignment.md)
- [Safety evals & Preparedness](safety-evals-and-preparedness.md)
- [Alignment reading list](../prep/alignment-reading-list.md)

## Sources
S6, S24, S26-S55
