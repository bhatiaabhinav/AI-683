from AI_683.common.search_problem import SearchProblem, State
from AI_683.common.graph_search import graph_search, Node
from typing import Callable, Set
import queue


def astar(problem: SearchProblem, heuristic_fn: Callable[[State], float]) -> Node:
    frontier_set = set()
    frontier_pq = queue.PriorityQueue()

    def frontier_add(frontier: Set, node: Node):
        frontier.add(node)
        h = heuristic_fn(node.state)
        f = node.cost + h
        setattr(node, "h", h)
        setattr(node, "f", f)
        frontier_pq.put((f, node))

    def frontier_pop(frontier: Set):
        f, node = frontier_pq.get()
        frontier.remove(node)
        return node

    soln_node = graph_search(problem, frontier_set, frontier_add, frontier_pop)
    return soln_node
