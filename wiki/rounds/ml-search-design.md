# ML search/recsys design round

A specific flavor of the ML system design round, asked of candidates
with search/recommender-system backgrounds. Confirmed by OpenAI's
recruiter description for the round (with interviewer Young Cha) in
S20.

## Format (verbatim from S20)

> "This will be an interview where we will be evaluating the
> candidate's search and/or recommendations systems experience and
> ways to adapt LLMs to interact with such systems. The candidate
> should be prepared for both working through an open ended ML
> question as well as specific questions related to algorithms or
> techniques typically employed in such settings." [S20]

Areas evaluated (verbatim from email):
1. Architectural components and flow for ML systems.
2. Ability to deep-dive into ML techniques relevant to search,
   ranking and retrieval.
3. Optimization techniques for ML models.
4. Metrics and evaluation.

## Strategy [S20]

- **Pick your area of expertise and lead the interview**. If you let
  the interviewer drive, they'll wander into your weakest topics.
- Be at-least-generic across the recsys stack and conserve time for
  one area where you go three layers deep.
- The signal they want: you've built and operated something at scale,
  not just read papers. Discuss training-serving consistency, online
  metrics, real-time-feature plumbing, A/B testing, cold start.

## Depth checklist (S20's "vertical themes")

The areas S20 prepared:

- **Retrieval**: dense vs. sparse retrieval, two-tower models, ANN
  indexes (HNSW, IVF, LSH), related-content / injection candidate
  generation, hierarchical structured retrieval (HSNN /
  hierarchical clustering encoder), generative retrieval (Recsys-GR).
- **Ranking**: multi-stage ranking, learning-to-rank
  (point-wise / pair-wise / list-wise), DCN / DCN-v2, attention
  factorization machines, deep-and-wide, multi-objective /
  multi-task losses, calibration.
- **Sparse features**: sparse hashing, QR-hashing for collision /
  size reduction, dynamic IDs, cross-feature hashing (e.g.
  `hash(country, zip)`), training-serving skew, embedding lookup
  tables, lifetime issues with ad/user IDs (cold start),
  semantically meaningful sparse IDs (keywords as IDs).
- **Embedding features**: learned embeddings, pretrained embeddings +
  graph (filament-style), KNN cluster IDs as features.
- **Vertical / specialized modules**: gated specialized modules,
  dedicated-task architectures, segmental feature importance,
  vertical NE.
- **LLMs in ranking and retrieval**: AdsLlama-style fine-tuning,
  LLM-derived features, embedding from LLM (LLM2Vec), HLLM,
  prompt-engineered classifiers, LLM-augmented user / ad embeddings.
- **Evaluation**: order-aware (nDCG, mAP, MRR), order-unaware
  (context-precision, context-recall), online (A/B, CTR, session
  metrics), latency-accuracy tradeoffs, fairness/bias.

## Broad-themes checklist (S20)

S20 organizes the broad ML-system-design surface as: problem
foundation → goal/metrics → ranking systems → training data (biases,
sampling, position-as-feature, feedback loops, cold-start) → labelling
(weighted labels, MTML) → logging (offline/online consistency, primary
keys) → feature engineering (foundational + advanced) → modeling
(multi-stage, retrieval, advanced architectures, specialized
modules) → calibration → distillation + warmup → online evaluation.

## Common open prompts

- Design a personalized recommender for a places/listings home page.
  Cold start. Multi-stage retrieval + ranking. Sparse hashing,
  attention-pooling, calibration [S20].
- **Design a RAG system and combine with LLMs.** Reported as an
  ML-screen prompt; interactive feedback round [S20].
- Bootstrapping / data-flywheel: from a large pool of unlabeled data,
  mine new labels using a classifier you build yourself [S20].
- Detect duplicate accounts (two accounts → same person). Real-time
  classification with retrieval [S20].

## Common pitfalls (from S20's mock-debriefs)

- Going wide instead of deep — surface 5 components at low resolution
  instead of 1 component at high resolution.
- Wrong cross-entropy formula on the whiteboard.
- Picking a weak baseline (random sampling over all users; one
  decision tree).
- Letting the interviewer drive while you fish for hints.
- Missing class-imbalance treatment / down-sampling.
- Skipping stratified sampling / position-bias / cohort logic.
- Skipping the offline → online → A/B story.

## Cross-refs
- [ML system design](ml-system-design.md)
- [Transformers topic](../topics/transformers.md)
- [ML questions bank](../questions/ml-questions.md)

## Sources
S1, S6, S9, S17, S20
