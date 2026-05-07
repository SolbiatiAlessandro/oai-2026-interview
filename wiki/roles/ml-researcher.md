# ML Researcher / Member of Technical Staff – Research

OpenAI does not generally use the title "ML Researcher" externally; the
closest job titles are **Member of Technical Staff – Research** and
**Research Scientist** (often paired with Research Engineer counterparts
on the same team). The loop is research-leaning: more emphasis on prior
work, paper discussion, scientific reasoning, and research-vision
questions, and somewhat less on production-coding density [S6, S7, S19].

## Loop shape

Typical shape, synthesized across sources [S1, S6, S7, S19]:

1. **Recruiter screen** — background, what you've published, what
   problem you'd want to work on at OpenAI.
2. **Hiring-manager / research-lead screen** — research direction, your
   most-impactful project, paper-level discussion.
3. **Technical phone screen** — usually 1× ML coding (e.g., implement
   attention or a minimal training loop in PyTorch/NumPy) and possibly
   1× general coding (lighter than the SWE screen) [S6].
4. **Onsite (4-6 rounds)** [S1, S6]:
   - **ML coding** — model component from scratch.
   - **ML debugging** — given a broken or under-performing training
     setup, diagnose and propose fixes; often centered on transformers
     and large-model training failure modes [S6].
   - **Research deep dive** — 45-60 min on your strongest past project;
     expect to whiteboard architectures, derive losses, defend metric
     choices, and answer "what would you do next?" [S5, S6].
   - **Research vision** — open question about the field, e.g. "what
     would you prioritize for next-gen multimodal reasoning?" [S17].
   - **Behavioral / mission-fit** — collaboration with engineers,
     disagreement, comfort with fast pivots, safety mindset [S1, S3].
5. **Debrief and decision.**

## Bar / signals

- **Scientific reasoning**: can you justify a modeling choice, design
  an ablation, identify confounders, and reason about evaluation under
  noisy metrics? [S6, S19]
- **End-to-end research execution**: not just paper-reading; have you
  run experiments at scale, debugged training, owned an evaluation,
  shipped something? [S6]
- **Coding still matters**: even on the research track, the coding bar
  is non-trivial — OpenAI is not a "pure paper" lab, and the loop
  reflects that [S6].
- **Recent OpenAI work fluency**: panels assume you've read recent
  papers from the org and competing labs and can place your work in
  context [S1, S6].

## Recommended reading

- The **Deep Learning Book** (foundational) [S1].
- **Spinning Up in Deep RL** (RL fundamentals) [S1].
- OpenAI's research blog: scaling laws, RLHF, instruction-following,
  evaluations, agentic-tool-use, post-training [S1].
- For LLM track: papers on training-stability, MoE, mixture-of-experts
  routing, long-context inference, post-training (DPO, GRPO, RLAIF),
  evaluations and red-teaming.

## Common ML / research questions reported

(Cross-referenced with [ml-questions](../questions/ml-questions.md).)

- Walk me through transformer attention; implement scaled-dot-product
  from scratch [S6, S19].
- How does RLHF differ from DPO, and when would you pick each? [S19]
- You see a sudden loss spike at step 50k of pretraining. Walk me
  through your diagnosis [S6, S19].
- Design an evaluation harness for a frontier reasoning model [S6].
- What's your favorite recent paper and why? [S6, S7]

## Conflicts / notes

- *Title fragmentation.* Some IC roles labeled "Research Engineer" are
  actually ML-Researcher-equivalents on certain teams. The loop differs
  primarily by team, not title — confirm with your recruiter.
- *"OpenAI is research-focused"* is partly outdated. Multiple
  commentators in 2025-2026 describe OpenAI as more pragmatic-product
  than DeepMind/Anthropic, with a coding-heavier research loop [S6].

## Cross-refs
- [Research Engineer](research-engineer.md)
- [ML coding round](../rounds/ml-coding.md)
- [Deep dive](../rounds/deep-dive.md)
- [Reading list](../prep/reading-list.md)
- [Transformers topic](../topics/transformers.md)

## Sources
S1, S3, S5, S6, S7, S17, S19
