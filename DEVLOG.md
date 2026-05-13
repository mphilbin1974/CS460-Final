# Development Log – The Torchbearer

**Student Name:** Matthew Philbin
**Student ID:** 828085252

> Instructions: Write at least four dated entries. Required entry types are marked below.
> Two to five sentences per entry is sufficient. Write entries as you go, not all in one
> sitting. Graders check that entries reflect genuine work across multiple sessions.
> Delete all blockquotes before submitting.

---

## Entry 1 – [5/6/2026]: Initial Plan

_Completed README.md parts 1, 2, and 3a; I intend to complete README.md entirely before coding so as to guarantee correctness, so implementation details are still tentative. I have identified that the problem requires knowing how to optimally get from any Source Node (Dungeon Entrance + Relic Chambers) to any other in a weighted, directed, connected graph, so I will use Dijkstra's algorithm on each source node to compute these routes and compose the problem from such. I hope to have a full implementation plan by the next entry in DEVLOG.md._

---

## Entry 2 – [5/13/2026]: [Short description]

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_Completed README.md parts 3, 4, 5, 6. The Torchbearer will find the minimal distance ordering using an exhaustive search algorithm with A* pruning to evaluate all possible orderings by considering the minimal distances between the start node, end node, and each relic chamber as determined by Dijkstra's algorithm. Orderings will then be searched exahustively using A* pruning with the following heuristic: $h(n)$ is the sum of the minimal distance to the next relic chamber and minimal distance from that relic chamber to the exit. Since all possible paths will either be searched or accurately pruned, the minimal-cost ordering will be searched and thus found. I will first implement distance precomputation ebtween important nodes using Dijkstra's algorithm; I expect to find the most difficulty in handling recursion for Dijkstra's and the exhaustive search, specifically traversing the dungeon and correctly tracking the state of visited rooms. I will create a small graph by hand to manually verify program outputs._

---

## Entry 3 – [Date]: [Short description]

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_Your entry here._

---

## Entry 4 – [Date]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_Your entry here._

---

## Final Entry – [Date]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.25 |
| Part 2: Precomputation Design | 0.5 |
| Part 3: Algorithm Correctness | 0.5 |
| Part 4: Search Design | 0.25 |
| Part 5: State and Search Space | 0.25 |
| Part 6: Pruning | |
| Part 7: Implementation | |
| README and DEVLOG writing | 0.1 |
| **Total** | |
