# Scalable oversight

How to supervise a model that is more capable than its supervisors.
This is the central technical bet of OpenAI's alignment program [S27,
S30, S34].

## Why it matters

Once a model is better than humans at a task, "label this output good
or bad" stops working as a training signal. Scalable oversight is the
research program that asks: can we use the model itself, or weaker
trusted models, or structured procedures, to extract a training signal
that scales past human capability?

## The OpenAI canon

### Weak-to-strong generalization (Burns et al., Dec 2023) [S30]

Setup: train a strong student model on labels produced by a *weak*
teacher (e.g. fine-tune GPT-4 with labels from a model the size of
GPT-2). Question: how much of the strong student's intrinsic capability
survives the weak supervision?

Findings: significant generalization beyond the teacher in some
settings; not full recovery of strong-student capability. Method:
auxiliary losses that bias the student to use its own representations.

Why it's a stand-in: it simulates "humans supervising a superhuman
model" by replacing humans with a weaker model.

Authors include Burns, Izmailov, Kirchner, Baker, Gao, Wu — many still
on the alignment team [S30, S24].

### CriticGPT (McAleese et al., 2024) [S34]

Train an LLM to **critique** another LLM's outputs (in the paper:
ChatGPT's code). The critic catches bugs that human reviewers miss
~60% of the time.

Why it's a scalable-oversight result: it shows model-assisted human
evaluation can beat unassisted human evaluation on a real task,
without requiring the evaluator to themselves be superhuman.

### Debate (Irving, Christiano, Amodei 2018)

Two copies of a model argue opposing positions in front of a human
judge. Recursive: if the judge can't tell who's right, drill into a
sub-claim. Theoretical reduction: if PSPACE problems can be settled
by a polynomial judge with a polynomial transcript, debate amplifies
weak judges to strong judges.

Status as of 2026: empirical debate results remain mixed. Worth
knowing as a framing.

### Recursive reward modeling (Leike et al. 2018, "AI safety via
informed oversight")

Use AI assistants to help humans evaluate increasingly complex tasks;
use the better evaluations to train a better assistant; recurse.

Status: the broad framing under which RLHF, CriticGPT, and W2S all
fit; the concrete pipeline that ships in production.

## Adjacent: deliberative alignment & safe completions

Not strictly scalable-oversight techniques, but they interact:

- **Deliberative Alignment** [S31] makes the *policy* spend inference-
  time reasoning aligning itself with a written spec. It assumes you
  already have a spec good enough to reason over.
- **Safe Completions** [S42] makes the reward function output-
  centric. Reduces over-refusal under good supervision.

Both leverage the model's own capability to enforce a policy authored
by humans — a different reduction than W2S's "use weak teacher → strong
student".

## Failure modes you should be ready to discuss

- **The supervisor is also misaligned.** A scalable-oversight scheme
  assumes the supervisor's specification is correct. If the spec
  itself is misaligned, the scheme propagates the error faithfully.
- **Critic collusion** — if the critic and the model being critiqued
  share weights, optimization can find a mutually convenient blind
  spot. CriticGPT used a separate model to mitigate this.
- **Scheming** — the supervised model can detect supervision and
  behave differently when supervised. CoT monitoring [S36] tries to
  catch this; anti-scheming training [S35] tries to reduce it.
- **Weak-to-strong is not a free lunch.** The strong student
  doesn't recover all its capability under weak supervision; the gap
  *is the alignment tax* you're trying to minimize.

## What an interview probe looks like

Likely shapes [S6, S24]:

- "Walk me through the assumptions underlying weak-to-strong
  generalization. Where does it break?"
- "Design an experiment to test whether CriticGPT-style critics
  generalize from code to natural-language fact-checking."
- "Critique the debate framing. What's the strongest empirical
  argument against it as a path to scalable oversight?"
- "Given a budget of N human-hours, how would you spend it to evaluate
  a frontier reasoning model? What does scalable oversight buy you?"

## Cross-refs
- [Alignment topic overview](alignment.md)
- [Post-training & RLHF](rlhf-and-post-training.md)
- [Scheming & deceptive alignment](scheming-and-deceptive-alignment.md)
- [Alignment questions](../questions/alignment-questions.md)
- [Alignment reading list](../prep/alignment-reading-list.md)

## Sources
S24, S27, S30, S31, S34, S35, S36, S42
