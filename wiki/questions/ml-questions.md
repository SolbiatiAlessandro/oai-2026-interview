# ML questions (bank)

Questions reportedly asked in ML-coding, ML-debugging, and ML-breadth
discussion rounds at OpenAI [S1, S6, S17, S18, S19].

## ML coding (implement-from-scratch)

| # | Task | Confidence | Sources |
|---|------|------------|---------|
| 1 | Scaled-dot-product attention (NumPy or PyTorch tensors only) | high | S6, S19 |
| 2 | Multi-head attention (heads, projections, batch dim) | high | S6, S19 |
| 3 | Tiny transformer block (attention + residual + MLP + layernorm) | high | S6 |
| 4 | Minimal training loop for a small LM | high | S6, S19 |
| 5 | LayerNorm / RMSNorm | medium | S19 |
| 6 | Softmax with numerical stability | high | S6, S19 |
| 7 | Cross-entropy loss with label smoothing | medium | S19 |
| 8 | K-means / KNN / logistic regression from scratch | medium | S19 |
| 9 | BPE / byte-pair-encoding tokenizer basics | medium | S19 |
| 10 | Beam search / nucleus sampling decoder | medium | S19 |

Common follow-ups: causal mask, padding mask, sequence packing,
mixed-precision concerns, FlashAttention IO-awareness.

## ML breadth / discussion

(See [transformers topic](../topics/transformers.md) for transformer-
specific depth.)

- Explain overfitting and the bias-variance trade-off; how do you
  detect and mitigate it? [S17]
- Compare optimizers: SGD, Adam, AdamW, Lion. When does each win? [S19]
- Explain regularization techniques: weight decay, dropout, data
  augmentation, early stopping [S17, S19].
- Walk through batch norm vs. layer norm vs. RMS norm; when do you
  pick which? [S19]
- Why do transformers use residual connections + layernorm? What
  fails without them? [S19]
- What is mixed-precision training and why does it matter? Where
  does it break? [S6, S19]
- Walk through RLHF: SFT → reward model → PPO/DPO/GRPO; what's the
  loss at each stage? [S19]
- DPO vs. PPO vs. GRPO: pros and cons; when do you pick which? [S19]
- Explain scaling laws (Chinchilla, etc.) and how they affect a
  training plan [S19].
- How does a mixture-of-experts work and what are the routing
  failure modes? [S19]
- Long-context inference: KV cache, paged attention, sliding window,
  ALiBi/RoPE — pros and cons [S19].

## ML debugging scenarios [S6, S19, S20]

The canonical OpenAI ML-debug round (60 min, PyTorch, recruiter
verbatim in [ml-debugging](../rounds/ml-debugging.md)): a working-but-
wrong multi-headed transformer with 4-5 bugs. Common bugs are listed
on the round page.

A second 30-min part (S20): convert an LLM training script into a
classification training task — pick the embedding to use, define the
modified loss, compute model accuracy.

Free-form scenarios you may also be handed:


The interviewer hands you symptoms; you diagnose.

- "Loss is NaN at step 200." → check learning rate, overflow in fp16,
  mismatched dtype, exploding gradients, bad data.
- "Loss is flat." → vanishing gradients, frozen params, learning rate
  too small, data shuffle issue, label leakage in eval.
- "Validation loss diverges from training after step N." → overfitting
  (regularize / data), distribution shift, eval-leak.
- "Throughput is 30% of theoretical." → CPU-bound dataloader, GPU
  starvation, mis-set num_workers, host-device transfer, missing
  amp.
- "Distributed training stalls every M steps." → checkpointing,
  collective ops imbalance, slow node, NCCL timeout.
- "Generations are all the same / degenerate." → temperature, repetition
  penalty, KV cache bug, sampling bug.

## Evaluation questions [S6, S19]

- Design an evaluation harness for an instruction-following LLM.
- How would you detect contamination of an eval set?
- How would you tell if a regression in win-rate is real vs. noise?
- How do you build a grader-model and validate its calibration?

## ML-search/recsys design questions [S20]

(See dedicated round page: [ml-search-design](../rounds/ml-search-design.md).)

- Design a personalized recommender for a places/listings home page
  (cold start, multi-stage retrieval + ranking, sparse hashing,
  attention-pooling, calibration).
- Design a RAG system and combine with LLMs (offline + online eval).
- Bootstrapping / data flywheel: from a large pool of unlabeled data,
  mine new labels using a classifier you build yourself.
- Detect duplicate accounts (two accounts → same person) — real-time
  classification with retrieval.
- Specific topical depth probes the interviewer can drop on you:
  attention formula on a whiteboard; cross-entropy formula and what
  changes without down-sampling; LoRA mechanics; mixture-of-experts
  routing; calibration definition + formula; ACE (Average Causal
  Effect); QR-hashing for sparse features.

## sysML / scaling-track questions [S23]

(See dedicated topic: [sysml-and-cuda](../topics/sysml-and-cuda.md).)

- Vector × matrix on GPU: vector `[B, 1, K]`, matrix `[B, K, N]` —
  design the most efficient algorithm.
- Design a tensor system that performs ops and computes gradients
  (mini autograd).
- Describe how to write an efficient MHA kernel on H100.
- Describe scaling LLM training from 8 GPU to 20k GPU — at each
  scale, the bottleneck and the parallelism technique you'd add.
- Large matrix multiplication in a two-level memory hierarchy.
- How would you improve quality of an LLM-based customer-support
  chatbot for a retailer?

## Research-vision questions [S6, S17]

- "What's your favorite recent paper and why?"
- "If you were to design the next-gen multimodal reasoning system,
  what would you prioritize?"
- "What's the biggest open problem in LLM post-training?"
- "Where do you think evaluation is headed?"

## Cross-refs
- [ML coding round](../rounds/ml-coding.md)
- [Transformers topic](../topics/transformers.md)
- [Reading list](../prep/reading-list.md)

## Sources
S1, S6, S17, S18, S19, S20, S23
