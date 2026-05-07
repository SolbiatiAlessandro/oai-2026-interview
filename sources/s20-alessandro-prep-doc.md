# S20 — Alessandro Solbiati's OpenAI ML-Engineer prep doc (raw source)

- Source URL: https://docs.google.com/document/d/1agAkPq_F-GFnbrCk4Daa85BYlSXcEWUwKRsGeLRL1GA/edit
- Author: Alessandro Solbiati (the owner of this repo)
- Date: 2025-02 (active prep window)
- Confidence: HIGH (primary, first-person, with verbatim recruiter emails and screenshots of real interview content)
- Ingested: 2026-05-07

## Loop snapshot (as recorded in the doc)

Stage 1 — phone screens (Wed 12 Feb 2025), both **PASSED**:
- Coding screen, 11:00–12:00 PT — practical multi-part coding in CoderPad.
- ML screen ("Machine Learning Search Design"), 13:00–14:00 PT, with
  Young Cha — open-ended ML system design with search/recsys/LLM
  framing, plus targeted depth questions.

Stage 2 — virtual onsite, in progress at the time of the doc:
- ML Debugging round (with Leo Gao, MTS) — 60 min, PyTorch transformer
  with 4-5 bugs, then a second part swapping LLM training to a
  classification task (embeddings → loss → accuracy).
- Project Deep Dive ("Technical Deep Dive — ML Focus") — 45 min slide-
  driven retrospective on a past ML project with strong "visual aid
  appreciated" steer from recruiter.
- Behavioral + XFN — hiring manager (~85% Meta-Jedi-style + 15%
  OpenAI-specific mission/safety/AGI questions) + 1× XFN partner
  conversation walking through working with PMs and competing priorities.

The doc also references other-role variants seen in 1Point3Acres:
- Coding SD: "Design enterprise internal chat similar to Slack".
- Researcher-screen-like linear-algebra round: debug multi-threaded
  back-propagation, including how to split a matrix for distributed
  computation.

## Verbatim recruiter emails captured in S20

### Coding screen email (excerpt)

> "Objective: Assess your proficiency in coding, problem-solving, and
> technical communication through a coding exercise/assignment. The
> coding exercises will involve implementing components of well-known
> systems or primitives, with interviewers choosing from a pool of
> similar questions. We'll be coding together in an environment like
> CoderPad. Most problems are broken into stages of increasing
> difficulty, and many will require reading and understanding existing
> code. While these exercises are language agnostic, we generally prefer
> modern Python."

Areas to prepare on (from email):
- Data structures & algorithms (arrays, lists, queues, maps, trees,
  sorting, searching, dynamic programming, backtracking, computational
  complexity, OOP, design patterns).
- Debugging & testing (debuggers, logs, instrumentation, unit tests,
  integration tests, test coverage).

Evaluation criteria (from email): working solution, completeness,
cleanliness/readability, time-to-completion, efficiency.

Tips for success (from email): understand requirements, plan approach,
write clean code, test thoroughly, optimize. Encouraged to think
out loud and ask clarifying questions; "begin with a suboptimal
solution and refine it as the problem progresses".

### ML Debug round email (verbatim)

> "This 60 minute interview will be a machine learning, debugging
> exercise. You'll be given a short implementation of a ML model (using
> Python and PyTorch) and be tasked to find and fix all bugs in order
> for the model to work successfully. This exercise tests your knowledge
> of ML architectures and algorithms, your ability to trace bugs back to
> their source, and your level of attention to detail. Familiarity with
> the Transformer model would be helpful."

### Technical Deep Dive (ML focus) email (verbatim)

> "This interview will be a technical deep dive where we'll ask you to
> walk a member or members of our engineering team through a technical
> project you led or contributed to, including the context/motivation,
> key architecture decisions, impact, learnings, etc. You're welcome to
> use whatever format you prefer (slides, virtual whiteboard, etc). In
> general, we're looking for evidence of the following: Ability to define
> clear, appropriate goals based on business and product context; Ability
> to devise and implement strong, thoughtful technical solutions to
> complex problems, from high-level architecture to key implementation
> details; Communication, about technical topics as well as product/
> business/organizational context."

> "We've found that it generally works best for candidates to pick one
> area or project and go deeper, since that enables you to spend less
> time on setting the context and more time to dive into the details."

### ML Search Design — Young Cha description (verbatim)

> "This will be an interview where we will be evaluating the candidate's
> search and/or recommendations systems experience and ways to adapt
> LLMs to interact with such systems. The candidate should be prepared
> for both working through an open ended ML question as well as specific
> questions related to algorithms or techniques typically employed in
> such settings."

Areas to consider (from email):
1. Architectural components and flow for ML systems.
2. Ability to deep dive into ML techniques relevant to search, ranking
   and retrieval.
3. Optimization techniques for ML models.
4. Metrics and evaluation.

### Behavioral / hiring-manager character (Brian, recruiter)

Captured in Alessandro's notes: ~85% Meta-Jedi-flavored behavioral
(key accomplishments, time allocation, career trajectory, conflict
resolution, feedback up & down) + ~15% OpenAI-specific:

- "Why OpenAI" — what fundamentally about the company attracts you?
- Mission / ambiguous-mission probes; how it resonates.
- Trust and safety — equivalent to Meta's user-trust framing; refer to
  Sam at all-hands.
- AGI risks: "Is AGI going to be the downfall of humanity?"
- Career fit: how you compare to other 4s and 5s on the team.

### Tech Deep Dive — recruiter colour (Brian)

- Stolen format from Stripe-style technical deep dive / project
  retrospect.
- 1:1 with another ML engineer or research engineer.
- Visual aid is appreciated.
- 25 minutes of talking + pulse-check questions.
- What graders care about: technical depth and breadth, business
  impact, complexity of the project. "Pick something recent."

## Coding-screen question pool (compiled by S20 from candidate reports)

| # | Problem | S20 status / notes |
|---|---------|--------------------|
| 1 | Time-based KV store | Asked. Real-timestamp input. Follow-ups: write tests, mock timestamp, ensure monotonicity, multi-thread locking, compare lock implementations. "Felt like system design." |
| 1b | String-manipulation KVStore (custom serialize/deserialize, no `json`) | Practiced. Filesystem persist + restore. |
| 1c | Strongly-typed-language `toString` serializer | Reported by another candidate. |
| 2 | In-memory DB | Asked / solved. Multi-step: query, WHERE, multi-column WHERE, ORDER BY single + multi column. Each step requires writing test. |
| 3 | Resumable iterator | Practiced. Asked elsewhere with `next/get_state/set_state`, comprehensive unit tests, then 2D resumable iterator over file iterator, then 3D iterator. |
| 4 | GPU credit class | Practiced. `addCredit / getBalance / useCredit` with expiration; soonest-expiry-first FIFO consumption; balance never negative. |
| 5 | Bitwise operations | Listed, not detailed. |
| 6 | Spreadsheet with cells | Listed (cycle-detection family). |
| 7 | Tree node-count via per-node `receiveMessage`/`sendMessage` API | Reported. Follow-up: idempotency under network retries. |
| 8 | Implement `cd` (PWD + input → new path), with `..`, abs paths, then symlink-map resolution + edge cases | Reported. |
| 9 | LRU cache (with `addKey(key)` and `getCountForKey(key)` shape) | Listed. |

## ML Search Design — depth checklist (from S20)

S20 organizes depth-prep as a 2-column "vertical themes" + "broad
themes" matrix. Highlights:

**"Solid yet" topics (S20 had down):** cross entropy, cosine similarity,
nDCG, mAP, point-wise/pair-wise ranking, contrastive learning, batch
normalization, sparse neural networks.

**"Not solid yet" topics (S20 was actively studying):** model
calibration, AUC formula, attention formula (scaled dot-product),
fine-tuning approaches, mixture-of-experts, LoRA, stratified sampling,
list-wise ranking, layer normalization, ACE (Average Causal Effect),
vertical ranking, GNN/filament/pretrained-embeddings (graph).

**"Vertical themes" (deep-dive areas S20 prepared):**

- Recsys neural architectures: retrieval (related-ads/injections,
  survival rate, CUFR/BUS, HSNN), ranking (DCN), sparse features
  (sparse hashing, QR-hashing, dynamic IDs), vertical ranking (gated
  specialized modules, dedicated tasks, AIOC/AFOC, vertical NE), graph
  learning (pretrained embeddings + filament), LLMs in ranking
  (AdsLlama, LLM features).
- LLM RAG: design + evaluation (order-aware nDCG/mAP, context-precision/
  recall).
- BERT (bidirectional encoder representation transformer).
- Visual: bbycroft.net/llm.

**"Broad themes" (full ML-system-design checklist):** problem
foundation, goal/metrics, ranking systems (multi-stage, learning-to-
rank pointwise/pairwise/listwise, multi-objective), training-data
biases (negative-class downsampling, position bias, feedback loops,
cold start, friend-interaction proxies), labelling (weighted labels,
MTML), logging (offline-online consistency, primary keys, training-
serving skew), feature engineering (foundational features at IC4,
window-based and real-time at IC5/IC6, sparse-feature lookup tables,
embedding features incl. pretrained), modeling (multi-stage, retrieval
TTSN, advanced — DCN/DCNv2, ensembles, deep-and-wide, attention FM,
gating, ResNet, MoE, LoRA), specialized modules, calibration,
distillation+warmup, LLM-for-ranking applications.

## ML-Debug round — known content (compiled by S20 from 1Point3Acres)

- Multi-headed transformer with ~4-5 bugs, runs but you must judge
  correctness yourself; familiarity with the model means ~15 min if
  fluent.
- Reported related variants: tensor-shape misalignment, missing
  attention scaling, training-loop bugs.
- Second part: convert LLM training to classification (pick embedding,
  compute modified loss, model accuracy).

S20 also captures debugging tooling notes:
- `tensor.retain_grad()` to inspect intermediate gradients.
- Layer-by-layer shape printing for fast localization.
- nanoGPT / minGPT as the canonical practice surface; Karpathy's
  *Let's build GPT* and Neel Nanda's transformer-circuits walkthrough.

## Tech Deep-Dive — slide template (from S20)

Seven sections, each scored on three axes (Technical Depth, Technical
Breadth, Business Impact):

1. Project Context & TLDR.
2. Business Motivation.
3. Your Role.
4. High-Level / Design Decisions.
5. Roadblocks (and how solved).
6. Impact (with concrete numbers).
7. Mistakes and Learnings.

Recruiter emphasis: visual aid; pick a recent and complex project; aim
for 25 min talk + Q&A; the interviewer is another ML or research
engineer.

## Behavioral — STAR matrix (from S20)

S20 maps Alessandro's strengths to canonical themes:

- Mission-driven / determined → climate-change pivot story.
- Open to feedback → conflict-then-friendship story (peer Prerna).
- Think outside the box → ads-ranking onboarding via Mandarin / WeChat.
- People-communication → SIM team-building.
- Self-weakness → "too excited, skip steps, zoom in too much".

"Why OpenAI" answer arc:
- Smart colleagues from Meta moved over; spoke positively.
- Mission resonates: AGI → benefit humanity (Sam's "Intelligence Age",
  AGI → climate change angle).
- Personal-conviction examples: girlfriend therapist (Operator for
  session notes), Allison reducing hallucinations for the 400M ChatGPT
  users.
- Drive is impact > comp/level.

## Karpathy / Neel-Nanda study plan (S20)

- Karpathy: Wavenet (1h), backprop ninja (2h), let's build GPT (2h),
  GPT tokenizer (2h), reproduce GPT-2 (4h × 3 sessions).
- Neel Nanda: what is a transformer (1h), implement GPT-2 from scratch
  (1h20), *A Mathematical Framework for Transformer Circuits*
  walkthrough (2h50).
- Codeforces Div.4 / Div.2 cadence in the prep window.

## Mock-interview learnings captured (S20)

S20 contains ~6 detailed write-ups from peer mock interviews
(Meta-shadow style). Recurring failure modes:

- Too slow to surface signals (interviewer 15 min in with no clear
  technical depth).
- Letting interviewer drive instead of guiding the conversation.
- Picking weak baselines (e.g. random sampling over all Meta users).
- Insufficient depth on cross-feature engineering, hashing tricks,
  attention math, calibration.
- Wrong cross-entropy formula on the whiteboard.

## Pointers / external links collected by S20

- 1Point3Acres OpenAI threads (multiple).
- Hugging Face Ultra-Scale Playbook (training LLMs on GPU clusters).
- FineWeb blog post (data curation).
- Pinecone offline-evaluation guide.
- Practical-LLMs / applied-llms.
- Karpathy YouTube series.

## Status

- Loop status as of doc snapshot: ML screen and Coding screen PASSED;
  ML debug, deep dive, behavioral all in active prep.
- This source supersedes a lot of the aggregator-quality material in
  S2/S3/S5/S7/S17 where they conflict, since it includes verbatim
  recruiter emails and a real-loop ground truth.
