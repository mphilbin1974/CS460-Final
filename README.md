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
| _Dungeon Entrance_ | _The Torchbearer must move from the Dungeon Entrance to the first Relic Chamber in the chosen sequence. Since the cost from $S$ to each $R \in M$ affects which relic chamber is chosen first, we run Dijkstra's with the Entrance as a source to find these costs._ |
| _Relic Chamber_ | _The Torchbearer must move from each Relic Chamber to the next Relic Chamber in the chosen sequence. Since the cost from the current chamber to each other relic chamber affects which is chosen next, we run Dijkstra's with each chamber as a source to find these costs._ |

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

For every vertex v in S, dist[v] is the true shortest-path distance from x to v. For every vertex u not in S, dist[u] is the length of the shortest discovered path from x to u whose internal vertices all lie in S.

- **Initialization : why the invariant holds before iteration 1:**
  _Before iteration 1, `S` is empty, `dist[x] == 0`, and `dist[y] == inf` for all `y != x`, where `inf` represents an unreachably high value; also, no paths to `x` have been discovered except for the trivial path `x -0-> x` which contains no internal vertices from `S`. Thus the invariant holds._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Suppose the algorithm finalizes the min-dist node and then discovers a new path with less distance: this new path must take a newly discovered edge (by the meaning of discovered) in addition to the current edges, since the minimum-distance path with the current edges is already found. Since edge weights are non-negative, adding a new edge that must add a non-negative amount to distance; thus it cannot have less distance than the previous min-dist path, and so thus we have a contradiction._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _The algorithm concludes when each Relic Chamber is in `S` along with the exit node; thus the invariant implies that `dist[v]` equals the cost of the shortest-distance path from `x` to `v`, where `v` may be an arbitrary Relic Chamber or the exit node._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_The distances calculated in Dijkstra's algorithm give the Torchbearer's minimal fuel cost to travel between two important chambers in the dungeon; from this the Torchbearer can order relic chambers to travel between all of them with minimal total cost._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:**
  _Traveling through the minimal-cost route possible to an undiscovered Relic Chamber forces the algorithm to take on later costs such that total costs are higher than a valid path from some other strategy._

- **Counter-example setup:**
  _Consider the following adjacency list:_

    `S : [(A, 1), (B, 2)]`
  
    `A : [(B, 10), (T, 15)]`
  
    `B : [(A, 1), (T, 10)]`
  
    `T : []`
  
- **What greedy picks:**
  _`S -1-> A -10-> B -10-> T` with total cost `1 + 10 + 10 = 21`._

- **What optimal picks:**
  _`S -2-> B -1-> A -15-> T` with total cost `2 + 1 + 15 = 18`._

- **Why greedy loses:**
  _Optimal picks `A` last, taking only one high-cost move by entering `T` through `A`, but Greedy chooses `A` immediately for having the minimum-distance path available; since `A` is not the last Relic Chamber, it must then take another high-cost edge to leave `A` and then another when entering `T`._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Any solution must traverse all the Relic Chambers in some given order before reaching the exit node, so the algorihtm must explore possible Relic Chamber orderings to produce one with minimal total fuel cost._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | `current_loc` | `node` | _Represents which room of the Dungeon the Torchbearer is in as a `node` in `G`._ |
| Relics already collected | `relics_visited_order` | `list[node]` | _Represents the relics already gathered as an indexed `list` of the Relic Chambers in `G` they were found in._ |
| Fuel cost so far | `cost_so_far` | `float` | _Represents the total fuel the Torchbearer has already spent; represented as a `float` so as to compare to the best-cost route found up to the current stage (also a `float`)._ |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | `set` |
| Operation: check if relic already collected | Time complexity: $O(1)$ |
| Operation: mark a relic as collected | Time complexity: $O(1)$ |
| Operation: unmark a relic (backtrack) | Time complexity: $O(1)$ |
| Why this structure fits | The `set` provides constant-time lookup, insertion, and deletion; we can equate `node` membership to being collected, and thus we have $O(1)$ operations for the above. |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** $O(k!)$

- **Why:** _If we naively take the minimum we must check every possible valid route to ensure we have it; this is equivalent to checking every ordering of $k$ terms, which is $O(k!)$._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _The total fuel cost of the minimal-cost valid path (ordering) found so far._
- **When it is used:** _When another ordering being explored passes that amount in cost, and before that ordering is expanded (before the Dungeon is explored) from that point._
- **What it allows the algorithm to skip:** _The algorithm can skip evaluating the cost of the rest of the ordering._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _The Torchbearer's current location, the relics it has already collected, and the precomputed minimal distances between important chambers and to the exit._
- **What the lower bound accounts for:** _Let the lower bound heuristic be the sum of the minimal distance to the next relic chamber and minimal distance from that relic chamber to the exit._
- **Why it never overestimates:** _Any remaining path must include the closest remaining relic chamber and the exit, thus it must include the minimal distance to reach these two. With no remaining relics, the path to the exit is already optimal, so the heuristic is unnecessary._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _If the sum of the fuel spent so far and the lower bound heuristic is not below the minimal-cost route found so far then it cannot possibly produce a cheaper route by adding positive edges. Thus this sum indicates whether a given path may lead to a new optimal solution (by A* pruning with the given heuristic). If not, this path cannot improve the algorithm and thus may be pruned._

---

## References

- _None beyond lecture notes._
