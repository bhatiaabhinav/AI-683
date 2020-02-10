from AI_683.common.search_problem import SearchProblem, State
from AI_683.common.graph_search import graph_search, Node
from typing import Callable


def astar(problem: SearchProblem, heuristic_fn: Callable[[State], float]) -> Node:
    return graph_search(problem, lambda n: n.cost + heuristic_fn(n.state))
