# Alignment Researcher reading list

Anchored on what the OpenAI alignment-research panel can be assumed to
know, plus what current/former alignment-team people have publicly
recommended [S1, S6, S24, S25, S45, S46, S47, S48].

Reading order is **prioritized** — Tier 1 first, then Tier 2, then
Tier 3.

## Tier 1 — non-negotiable, read end-to-end

### OpenAI's own alignment papers (read in arc order)

1. *Weak-to-strong generalization* (Burns et al., Dec 2023) [S30].
2. *CriticGPT — LLM critics help catch LLM bugs* (McAleese et al.,
   Jul 2024) [S34].
3. *The Instruction Hierarchy* (Wallace et al., Apr 2024) [S32].
4. *Scaling and evaluating sparse autoencoders* (Gao et al.,
   Jun 2024) [S33].
5. *Deliberative Alignment* (Guan et al., Dec 2024) [S31].
6. *Sycophancy in GPT-4o* + *Expanding on sycophancy* (Apr-May
   2025) [S41].
7. *GPT-5 Safe Completions* (Aug 2025) [S42].
8. *Detecting and reducing scheming* (OpenAI × Apollo, Sept 2025)
   [S35].
9. *Chain of Thought Monitoring* + *Evaluating CoT monitorability*
   (Mar / Jul 2025) [S36].
10. *Natural emergent misalignment from reward hacking in
    production RL* (Nov 2025, arXiv 2511.18397) [S54].

### alignment.openai.com (Dec 2025 launch)

Read all four launch posts plus the Dec 22 emergent-misalignment
suppression post [S26]:

- *Hello World* (Dec 1).
- *Debugging misaligned completions with sparse-autoencoder latent
  attribution* (Dec 1).
- *A Practical Approach to Verifying Code at Scale* (Dec 1).
- *Sidestepping Evaluation Awareness with Production Evaluations*
  (Dec 18).
- *Helpful assistant features suppress emergent misalignment*
  (Dec 22).

### System cards (safety sections)

Skim all; read the most-recent two end-to-end [S53]:

- o1 (Dec 2024).
- o3-mini (Jan 31, 2025).
- GPT-4.5 (Feb 27, 2025).
- o3 / o4-mini (Apr 16, 2025).
- GPT-5 (Aug 13, 2025) ← deepest dive.
- gpt-oss (Aug 5, 2025).

### Specs and frameworks

- **Model Spec** 2025-12-18 [S40].
- **Preparedness Framework v2** (Apr 2025) [S39].
- *Our approach to alignment research* [S27] and *How we think about
  safety alignment* [S28].

## Tier 2 — high-leverage external

### Anthropic alignment canon (the OpenAI panel assumes you've read)

For full context see
[`cross-lab/anthropic-alignment.md`](../cross-lab/anthropic-alignment.md)
and
[`cross-lab/anthropic-alignment-interview.md`](../cross-lab/anthropic-alignment-interview.md).

- *Sleeper Agents* (Hubinger et al., Jan 2024) [S60]. Required.
- *Constitutional AI / RLAIF* (Bai et al., Dec 2022) [S61]. Required.
- *Anthropic interpretability canon* — Toy Models of Superposition →
  Towards Monosemanticity → Scaling Monosemanticity → Crosscoders +
  Influence Functions [S67]. Required end-to-end if interp is your
  area; required-skim otherwise.
- *Auditing LMs for Hidden Objectives* (Marks et al., Mar 2025) [S64].
- *Petri* release post + tech report (Oct 2025) [S57] — pair with
  [`topics/petri-and-auditing.md`](../topics/petri-and-auditing.md).
- *SHADE-Arena* (Kutasov et al., Jun 2025) [S63].
- *Agentic Misalignment* (Anthropic, Jun-Oct 2025) [S62].
- *Sycophancy in LMs* (Sharma et al., ICLR 2024) [S66].
- *Many-Shot Jailbreaking* (Anil et al., NeurIPS 2024) [S65].
- *Anthropic Recommended Directions* (Bowman et al., 2025) [S58].
- *Sam Bowman's FAQ + The Checklist* [S68] — hiring-criteria proxy.
- *Ethan Perez project-selection + empirical-tips essays* [S69].
- *Hubinger's Alignment Stress-Testing intro* [S70].
- *Anthropic Frontier Red Team* [S73] — for FRT-flavor candidates.

### Other cross-lab alignment papers

- Greenblatt et al. — *Alignment Faking* (Dec 2024) [S37].
- Greenblatt et al. — *AI Control: Improving Safety Despite
  Intentional Subversion* (Dec 2023) [S38].
- Apollo — *Frontier models are capable of in-context scheming*
  [S50].
- Apollo — *Stress testing deliberative alignment for anti-scheming
  training* (Sept 2025) [S35].
- Hubinger et al. — *Risks from Learned Optimization in Advanced ML
  Systems* (2019). Foundational mesa-optimizer / deceptive-alignment
  framing.

### Scalable-oversight foundations

- Christiano, Shlegeris, Amodei — *Supervising strong learners by
  amplifying weak experts* (2018).
- Irving, Christiano, Amodei — *AI safety via debate* (2018).
- Leike et al. — *Scalable agent alignment via reward modeling*
  (2018).

### Mech interp

- Neel Nanda's *Concrete steps to get started* and *Prereqs for mech
  interp* [S48].
- Anthropic — *Toy models of superposition* (2022).
- Anthropic — *Towards Monosemanticity* / *Scaling Monosemanticity*
  (2023-2024).
- Olah et al. — *Zoom In: An Introduction to Circuits* (2020).
- ARENA curriculum (multi-week practical track).

### Reward hacking / post-training

- Lilian Weng — *Reward Hacking in RL* (Nov 2024) [S46]. Canonical.
- Rafailov et al. — *Direct Preference Optimization* (2023).
- Ouyang et al. — *Training LMs to follow instructions with human
  feedback* (InstructGPT, 2022).
- Sundeep Teki — *The complete guide to post-training LLMs* (2025)
  [S6, ref `sundeepteki.org/.../complete-guide-to-post-training-...`].
- DeepSeek — *DeepSeek-R1* / *DeepSeekMath* for GRPO context.

### AI safety in scope (worldview-setting)

- Anthropic Alignment Science blog (full archive — interviewers cite
  it as a benchmark for what good alignment-science writing looks
  like).
- Christiano — *What failure looks like* (2019).
- Christiano — *Eliciting Latent Knowledge* (ELK) report (2021).
- Bostrom — *Superintelligence* (selected chapters).
- Hubinger — *Model organisms of misalignment* framing posts.

## Tier 3 — depth bets / signaling

### Boaz Barak — Harvard CS 2881 syllabus [S45]

Boaz Barak (associated with the Researcher-Alignment role per S31)
taught Harvard's *AI Safety* course in Fall 2025. The reading list
is the closest public proxy for the depth bar of this role:

- *AI 2027* (forecasting essay).
- Selected chapters of Bostrom's *Superintelligence*.
- METR's autonomous-replication evaluations.
- *Replicating Emergent Misalignment* (homework assignment).

Endorsed by Owain Evans on X (post `1964869006617403709`).

### Podcasts (calibration)

- 80,000 Hours #159 — Jan Leike on superalignment hiring [S47].
- 80,000 Hours — Jan Leike on becoming an ML alignment researcher
  [S47].
- 80,000 Hours — Neel Nanda on mechanistic interpretability.
- AXRP #39 — Hubinger on model organisms of misalignment [S49].
- Dwarkesh × Sutskever (Nov 2025) — for SSI-vs-OpenAI alignment-
  philosophy framing [S24].

### People to follow on X

- @boazbaraktcs (Boaz Barak) [S45].
- @OwainEvans_UK (Owain Evans).
- @woj_zaremba (Wojciech Zaremba).
- @joannejang (Joanne Jang — left OpenAI; still posts on the Model
  Spec).
- @OpenAI status thread on CoT monitoring (`status/1945156362859589955`).

## Gaps to be explicit about

This list is anchored on **public** signal. Two specific gaps:

- **No first-person OpenAI Alignment Researcher loop writeup** exists
  publicly as of May 2026 [S24]. The closest substitutes are general
  OpenAI Researcher writeups (Exponent / Linkjob; treat carefully) and
  ML Researcher loops in S20 / S6.
- **The team's internal reading list** likely differs in details. If
  your recruiter shares one, *that* supersedes this page.

## Cross-refs
- [Researcher, Alignment role](../roles/alignment-researcher.md)
- [Alignment timeline / study plan](alignment-timeline.md)
- [Alignment topic overview](../topics/alignment.md)
- [Why OpenAI](why-openai.md)

## Sources
S1, S6, S19, S24, S25, S26, S27, S28, S30-S55
