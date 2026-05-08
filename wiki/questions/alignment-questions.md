# Alignment-specific questions (bank)

Probe-shaped questions for the alignment-specific technical round and
the research / paper-presentation round. Synthesized from the published
work + adjacent-loop reporting [S6, S24-S55] — not first-person-
verified for the Researcher-Alignment role specifically (no clean
first-person writeup exists publicly as of May 2026; treat as
high-recall, calibrate with your recruiter).

## Paper-arc and reading-fluency probes

- "Walk me through the arc of OpenAI's alignment work from RLHF to
  today." (Expect to name InstructGPT → CriticGPT → W2S → Instruction
  Hierarchy → SAEs → Deliberative Alignment → Sycophancy retro →
  Anti-Scheming + CoT monitoring → Safe Completions → alignment.openai.com
  posts. See [alignment topic](../topics/alignment.md).) [S24]
- "What's your favorite recent alignment paper, and what's the
  strongest objection to it?" [S6, S24]
- "What surprised you in the GPT-5 system card?" [S53]
- "Pick a recent alignment.openai.com post. Critique it." [S26]

## Scalable oversight probes

- "Walk me through the assumptions underlying weak-to-strong
  generalization. Where does it break?" [S30]
- "Design an experiment to test whether CriticGPT-style critics
  generalize from code to natural-language fact-checking." [S34]
- "Critique the debate framing as a path to scalable oversight."
- "Given a budget of N human-hours, how would you spend it to
  evaluate a frontier reasoning model? What does scalable oversight
  buy you?" [S6, S24]

## Post-training / RLHF / reward-hacking probes

- "Derive the DPO loss from the RLHF objective on the whiteboard."
- "Why does GRPO drop the critic? When would you pick it over PPO?"
- "Walk me through the GPT-4o sycophancy incident. What signal
  would have caught it earlier? What policy / reward / eval change
  would have prevented it?" [S41]
- "Design a preference-data collection protocol that resists
  sycophancy." [S46]
- "Implement a small RLHF or DPO loss from scratch in PyTorch."
  (See [ml-coding](../rounds/ml-coding.md).)
- "Reward hacking and scheming — what's the relationship? When does
  reward hacking shade into deceptive alignment?" [S35, S46, S54]
- "What is *safe completions*? What changed vs. deliberative
  alignment? Why?" [S31, S42]

## Mechanistic interpretability probes

- "Walk me through how you'd train a SAE on GPT-4 activations from
  scratch. Loss? Sparsity penalty? Dead features?" [S33]
- "Given a SAE feature you suspect is 'sycophancy', design a study
  to test whether it's *causally* responsible for sycophantic
  behavior." [S26, S33]
- "Critique the use of SAE-latent attribution as an alignment
  debugging tool. What does it miss?" [S26]
- "Why is superposition a problem? How do SAEs sidestep it? What's
  the limit?" [S33]
- "Helpful-assistant features suppress emergent misalignment when
  amplified [S26]. Walk me through how you'd validate that result on
  a held-out distribution."

## Scheming, deceptive alignment, and control probes

- "Walk me through the OpenAI × Apollo anti-scheming paper.
  Threat model, intervention, measurement, limits." [S35]
- "If you were designing an eval for scheming, how would you make
  it eval-aware-resistant?" [S26, S35]
- "Distinguish alignment from control [S38]. Where does the alignment
  research community draw that line, and where do you think it
  *should* be drawn?"
- "Pick one assumption underlying the alignment-faking paper [S37]
  that you think is fragile. Defend why."
- "What would scheming look like in a base model, before any RLHF?"

## Eval-design and Preparedness probes

- "Design a capability elicitation procedure for biological-weapon
  uplift on a frontier reasoning model." [S39]
- "Design an eval that detects sandbagging." [S24]
- "How do you tell whether a model's win-rate regression on safety
  evals is real vs. noise? Walk me through the statistics."
- "Critique Preparedness Framework v2's threshold definitions.
  What's a category you'd add or refine?" [S39]
- "Design an evaluation harness for the instruction hierarchy." [S32]
- "How would you red-team Deliberative Alignment?" [S31]

## Research-vision probes

- "What's the biggest open problem in alignment as you see it?"
- "If you had 12 months and a 1k-H100-cluster budget, what would
  you work on?"
- "Where do you think interpretability is headed in 2026-2027?"
- "What's a result you'd most like to see disconfirmed?"
- "What's an alignment direction OpenAI is *not* working on that you
  think it should?"

## Behavioral probes (alignment-flavored)

- "Why OpenAI vs. Anthropic vs. SSI?" [S24] — see
  [why-openai](../prep/why-openai.md).
- "What would you do if you found a model behaving in a misaligned
  way during training?" [S24]
- "Tell me about a time you raised a concern about AI safety or
  research quality that wasn't popular."
- "How do you reason under deep uncertainty about a research
  direction?"
- "How do you do alignment research at a company where the alignment
  team has been reshuffled twice?" (Mission Alignment dissolution
  Feb 2026 [S44]; expect this probe.)
- "Tell me about a project where you had to collaborate with a
  research scientist who held a strongly-held view different from
  yours." [S3, S20]

## Coding-side probes (still asked; alignment role doesn't exempt you)

The standard coding-screen pool from S2 / S20 still applies. See
[coding-questions](coding-questions.md). High-yield five for an
alignment role:

1. **Time-based KV store** with serialization / versioning [S2, S20].
2. **In-memory SQL DB** subset (CRUD + WHERE + ORDER BY) [S2, S3].
3. **Resumable iterator** with state checkpointing [S2, S20].
4. **Implement attention from scratch** [S6, S19].
5. **Implement a tiny RLHF or DPO loop** end-to-end (alignment-
   specific extension).

## Cross-refs
- [Researcher, Alignment role](../roles/alignment-researcher.md)
- [Alignment topic overview](../topics/alignment.md)
- [Post-training & RLHF](../topics/rlhf-and-post-training.md)
- [Scalable oversight](../topics/scalable-oversight.md)
- [Interpretability](../topics/interpretability.md)
- [Reward hacking](../topics/reward-hacking.md)
- [Scheming & deceptive alignment](../topics/scheming-and-deceptive-alignment.md)
- [Safety evals & Preparedness](../topics/safety-evals-and-preparedness.md)
- [Coding questions](coding-questions.md)
- [ML questions](ml-questions.md)

## Sources
S2, S3, S6, S19, S20, S24-S55
