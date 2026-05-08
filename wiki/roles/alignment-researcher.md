# Researcher, Alignment (primary focus)

The OpenAI **Researcher, Alignment** role (`openai.com/careers/
researcher-alignment-san-francisco/`) is a research-track IC role on
the post-Superalignment, post-Mission-Alignment alignment teams. The
loop is research-leaning (paper presentation, alignment-specific
technical, lighter coding density than MLE/RE) but the coding bar is
non-trivially close to the RE bar [S6, S20, S25]. This page is the
**primary focus** of this KB as of 2026-05-08.

## Caveat up front

**No clean first-person Alignment Researcher loop writeup exists
publicly as of May 2026** [S24]. The loop reconstructed below is a
synthesis of (a) the official job description, (b) general OpenAI
Researcher / Research-Engineer loop reporting (S1, S3, S5, S6, S20),
and (c) candidate accounts of adjacent ML-Researcher / RE loops.
Verify the specific round mix with your recruiter; this page leans
high-recall, treat round count as ±1.

## Reconstructed loop

1. **Recruiter screen** (~30-45 min). "Why OpenAI / why alignment" is
   probed harder than for SWE/MLE. Logistics: SF hybrid, 3 days in
   office; PhD or equivalent expected per JD [S25].
2. **Hiring-manager screen** (~30-45 min) with the team lead. As of
   Feb 2026 the hiring manager is typically on Alignment, Alignment
   Science, Alignment Training, or Misalignment Research, since
   *Mission Alignment* was disbanded [S24, S44].
3. **Coding screen** (~60 min, CoderPad). Same gated production-coding
   format as MLE/SWE/RE loops — see [coding round](../rounds/coding.md).
   Two-of-four-correct gate still applies despite this being a
   research role [S2, S3, S20].
4. **ML coding screen** (~60 min) — implement attention / a small
   transformer / an RLHF or DPO loss / a CriticGPT-style critic loop
   from scratch. See [ml-coding](../rounds/ml-coding.md) and
   [post-training topic](../topics/rlhf-and-post-training.md).
5. **Research / paper presentation** (~45-60 min). Present a prior
   alignment / ML project. Probing on choices, ablations, alternatives,
   "what would you do next?". See
   [deep-dive-template](../prep/deep-dive-template.md) — keep the
   *research-taste* version, not the staff-eng technical-leadership
   version.
6. **Alignment-specific technical** (~60 min). Discussion +
   whiteboard. Likely shapes:
   - Design an evaluation for a specific safety property.
   - Critique a recent alignment paper end-to-end.
   - Propose a research direction given an open problem.
   - Walk through a concrete threat model and what experiments
     would falsify it.
   - Read a snippet of broken alignment code and fix it.
   See [alignment-questions](../questions/alignment-questions.md) for
   the bank of probes.
7. **Behavioral / mission-fit** (~30-45 min). Heavier than for SWE
   loops. Reported prompts: "why OpenAI vs. Anthropic / SSI", "what
   would you do if you found a model behaving in a misaligned way
   during training?". See [why-openai](../prep/why-openai.md) and
   [behavioral](../rounds/behavioral.md).
8. Some loops include a **48-hour take-home** (build an eval harness,
   write a small alignment-research tool). More common on engineering-
   leaning postings (Alignment Training) than on the research IC
   posting [S24].

End-to-end: 4-8 weeks. Onsite block: 4-6 hours over 1-2 days. Tooling:
CoderPad standard; some candidates report own-IDE-with-screenshare
allowed [S3, S11, S20].

## What's distinctively graded

Alignment Researcher candidates report being graded against a slightly
different rubric than MLE/RE [S24, S25]:

- **Empirical research taste** — can you design a clean experiment
  that *falsifies* a specific safety hypothesis? Not "would training
  on more data help?" but "what's the smallest study that would
  change your mind?".
- **Literature fluency** — can you place your work and theirs in the
  arc from RLHF → CriticGPT → W2S → Deliberative Alignment → Safe
  Completions → Anti-Scheming? Naming papers without understanding the
  *delta* each one adds is a red flag.
- **Threat-model clarity** — can you separate alignment from control
  (Greenblatt et al. [S38])? Distinguish capability eval from
  alignment eval? Articulate why scheming is hard to detect with the
  current toolkit?
- **Coding density** — non-negotiable. The Sundeep-Teki framing of
  OpenAI as "pragmatic scalers" applies to alignment too [S6]; you
  should be able to spin up a training loop and an eval harness fast.
- **Mission alignment** — not generic AGI hype. A specific view on
  what's worth working on, why now, and what your evidence-update
  rules are. See [why-openai](../prep/why-openai.md).

## What's *not* graded the same as MLE

- **Production-system depth** matters less than for MLE / RE. You
  don't need to be ready to design ChatGPT-for-100M-users or a
  fault-tolerant training pipeline at staff-grade detail.
- **Pure ML-system-design** is partially substituted by alignment-eval
  / alignment-experiment design.
- **sysML / kernel-level depth** [S23] is *not* expected for the
  research IC track (it is expected on Alignment-Training-engineering
  and on training-infra teams).

## Reading list (anchored on this role)

See [alignment-reading-list](../prep/alignment-reading-list.md). Highest
priorities, do these first:

1. **OpenAI's alignment papers, in order** [S30, S31, S32, S33, S34, S35,
   S36, S42]: Weak-to-strong → CriticGPT → Instruction Hierarchy →
   Scaling SAEs → Deliberative Alignment → Safe Completions → Anti-
   scheming + CoT monitoring.
2. **alignment.openai.com Dec-2025 launch posts** [S26]: "Hello
   World", emergent-misalignment suppression, eval-awareness
   sidestepping, SAE latent attribution, code verification at scale.
3. **GPT-5 system card** safety section + Preparedness Framework v2
   [S39, S53].
4. **Lilian Weng — Reward Hacking in RL** [S46]; **Greenblatt et al.
   Alignment Faking & AI Control** [S37, S38]; **Apollo Research
   scheming work** [S50].
5. **Boaz Barak Harvard CS 2881 syllabus** [S45] — closest public
   proxy for one of this role's likely interviewers.

## Adjacent role distinctions

- **Researcher, Alignment Science** [S25] — empirical-science framing;
  ran the December 2025 launch of `alignment.openai.com`.
- **Researcher, Alignment Training** — post-training-flavored; closer
  to RLHF-engineering bar.
- **Researcher, Misalignment Research (NYC)** — model-organisms-of-
  misalignment work; co-published Sept 2025 with Apollo Research [S35].
- **Member of Technical Staff, Practical Alignment** — engineering-
  heavy alignment work shipping into product.
- **Research Engineer, Safety Systems** — owns deployed safety stack
  (refusal training, classifiers, deployment evals).
- **Member of Technical Staff, Preparedness** — capability evaluations
  on frontier models. **Head of Preparedness role open** as of
  Dec 2025; reported comp ~$555K [S25].

If you're applying to multiple of these, the loop differs *most* in
round 6 (alignment-specific technical) and the depth of the paper
presentation, *less* in coding.

## Comp band [S55]

Levels.fyi May 2026:

- Research Scientist L4 ~$771K total comp.
- L5 ~$1.0-1.47M (median ~$1.0M).
- "Researcher, Alignment" not separately broken out; assume Research
  Scientist band.
- PPU valuation moves the headline; any single number is a snapshot.

## Cross-refs
- [Alignment topic](../topics/alignment.md) — what the field is
  doing.
- [OpenAI alignment org map](../topics/openai-alignment-org.md).
- [Post-training & RLHF / DPO / GRPO](../topics/rlhf-and-post-training.md).
- [Scalable oversight](../topics/scalable-oversight.md).
- [Interpretability](../topics/interpretability.md).
- [Reward hacking](../topics/reward-hacking.md).
- [Scheming & deceptive alignment](../topics/scheming-and-deceptive-alignment.md).
- [Safety evals & Preparedness](../topics/safety-evals-and-preparedness.md).
- [Alignment reading list](../prep/alignment-reading-list.md).
- [Alignment timeline / study plan](../prep/alignment-timeline.md).
- [Alignment questions bank](../questions/alignment-questions.md).
- [Why OpenAI](../prep/why-openai.md).

## Sources
S1, S2, S3, S5, S6, S11, S20, S23, S24, S25, S26, S30-S55
