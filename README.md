# oai-2026-interview

A living wiki/knowledge base about OpenAI's interview process in 2026, built
following Andrej Karpathy's
[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
pattern: an LLM agent ingests raw sources (blog posts, YouTube videos, forum
threads, Glassdoor data, official OpenAI guides, candidate writeups) and
incrementally maintains structured Markdown pages.

Scope of roles covered:

- **ML / AI Engineer** (primary focus)
- **ML / Research Engineer** (research-adjacent)
- **Member of Technical Staff – Research / ML Researcher**
- **Software Engineer** (backend / infra / product)
- Related: Applied AI Engineer, Forward-Deployed Engineer

The KB also tracks the *meta* topic of how AI is reshaping interviews in 2026
(AI-coding-allowed loops, AI-proctoring, AI-generated questions) and how
OpenAI's own loop has evolved in response.

## Layout

```
.
├── CLAUDE.md              # schema + workflow for the LLM agent
├── index.md               # catalog of all wiki pages
├── log.md                 # append-only timeline of ingests/updates
├── sources/               # raw sources (URL registry; downloaded copies as
│                          # needed)
│   └── sources.md
└── wiki/                  # LLM-generated pages
    ├── overview.md
    ├── roles/             # one page per role
    ├── rounds/            # one page per interview round / stage
    ├── questions/         # known asked questions, by round
    ├── topics/            # ML/SWE topics that come up
    ├── tooling/           # CoderPad, AI-in-interviews, etc.
    └── prep/              # reading list, timelines, practice plans
```

## How to use

1. Read `wiki/overview.md` for the big picture.
2. Jump to your target role under `wiki/roles/`.
3. Drill into the rounds you have scheduled under `wiki/rounds/`.
4. Use `wiki/questions/` for question banks and `wiki/prep/` for study plans.
5. Every claim should trace back to a source listed in `sources/sources.md`.

## How to extend

Hand a new URL or transcript to the agent and ask it to ingest. The agent
should:

1. Add the source to `sources/sources.md` (assigning it an `S<N>` ID).
2. Append a `log.md` entry.
3. Update or create the relevant wiki page(s), citing `S<N>`.
4. Update `index.md` if a new page was created.
5. Lint for contradictions and stale claims.

See `CLAUDE.md` for the full schema and conventions.
