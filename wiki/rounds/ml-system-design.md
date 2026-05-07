# ML system design

ML/MLE/RE loops typically include a system-design round explicitly framed
around an ML system: training infrastructure, serving infrastructure, an
evaluation pipeline, or a retrieval/agent system. This is **not** a pure
SWE design — it expects ML-specific reasoning [S5, S6, S9, S17].

## Canonical prompts

- **Design a fault-tolerant training pipeline** for a >100B-param
  model. Concurrency, checkpointing, recovery, gradient sync,
  failure handling [S5, S6, S17].
- **Design ChatGPT** at frontier scale (100M+ users). Inference
  serving, caching, rate-limiting, safety-filtering, telemetry
  [S3, S5, S9].
- **Design an evaluation pipeline** for a frontier reasoning model.
  Datasets, prompt management, grader-models, score aggregation,
  drift detection [S6, S17].
- **Design a vector-database-backed RAG system**. Index choices,
  refresh, eval, rate-limit, hybrid retrieval [S6].
- **Design an agentic tool-use pipeline**. Planner, tool registry,
  execution, observability, guardrails [S6].

## What good answers cover [S5, S6, S9, S17]

- **Workload model**: tokens/s, batch sizes, sequence lengths, peak
  vs. avg, autoregressive vs. prefill.
- **Compute / memory math**: parameter count → memory footprint
  (incl. KV cache), GPU/host bandwidth, parallelism plan (DP / TP /
  PP / EP).
- **Training-specific**: optimizer state memory, ZeRO, mixed precision,
  checkpoint cadence, activation recomputation.
- **Serving-specific**: continuous batching, KV-cache reuse,
  speculative decoding, paged attention, tail-latency mitigation.
- **Reliability**: bad-input handling, timeouts, circuit breakers,
  poisoned-cache invalidation, rolling deploys vs. shadow traffic.
- **Eval and feedback**: A/B traffic, online metrics, offline eval
  harness, win-rate vs. baseline.
- **Safety and policy**: prompt-injection defenses, content filters,
  red-team coverage, rate-limit bypass.
- **Cost**: $/1k tokens at the design point, knobs that move it
  most.

## Pitfalls

- Treating it as a SWE design: not enough ML-specific reasoning
  (capacity math, parallelism plan, KV cache, eval) [S6].
- Treating it as a research talk: hand-waving the infra and skipping
  capacity numbers, queue depths, failure handling [S6].
- Designing a *system* without a *workload*: failing to articulate
  who the users are and what they actually do [S5, S9].

## Cross-refs
- [System design (general)](system-design.md)
- [System-design questions](../questions/system-design-questions.md)
- [Transformers topic](../topics/transformers.md)
- [Reading list](../prep/reading-list.md)

## Sources
S3, S5, S6, S9, S17
