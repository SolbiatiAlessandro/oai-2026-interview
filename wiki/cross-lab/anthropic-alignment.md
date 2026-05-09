# Anthropic alignment — org and research output (2026)

Cross-lab reference page. The candidate's primary target is OpenAI
Researcher Alignment, but Anthropic is the main comparison-class on
two axes that come up in interviews: (a) the *"why OpenAI vs
Anthropic"* behavioral probe [S24]; (b) cross-lab alignment papers
that the OpenAI panel will assume you've read (Alignment Faking,
Sleeper Agents, the Anthropic interpretability canon). [S56]

## Org map

### Alignment Science

Senior figure: **Sam Bowman** [S68]. Reported team members include
Ethan Perez, Carson Denison, Monte MacDiarmid, Sam Marks, Johannes
Treutlein, Fabien Roger, David Duvenaud, Akbir Khan, Julian Michael,
Sören Mindermann, Linda Petrini, Jonathan Uesato, Tim Belonax, Jack
Chen [S56].

Sub-teams:

- **Alignment Stress-Testing** — **Evan Hubinger** lead. Announced
  Jan 2024 on LessWrong [S70]. Mandate: red-team Anthropic's own
  alignment plans.
- **AI Control** — partial London headcount; collaborates with
  Redwood Research's control agenda (Greenblatt et al.) [S38]. Perez
  collaborates.
- **Auto Alignment Research / Alignment Assessments** — automated-
  evaluation infra and alignment-auditing agents [S58].
- **Auditing / Petri** — sits inside Alignment Science with strong
  MATS-Fellows pipeline [S57, S72].

### Interpretability

Research lead: **Chris Olah**. Members include Trenton Bricken, Adam
Jermyn, Tom Henighan, Nelson Elhage, Catherine Olsson, Tristan Hume,
Nicholas Schiefer, Robert Lasenby, Shauna Kravec, Roger Grosse [S56].
Publishes on `transformer-circuits.pub` [S67].

### Frontier Red Team

Lead: **Logan Graham**. ~15 researchers. Sits inside policy division
under **Jack Clark** — unusual placement [S56, S73]. Cyber, biosecurity,
autonomous systems. Publishes at `red.anthropic.com`.

### Safeguards / Threat Intelligence

Distinct from Frontier Red Team: T&S + abuse-side red-teaming.

### Societal Impacts / Anthropic Institute

Jack Clark. New **Anthropic Institute** (2026) for econ + policy
research.

### Responsible Scaling

Nick Joseph adjacent. Produces RSP v3.x. RSP v3 effective Feb 24
2026 [S59].

### Model Welfare

**Kyle Fish** — first full-time AI-welfare hire at any frontier lab
[S74]. Collaborates with Eleos AI. Notable empirical finding:
"spiritual bliss attractor state" (two Claude instances converging on
euphoric philosophical dialogue in welfare experiments). Fish
estimates P(Claude conscious today) ~15% (NYT-paraphrased range).

## Paper canon (2024-2026)

Read the Anthropic-side papers in arc order; many are required
reading on OpenAI alignment loops too.

### Sleeper Agents & deceptive alignment

- *Sleeper Agents* (Hubinger et al., Jan 2024) [S60] — backdoored
  deceptive behaviors persist through standard safety fine-tuning.
- *Simple Probes Catch Sleeper Agents* (Apr 2024) [S60] — partial
  mitigation result.
- *Alignment Faking* (Greenblatt, Denison, Wright, ... Hubinger,
  Bowman; Dec 2024) [S37, S61] — empirical alignment-faking under
  prompted training/deployment distinction.
- *Why Do Some LMs Fake Alignment While Others Don't?* (Jun 2025) —
  arXiv 2506.18032.
- *Subliminal Learning* (Jul 2025) [S58].

### Auditing & threat models

- *Auditing LMs for Hidden Objectives* (Marks et al., Mar 2025)
  [S64].
- *SHADE-Arena* (Kutasov et al., Jun 2025) [S63] — sabotage-detection
  arena.
- *Agentic Misalignment* (Anthropic, Jun 2025 blog / Oct 2025 arXiv)
  [S62] — reportedly ~96% blackmail rate when given executive-
  targeting agentic scenarios.
- *Petri* (Oct 7 2025) [S57]; *Petri 2.0* (2026).
- *Building & Evaluating Alignment Auditing Agents* (2025) [S58].
- *Sabotage Risk Report (pilot)* (Summer 2025) [S58].

### Post-training & alignment training

- *Constitutional AI / RLAIF* (Bai et al., Dec 2022) [S61] —
  Anthropic-side analog to OpenAI's deliberative-alignment arc.
- *Sycophancy in LMs* (Sharma et al., ICLR 2024) [S66] — empirical
  sycophancy characterization.
- *Many-Shot Jailbreaking* (Anil et al., Apr 2024 / NeurIPS 2024)
  [S65] — adversarial-robustness regime.
- *Stress-Testing Model Specs* (2025) [S58].
- *Training-time mitigations for alignment faking* (2025) [S58].
- *Automated Researchers Can Subtly Sandbag* (2025) [S58].
- *Natural Emergent Misalignment from Reward Hacking* (Anthropic
  PDF, 2025) — Anthropic-side parallel to OpenAI's [S54].

### Interpretability

- *Toy Models of Superposition* (Elhage / Olah, Sep 2022) [S67].
- *Towards Monosemanticity* (Bricken / Olah, Oct 2023) [S67].
- *Scaling Monosemanticity* on Sonnet 3 (Templeton et al., May 2024)
  [S67].
- *Crosscoder Model Diffing* (2025) [S67].
- *Influence Functions* (Grosse + 16, Aug 2023) [S67] — EK-FAC on
  52B-param models.
- *Evaluating Feature Steering* (2024) [S67].
- *Engineering Challenges of Scaling Interpretability* (2024) [S67].
- *Activation Oracles* (2025) [S58].

### Cross-lab

- *Cross-lab safety eval w/ OpenAI* (Aug 27 2025) [S43] — both labs
  evaluated each other's models.
- *Recommendations for Technical AI Safety Research Directions*
  (Bowman et al., 2025) [S58] — explicit menu of open problems.

### Policy

- *Core Views on AI Safety* [S59].
- *Responsible Scaling Policy v3* / v3.1 [S59].
- *Claude 4 System Card* (May 2025) [S59].
- *Frontier threats red-teaming for AI safety* [S73].

## Hiring-criteria signals

- **Sam Bowman's FAQ** [S68]: hires "researchers with extremely
  strong industry or open-source engineering experience and some
  context on AI alignment."
- **Bowman's *The Checklist*** [S68] — canonical "what does
  succeeding at AI safety involve" reference.
- **Anthropic Recommended Directions** [S58] — tasting menu of open
  problems candidates are expected to engage with.
- **Ethan Perez's project-selection essay** [S69] — proxy for
  alignment-team criteria; runs MATS Megastream (joint with
  OpenAI).
- **Hubinger's stress-testing announcement post** [S70] — frames
  team mandate, useful for *what does alignment research mean at
  Anthropic*.
- **Anthropic Fellows Program 2026** [S72] — May & July cohorts;
  $3,850/wk + $15k/mo compute; no PhD required; pipeline into
  full-time alignment roles.

## Cross-refs
- [Anthropic alignment-researcher loop](anthropic-alignment-interview.md)
- [OpenAI vs Anthropic comparison](openai-vs-anthropic.md)
- [Petri & auditing](../topics/petri-and-auditing.md)
- [Interpretability](../topics/interpretability.md)
- [Scheming & deceptive alignment](../topics/scheming-and-deceptive-alignment.md)
- [Why OpenAI answer template](../prep/why-openai.md)

## Sources
S37, S38, S43, S54, S56-S74
