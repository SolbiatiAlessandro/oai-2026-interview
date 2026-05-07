# System design round (general)

Open-ended whiteboard design. ~45-60 min. The design is graded on
how you *drive* the conversation as much as on the artifact: scope,
clarify, sketch, justify trade-offs, dive deeper on what the
interviewer probes [S3, S5, S9].

## Format

- **Duration**: 45-60 min [S5, S9].
- **Tooling**: shared whiteboard (Excalidraw/CoderPad whiteboard).
- **Prompt shape**: "Design X" — open-ended. The first part of the
  round is *yours* to scope.

## Canonical prompts seen

(See [system-design-questions](../questions/system-design-questions.md)
for the full bank.)

- Design Slack [S3, S9]
- Design Online Chess [S3]
- Design GitHub Actions [S3]
- Design a Payment System [S3]
- Design ChatGPT (or "ChatGPT for 100M users") [S3, S5]
- Design a webhook system [S3]

## Recommended cadence

5-10 min scope and clarify, 15-20 min skeleton, then drill into 1-2
components based on interviewer interest [S3, S5, S9]. Practical
checklist:

1. **Functional scope**: features in vs. out.
2. **Non-functional**: scale, latency, durability, consistency,
   security, cost.
3. **Capacity estimates**: QPS, payload size, storage, fan-out.
4. **High-level boxes-and-arrows**: clients, API, services, data,
   queues.
5. **Data model**: tables / objects / indexes.
6. **Protocols**: sync vs. async, idempotency, retries.
7. **Reliability**: failure modes, replication, regions, SLOs.
8. **Performance**: hot path optimizations, caching, sharding.
9. **Trade-off summary** before time runs out.

## Bar / signals [S3, S9]

- **Drive the room.** Don't wait to be asked the next question. Walk
  the interviewer through your decision tree.
- **Trade-offs over technologies.** Don't name-drop Kafka without
  saying *why* it beats SQS in the use case.
- **Reasonable defaults**, then refine. Pick a SQL primary, RW-replicas,
  Redis cache; *then* discuss when you'd shard or move to a wide-column
  store.
- **Failure modes**. The interviewer will pick one box and ask "what
  happens when this dies?" [S3].
- **End on a summary**: what you built, the open questions, what you'd
  do next.

## ML-flavored variants

For ML/MLE/RE candidates, "Design ChatGPT" is the canonical [S3, S5].
The interview folds in ML-system-design content (model serving,
retrieval, evaluation, feedback loops). See
[ML system design](ml-system-design.md).

## Cross-refs
- [ML system design](ml-system-design.md)
- [System-design questions](../questions/system-design-questions.md)

## Sources
S3, S5, S9
