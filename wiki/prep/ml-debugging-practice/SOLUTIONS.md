# Solutions — don't read until you've tried

Five planted bugs. Listed in roughly the order they bite the loss.

## Bug 1 — Missing attention scaling (`model.py`, `CausalSelfAttention.forward`)

```python
att = q @ k.transpose(-2, -1)
```

Should be:

```python
att = (q @ k.transpose(-2, -1)) / math.sqrt(self.d_head)
```

Why: without `1/√d_k` the logits grow as `O(d_head)`. Softmax saturates to
near one-hot, gradients vanish across the attention layer. Standard
"Attention Is All You Need" detail.

## Bug 2 — Wrong Q/K/V head reshape (`model.py`, `CausalSelfAttention.forward`)

```python
q = q.reshape(B, self.n_heads, T, self.d_head)
k = k.reshape(B, self.n_heads, T, self.d_head)
v = v.reshape(B, self.n_heads, T, self.d_head)
```

`view` reads the underlying buffer in row-major order. The projection
output is laid out as `(B, T, n_heads * d_head)`, so the contiguous chunk
of size `d_head` corresponds to **one head at one position**, not "all
heads at one position." Reshaping to `(B, n_heads, T, d_head)` therefore
splits the time axis across heads — head 0 sees the first `T/n_heads`
positions of every step, etc. Each "head" gets a different slice of the
sequence, attention is computed over a scrambled axis, and there is no
gradient signal that maps back to per-token features.

Fix is the standard split-then-transpose:

```python
q = q.view(B, T, self.n_heads, self.d_head).transpose(1, 2)
k = k.view(B, T, self.n_heads, self.d_head).transpose(1, 2)
v = v.view(B, T, self.n_heads, self.d_head).transpose(1, 2)
```

## Bug 3 — Softmax over the wrong dim (`model.py`, `CausalSelfAttention.forward`)

```python
att = F.softmax(att, dim=-2)
```

`att` has shape `(B, h, T_q, T_k)`. We want a probability distribution
over **keys** for each query, i.e. last dim. `dim=-2` normalizes over
queries instead — columns sum to 1, rows don't. Fix:

```python
att = F.softmax(att, dim=-1)
```

## Bug 4 — Missing residual on the attention sublayer (`model.py`, `Block.forward`)

```python
x = self.attn(self.ln1(x))
x = x + self.mlp(self.ln2(x))
```

The first line **replaces** `x` instead of adding to it. The token and
positional embeddings never reach the MLP / output head except through
the (broken) attention. Fix:

```python
x = x + self.attn(self.ln1(x))
x = x + self.mlp(self.ln2(x))
```

## Bug 5 — Missing `optimizer.zero_grad()` (`train.py`, training loop)

```python
_, loss = model(x, y)
loss.backward()
optim.step()
```

Gradients accumulate across steps because nothing clears them. After a
few steps the running gradient is a sum of stale gradients pointing in
inconsistent directions; the AdamW step is dominated by noise and the
loss never settles. Fix:

```python
_, loss = model(x, y)
optim.zero_grad(set_to_none=True)
loss.backward()
optim.step()
```

## Sanity check after fixing

With all five fixed and `torch.manual_seed(0)`, training on a CPU
produces something close to:

```
step    0 | loss 2.6349
step   50 | loss 0.4906
step  100 | loss 0.1078
step  150 | loss 0.0559
step  200 | loss 0.0369
step  300 | loss 0.0210
step  400 | loss 0.0140
step  450 | loss 0.0118
final loss 0.0101
```

The corpus is perfectly periodic, so a working model essentially memorizes
the cycle. Anything still bouncing around `0.3 – 1.0` means at least one
bug is unfixed.
