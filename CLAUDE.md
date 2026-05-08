# CLAUDE.md – schema and workflow for the OAI-2026-interview wiki

This file is the schema. The LLM agent reads it on every session and uses it
as the source of truth for structure, conventions, and operations on this
repository.

The pattern follows Andrej Karpathy's
[LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f):
three layers — **raw sources**, the **wiki**, and **this schema**. Raw
sources are immutable; the wiki is incrementally maintained Markdown; this
file describes the bookkeeping.

## Mission

Maintain an up-to-date, high-signal knowledge base on how OpenAI interviews
candidates in 2026.

**Primary focus (2026-05-08 onward): Researcher, Alignment.** The repo owner
is interviewing for this role, so the KB optimizes depth on alignment
research (post-training / RLHF / safe completions, scalable oversight,
mech interp / SAEs, reward hacking, scheming / deceptive alignment, eval
design / Preparedness). See `wiki/roles/alignment-researcher.md`.

**Secondary roles still covered**: ML Engineer, ML Researcher, Research
Engineer, Software Engineer, Applied AI / Forward-Deployed. These pages
remain useful because the alignment loop reuses the coding screen and ML
coding screen from those tracks.

The KB is built from publicly available sources only (blog posts, YouTube,
Glassdoor, Blind, Reddit, LessWrong, Alignment Forum, podcasts, OpenAI's
own pages, candidate writeups, papers).

No private/NDA material. No personal candidate data beyond what authors
publicly self-disclose.

## Directory layout (authoritative)

```
README.md
CLAUDE.md                 — this file
index.md                  — catalog of every wiki page, grouped by section
log.md                    — append-only chronological log of ingests & edits
sources/
  sources.md              — registry of raw sources, IDs S1, S2, …
  <optional clipped copies>.md
wiki/
  overview.md
  roles/<role>.md
  rounds/<round>.md
  questions/<round>-questions.md
  topics/<topic>.md
  tooling/<tool>.md
  prep/<artifact>.md
```

Page filename convention: lower-kebab-case, no spaces.

## Source registry (`sources/sources.md`)

Every source gets a stable ID `S<N>`. Each entry contains:

- `id`: `S<N>`
- `url`
- `type`: blog | yt | glassdoor | blind | reddit | podcast | official |
  forum | gist | doc | other
- `author` (if known)
- `date_published` (ISO yyyy-mm-dd, best-effort)
- `roles_covered`
- `summary` (1-3 sentences)
- `confidence`: high | medium | low (low = anonymous/single source/uncorroborated)
- `ingested_at` (ISO date)

Wiki claims cite sources inline as `[S<N>]`. Multiple supporting sources
are concatenated: `[S1, S7, S12]`.

## Wiki page conventions

- Start with a one-paragraph summary.
- Use H2 for the major sections; H3 for subsections.
- Cite a source on any non-obvious factual claim with `[S<N>]`.
- Mark uncertain or contested claims explicitly (e.g. *"Conflict: S3 says X,
  S9 says Y"*).
- Quote candidate language sparingly and never copy more than ~25 words
  from any single source verbatim. Paraphrase by default.
- Add a `## Cross-refs` section at the bottom listing related wiki pages.
- Add a `## Sources` section at the bottom listing only source IDs used.

## Operations

### Ingest

Triggered when a new URL/transcript is provided.

1. Fetch the source. If it requires auth, ask the user for a paste/excerpt.
2. Allocate the next `S<N>` ID and append to `sources/sources.md`.
3. Read existing wiki pages that overlap (use `index.md`).
4. Update or create pages. Prefer updating: integrate the new info into the
   existing structure rather than appending a "new info" block.
5. When a page becomes large (~> 600 lines) or covers multiple distinct
   sub-topics, split it.
6. Update `index.md` if pages were added/renamed.
7. Append a `log.md` entry: date, source ID, pages touched, 1-line summary.

### Query

When the user asks a question:

1. Search the wiki first (look at `index.md`).
2. If the answer is in the wiki, answer using it and cite source IDs.
3. If the wiki is missing relevant info, say so. Optionally fetch new
   sources, then ingest, then answer.
4. If the answer surfaced new high-value insight, file it back into the
   appropriate wiki page so the next query benefits.

### Lint

Periodically (or on demand):

- Find contradictions across pages and flag them.
- Find orphaned pages (not in `index.md` or not referenced by any other page).
- Find stale claims (sources older than 18 months making time-sensitive
  claims like compensation, recruiter names, tooling).
- Find dead links in `sources/sources.md`.
- Confirm every `[S<N>]` resolves to an entry in `sources/sources.md`.

## Recency policy

OpenAI's process changes fast. Tag claims with the source's publish date
when the claim is time-sensitive. Prefer sources from 2025-2026. Older
sources may still be cited but should be marked `[S<N>, 2024]`-style.

## Tone

Direct, factual, candidate-useful. No hype, no marketing copy. Distinguish
*reported by candidates* (single anecdote) from *consistent across N sources*.

## What goes where (cheat sheet)

| Information type                          | Page family               |
| ----------------------------------------- | ------------------------- |
| End-to-end loop for a specific job title  | `wiki/roles/`             |
| Format/expectations of a single round     | `wiki/rounds/`            |
| Specific questions reportedly asked       | `wiki/questions/`         |
| Technical concept candidates should know  | `wiki/topics/`            |
| Platforms (CoderPad), AI-tools rules      | `wiki/tooling/`           |
| Reading lists, study plans, timelines     | `wiki/prep/`              |
| Cross-cutting summary                     | `wiki/overview.md`        |

## Don'ts

- Don't invent sources or fabricate IDs.
- Don't add a page without registering it in `index.md`.
- Don't delete `log.md` entries (append-only).
- Don't paste large copyrighted blocks; paraphrase and cite.
