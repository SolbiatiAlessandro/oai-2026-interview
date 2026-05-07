# ML debugging round

A 60-minute, **PyTorch-flavored, fix-the-broken-transformer** round. The
canonical OpenAI ML round in 2025-2026 for ML-Engineer and Research-
Engineer loops [S6, S20, S19].

## Format (verbatim from OpenAI's recruiter email, captured in S20)

> "This 60 minute interview will be a machine learning, debugging
> exercise. You'll be given a short implementation of a ML model
> (using Python and PyTorch) and be tasked to find and fix all bugs in
> order for the model to work successfully. This exercise tests your
> knowledge of ML architectures and algorithms, your ability to trace
> bugs back to their source, and your level of attention to detail.
> Familiarity with the Transformer model would be helpful." [S20]

## What's actually given

- A working-but-wrong PyTorch implementation of a small ML model.
  Most-reported subject: a **multi-headed transformer** with ~4-5
  bugs [S20].
- The code **runs**. Outputs look plausible. You have to judge for
  yourself whether each numerical/structural behavior is correct
  [S20].
- A second 30-minute part is sometimes appended: convert a small LLM
  training script into a classification training task — pick the
  embedding to use, define the loss, compute model accuracy [S20].

## Bug families to expect [S20, S6, S19]

- **Tensor-shape misalignment**: Q/K/V projections, head reshape,
  permute/transpose around `softmax(QK^T)`.
- **Missing attention scaling**: divide by `sqrt(d_k)` before
  softmax.
- **Wrong masking**: causal mask off by one, padding mask applied
  after softmax instead of before, mask broadcast mistake.
- **Wrong softmax dim**: `dim=-1` vs. `dim=-2`.
- **Wrong residual / norm placement**: pre-norm vs. post-norm
  swapped; residual added before instead of after the sublayer.
- **Optimizer step / loss bugs**: `loss.backward()` missing,
  `optimizer.zero_grad()` missing, accumulation of gradients,
  detached graph.
- **Dtype / device bugs**: tensors on `cpu` vs. `cuda`; mixed-precision
  overflow in softmax/layernorm.
- **Embedding bugs**: positional encoding not added; vocab off-by-one;
  wrong `nn.Embedding` shape.
- **Training-loop bugs**: dataset not shuffled, eval inside training
  loop without `model.eval()`, batch norm in inference mode.

## Debugging tooling worth practicing [S20]

- `tensor.retain_grad()` on intermediate activations to inspect
  gradient flow on the backward pass.
- Per-layer shape printing in a one-liner loop to localize the broken
  module fast.
- `torch.autograd.set_detect_anomaly(True)` while bisecting.
- `assert tensor.shape == expected_shape` peppered through forward.
- Tiny reproducible inputs (`B=2, T=4, d=8`) so you can mentally trace
  a forward pass.

## How candidates are graded

- **Time-to-first-fix**: a fluent candidate finishes 4-5 bugs in
  ~15 min if they've practiced [S20].
- **Sound diagnosis**: explain *why* this is a bug, not just patch
  syntax.
- **Numerical judgement**: spot when a "running" model is producing
  the wrong distribution.
- **ML knowledge**: causal masking, scaling, residuals, optimizers,
  not just Python pattern-matching.

## Practice surface (high-yield)

- **nanoGPT** and **minGPT** (Karpathy) — implement once from scratch,
  then have an LLM inject 4-5 bugs and debug under a 20-min timer
  [S20].
- Karpathy's *Let's build GPT* and *backprop ninja* videos — build the
  forward and backward by hand once.
- Neel Nanda — *implement GPT-2 from scratch* and *A Mathematical
  Framework for Transformer Circuits* [S20].
- The fla-org / flash-linear-attention reference for production-style
  attention code [S23].

## Variant: multi-threaded back-propagation

A reported research-screen-style variant: debug a **multi-threaded
back-propagation** implementation, including how to split the matrix
for distributed compute across machines [S20]. Maps to sysML / scaling
loops — see [sysml-and-cuda](../topics/sysml-and-cuda.md).

## Cross-refs
- [ML coding round](ml-coding.md)
- [Transformers topic](../topics/transformers.md)
- [sysML & CUDA topic](../topics/sysml-and-cuda.md)
- [ML questions bank](../questions/ml-questions.md)

## Sources
S6, S19, S20, S23
