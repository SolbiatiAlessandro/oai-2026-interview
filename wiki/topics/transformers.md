# Transformers & attention

The single most-tested ML topic in OpenAI ML and Research-Engineer loops.
The bar is "implement scaled-dot-product attention from scratch in <30
minutes, then multi-head, then a transformer block" [S6, S19].

## What you must be fluent on

### Mechanics

- Q/K/V projections from input embeddings.
- Scaled-dot-product attention: `softmax(QK^T / sqrt(d_k)) V`.
- Why the `sqrt(d_k)` scaling exists (variance control on dot products).
- Numerical stability of softmax: subtract max before exp.
- Causal mask (decoder self-attention) and padding mask (variable
  sequence length).
- Multi-head: split the embed dim across heads; project per head; concat;
  output projection.
- Position encoding: sinusoidal, learned, ALiBi, RoPE — what each
  gives you and what fails.

### Architectural pieces

- Pre-norm vs. post-norm. Why pre-norm scales to deep models.
- LayerNorm vs. RMSNorm.
- MLP block: 4× hidden expansion (or SwiGLU 2/3 ratio).
- Residual connections: gradient pathway, what fails without them.
- Decoder vs. encoder vs. encoder-decoder.

### Performance / inference

- KV-cache: what it stores, why it changes the FLOPs profile of
  decoding.
- Prefill vs. decode regimes (compute-bound vs. memory-bound).
- FlashAttention: tile-based, IO-aware; reduces HBM roundtrips.
- Paged attention (vLLM-style): non-contiguous KV-cache pages.
- Speculative decoding, continuous batching, chunked prefill.

### Training dynamics

- Learning-rate schedule: warmup + cosine; why warmup matters.
- Mixed precision: bf16 vs. fp16 + loss scaling; where overflow hits
  (softmax, layernorm, attention scores).
- Gradient clipping and why it stabilizes large-LR runs.
- Activation recomputation (a.k.a. checkpointing) for memory.
- Optimizer state memory (AdamW: 2× param count in fp32 + master copy).

### Distributed training

- Data parallel (DP), Tensor parallel (TP), Pipeline parallel (PP),
  Expert parallel (EP).
- ZeRO stages 1/2/3 and what each shards.
- 3D parallelism: which dim goes where, communication costs.
- Bubbles in pipeline parallel and how interleaved schedules
  reduce them.
- Gradient accumulation for large effective batch sizes.

## High-yield drills

1. Implement attention end-to-end on a whiteboard from memory.
2. Implement multi-head attention in PyTorch tensors, no `nn` modules.
3. Walk through a decoder forward pass with KV-cache step-by-step.
4. Compute the FLOPs and parameter count for a given config (depth,
   heads, hidden, vocab, seqlen).
5. Diagnose: "loss is NaN at step 50k of pretraining." Walk through
   your check-list.

## Reading

- Original Transformer: Vaswani et al., *Attention Is All You Need*.
- The Illustrated Transformer (Jay Alammar) — solid visual reference.
- Karpathy's *Let's build GPT* (YouTube) — implements the full thing.
- FlashAttention paper (Dao et al.).
- LLaMA, GPT-NeoX papers — modern decoder-only architectural choices.
- Scaling laws: Hoffmann et al. (Chinchilla), Kaplan et al.

## Cross-refs
- [ML coding round](../rounds/ml-coding.md)
- [ML system design](../rounds/ml-system-design.md)
- [ML questions](../questions/ml-questions.md)
- [Reading list](../prep/reading-list.md)

## Sources
S1, S6, S19
