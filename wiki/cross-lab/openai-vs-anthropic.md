# OpenAI vs Anthropic — comparison for the "why OpenAI" probe

The *"why OpenAI vs Anthropic"* question is the single most-asked
behavioral probe on the OpenAI Alignment Researcher loop [S24, S77].
Generic answers fail. This page is the cross-lab evidence base for
constructing a non-generic answer.

Pair with [why-openai](../prep/why-openai.md) (the answer-construction
template) and [behavioral-questions](../questions/behavioral-questions.md).

## Comparison matrix

| Axis | OpenAI | Anthropic |
|---|---|---|
| Stated mission | Build AGI that benefits all of humanity [S1] | Race-to-the-top on safety; build the safest frontier lab [S59, S77] |
| Public alignment agenda | RLHF → Deliberative Alignment → Safe Completions [S31, S42] | Constitutional AI → RLAIF → Stress-Testing → Auditing [S61, S70] |
| Interpretability | Scaling SAEs on GPT-4 [S33]; Dec 2025 latent-attribution post [S26] | Toy Models → Towards Monosemanticity → Scaling Monosemanticity → Crosscoders [S67]. Substantially more public output. |
| Scalable oversight | Weak-to-strong [S30], CriticGPT [S34] | Recommended Directions explicitly lists scalable oversight [S58] |
| Scheming agenda | OpenAI × Apollo anti-scheming [S35]; CoT monitoring [S36] | Sleeper Agents [S60], Alignment Faking [S37], Petri [S57], Agentic Misalignment [S62], SHADE-Arena [S63] |
| Public auditing infra | Internal evals; Evaluations Hub [S29] | Petri open-sourced [S57], built on UK AISI's Inspect |
| Policy commitment | Preparedness Framework v2 (Apr 2025) [S39] | RSP v3.0 / v3.1 (effective Feb 24 2026) [S59] |
| Org stability (last 24mo) | Superalignment dissolved May 2024; Mission Alignment dissolved Feb 2026 [S44]; Model Behavior folded Sept 2025 | More stable; Hubinger team formed Jan 2024 still intact [S70] |
| Standalone alignment blog | alignment.openai.com (launched Dec 2025) [S26] | alignment.anthropic.com (older, deeper archive) [S58] |
| Headcount on alignment | Multiple teams (Alignment, Alignment Science, Alignment Training, Misalignment Research) but each smaller; reorg-prone [S25] | More concentrated under Bowman + Olah; ~18 on Interpretability [S56] |
| Policy / safety placement | Preparedness in research org | Frontier Red Team in policy division under Jack Clark [S73]. Notable structural choice. |
| RS comp (Levels.fyi 4/27/2026) | $763K-$1.44M+ (L4-L5 RS) [S55] | $320K-$1.05M+ TC; median ~$746K [S76] |
| 2-yr retention (Signalfire) | ~67% | ~80% [S76] |
| Take-home interview component | Less common | Yes for Fellows track (~5h) [S71] |
| "Why Anthropic / Why OpenAI" framing | "AGI that benefits humanity" + scale as a lever | "Race to the top on safety" + RSP as binding commitment [S77] |

## What's distinctively *OpenAI*

A non-generic *why-OpenAI* answer points to things only OpenAI has:

- **Frontier deployment scale** — 700M+ ChatGPT weekly users; the
  alignment of *deployed* frontier models is being decided in real
  time at OpenAI in a way it is not at any other lab.
- **Deliberative Alignment / Safe Completions** as a coherent
  alignment-architecture bet [S31, S42]. The o-series reasons over a
  written spec at inference; you'd shape that spec.
- **Model Spec** [S40] — the longest-running public articulation of
  intended model behavior at any lab; Anthropic's *Stress-Testing
  Model Specs* paper [S58] explicitly engages with it.
- **Operational alignment-via-product** — production sycophancy
  retrospectives [S41], real-time deployment loops, hundreds of
  millions of feedback signals.
- **Cross-lab safety eval (Aug 2025)** [S43] — OpenAI invited
  Anthropic to evaluate its models; this is non-trivial evidence of
  taking external scrutiny seriously.

## What's distinctively *Anthropic*

A candidate doing serious comparison-shopping should be honest about
what OpenAI doesn't have that Anthropic does:

- **More public interpretability output** [S67] — `transformer-
  circuits.pub` has a deeper archive than OpenAI's interpretability
  surface. If interp depth is your draw, this matters.
- **Petri open-sourced** [S57] vs OpenAI's internal-only auditing
  infrastructure.
- **RSP as a binding commitment** [S59] vs Preparedness Framework as
  a process document. Anthropic has publicly delayed releases on
  capability triggers; OpenAI hasn't done so as visibly.
- **Org stability** — OpenAI dissolved its alignment team twice
  (Superalignment May 2024, Mission Alignment Feb 2026) [S44].
  Anthropic's Alignment Science team has not had equivalent shocks.
- **Concentration of senior alignment talent** — Bowman, Hubinger,
  Olah, Perez are all at Anthropic. Several ex-OpenAI alignment
  leads (Leike, Schulman) are now also at Anthropic.
- **Frontier Red Team transparency** [S73] — Anthropic publishes
  more red-team detail than OpenAI's Preparedness team does.

## How to use this page in an answer

1. **Pick 2 things that only OpenAI has** that connect to your
   research interest. Don't list five; the panel will ask follow-ups
   and you want depth.
2. **Acknowledge 1 thing Anthropic has that OpenAI lacks** that you
   considered. Honesty about the comparison is positively graded
   [S77].
3. **Connect it to your career** — what specifically you want to
   work on, why now, what evidence updates you. See
   [why-openai](../prep/why-openai.md) for the full template.

## What to avoid

- "Both labs are great, but OpenAI feels like the right fit" — generic.
- "OpenAI is closer to AGI" — speculative; both panels reject it.
- Bashing Anthropic — "race to the top" is the framing OpenAI uses
  too; treating Anthropic as a competitor diminishes you.
- Listing only OpenAI products you use; you're not interviewing for
  product roles.
- Hand-waving the org instability ("teams change everywhere"). The
  Mission Alignment dissolution [S44] is a real fact and a real
  candidate concern; address it directly.

## Cross-refs
- [Anthropic alignment overview](anthropic-alignment.md)
- [Anthropic interview loop](anthropic-alignment-interview.md)
- [Why OpenAI answer template](../prep/why-openai.md)
- [OpenAI alignment org map](../topics/openai-alignment-org.md)
- [Behavioral questions](../questions/behavioral-questions.md)
- [Alignment questions](../questions/alignment-questions.md)

## Sources
S1, S24-S26, S29-S44, S55-S77
