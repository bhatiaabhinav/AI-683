from AI_683.problems.grid_problem import GridProblem
from AI_683.common.astar import astar
import numpy as np


g = GridProblem(np.array([0, 0]), np.array([2, 5]))


def test_gridsimple():
    soln, exploration_seq = astar(g, lambda s: np.linalg.norm(s.point - g.goal_state.point, ord=2))
    assert soln.cost == 5


soln, exploration_seq = astar(g, lambda s: np.linalg.norm(s.point - g.goal_state.point, ord=2))
print("Soln Trace:")
soln.print_trace_to_parent()

print("")
print("Exploration Trace ({0}):".format(len(exploration_seq)))
print(exploration_seq)
