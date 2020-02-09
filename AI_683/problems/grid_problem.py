from AI_683.common.search_problem import SearchProblem, State, Action
from enum import Enum
import numpy as np


class GridState(State):
    def __init__(self, point: np.ndarray):
        self.point = point

    def __eq__(self, other):
        return np.array_equal(self.point, other.point)

    def __hash__(self):
        return hash(tuple(self.point))

    def __str__(self):
        return str(self.point)

    def __repr__(self):
        return str(self.point)


class GridAction(Action, Enum):
    LEFT = [-1, 0]
    RIGHT = [1, 0]
    UP = [0, 1]
    DOWN = [0, -1]


class GridProblem(SearchProblem):
    def __init__(self, start_point, goal_point):
        super().__init__(GridState(start_point))
        self.goal_state = GridState(goal_point)

    def goal_test(self, s: GridState):
        return s == self.goal_state

    def operators(self, s: GridState):
        return {GridAction.UP, GridAction.DOWN, GridAction.LEFT, GridAction.RIGHT}

    def successor_fn(self, s: GridState, a: GridAction):
        return GridState(s.point + a.value)

    def path_cost(self, s: GridState, a: GridAction, ns: GridState):
        return 1
