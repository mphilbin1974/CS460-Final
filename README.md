# The Torchbearer

**Student Name:** Matthew Philbin
**Student ID:** 828085252
**Course:** CS 460 – Algorithms | Spring 2026

> This README is your project documentation. Write it the way a developer would document
> their design decisions , bullet points, brief justifications, and concrete examples where
> required. You are not writing an essay. You are explaining what you built and why you built
> it that way. Delete all blockquotes like this one before submitting.

---

## Part 1: Problem Analysis

> Document why this problem is not just a shortest-path problem. Three bullet points, one
> per question. Each bullet should be 1-2 sentences max.

- **Why a single shortest-path run from S is not enough:**

  _A single shortest-path run from $S$ tells the Torchbearer how to travel from $S$ to any relic chamber, but once at a relic chamber it has no shortest path for its next move. While the Torchbearer could move from $S$ to any relic chamber with minimal fuel loss, it would not have enough information to move from $S$ to all relic chambers (and then the exit) with minimal fuel loss._

- **What decision remains after all inter-location costs are known:**
  
  _What sequence should the Torchbearer explore the relic chambers in to leave with minimal cost?_

- **Why this requires a search over orders (one sentence):**
  
  _Different paths that reach each relic chamber and the exit may have different overall costs and there is no greedy method to bypass a search over order by leveraging local optimality (see Part 4)_

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

> List the source node types as a bullet list. For each, one-line reason.

| Source Node Type | Why it is a source |
|---|---|
| _Dungeon Entrance_ | _The Torchbearer must move from the Dungeon Entrance to the first Relic Chamber in the chosen sequence. Since the cost from $S$ to each $R\in M$ affects which relic chamber is chosen first, we run Dijkstra's with the Entrance as a source to find these costs_ |
| _Relic Chamber_ | _The Torchbearer must move from each Relic Chamber to the next Relic Chamber in the chosen sequence. Since the cost from the current chamber to each other relic chamber affects which is chosen next, we run Dijkstra's with each chamber as a source to find these costs_ |

### Part 2b: Distance Storage

> Fill in the table. No prose required.

| Property | Your answer |
|---|---|
| Data structure name | _Nested Dictionary_ |
| What the keys represent | _Outer: Source Nodes; Inner: Each possible destination_ |
| What the values represent | _Outer: The minimal cost from the Source Node to each possible destination; Inner: The minimal cost from the Source Node to the given destination_ |
| Lookup time complexity | $O(1)$ |
| Why O(1) lookup is possible | _Python dictionaries are implemented via hashmaps, which use a hash function to do lookups in constant time. A nested dictionary (2-deep) lookup thus has a time complexity of $O(1) + O(1) = O(1)$._ |

### Part 2c: Precomputation Complexity

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _We run Dijkstra's once per source node, so this is_ $|\text{Source Nodes}| = |M \cup \{S\}| = 1 + k \in O(k)$
- **Cost per run:** $O(m\log{n})$
- **Total complexity:** $O(k)(O(m\log{n})) = O(km\log{n})$
- **Justification (one line):** _Dijkstra's runs once in $O(m\log{n})$ time from each of the $k + 1$ source nodes, giving the result._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _The value of `dist` at that node `v` is the smallest amount of fuel the Torchbearer can burn to reach `v` from the Dungeon Entrance `x`._

- **For nodes not yet finalized (not in S):**
  _The value of `dist` at that node `v` is the smallest amount of fuel the Torchbearer must burn to reach that node from the Dungeon Entrance `x` by taveling only throguh nodes `u` whose cheapest possible path is already known (i.e., `u` in `S`)._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

For every vertex v in S, dist[v] is the true shortest-path distance from x to v. For every vertex u not in S, dist[u] is the length of the shortest discovered path from x to u whose internal vertices all lie in S.

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
