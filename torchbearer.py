"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Matthew Philbin
Student ID:   828085252

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    Compelte TODO
    """
    answers = '''
    - **Why a single shortest-path run from S is not enough:**
    _A single shortest-path run from $S$ tells the Torchbearer how to travel from $S$ to any relic chamber, but once at a relic chamber it has no shortest path for its next move. While the Torchbearer could move from $S$ to any relic chamber with minimal fuel loss, it would not have enough information to move from $S$ to all relic chambers (and then the exit) with minimal fuel loss._
    - **What decision remains after all inter-location costs are known:**
    _What sequence should the Torchbearer explore the relic chambers in to leave with minimal cost?_
    - **Why this requires a search over orders (one sentence):**
    _Different paths that reach each relic chamber and the exit may have different overall costs and there is no greedy method to bypass a search over order by leveraging local optimality (see Part 4)_
    '''
    return answers
    answers = '''
    - **Why a single shortest-path run from S is not enough:**
    _A single shortest-path run from $S$ tells the Torchbearer how to travel from $S$ to any relic chamber, but once at a relic chamber it has no shortest path for its next move. While the Torchbearer could move from $S$ to any relic chamber with minimal fuel loss, it would not have enough information to move from $S$ to all relic chambers (and then the exit) with minimal fuel loss._
    - **What decision remains after all inter-location costs are known:**
    _What sequence should the Torchbearer explore the relic chambers in to leave with minimal cost?_
    - **Why this requires a search over orders (one sentence):**
    _Different paths that reach each relic chamber and the exit may have different overall costs and there is no greedy method to bypass a search over order by leveraging local optimality (see Part 4)_
    '''
    return answers


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    Compelete TODO
    """
    return [spawn] + relics.copy()
    return [spawn] + relics.copy()


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    Completed TODO
    """
    costs = {node: float('inf') for node in graph}
    costs[source] = 0

    heap = []
    heapq.heappush(heap, (0, source))

    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if current_cost > costs[current_node]:
            continue # skip duplciates in the heap

        for neighbor, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    
    return costs


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    Completed TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    dist_table = {source: run_dijkstra(graph, source) for source in sources}
    return dist_table


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    Complete TODO
    """
    answers = '''
    3a:
    - **For nodes already finalized (in S):**
    _The value of `dist` at that node `v` is the smallest amount of fuel the Torchbearer can burn to reach `v` from the Dungeon Entrance `x`._
    - **For nodes not yet finalized (not in S):**
    _The value of `dist` at that node `v` is the smallest amount of fuel the Torchbearer must burn to reach that node from the Dungeon Entrance `x` by taveling only throguh nodes `u` whose cheapest possible path is already known (i.e., `u` in `S`)._
    
    3b:
    - **Initialization : why the invariant holds before iteration 1:**
    _Before iteration 1, `S` is empty, `dist[x] == 0`, and `dist[y] == inf` for all `y != x`, where `inf` represents an unreachably high value; also, no paths to `x` have been discovered except for the trivial path `x -0-> x` which contains no internal vertices from `S`. Thus the invariant holds._

    - **Maintenance : why finalizing the min-dist node is always correct:**
    _Suppose the algorithm finalizes the min-dist node and then discovers a new path with less distance: this new path must take a newly discovered edge (by the meaning of discovered) in addition to the current edges, since the minimum-distance path with the current edges is already found. Since edge weights are non-negative, adding a new edge that must add a non-negative amount to distance; thus it cannot have less distance than the previous min-dist path, and so thus we have a contradiction._

    - **Termination : what the invariant guarantees when the algorithm ends:**
    _The algorithm concludes when each Relic Chamber is in `S` along with the exit node; thus the invariant implies that `dist[v]` equals the cost of the shortest-distance path from `x` to `v`, where `v` may be an arbitrary Relic Chamber or the exit node._

    3c:
    _The distances calculated in Dijkstra's algorithm give the Torchbearer's minimal fuel cost to travel between two important chambers in the dungeon; from this the Torchbearer can order relic chambers to travel between all of them with minimal total cost._
    '''
    return answers
    answers = '''
    3a:
    - **For nodes already finalized (in S):**
    _The value of `dist` at that node `v` is the smallest amount of fuel the Torchbearer can burn to reach `v` from the Dungeon Entrance `x`._
    - **For nodes not yet finalized (not in S):**
    _The value of `dist` at that node `v` is the smallest amount of fuel the Torchbearer must burn to reach that node from the Dungeon Entrance `x` by taveling only throguh nodes `u` whose cheapest possible path is already known (i.e., `u` in `S`)._
    
    3b:
    - **Initialization : why the invariant holds before iteration 1:**
    _Before iteration 1, `S` is empty, `dist[x] == 0`, and `dist[y] == inf` for all `y != x`, where `inf` represents an unreachably high value; also, no paths to `x` have been discovered except for the trivial path `x -0-> x` which contains no internal vertices from `S`. Thus the invariant holds._

    - **Maintenance : why finalizing the min-dist node is always correct:**
    _Suppose the algorithm finalizes the min-dist node and then discovers a new path with less distance: this new path must take a newly discovered edge (by the meaning of discovered) in addition to the current edges, since the minimum-distance path with the current edges is already found. Since edge weights are non-negative, adding a new edge that must add a non-negative amount to distance; thus it cannot have less distance than the previous min-dist path, and so thus we have a contradiction._

    - **Termination : what the invariant guarantees when the algorithm ends:**
    _The algorithm concludes when each Relic Chamber is in `S` along with the exit node; thus the invariant implies that `dist[v]` equals the cost of the shortest-distance path from `x` to `v`, where `v` may be an arbitrary Relic Chamber or the exit node._

    3c:
    _The distances calculated in Dijkstra's algorithm give the Torchbearer's minimal fuel cost to travel between two important chambers in the dungeon; from this the Torchbearer can order relic chambers to travel between all of them with minimal total cost._
    '''
    return answers


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    Complete TODO
    """
    answers = '''
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

    - _Any solution must traverse all the Relic Chambers in some given order before reaching the exit node, so the algorihtm must explore possible Relic Chamber orderings to produce one with minimal total fuel cost._
    '''
    return answers


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    Complete TODO
    """
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    cost, order = find_optimal_route(dist_table, spawn, relics, exit_node)
    return cost, order
    dist_table = precompute_distances(graph, spawn, relics, exit_node)
    cost, order = find_optimal_route(dist_table, spawn, relics, exit_node)
    return cost, order


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
