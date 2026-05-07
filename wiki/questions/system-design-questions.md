# System-design questions (bank)

Open-ended "Design X" prompts reported across OpenAI loops [S3, S5, S6,
S9, S17].

## General SWE prompts

| # | Prompt | Confidence | Sources |
|---|--------|------------|---------|
| 1 | Design Slack | high | S3, S9 |
| 2 | Design Online Chess | medium | S3 |
| 3 | Design GitHub Actions | medium | S3 |
| 4 | Design a Payment System | medium | S3 |
| 5 | Design ChatGPT (or "ChatGPT for 100M users") | high | S3, S5 |
| 6 | Design a webhook system | medium | S3 |
| 7 | Design a rate-limiter | medium | S9 |
| 8 | Design a notification fan-out service | low | S9 |

## ML / training prompts

| # | Prompt | Confidence | Sources |
|---|--------|------------|---------|
| 1 | Design a fault-tolerant training pipeline (>100B params) | high | S5, S6, S17 |
| 2 | Design an inference-serving system at frontier scale | high | S5, S6, S9 |
| 3 | Design an evaluation pipeline for a frontier reasoning model | medium | S6, S17 |
| 4 | Design a vector-DB-backed RAG system | medium | S6 |
| 5 | Design an agentic tool-use pipeline (planner, tools, exec) | medium | S6 |
| 6 | Design data ingestion + filtering pipeline for LLM pretraining | low | S6 |
| 7 | Design a feedback / preference-data collection system for RLHF | low | S6 |
| 8 | Design a personalized places/listings recommender (cold start) | medium | S20 |
| 9 | Detect duplicate accounts at scale (real-time classification + retrieval) | medium | S20 |
| 10 | Bootstrapping from unlabeled data ("data flywheel") | medium | S20 |

## sysML / scaling track [S23]

| # | Prompt | Confidence | Sources |
|---|--------|------------|---------|
| 1 | Scale LLM training from 8 GPU → 20k GPU; bottlenecks & parallelism plan | high | S23 |
| 2 | Vector × matrix on GPU: `[B,1,K] × [B,K,N]` | high | S23 |
| 3 | Design a tensor + autograd system | high | S23 |
| 4 | Efficient MHA kernel on H100 | high | S23 |
| 5 | Two-level-memory matrix multiplication | medium | S23 |
| 6 | Improve quality of an LLM-based customer-support chatbot | high | S23 |

## Approach

For each prompt, the answer should walk through:

1. **Functional scope** + non-functional targets.
2. **Capacity numbers** (QPS, payload, storage, GPU/host BW).
3. **Architecture sketch** (boxes + arrows).
4. **Data model** + key APIs.
5. **Failure modes** + reliability story.
6. **Performance hot path** + cost knobs.
7. **For ML prompts**: parallelism plan, KV-cache strategy, eval/feedback,
   safety/policy.

## See also

- [System design round](../rounds/system-design.md)
- [ML system design](../rounds/ml-system-design.md)

## Sources
S3, S5, S6, S9, S17, S20, S23
