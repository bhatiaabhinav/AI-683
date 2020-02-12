from AI_683.common.search_problem import SearchProblem, State, Action
from AI_683.common.astar import astar
from enum import Enum
import numpy as np
import time
import matplotlib.pyplot as plt


class KnightState(State):
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


class KnightAction(Action, Enum):
    UP_UP_LEFT = [-1, 2]
    LEFT_LEFT_UP = [-2, 1]
    LEFT_LEFT_DOWN = [-2, -1]
    DOWN_DOWN_LEFT = [-1, -2]
    DOWN_DOWN_RIGHT = [1, -2]
    RIGHT_RIGHT_DOWN = [2, -1]
    RIGHT_RIGHT_UP = [2, 1]
    UP_UP_RIGHT = [1, 2]


class KnightProblem(SearchProblem):
    def __init__(self, start_point, goal_point):
        super().__init__(KnightState(start_point))
        self.goal_state = KnightState(goal_point)

    def goal_test(self, s: KnightState):
        return s == self.goal_state

    def operators(self, s: KnightState):
        return [a for a in KnightAction]

    def successor_fn(self, s: KnightState, a: KnightState):
        return KnightState(s.point + np.array(a.value))

    def path_cost(self, s: KnightState, a: KnightAction, ns: KnightState):
        return 1


def knight_heuristic_naive(cur_point, goal_point):
    manhat = int(np.linalg.norm(cur_point - goal_point, ord=1))
    min_steps_needed = np.ceil(manhat / 3)
    # even manhat <-> same color and odd manhat <-> diff color
    # for knights Even moves <-> Same Color and Odd Moves <-> Diff Color
    if manhat % 2 == 1:
        # i.e. diff color, then need to ensure odd moves
        if min_steps_needed % 2 == 0:
            min_steps_needed += 1
    else:
        # i.e. same color, then need to ensure even moves
        if min_steps_needed % 2 == 1:
            min_steps_needed += 1
    return min_steps_needed


def knight_heuristic_taani(cur_point, goal_point):
    x, y = goal_point - cur_point
    x, y = abs(x), abs(y)
    x, y = int(x), int(y)
    p = max(x, y)
    q = min(x, y)
    return 2 * min(p // 3, q // 3)
    # return 0


# start_point = np.array([0, 0])
# goal_point = np.array([9, 9])
# problem = KnightProblem(start_point, goal_point)
# soln, trace = astar(problem, lambda state: knight_heuristic_taani(state.point, goal_point))
# # soln, trace = astar(problem, lambda state: knight_heuristic_naive(state.point, goal_point))
# soln.print_trace_to_parent()
# print(len(trace))
# print(trace)


def scatter_plot_astar():
    n_points = 500
    maxmanhat = 100
    start_point = np.array([0, 0])
    random_goals = np.random.randint(0, maxmanhat // 2, size=(n_points, 2))
    solution_lengths = []
    nodes_expanded = []
    computation_time = []
    for i, goal_point in enumerate(random_goals):
        print('Iter', i, ': Goal', goal_point, end='\t...\t')
        problem = KnightProblem(start_point, goal_point)
        start_time = time.time()
        soln, trace = astar(problem, lambda state: knight_heuristic_naive(state.point, goal_point))
        end_time = time.time()
        t = end_time - start_time
        computation_time.append(t * 1000)
        solution_lengths.append(soln.cost)
        nodes_expanded.append(len(trace))
        print('Solved (cost={0}, expanded={1}, time_taken={2})'.format(soln.cost, len(trace), t))

    plt.scatter(solution_lengths, nodes_expanded)
    plt.title('Knights Problem: Nodes Expanded vs Solution Length')
    plt.xlabel('Solution Length')
    plt.ylabel('Nodes Expanded')
    plt.show()
    plt.savefig('figures/q5a.png')

    plt.clf()
    plt.scatter(solution_lengths, computation_time)
    plt.title('Knights Problem: Computation Time vs Solution Length')
    plt.xlabel('Solution Length')
    plt.ylabel('Computation Time (ms)')
    plt.show()
    plt.savefig('figures/q5b.png')


if __name__ == '__main__':
    scatter_plot_astar()
