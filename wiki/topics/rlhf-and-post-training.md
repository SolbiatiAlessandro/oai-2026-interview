# Post-training: RLHF → DPO → GRPO → safe completions

The post-training stack is alignment's main delivery vehicle. Required
fluency for the Researcher-Alignment loop [S6, S19, S24, S46]. The
panel will assume you can derive these losses on a whiteboard and
discuss the failure modes of each.

## The pipeline

### 1. SFT (supervised fine-tuning)

Fit the model to high-quality demonstration data via standard cross-
entropy on token sequences. Sets the prior the rest of the stack
operates on. Failure modes: capability regression, narrow distribution
of demos.

### 2. Reward modeling

Collect preference comparisons `(prompt, completion_a, completion_b,
preferred)`. Train `r_φ` via Bradley-Terry:

```
P(a > b) = σ(r_φ(prompt, a) - r_φ(prompt, b))
loss = -log P(preferred > non-preferred)
```

Failure modes: distribution shift between RM training and policy-roll-
out distribution, length bias, sycophancy bias [S46].

### 3. RLHF (PPO with KL penalty)

Optimize the policy `π_θ` against `r_φ` while penalizing KL from a
frozen reference (typically the SFT model) `π_ref`:

```
J(θ) = E[r_φ(x, y) - β · KL(π_θ(·|x) || π_ref(·|x))]
```

PPO clipping prevents catastrophic policy updates. Common knobs: KL
coefficient `β`, sampling temperature, advantage normalization.

Failure modes:
- Reward hacking (Goodhart's law on `r_φ`) [S46].
- Mode collapse if `β` is too low.
- Over-refusal if RM was trained on too many "harmful" labels.
- Sycophancy as reward hacking [S41, S46].

### 4. DPO (Direct Preference Optimization)

Skip the explicit RM. Derive a closed-form policy update from the same
preference data:

```
loss = -log σ( β · log(π_θ(y_w|x)/π_ref(y_w|x))
              - β · log(π_θ(y_l|x)/π_ref(y_l|x)) )
```

Why it works: under the Bradley-Terry assumption, the optimal RLHF
solution has the form `π*(y|x) ∝ π_ref(y|x) · exp(r(x,y)/β)`. Solving
for `r` and plugging into the BT preference probability gives the DPO
loss directly on `π_θ`, with no RM in the loop.

Trade-offs vs. RLHF:
- ✅ Simpler, no RM training, no rollout sampling.
- ❌ Cannot exploit better-than-data completions via online sampling.
- ❌ More sensitive to preference-data noise.
- ❌ The implicit reward is the policy, so reward hacking shows up
  directly in the policy's behavior.

### 5. GRPO (Group-Relative Policy Optimization)

Drops the value-function critic. Sample a group of `G` completions per
prompt, compute group-relative advantages:

```
A_i = (r_i - mean(r_1..r_G)) / std(r_1..r_G)
```

Update via PPO-style clipped ratio with `A_i` as the advantage.

Why it matters: dramatically simpler infra (no critic to train and
keep in sync), and works well when rewards are sparse / verifiable
(e.g. unit-test-passes for code, ground-truth-match for math). DeepSeek
popularized it; OpenAI's o-series uses related ideas.

### 6. Safe completions (GPT-5, 2025) [S42]

Reframes the alignment objective. Instead of "comply" vs. "refuse" as
the safety axis, train the model to produce a *safe completion* —
the most-helpful response that stays inside the policy. Output-
centric reward function replaces the binary refusal head.

Why it matters:
- Removes the over-refusal failure mode from policy-aligned RL.
- Lets the model find creative-but-safe paths through ambiguous
  requests.
- Pairs naturally with Deliberative Alignment [S31] — the model
  reasons over the spec to *find* the safe completion.

## Reward hacking — the recurring failure mode

(See [reward-hacking topic](reward-hacking.md) for the full treatment.)

- **Goodhart's law**: every proxy reward eventually decouples from the
  true objective at the optimum.
- **Length bias**: humans (and RMs trained on human preferences) often
  prefer longer answers; policies learn to inflate.
- **Sycophancy** [S41]: agreeing with the user's stated belief is
  preferred → RL pushes toward sycophantic completions.
- **Reasoning-time reward hacking**: in CoT-trained models, the
  policy can learn to game the reasoning trace itself [S36].

Lilian Weng's Nov 2024 *Reward Hacking in RL* post [S46] is still the
canonical reference; expect the panel to assume you've read it.

## Where this hits in the loop

- **ML coding screen / ML coding onsite**: implement a tiny RLHF
  step, a DPO loss, or a CriticGPT-style critic loop from scratch.
  See [ml-coding](../rounds/ml-coding.md).
- **Alignment-specific technical**: design an experiment to detect
  reward hacking before deployment; design a preference-collection
  protocol that resists sycophancy; explain why DPO might or might
  not catch a specific failure mode.
- **Behavioral**: the sycophancy-in-GPT-4o retrospective [S41] is a
  natural launching point for "tell me about a quality vs. shipping
  trade-off" stories.

## Reading

- *Training language models to follow instructions* (Ouyang et al.,
  InstructGPT, 2022).
- *Direct Preference Optimization* (Rafailov et al., 2023).
- *DeepSeekMath / DeepSeek-R1* (GRPO popularization, 2024-2025).
- *Safe Completions in GPT-5* [S42].
- Lilian Weng — *Reward Hacking in RL* [S46].
- Sundeep Teki — *The complete guide to post-training LLMs* [S6].
- *Constitutional AI* (Anthropic) for the comparison-class.

## Cross-refs
- [Alignment topic overview](alignment.md)
- [Reward hacking topic](reward-hacking.md)
- [Scalable oversight](scalable-oversight.md)
- [ML coding round](../rounds/ml-coding.md)
- [Alignment questions](../questions/alignment-questions.md)

## Sources
S6, S19, S24, S31, S34, S36, S41, S42, S46
