# sysML & CUDA / Triton (scaling-track depth)

The depth surface for the sysML / ML-infra / scaling / training-infra
track at OpenAI. Many job titles here are generic ("ML Engineer",
"Research Engineer", "Software Engineer"), but the loop interviews at
the level of distributed training, GPU kernels, and parallelism math
[S6, S20, S23]. If you're targeting a team like *Scaling*, *Training-
Infra*, *Post-training*, or any team whose research runs at frontier
scale, plan to clear this surface in addition to standard ML coding.

> Cultural signal from S23: "0 bullshit, only code firing." A
> teammate doing "bullshit" was let go. Coding density and low-level
> depth dominate this track.

## Parallelism techniques you must own

For each: what it shards, what it doesn't, communication primitives,
where it breaks.

- **Data Parallel (DP)** — replicate model, shard batch. AllReduce on
  gradients. Bandwidth-bound; usable up to ~hundreds of GPUs cleanly.
- **Tensor Parallel (TP)** — shard individual matmul over GPUs;
  inserts AllReduce / AllGather inside each layer. Megatron-LM style.
  High intra-node bandwidth required (NVLink); rarely scales past one
  node well.
- **Pipeline Parallel (PP)** — split layers across stages; micro-batch
  to fill the pipeline. GPipe / 1F1B / interleaved-1F1B; understand
  pipeline-bubble math.
- **Expert Parallel (EP)** — for MoE; route tokens to experts on
  different GPUs; AllToAll communication, load-balancing losses.
- **ZeRO / FSDP** — DP that shards optimizer states (Z1), gradients
  (Z2), parameters (Z3). Memory savings vs. communication cost.
- **3D parallelism** — combine DP × TP × PP. Mapping dim → device
  topology to minimize collectives over slow links.
- **Sequence / context parallelism** — for very long contexts, shard
  the sequence dim across GPUs.

For the "scale 8 → 20k GPU" question [S23], walk the
**bottleneck-by-scale** path:

- 8 GPU → DP works; AllReduce over NVLink dominates.
- ~64 GPU → start to ZeRO-shard optimizer state (memory) and
  introduce TP for big layers.
- ~256-1k GPU → introduce PP across nodes; manage bubble carefully
  with interleaved schedules; AllReduce → ring or hierarchical.
- ~4k+ GPU → 3D parallelism + ZeRO-3 + careful overlap of comm and
  compute; per-node failure recovery becomes a first-class concern.
- ~20k GPU → MoE / EP for capacity, async checkpointing,
  fault-tolerant training (in-flight node loss), per-rank IO
  bandwidth, network topology-aware mappings.

## GPU-kernel depth

OpenAI's sysML loop expects fluency on the kernel side. The canonical
warm-up question (S23): given a vector `[B,1,K]` and a matrix
`[B,K,N]`, design the most efficient GPU algorithm.

What you should be able to discuss:

- **Memory hierarchy on H100**: HBM3 (~3 TB/s, ~80 GB), L2 cache,
  shared memory, registers. Compute-vs-memory roofline by op.
- **Tiled matmul**: blocking for shared-memory; warp-level tiling;
  tensorcore mma instructions; FP8/BF16 paths.
- **Two-level memory matmul** [S23]: explicit staging through L2 /
  shared-memory; double-buffering (prefetching tiles while computing).
- **Fused kernels**: avoid intermediate HBM round-trips. Examples:
  fused softmax + dropout, fused attention (FlashAttention).
- **FlashAttention v2/v3**: tile over sequence, online softmax,
  no materialization of `QK^T`. IO-bound → compute-bound shift.
- **Sliding-window attention** kernel: tile only over the window,
  causal-mask combined with the window mask cheaply.

### Triton

OpenAI's own Triton is the expected DSL [S23]. You should know:

- The block-pointer / grid programming model.
- Loading tiles, accumulating in registers, storing once.
- Auto-tuning via `triton.autotune` configs.
- Common pitfalls: bank conflicts, mask handling for partial tiles,
  numerical stability of softmax in bf16.

Recommended reading [S23]:

- `https://github.com/fla-org/flash-linear-attention` — production-
  grade Torch + Triton implementations of linear-attention variants.
- The original Triton tutorials (matmul, softmax, layernorm,
  attention).
- DeepSeek-V3 and Llama-3 technical reports for what frontier-scale
  parallelism plans look like in production.

## Autograd-system design [S23]

"Design a system to perform tensor operations and compute gradients."
What good answers cover:

- **Tensor abstraction**: storage + stride + dtype + device + grad.
- **Op registry** with forward + backward functions.
- **Computation graph**: dynamic (define-by-run, PyTorch-style) vs.
  static (define-then-run). Trade-offs on optimizability vs. ease of
  use.
- **Autograd engine**: topological-sort the graph, scatter outgoing
  gradients, accumulate, free intermediate buffers.
- **Memory tricks**: activation checkpointing (recompute on backward
  to save memory), gradient accumulation across micro-batches.
- **Distributed angle**: communication hooks on the backward graph
  (DDP `register_comm_hook`), overlap comm with compute.

## LLM customer-support quality [S23]

The "improve a customer-support chatbot for a retailer" prompt is a
disguised end-to-end LLM-systems question. Cover:

- **Eval first**: build a labeled eval set from real tickets; track
  resolution rate, escalation rate, hallucination rate, deflection
  rate.
- **Data flywheel**: capture conversation outcomes, mine for
  high-quality preference pairs.
- **Retrieval**: structured product / policy data via RAG; hybrid
  retrieval (BM25 + dense); freshness pipeline.
- **Model training**: SFT on cleaned tickets → DPO / RLAIF on
  preference data → continual-evaluation gate before each release.
- **Guardrails**: PII redaction, refusal / escalation policy, prompt-
  injection defenses on retrieved content.
- **Online**: A/B traffic, real-time monitoring, shadow-mode regression
  catch.

## Practice / drilling

- Reproduce nanoGPT once. Then write a Triton MHA kernel and benchmark
  vs. `nn.MultiheadAttention` on a single H100.
- Implement a tiny autograd engine (Karpathy's *micrograd* is the
  canonical 100-line version; extend to tensors).
- Read the FlashAttention-2 paper end-to-end, then the FlashAttention-3
  paper, and explain the algorithmic and hardware deltas.
- Sketch a 3D-parallelism plan for a 70B-param model on 1024 H100s.

## Cross-refs
- [Transformers topic](transformers.md)
- [ML system design](../rounds/ml-system-design.md)
- [ML coding round](../rounds/ml-coding.md)
- [Reading list](../prep/reading-list.md)

## Sources
S6, S19, S20, S23
