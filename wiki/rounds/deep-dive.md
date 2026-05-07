# Deep dive (project retrospective)

A 30-45 min conversation about a single past project. The interviewer
plays an aggressive co-author: probing decisions, alternatives
considered, what went wrong, what you'd change [S3, S5, S13].

This round is the most-frequently-cited reason for *post-technical*
rejections [S3, S11]. Treat it as a graded round, not a friendly chat.

## Format

- **Duration**: 30-45 min. (At staff, the related "technical project
  presentation" is a 45-min slide-driven version — see
  [technical-project-presentation](technical-project-presentation.md))
- **Materials**: usually no slides for the regular deep dive; you draw
  on the whiteboard as needed.
- **Probe pattern**: "Why X?" → "What did you consider instead?" →
  "What was the failure mode?" → "How did you measure success?" →
  "What would you do differently now?"

## Picking the project

Select a project where:

- You owned a non-trivial technical decision (not "I implemented
  feature N of system Y") [S5].
- The problem had real ambiguity and you can articulate the
  trade-offs you made.
- The outcome is measurable, even if mixed.
- For ML / research roles: you can defend modeling choices, ablations,
  evaluation choices, and limitations [S5, S6].

Avoid:

- Projects you weren't the primary technical owner of.
- Projects too old (>3 years) — interviewers will probe for current
  technical fluency.
- Projects under NDA you can't discuss substantively.

## What good answers do [S3, S5, S6]

- Open with a 2-min summary: problem, your role, headline result.
- Use a clean diagram you can sketch quickly (one box-and-arrow,
  one model/data flow).
- Justify the *why* at every choice; reference alternatives.
- Be honest about failure modes and limitations — this is graded,
  evasion is read as red flag.
- Prepare follow-ups: "what would you do next?" and "how would this
  scale 100×?" come up nearly every time [S5].

## What fails candidates

- Resume-recital: walking through what was built without explaining
  *why* [S3, S5].
- Defensive answers when probed on weaknesses [S3, S11].
- Inability to discuss alternatives considered.
- Vague metrics ("it improved a lot") [S5].

## Cross-refs
- [Technical project presentation](technical-project-presentation.md)
- [Behavioral](behavioral.md)
- [Recruiter screen](recruiter.md)

## Sources
S3, S5, S6, S11, S13
