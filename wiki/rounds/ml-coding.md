# ML coding round

The ML-coding round is the round most-distinctive to ML/RE/Researcher
loops. You are asked to **implement a model component from scratch** in
NumPy or PyTorch (sometimes plain Python). The canonical archetype is
*"implement scaled-dot-product attention, then multi-head attention,
then a transformer block"* [S6, S19].

## Format

- **Duration**: 60 min, occasionally 75 min for staff loops [S6].
- **Tooling**: CoderPad with Python; some interviewers permit Jupyter-
  style or screen-share own-IDE [S6].
- **Constraints**: tensor ops only — no `torch.nn.MultiheadAttention`
  unless explicitly allowed. The point is whether you understand what
  the API does, not whether you can call it [S6, S19].

## Canonical questions

1. **Scaled-dot-product attention** in NumPy or PyTorch tensors only
   [S6, S19]. Follow-ups: causal mask, padding mask, batch dimension,
   numerical stability of softmax.
2. **Multi-head attention** — heads, projections, reshape vs.
   `view`/`einsum`, output projection [S6].
3. **Tiny transformer block** (attention + residual + MLP +
   layernorm) [S6].
4. **Minimal training loop** for a tiny LM: data batching, forward,
   loss, backward, optimizer step, eval [S6, S19].
5. **K-means / KNN / logistic regression / softmax-classifier from
   scratch** for less senior loops or as a warm-up [S19].
6. **Tokenizer / BPE basics** when the team is post-training- or
   data-leaning [S19].
7. **ML debugging / training-dynamics** scenario: loss spikes,
   gradient explosions, dead ReLUs, NaNs in fp16 — diagnose and fix
   [S6, S19].

## Bar / signals

- Can you write attention without a reference, including masking and
  numerical-stability tricks? [S6]
- Do you reach for `einsum`/explicit matmul vs. magical reshapes? Does
  your code handle batch and head dimensions correctly? [S6]
- Do you know the failure modes of training, not just the math? [S6, S19]
- Time-and-space complexity analysis when asked [S19].

## Common follow-ups

- "Make it causal." → triangular mask, scaled before softmax.
- "Add padding mask." → `-inf` on padded positions, careful with
  softmax dtype.
- "What's the FLOPs of MHA at sequence length N?" → `O(N^2 * d)` for
  attention, `O(N * d^2)` for projections; matters when discussing
  long-context.
- "How would FlashAttention change this?" — IO-aware attention,
  tile-based block compute, reduces HBM reads/writes; expected fluency
  for staff/research roles [S6, S19].
- "Where does mixed-precision break?" → softmax-stability, layernorm,
  loss-scaling [S6, S19].

## Why this round exists

OpenAI is checking that you've actually built models, not just used
them. The bar is "30 minutes from blank file to a working transformer
block, with a sensible training loop" — that's the working assumption
of the panel [S6].

## Cross-refs
- [Transformers topic](../topics/transformers.md)
- [ML questions](../questions/ml-questions.md)
- [Reading list](../prep/reading-list.md)

## Sources
S1, S6, S17, S18, S19
