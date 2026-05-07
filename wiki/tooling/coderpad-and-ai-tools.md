# CoderPad & AI tools in OpenAI interviews

What tooling OpenAI uses for technical interviews in 2026, and the
status of AI-coding-assistant use during the loop. This is the meta
"how does AI fit in 2026 interviews" question.

## Default platform

- **CoderPad** (or equivalent shared editor) is the default for the
  coding screens [S1, S2, S3].
- Editor experience is intentionally stripped: limited autocomplete,
  no language-server fluency, basic test-runner. Practice in CoderPad
  before the screen [S1, S5].
- Some onsite rounds — especially at staff levels — allow **screen-
  shared own IDE**. Confirm with your recruiter; behavior varies by
  team and interviewer [S3, S11].
- System design rounds use a **shared whiteboard** (often Excalidraw or
  CoderPad's whiteboard) [S3, S9].

## AI-tool policy

OpenAI has not, as of public information through mid-2026, published a
"please use AI" policy for candidate-side coding interviews [S2, S3, S22].
Live coding rounds still center on candidate-authored code. Several
data points:

- Hello Interview's reporting on real OpenAI coding rounds [S2] and
  the L5 guide [S3] describe live, narrated, interviewer-watched
  coding without AI assistance as the default.
- LockedIn AI's industry roundup [S22] lists companies that **explicitly
  invite** AI use in interviews (Canva, Shopify, Meta in some rounds).
  OpenAI is **not** on that list.
- 2026 industry trend [S21] is split: some labs invite AI use to test
  AI-collaboration skills; others harden against AI cheating with
  proctoring or AI-resistant problem design.

> Practical implication: **assume AI assistants are not allowed in OpenAI
> coding rounds unless your interviewer explicitly invites them.** If
> your recruiter says otherwise, follow that — but plan for the no-AI
> default.

## Why the OpenAI bar is "AI-resistant" by design

The kind of problems OpenAI gives [S2, S4]:

- Multi-part, stateful problems (KV stores with versioning, spreadsheets
  with cycles) where the *spec* is the hard part.
- Production-quality code that an LLM can stub but rarely finishes
  cleanly under interviewer probing.
- Long, talk-while-typing sessions.
- Heavy follow-up probes ("now make it concurrent", "now make get O(1)")
  that require you to refactor under interviewer push.

Even a strong AI assistant struggles to keep state across that
interview shape. Most of the bar is in the candidate's *driving*, not
in writing first-pass code.

## What about ML coding rounds?

ML coding (implement attention from scratch) is similarly AI-resistant
in 2026 — the panel watches you write, asks "why this scaling?", "what
breaks in fp16 here?", and probes for derivation, not just functioning
code [S6, S19].

## Tooling on the candidate side

Things candidates report using to prep [S5, S13]:

- **CoderPad sandbox** — practice in the actual environment.
- **Excalidraw / Whimsical** — practice system-design diagrams.
- **1Point3Acres** — recent OpenAI-specific question reports [S5].
- **LeetCode + own solutions for the recurring questions** (LRU,
  LC 981, LC 2408 etc.) [S5, S12].
- **YouTube system-design walkthroughs** (Hello Interview, ByteByteGo)
  [S3, S13].

## Open questions / pending verification

- Whether any specific OpenAI teams permit AI coding assistants in 2026
  (not publicly documented; ask recruiter).
- Whether OpenAI uses a remote-proctoring tool beyond the interviewer
  on the call (no public evidence).

## Cross-refs
- [Coding round](../rounds/coding.md)
- [ML coding round](../rounds/ml-coding.md)
- [System design round](../rounds/system-design.md)

## Sources
S1, S2, S3, S5, S6, S9, S11, S12, S13, S19, S21, S22
