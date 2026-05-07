# Coding questions (bank)

Questions reportedly asked in OpenAI's general / SWE-flavored coding rounds.
Each entry: short title, summary, role/round, expected follow-ups, source(s).

> Bias warning: aggregator and Medium sources sometimes recycle each other,
> so the same problem can appear "in multiple sources" without independent
> confirmation. Confidence column is best-effort.

| # | Problem | Round | Confidence | Sources |
|---|---------|-------|------------|---------|
| 1 | LRU cache | Coding screen / onsite | high | S5, S12 |
| 2 | KV-store serialize / deserialize | Coding | high | S2, S3 |
| 3 | Time-based / versioned KV store | Coding | high | S2, S3, S4 |
| 4 | Resumable iterator | Coding | medium | S2 |
| 5 | In-memory SQL DB (CRUD subset) | Coding | medium | S2, S3 |
| 6 | Unix `cd` w/ symlinks + cycles | Coding | medium | S2 |
| 7 | Multithreaded web crawler | Coding | medium | S2 |
| 8 | Spreadsheet API (`getCell`/`setCell`) + cycle detection | Coding | high | S2, S4 |
| 9 | GPU credit accounting (FIFO by expiry) | Coding | medium | S4 |
| 10 | Disease spread in a flower grid | Coding screen | medium | S3 |
| 11 | LeetCode 2408 "Design SQL" | Coding | medium | S3 |
| 12 | Credit tracking service for token balances | Coding | medium | S3 |
| 13 | Webhook system (basic) | Coding | low | S3 |
| 14 | Tree node-count via per-node `receiveMessage`/`sendMessage` API + idempotency under retries | Coding | medium | S20 |
| 15 | String-manipulation KV store: persist + restore from filesystem, custom serialization (no `json`) | Coding | high | S20 |
| 16 | Strongly-typed-language `toString` serializer | Coding | low | S20 |

## Detailed notes

### LRU cache [S5, S12]

The single most-cited OpenAI coding question. Implement `get(key)` and
`put(key, value)` in O(1). Standard solution: doubly-linked list +
hashmap. Follow-ups: thread-safety, TTL eviction, persistence.

### Time-based / versioned KV store [S2, S3, S4]

`set(key, value, timestamp)`, `get(key, timestamp)` returning the value
active at or before `timestamp`. Naive: dict-of-lists + binary search
(LeetCode 981). Follow-ups: range queries, persistence, concurrent writes,
serialize/deserialize so two processes can share state.

### KV-store serialize / deserialize [S2]

Encode `{key: value}` such that arbitrary delimiters in keys/values can
be parsed back. Length-prefix encoding (e.g. `3:key5:value`) is the
standard answer; the same pattern is used by Redis's RESP protocol.

### Resumable iterator [S2]

Iterator that supports `next`, `pause`, `resume` across multiple invocations.
Maintain explicit state; possibly serialize to a token. Follow-ups: skip,
reset.

### In-memory SQL DB [S2, S3]

Subset of SQL: tables with typed columns, `INSERT`, `SELECT ... WHERE`.
Follow-ups: indexes on columns, joins, transactions.

### Unix `cd` with symlinks [S2]

Resolve a target path string from a current working directory, handling
`.`, `..`, absolute paths, environment-style refs, and symlinks. Detect
symlink cycles.

### Multithreaded web crawler [S2]

Concurrent BFS of a URL graph: thread pool, dedup set, host rate-limiting,
graceful shutdown. Follow-ups: backoff on errors, persisting state.

### Spreadsheet API [S2, S4]

`setCell(name, formula_or_value)` / `getCell(name)`. Formulas reference
other cells. Detect cycles via DFS+visited-set. Follow-up: O(1)
`getCell` via topo-order recompute and dirty-marking.

### GPU credit accounting [S4, S20]

Reported class signature [S20]:

```python
class GPUCredit:
    def addCredit(creditID: str, amount: int,
                  timestamp: int, expiration: int) -> None: ...
    def getBalance(timestamp: int) -> int | None: ...
    def useCredit(timestamp: int, amount: int) -> None: ...
```

A credit can be used during `[timestamp, timestamp + expiration]`
(check inclusive vs. exclusive with the interviewer; examples given
were inclusive). Track credits with expiry; consume credits soonest-
to-expire first (min-heap or queue ordered by expiry). Balance never
negative. Follow-ups: refund, pre-allocation, concurrency.

### Time-based KV store — extended follow-ups [S20]

Beyond the basic LeetCode 981 shape, OpenAI's variant uses a real
timestamp as input and probes:
- Write tests; mock the timestamp source.
- Ensure timestamps are strictly monotonic.
- Multi-thread locking — compare implementations and discuss
  efficiency. The interview shape "felt like system design".

### Tree node-count via messaging API [S20]

Implement a `Node` class where each node communicates with its parent
or children via:
- `receiveMessage(from_node_id, message)` — handle inbound.
- `sendMessage(to_node_id, message)` — assume executes
  `receiveMessage` on the recipient.

A designated root receives `receiveMessage(null, message)` from an
external source. Have the root count the total nodes in the n-ary
tree and print the result. Follow-up: ensure idempotency under
network retries.

### Implement `cd` with symlink resolution [S20]

```python
def cd(pwd: str, input: str) -> str: ...
# cd("/home/bugs", ".")        -> "/home/bugs"
# cd("/home/bugs", "bunny")    -> "/home/bugs/bunny"
# cd("/home/bugs", "../daffy") -> "/home/daffy"
```

Part 2: extend with a symlink map; after each segment, replace with
the mapped path if present. Edge cases: cycles, partial paths,
trailing-slash, symlinks pointing back into the resolved path.

```python
def cd(pwd: str, input: str,
       symlinkmap: dict[str, str]) -> str: ...
# cd("/home/bugs", "lola/../basketball",
#    {"/home/bugs/lola": "/home/lola"})
# -> "/home/lola/basketball"
```

## How candidates suggest preparing [S2, S4, S5, S12]

- Implement each question above end-to-end in Python in <60 min.
- Add a test harness for each. Practice exposing edge cases yourself.
- Take a problem you've already done and add a follow-up: persistence,
  concurrency, eviction, cycles.
- Practice in CoderPad (or a stripped-down web editor) — full-IDE
  comfort fails when you lose autocomplete.

## Cross-refs
- [Coding round](../rounds/coding.md)
- [Reading list](../prep/reading-list.md)
- [CoderPad & AI tools](../tooling/coderpad-and-ai-tools.md)

## Sources
S2, S3, S4, S5, S12, S20
