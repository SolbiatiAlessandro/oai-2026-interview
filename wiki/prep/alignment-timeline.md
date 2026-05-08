# Alignment Researcher — timeline & study plan

Concrete week-by-week prep for the **Researcher, Alignment** loop
[S25]. Optimized for someone with strong ML-engineer fundamentals who
needs to add alignment-research depth.

## Variant A — 4 weeks, full-time prep

### Week 1 — alignment-paper arc + Model Spec

- Day 1: Read the Model Spec (2025-12-18) [S40] and *Our approach to
  alignment research* [S27] end-to-end.
- Day 2: *Weak-to-strong generalization* [S30] — read paper, take
  notes, write a 1-paragraph summary plus 3 critiques.
- Day 3: *CriticGPT* [S34] — same drill. Compare to W2S.
- Day 4: *Instruction Hierarchy* [S32] + *Scaling SAEs* [S33].
- Day 5: *Deliberative Alignment* [S31] + *Safe Completions* [S42].
  Write the arc connecting them.
- Day 6: *Sycophancy retrospectives* [S41] + Lilian Weng's reward-
  hacking post [S46].
- Day 7: GPT-5 system card safety section [S53] end-to-end.

### Week 2 — scheming + interp + control

- Day 1: Greenblatt *Alignment Faking* [S37] + *AI Control* [S38].
- Day 2: Apollo *In-context scheming* [S50] + OpenAI × Apollo
  *Anti-scheming* [S35].
- Day 3: AXRP #39 — Hubinger on model organisms [S49].
- Day 4: *CoT Monitoring* [S36] + cross-lab CoT-monitorability
  signed paper.
- Day 5: alignment.openai.com Dec 2025 posts [S26] — all four
  launch posts + the Dec 22 emergent-misalignment-suppression post.
- Day 6: Neel Nanda mech-interp prereq + getting-started [S48]; pick
  one ARENA chapter and work it.
- Day 7: Train a tiny SAE on GPT-2 small activations on Colab; get
  reconstruction-vs-sparsity curve.

### Week 3 — coding + ML coding

- Day 1: Implement a minimal RLHF loop end-to-end (SFT → RM → PPO
  with KL) on a toy model.
- Day 2: Implement DPO loss from scratch and run on the same data;
  compare.
- Day 3: Implement GRPO (group-relative advantages, no critic) on
  a verifiable-reward task.
- Day 4-5: OpenAI coding-screen practice — time-based KV store,
  in-memory DB, GPU credit accounting, spreadsheet API. See
  [coding-questions](../questions/coding-questions.md).
- Day 6: Implement scaled-dot-product attention + multi-head + a
  tiny transformer block from scratch. See
  [ml-coding](../rounds/ml-coding.md).
- Day 7: Mock coding round (60 min, peer or solo with timer).

### Week 4 — paper presentation + behavioral + mocks

- Day 1: Pick the project for the research / paper presentation —
  must be alignment-relevant or research-shaped. Use the
  [deep-dive-template](deep-dive-template.md), but bias toward
  research-taste over staff-eng-leadership.
- Day 2: Build 6-8 slides; rehearse the 25-min talk.
- Day 3: STAR stories — disagreement, failure, prioritization,
  quality / safety, mentorship, research-eng collab. See
  [behavioral](../rounds/behavioral.md).
- Day 4: *Why OpenAI* — write the non-generic answer using the
  [why-openai](why-openai.md) template.
- Day 5: Mock alignment-specific technical round (45 min) with a
  peer who works in alignment if possible. Use questions from
  [alignment-questions](../questions/alignment-questions.md).
- Day 6: Full mock loop (1× coding, 1× ML coding, 1× paper
  presentation, 1× alignment technical, 1× behavioral).
- Day 7: Light review — alignment.openai.com, Model Spec, GPT-5
  system card. Sleep.

## Variant B — 8 weeks part-time (~12 hrs/week)

Same content, half-pace:

- Weeks 1-2: alignment paper arc + Model Spec.
- Weeks 3-4: scheming + interp + control.
- Weeks 5-6: coding + ML coding.
- Week 7: paper presentation + STAR stories.
- Week 8: Why-OpenAI + full mock loop.

## Variant C — Engineering-leaning Alignment Training

If your role is **Researcher, Alignment Training** (more post-training-
engineering-flavored):

- Drop one mech-interp day from Week 2.
- Add one day on production RLHF infra (Open Source: TRL, Axolotl;
  internal frameworks discussion).
- Add one day on safe-completions-style reward design [S42] —
  implement an output-centric reward function on a toy task.
- Increase coding-screen practice from 2 days to 3.

## Variant D — Misalignment Research (NYC)

If your role is **Researcher, Misalignment Research**:

- Replace the post-training week (W3 days 1-3) with a "model
  organisms" week: re-read Hubinger [S49], implement a simple alignment-
  faking eval inspired by Greenblatt [S37], design a scheming detector
  inspired by [S35].
- Increase Apollo Research depth — read all the recent Apollo posts
  [S50].

## Cross-cutting hygiene

- Daily: 30 min CoderPad practice (any problem).
- Daily: 15 min skim of one OpenAI / Anthropic / Apollo post.
- 2× per week: paper of the day — read end-to-end, write summary +
  3 critiques.
- 2× per week: alignment-technical mock with a peer.
- Day before / day of: light review only. Sleep is highest-EV
  preparation [S5, S13].

## Cross-refs
- [Alignment reading list](alignment-reading-list.md)
- [Alignment topic overview](../topics/alignment.md)
- [Researcher, Alignment role](../roles/alignment-researcher.md)
- [Alignment questions](../questions/alignment-questions.md)
- [Why OpenAI](why-openai.md)
- [Deep-dive slide template](deep-dive-template.md)

## Sources
S5, S13, S24-S55
