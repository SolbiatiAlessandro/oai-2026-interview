# ML debugging practice — fix-the-broken-transformer

Mock of OpenAI's 60-minute ML debugging round. You have a tiny PyTorch
character-level transformer and a training script. The training **runs**
but the **loss does not go down**. Find and fix the bugs.

See [`../../rounds/ml-debugging.md`](../../rounds/ml-debugging.md) for the
round's format, scoring, and bug families.

## Setup

```bash
pip install torch
cd wiki/prep/ml-debugging-practice
```

## Task

Train a 2-layer character-level transformer on a synthetic, perfectly
periodic corpus (`"abcdefghij"` repeated). With a working model the loss
falls below `0.05` within a few hundred steps. As shipped, the loss
drops some early but then **bounces around 0.3 – 1.0** and never
converges — exactly the "the model is not training" picture you'll get
in the round.

## Start training

```bash
python train.py
```

You should see something like:

```
step    0 | loss 2.47
step   50 | loss 0.89
step  100 | loss 0.33
step  150 | loss 0.15
step  200 | loss 0.25
step  300 | loss 0.38
step  400 | loss 0.84
final loss ~0.5 – 1.0
baseline (uniform): 2.3026
```

The loss is not converging. Fix the bugs.

A correct, all-fixes run reaches `< 0.05` by step 150 and `< 0.02` by
step 400.

## Rules of the game (mirrors the real round)

- The code runs end-to-end. No tracebacks. Outputs look plausible.
- Bugs are spread across **the model** and **the training loop**.
- There are **5 bugs**. A fluent candidate finds 4-5 in ~15 min.
- Do not change the architecture, hyperparameters, dataset, or
  optimizer. Just fix bugs.
- Target: loss < `0.05` within `500` steps.

## Suggested workflow

1. Read `model.py` and `train.py` end-to-end before touching anything.
2. Sanity-check shapes with tiny inputs (`B=2, T=4`).
3. Print intermediate tensors / gradients. `set_detect_anomaly(True)`
   if you suspect autograd issues.
4. Bisect: disable layers, swap in `nn.Identity`, see what changes.
5. Each fix should come with a one-sentence "why this was a bug."

## Files

- `model.py` — buggy `TinyGPT` (causal self-attention + MLP blocks).
- `train.py` — buggy training loop on the synthetic dataset.
- `SOLUTIONS.md` — **don't open until you give up or finish.** The 5
  bugs, where they live, and why each one prevents learning.

## Stretch (the reported 30-min part 2 [S20])

Once training works, convert this next-token LM into a sequence-
classification task: given a length-16 window, predict whether the
window is sorted (ascending) or not. Pick which token's hidden state
to feed the classifier head, define the loss, and report accuracy.
