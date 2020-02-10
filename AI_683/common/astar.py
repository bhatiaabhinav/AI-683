from AI_683.common.search_problem import SearchProblem, State
from AI_683.common.graph_search import graph_search, Node
from typing import Callable, Tuple, List


def astar(problem: SearchProblem, heuristic_fn: Callable[[State], float]) -> Tuple[Node, List[Tuple[Node, float]]]:
    """Runs astar with given heuristic

    Arguments:
        problem {SearchProblem} -- [description]
        heuristic_fn {Callable[[State], float]} -- takes in a State and returns an underestimate of optimal cost to the goal from that state

    Returns:
        Tuple[Node, List[Tuple[Node, float]]] -- goal_node, oredered list of (node, f-value of node) which were expanded
    """
    return graph_search(problem, lambda n: n.cost + heuristic_fn(n.state))
