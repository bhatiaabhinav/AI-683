import numpy as np
from AI_683.HW1.q5 import KnightProblem, knight_heuristic_naive, astar


def test_simple_knight():
    start_point = np.array([0, 0])
    goal_point = np.array([2, 2])
    problem = KnightProblem(start_point, goal_point)
    soln, trace = astar(problem, lambda state: knight_heuristic_naive(state.point, goal_point))
    assert soln.cost == 4
    soln.print_trace_to_parent()
    print(len(trace))
    print(trace)
