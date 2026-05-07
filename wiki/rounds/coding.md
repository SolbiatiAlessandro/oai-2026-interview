# Coding round (general SWE flavor)

The general-coding round is OpenAI's most consistently described
interview: ~60-75 min, in CoderPad (sometimes screen-shared own IDE),
practical problems with multiple sub-parts, and a strong "type-the-whole-
hour" tempo [S1, S2, S3, S4, S5].

## Format

- **Duration**: typically 60 min for the screen, up to 75 min onsite
  [S2, S5].
- **Tooling**: CoderPad is the default; some staff candidates report
  being allowed to use their own IDE with screen-share [S3, S11].
- **Languages**: language-agnostic, but OpenAI's recruiter email
  states "we generally prefer modern Python" [S20]. Python is the
  community-preferred default for candidate productivity [S4, S5].
- **Problem shape**: one realistic problem, divided into 3-5 sub-tasks
  that build on each other (not several independent algorithm puzzles)
  [S2, S4, S20].

## Verbatim from OpenAI's recruiter email [S20]

> "Assess your proficiency in coding, problem-solving, and technical
> communication through a coding exercise/assignment. The coding
> exercises will involve implementing components of well-known systems
> or primitives, with interviewers choosing from a pool of similar
> questions. We'll be coding together in an environment like CoderPad.
> Most problems are broken into stages of increasing difficulty, and
> many will require reading and understanding existing code."

Areas to prepare on (per email):
- Data structures & algorithms (arrays, lists, queues, maps, trees,
  sorting, searching, dynamic programming, backtracking, OOP, design
  patterns).
- Debugging & testing (debuggers, logs, instrumentation, unit tests,
  integration tests, test coverage).

Evaluation criteria (per email): working solution, completeness, code
cleanliness/readability, time-to-completion, efficiency.

Tips for success (per email): understand requirements, plan, write
clean code, test thoroughly, optimize. They explicitly encourage
"begin with a suboptimal solution and refine it as the problem
progresses."

## What's actually asked (canonical list)

(See [coding-questions](../questions/coding-questions.md) for the full
bank.)

- **LRU cache** — the single most-asked problem [S5, S12].
- **Time-based / versioned key-value store** with serialization,
  persistence, concurrency follow-ups [S2, S4].
- **KV store serialize/deserialize** (length-prefix encoding,
  Redis-protocol-style) [S2].
- **Resumable iterator** — pause/resume across multiple calls,
  with skip and reset [S2].
- **In-memory SQL database** — tables, INSERT, SELECT-WHERE [S2, S3].
- **Unix `cd`** with `..`, absolute paths, symbolic-link resolution
  and cycle detection [S2].
- **Multithreaded web crawler** — concurrency, dedup, rate-limit [S2].
- **Spreadsheet formula evaluator** — cell references, recompute,
  cycle detection via DFS+set [S2, S4].
- **GPU credit accounting** — soonest-expiry-first FIFO consumption
  [S4].

## Bar / signals [S2, S3, S4, S5, S12]

- **Volume of correct code per hour.** Candidates report typing nearly
  the whole hour. The interviewer is calibrating how many sub-parts
  you reach with clean, correct, edge-case-aware code.
- **Production polish.** Naming, function decomposition, simple state
  invariants, sensible error paths.
- **Edge cases voiced and handled.** Empty input, duplicate writes,
  concurrent updates, cycles.
- **Communication.** Talk through your approach, ask clarifying
  questions, narrate trade-offs as you write.
- **Optimization on demand.** First a working solution, then a
  follow-up "make `getCell` O(1)" or "add concurrency" [S4].

## Things that fail candidates

- **Trying to find a clever trick.** OpenAI deliberately picks problems
  where the obvious approach works; don't pattern-match to LeetCode
  Hard [S2, S5].
- **Going silent** while typing. The round is half-graded on
  communication [S3].
- **Skipping tests / sanity-checks.** Many problems have a clearly
  testable surface (e.g. `setCell`/`getCell`); demonstrate basic tests
  yourself when time allows [S4].
- **Not finishing.** "2/4 or low 3/4 on coding will fail you" is
  reported repeatedly; finishing 3 of 4 sub-parts cleanly beats
  half-finishing all 4 [S3, S11].

## Cross-refs
- [Coding questions](../questions/coding-questions.md)
- [ML coding](ml-coding.md)
- [CoderPad & AI tools](../tooling/coderpad-and-ai-tools.md)

## Sources
S1, S2, S3, S4, S5, S11, S12, S20
