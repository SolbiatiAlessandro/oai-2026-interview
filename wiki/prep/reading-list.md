# Reading list

Curated reading list for OpenAI interview prep, anchored on what OpenAI
itself recommends [S1] and what candidate write-ups consistently cite
[S5, S6, S13, S19].

## Officially recommended by OpenAI [S1]

- **Deep Learning** — Goodfellow, Bengio, Courville. Foundational text;
  needed for ML breadth in the loop.
- **Spinning Up in Deep RL** — OpenAI's own RL primer; expected
  fluency on RL-adjacent teams (post-training, reasoning, agents).
- **OpenAI's research blog & launch posts** — recent model and agent
  announcements; the panel will assume you've read them.

## ML / Transformers (high-yield)

- *Attention Is All You Need* (Vaswani et al., 2017) — original
  transformer.
- *The Illustrated Transformer* (Jay Alammar) — visual companion.
- Karpathy's *Let's build GPT* and *Zero to Hero* YouTube series —
  hands-on transformer construction.
- *FlashAttention* (Dao et al.) — IO-aware attention; expected
  fluency at staff/research level.
- LLaMA 2/3, GPT-NeoX, Mistral papers — modern architectural choices
  (RMSNorm, RoPE, SwiGLU, GQA).
- Chinchilla (Hoffmann et al.) and Kaplan scaling-laws paper.

## Post-training / RLHF

- *InstructGPT* (Ouyang et al., 2022) — SFT → RM → PPO pipeline.
- *DPO* (Rafailov et al., 2023) — direct preference optimization.
- *GRPO* / *RLHF without PPO* family — recent variants.
- *Constitutional AI* (Anthropic) — useful comparison.

## Distributed training

- ZeRO papers (Rajbhandari et al.) — what each stage shards.
- Megatron-LM (Shoeybi et al.) — tensor + pipeline parallelism.
- GPipe / 1F1B (Huang et al., Narayanan et al.) — pipeline schedules.
- *Reducing Activation Recomputation in Large Transformer Models*
  (Korthikanti et al.).

## Inference / serving

- *Efficient Memory Management for LLM Serving with PagedAttention*
  (Kwon et al., vLLM) — paged KV cache.
- *Speculative Decoding* (Leviathan et al., Chen et al.) — speculative
  sampling.
- *Continuous Batching* writeups (Orca paper, Yu et al.).

## Evaluation

- *Sparks of AGI* (Bubeck et al.) — qualitative eval framing.
- HELM and lm-evaluation-harness — practical eval scaffolds.
- *Holistic Evaluation of Language Models* (Liang et al.).

## SWE / system design

- *Designing Data-Intensive Applications* (Kleppmann) — gold standard.
- ByteByteGo book / YouTube — fluency on common designs (Slack,
  payments, rate-limiters, notifications).
- Hello Interview's OpenAI system-design pages [S3, S9] — current
  prompts.

## Coding practice

- The 10 problems in [coding-questions](../questions/coding-questions.md)
  — implement each end-to-end in <60 min in Python.
- LeetCode 146 (LRU), 981 (Time-based KV), 2408 (Design SQL) — the
  named LeetCode references that surface in OpenAI loops [S3, S5,
  S12].
- Implement attention, multi-head attention, layernorm, softmax,
  cross-entropy from scratch in NumPy and PyTorch tensors [S6, S19].

## Optional but cited

- *Why Greatness Cannot Be Planned* (Stanley & Lehman) — research
  vision discussions sometimes touch on novelty / open-ended search.
- *The OpenAI Charter* and recent safety/release-policy posts —
  prepare a non-generic mission answer [S1, S3].

## Cross-refs
- [Timeline & study plan](timeline.md)
- [Transformers topic](../topics/transformers.md)
- [ML coding round](../rounds/ml-coding.md)

## Sources
S1, S3, S5, S6, S9, S12, S13, S19
