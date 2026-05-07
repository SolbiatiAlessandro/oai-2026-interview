# Project Deep-Dive — slide template

A 7-section structure for the OpenAI project-deep-dive / technical-
project-presentation round, derived from S20's Stripe-style template
adapted to OpenAI's grading axes (Technical Depth, Technical Breadth,
Business Impact) [S20, S3, S13].

The recruiter's official email for this round (verbatim, S20):

> "This interview will be a technical deep dive where we'll ask you
> to walk a member or members of our engineering team through a
> technical project you led or contributed to, including the
> context/motivation, key architecture decisions, impact, learnings,
> etc. You're welcome to use whatever format you prefer (slides,
> virtual whiteboard, etc). … We've found that it generally works
> best for candidates to pick one area or project and go deeper."

Recruiter colour from S20: 25 minutes of talking + Q&A; visual aid is
appreciated; pick **a recent and complex** project; the interviewer is
another ML or Research Engineer.

## Per-section template

For each section, hit all three axes (Depth, Breadth, Impact).

### A. Project Context & TLDR (3 min)

- Depth: Headline outcome in one number. Your role and team size.
- Breadth: What systems / teams the project touched.
- Impact: Why the audience/customer cared.

### B. Business Motivation (5 min)

- Depth: Specific problem articulation; why it was hard.
- Breadth: Where the problem sat in the org's broader strategy.
- Impact: The metric that mattered (revenue, latency, retention,
  engagement, donations, etc.) and the baseline.

### C. Your Role (3 min)

- Tech-Lead vs. IC distinction. What *you* personally drove
  technically vs. what your team owned.
- Cross-functional partners (PM, DS, infra teams).

### D. High-Level / Design Decisions (10 min — the meat)

- Key architectural choices with explicit alternatives considered.
- The framework you used to converge: cost, latency, scalability,
  maintainability, complexity vs. expected lift.
- Key trade-offs: availability vs. consistency, online vs. offline,
  ad-hoc vs. principled.
- One or two technical-considerations sub-stories you can drill into
  if the interviewer asks "go deeper here".

### E. Roadblocks (5 min)

- Capacity / GPU constraints.
- Data or feature constraints (sparsity, privacy).
- Model-owner / cross-team alignment friction.
- Communication of intermediate metrics to non-technical
  stakeholders.

### F. Impact (5 min)

- Concrete numbers. Baseline → target → result.
- Business / product / scientific impact.
- Whether the work generalized (other teams adopted it).

### G. Mistakes and Learnings (2 min)

- What you'd do differently with hindsight.
- A concrete change to your decision process you've adopted since.

## Common pitfalls [S20, S3]

- Resume re-tour: walking through what was *built* without explaining
  *why*. The graders score *why* much higher than *what*.
- Implementation-detail dump that eats your design-decisions time.
- Project where you weren't the primary technical owner — interviewers
  drill into *your* judgement, and "we" answers don't earn points.
- Vague impact ("it improved a lot") with no baseline or measurement.
- Missed time control. Run a dry-run with a stopwatch — many
  candidates over-build slides and miss section F entirely [S20].

## Worked example structure (compressed from S20's draft)

A real example S20 was preparing — Meta SIM (Social Impact
Monetization) ML lead role:

- A: Led 4 ML engineers improving ad relevance for the social-impact
  segment; ~$76M incremental revenue in 2024.
- B: Meta's social-responsibility strategy ↔ sustainable business
  case; goaling on incremental-revenue + tracking ads-driven
  donations.
- C: Tech-Lead; owned roadmap, delegated, drove cross-team comms;
  personally introduced gated specialized modules + sparse embedding
  features + pretrained-graph embeddings.
- D: Choice between vertical-NE-only metric vs. broader topline; chose
  Vertical NE as more movable; designed gated modules so that
  vertical-specific patterns could be learned without tower bloat.
- E: GPU capacity (architecture optimization), feature-capacity
  (sparse-features cross-vertical), privacy concerns, model-owner
  alignment, communicating NE gains to non-technical stakeholders.
- F: NE gains across multiple production ranking models; vertical
  ranking adopted by other teams; $76M iRev measured over 4 years;
  lift in nonprofit advertiser demand.
- G: Underestimated complexity; should have involved model-owners
  earlier; model-explainability gap made it hard to communicate
  impact beyond iRev.

## Cross-refs
- [Deep dive round](../rounds/deep-dive.md)
- [Technical project presentation](../rounds/technical-project-presentation.md)
- [Behavioral](../rounds/behavioral.md)

## Sources
S3, S5, S13, S20
