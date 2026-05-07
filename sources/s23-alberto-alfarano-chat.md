# S23 — Alberto Alfarano (Meta sysML / OpenAI candidate signal) chat

- Source: WhatsApp / Messenger excerpt, Italian, dated 2025-03-11,
  shared by the repo owner.
- Author: Alberto Alfarano (Meta engineer working on sysML / FAIR-style
  large-model engineering).
- Confidence: HIGH (first-person from a practicing peer; specific,
  named questions and recommended reading).
- Ingested: 2026-05-07

## Why this source matters

This source documents the **sysML / "ML systems engineer" track** at
OpenAI, which is essentially invisible in aggregator sources. It is a
heavier, more low-level loop: distributed training math, GPU kernels
(Triton/CUDA), parallelism strategies (data / tensor / model / pipeline /
expert), IO-aware attention. The bar is "0 bullshit, only code firing",
and Alberto reports a teammate being let go for not meeting it.

Treat this as the canonical signal for sysML / ML-infra / scaling-team
loops at OpenAI in 2025-2026.

## Sample questions (verbatim, paraphrased to English from Italian)

1. **Vector × matrix on GPU.** Given a vector of shape `[B, 1, K]` and
   a matrix of shape `[B, K, N]`, design an efficient algorithm to
   compute the vector-matrix multiplication on GPU.
2. **Tensor system + autograd.** Design a system to perform tensor
   operations and compute gradients of those operations.
3. **MHA kernel on H100.** Describe how to write an efficient
   multi-head attention kernel on a GPU like H100.
4. **8 GPU → 20k GPU.** Describe the process of scaling up the training
   of an LLM from small scale (e.g. 8 GPU) to large scale (e.g. 20k
   GPU). Walk through the considerations of which limitations you'll
   hit at certain points and which parallelism techniques you'll use.
5. **Two-level memory matmul.** Large matrix multiplication in two
   memory levels.
6. **LLM customer-support quality.** How would you improve the quality
   of an LLM-based customer-support chatbot for a retailer?

## Adjacent topics Alberto reports as in-scope on this track

- Tensor parallelism, data parallelism, model parallelism — and the
  exact math for laying attention compute on the right GPUs.
- Fast matrix multiplication.
- Writing CUDA kernels in **Triton** (OpenAI's Python-front-end DSL)
  for fused operations like sliding-window attention + conv1d.

A reported standard prep prompt Alberto and his colleagues use:

> "Take Llama base and Llama-Instruct. How do you make this model
> top-tier on coding tasks? You have unlimited budget for data
> collection and enough machines."

## Recommended resource (cited verbatim by Alberto)

- `https://github.com/fla-org/flash-linear-attention` — efficient
  implementations of state-of-the-art linear-attention models in
  Torch and Triton. Good source of CUDA-kernel idioms.
- Read the literature directly — Llama and DeepSeek technical reports
  for what "production scaling" looks like.
- Alberto's own learning approach for CUDA: no single course; read
  github examples (especially fla-org), copy-paste, swear, repeat.

## Cultural signal from the chat

- Team described as "0 bullshit, only code firing" — emphasis on
  shipping low-level code, not docs/posts/communication.
- Reported example: a teammate doing "bullshit" was let go.
- Implication: this loop weights coding density and sysML depth far
  above the behavioral / mission-fit weight that dominates the
  Applied-team loops described in S20.

## How this maps into the wiki

- Adds a `wiki/topics/sysml-and-cuda.md` page (the depth surface for
  these questions).
- Adds a sysml-questions section to `wiki/questions/ml-questions.md`
  (or a dedicated `sysml-questions.md` if it grows).
- Calibrates `wiki/roles/ml-engineer.md` and
  `wiki/roles/research-engineer.md`: certain teams ("scaling",
  "training-infra", post-training infra) interview at the level shown
  here, even when the job title is generic ML Engineer or Research
  Engineer.
