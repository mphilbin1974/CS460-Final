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

## Entry 2 – [5/13/2026]: Completed Documentation

> Required. Write this before writing any code. Describe your plan: what you will
> implement first, what parts you expect to be difficult, and how you plan to test.

_Completed README.md parts 3, 4, 5, 6. The Torchbearer will find the minimal distance ordering using an exhaustive search algorithm with A* pruning (which I know from hobby game dev) to evaluate all possible orderings by considering the minimal distances between the start node, end node, and each relic chamber as determined by Dijkstra's algorithm. Orderings will then be searched exahustively using A* pruning with the following heuristic: $h(n)$ is the sum of the minimal distance to the next relic chamber and minimal distance from that relic chamber to the exit. Since all possible paths will either be searched or accurately pruned, the minimal-cost ordering will be searched and thus found. I will first implement distance precomputation ebtween important nodes using Dijkstra's algorithm; I expect to find the most difficulty in handling recursion for Dijkstra's and the exhaustive search, specifically traversing the dungeon and correctly tracking the state of visited rooms. I will trace a small graph by hand to manually verify program outputs._

---

## Entry 3 – [5/13/2026]: Began Code

> Required. At least one entry must describe a bug, wrong assumption, or design change
> you encountered. Describe what went wrong and how you resolved it.

_I had to make a number of small changes upon starting the implementation. I realized that with the whole algorithm already documented it made sense to begin with the declarative functions, so I began by implementing the main pipeline in `solve`, `precompute_distances`, and `select_sources`, and then began writing the lower-level functions. I ran into a few errors in `run_dijkstra`, mostly since I had never used the Python `heapq` module before: the syntax is a little weird to me and the tuple required for a push argument (`cost`, `node`) is the opposite order of the edge tuples (`node`, `cost`) in `graph`. I fixed these foremost by consulting the documentation and also just by unpacking edges into named variables to not deal with magic numbers in my code (which I should have done from the beginning)._

---

## Entry 4 – [5/14/2026]: Post-Implementation Reflection

> Required. Written after your implementation is complete. Describe what you would
> change or improve given more time.

_With time I would be most interested to change the heuristic function to see if I can get slightly faster search times. This is because the solution is already otpimal (since the search is exhaustice), but is based on DFS, which has a drawback in that it tends to waste time exploring useless branches. So while improving the output is not possible, improving the performance may be, and the open-ended nature of choosing a heuristic makes me think I could come up with a better one with time to iterate._

---

## Final Entry – [5/14/2026]: Time Estimate

> Required. Estimate minutes spent per part. Honesty is expected; accuracy is not graded.

| Part | Estimated Hours |
|---|---|
| Part 1: Problem Analysis | 0.25 |
| Part 2: Precomputation Design | 0.5 |
| Part 3: Algorithm Correctness | 0.5 |
| Part 4: Search Design | 0.25 |
| Part 5: State and Search Space | 0.25 |
| Part 6: Pruning | 0.5 |
| Part 7: Implementation | 3.5 |
| README and DEVLOG writing | 0.25 |
| **Total** | 6 |
