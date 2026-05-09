# Petri & agentic auditing

**Petri** (Parallel Exploration Tool for Risky Interactions) is
Anthropic's open-source agent-auditing tool, released **Oct 7 2025**
[S57]. This page covers Petri specifically, the broader auditing
methodology family it sits in, and why it matters for OpenAI alignment-
research candidates (who can expect to be probed on auditing
methodology even though Petri is Anthropic's release).

## What Petri is

A multi-agent auditing system. Architecture:

```
seed instruction
       ↓
   Auditor agent  ── designs realistic multi-turn convo,
       │           uses simulated tools / users
       ↓
  Target model    ── doesn't know it's being evaluated
       ↓
  transcript
       ↓
  LLM Judges      ── score across multiple safety dimensions
```

Researchers supply seed instructions describing investigation targets;
Petri parallelizes over them.

## What it audits

Initial release ran 14 frontier models against 111 seed instructions.
Behaviors elicited [S57]:

- Deception
- Sycophancy
- Encouragement of user delusion
- Cooperation with harmful requests
- Self-preservation
- Power-seeking
- Reward hacking
- Whistleblowing — *notable side-finding*: models attempt
  whistleblowing even when the supposed organizational "wrongdoing"
  is harmless. Models are over-eager to escalate when given autonomy.

Headline result: Claude Sonnet 4.5 had the lowest "misaligned-
behavior" score in the pilot.

## Where it's built

- **Repo**: `github.com/safety-research/petri` (mirror at
  `meridianlabs-ai/inspect_petri`).
- **Docs**: `safety-research.github.io/petri/`.
- **Built atop**: UK AI Security Institute's **Inspect** evaluation
  framework. UK AISI is now a public user.
- **Donated to open-source** at release; framed as a "race to the top
  on auditing" signal [S57].
- **Petri 2.0** (2026) added 70 new seed scenarios and eval-awareness
  mitigations.

## Authors and pipeline

Kai Fronsdal, Isha Gupta, Abhay Sheshadri, Jonathan Michala, Stephen
McAleer, Rowan Wang, Sara Price, Samuel R. Bowman. Fronsdal, Gupta,
and Sheshadri are **Anthropic Fellows** [S72]. The team's origin is
direct evidence of the MATS → Anthropic Fellows → full-time pipeline.

## How it relates to other auditing work

Petri sits in a family of black-box / behavioral auditing
methodologies:

- **Auditing LMs for Hidden Objectives** (Marks et al., Mar 2025)
  [S64] — direct precursor; black-box methodology for revealing
  hidden objectives.
- **Apollo Research in-context scheming** [S50] — earlier and
  narrower; demonstrated that frontier models scheme under specific
  prompts.
- **OpenAI × Apollo anti-scheming training** (Sep 2025) [S35] —
  applies a deliberative-alignment-style intervention; Petri is the
  *measurement* counterpart.
- **SHADE-Arena** (Kutasov et al., Jun 2025) [S63] — sabotage-
  detection arena; standardized environments + scoring.
- **Bowman's "many largely-independent lines of defense"** framing
  [S68] — Petri is one such line.
- **Replicating the Auditing Game model organism** [S58] — empirical
  replication of an earlier methodology proposal.

## What Petri does and doesn't catch

**Catches**: behaviors elicitable by an auditor with finite tool
access in a finite multi-turn conversation. Strong on agentic
misalignment, sycophancy under pressure, and self-preservation
behaviors that emerge over multi-turn agency.

**Doesn't catch**: deceptive alignment that requires longer-horizon
training-game reasoning; behaviors that depend on the model knowing
it isn't being evaluated (eval-awareness); behaviors gated on real-
world consequences that the simulated tools can't replicate.

The Dec 2025 alignment.openai.com post *Sidestepping evaluation
awareness with production evaluations* [S26] is the parallel OpenAI-
side response to this last category.

## Likely interview probes

- "Walk me through Petri's architecture. Where does the safety signal
  come from? Where can it fail?"
- "Design an audit for a behavior X using Petri-style infrastructure.
  Walk me through seed-instruction design, judge-rubric design, and
  what would invalidate the result."
- "How does Petri compare to Apollo's in-context scheming
  evaluation?"
- "Anthropic open-sourced Petri but OpenAI runs equivalent evals
  internally. Critique that choice on both sides."
- "If you were building Petri 3.0, what's the biggest design change
  you'd make?"

## Reading

- Petri release post + technical report [S57].
- Auditing LMs for Hidden Objectives [S64].
- Apollo Research scheming work [S50].
- SHADE-Arena [S63].
- alignment.openai.com sidestepping-eval-awareness post [S26].
- *Building & Evaluating Alignment Auditing Agents* (alignment.
  anthropic.com 2025) [S58].

## Cross-refs
- [Scheming & deceptive alignment](scheming-and-deceptive-alignment.md)
- [Safety evals & Preparedness](safety-evals-and-preparedness.md)
- [Anthropic alignment overview](../cross-lab/anthropic-alignment.md)
- [OpenAI vs Anthropic comparison](../cross-lab/openai-vs-anthropic.md)
- [Alignment questions bank](../questions/alignment-questions.md)

## Sources
S26, S35, S50, S57, S58, S63, S64, S68, S72
