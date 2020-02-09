from AI_683.common.search_problem import SearchProblem
from typing import Collection, Callable


class Node:
    """Node data structure used for graph-search"""

    def __init__(self, state, cost, parent_node):
        self.cost = cost  # g-value of the node
        self.state = state  # the state of the problem contained in the node
        self.parent_node = parent_node

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)


def graph_search(problem: SearchProblem, frontier: Collection, frontier_add_fn: Callable[[Collection, Node], None], frontier_pop_fn: Callable[[Collection], Node]):
    """returns the goal leaf_node

    Arguments:
        problem {SearchProblem} -- [description]
        frontier {Collection} -- [description]
        frontier_append_fn {Callable[[Collection, Node], None]} -- [description]
        leaf_node_choose_fn {Callable[[Collection], Node]} -- [description]

    Returns:
        [type] -- [description]
    """
    start_node = Node(problem.start_state, 0)
    frontier_add_fn(frontier, start_node)
    explored_set = set()
    while not len(frontier) == 0:
        leaf_node = frontier_pop_fn(frontier)
        s = leaf_node.state
        if problem.goal_test(s):
            return leaf_node
        explored_set.add(leaf_node)

        # now expand the node:
        legal_actions = problem.operators(leaf_node.state)
        for a in legal_actions:
            ns = problem.successor_fn(s, a)
            node = Node(ns, leaf_node.cost + problem.path_cost(s, a, ns), leaf_node)
            if node not in frontier and node not in explored_set:
                frontier_add_fn(frontier, node)

    return None  # failure
