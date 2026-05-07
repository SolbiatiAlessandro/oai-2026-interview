"""Training loop for TinyGPT on a synthetic periodic corpus.

Run: `python train.py`. Loss should fall below 0.05 within 500 steps when
the model and the loop are correct. As shipped it plateaus near
ln(vocab_size) ~ 2.30.
"""

import torch

from model import TinyGPT


def main() -> None:
    torch.manual_seed(0)

    text = "abcdefghij" * 200
    chars = sorted(set(text))
    vocab_size = len(chars)
    stoi = {c: i for i, c in enumerate(chars)}
    data = torch.tensor([stoi[c] for c in text], dtype=torch.long)

    block_size = 16
    batch_size = 32
    steps = 500
    lr = 3e-4

    def get_batch() -> tuple[torch.Tensor, torch.Tensor]:
        ix = torch.randint(0, len(data) - block_size - 1, (batch_size,))
        x = torch.stack([data[i : i + block_size] for i in ix])
        y = torch.stack([data[i + 1 : i + block_size + 1] for i in ix])
        return x, y

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = TinyGPT(
        vocab_size=vocab_size,
        d_model=64,
        n_heads=4,
        n_layers=2,
        block_size=block_size,
    ).to(device)
    optim = torch.optim.AdamW(model.parameters(), lr=lr)

    model.train()
    last = float("nan")
    for step in range(steps):
        x, y = get_batch()
        x, y = x.to(device), y.to(device)
        _, loss = model(x, y)
        loss.backward()
        optim.step()
        last = loss.item()
        if step % 50 == 0:
            print(f"step {step:4d} | loss {last:.4f}")

    uniform = torch.log(torch.tensor(float(vocab_size))).item()
    print(f"final loss {last:.4f}")
    print(f"baseline (uniform): {uniform:.4f}")


if __name__ == "__main__":
    main()
