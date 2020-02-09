from AI_683.problems.grid_problem import GridProblem
from AI_683.common.astar import astar
import numpy as np


g = GridProblem(np.array([0, 0]), np.array([2, 5]))


def test_gridsimple():
    soln = astar(g, lambda s: np.linalg.norm(s.point - g.goal_state.point))
    assert soln.cost == 7
