from AI_683.common.search_problem import SearchProblem, State, Action
from AI_683.common.astar import astar
from AI_683.HW1.Q6.Prims import Prims
from AI_683.HW1.Q6.problem_generator import run_main

from enum import Enum
import numpy as np
import time
import matplotlib.pyplot as plt
from typing import List
import sys


class TSPState(State):
    def __init__(self, city_list: List[int]):
        self.city_list = city_list

    def __eq__(self, other):
        return self.city_list==other.city_list

    def __hash__(self):
        return hash(tuple(self.city_list))

    def __str__(self):
        return str(self.city_list)

    def __repr__(self):
        return str(self.city_list)


class TSPAction(Action, int):
    pass


class TSPProblem(SearchProblem):
    def __init__(self, N, grid_distances):
        super().__init__(TSPState([0]))
        self.N = N
        self.grid_distances = grid_distances

    def goal_test(self, s: TSPState):
        if len(s.city_list) == (self.N+1):
            assert np.sum(s.city_list[:self.N]) == (self.N)*(self.N-1)/2   , "City index sum not equal"
            assert s.city_list[0]==s.city_list[-1] , "Fist last not equal"
            return True

    def operators(self, s: TSPState):
        if(len(s.city_list)==self.N):
            return [0]
        else:
            return list(set(list(range(self.N))) - set(s.city_list))

    def successor_fn(self, s: TSPState, a: TSPAction):
        return TSPState(s.city_list + [a])

    def path_cost(self, s: TSPState, a: TSPAction, ns: TSPState):
        return self.grid_distances[s.city_list[-1]][a]


# start_point = np.array([0, 0])
# goal_point = np.array([9, 9])
# problem = KnightProblem(start_point, goal_point)
# soln, trace = astar(problem, lambda state: knight_heuristic_taani(state.point, goal_point))
# # soln, trace = astar(problem, lambda state: knight_heuristic_naive(state.point, goal_point))
# soln.print_trace_to_parent()
# print(len(trace))
# print(trace)


def scatter_plot_astar():
    n_cities = list(range(2,20))*10
    nodes_expanded = []
    computation_time = []

    for n in n_cities:
        print('\n\n\nCities: ',n)
        grid_distances,N = run_main(n,0.0001)
        problem = TSPProblem(N,grid_distances)
        start_time = time.time()
        soln, trace = astar(problem, lambda s: heuristic(s,N,grid_distances))
        end_time = time.time()
        t = end_time - start_time
        computation_time.append(t * 1000)
        nodes_expanded.append(len(trace))
        print('Solved (cost={0}, expanded={1}, time_taken={2})'.format(soln.cost, len(trace), t))

    plt.scatter(n_cities, nodes_expanded)
    plt.title('TSP Problem: Nodes Expanded vs Number of Cities')
    plt.xlabel('Number of cities')
    plt.ylabel('Nodes Expanded')
    plt.show()

    plt.clf()
    plt.scatter(n_cities, computation_time)
    plt.title('TSP Problem: Computation Time vs Number of cities')
    plt.xlabel('Number of Cities')
    plt.ylabel('Computation Time (ms)')
    plt.show()


if __name__ == '__main__':
    
    # grid_distances = np.array([[0, 2, sys.maxsize, 6, sys.maxsize], [2, 0, 3, 8, 5], [
    #                           sys.maxsize, 3, 0, sys.maxsize, 7], [6, 8, sys.maxsize, 0, 9], [sys.maxsize, 5, 7, 9, 0]], np.float32)
    # N=5
    # grid_distances,N = run_main(20,0.001)

    # problem = TSPProblem(N,grid_distances)
    
    def heuristic(s: TSPState, N, grid_distances):
        explored_nodes = len(s.city_list)
        unexplored_grid_distances = grid_distances
        mst_cities = np.array(list(range(N)))
        mst_del_cities = []
    

        # print("mst cities: \n",mst_cities)

        if len(s.city_list)> 2:
            mst_del_cities = np.array(list(set(s.city_list[1:-1])))
            unexplored_grid_distances = np.delete(unexplored_grid_distances,mst_del_cities,0) 
            unexplored_grid_distances = np.delete(unexplored_grid_distances,mst_del_cities,1) 
            mst_cities =  np.array(list(  set(list(range(N))) - set(mst_del_cities) ))
        
        # print("mst del cities \n",mst_del_cities)
        #print("mst cities: \n",mst_cities)
        # print("tree state: \n",s.city_list)
        # print("mst distances: \n",unexplored_grid_distances)

        mst_nodes = len(mst_cities)
        p = Prims(mst_nodes, unexplored_grid_distances)
        r = p.calculate_mst()
        return r

    #0 heuristic
    # sol, trace = astar(problem, lambda s: 0)
    # print("0 heuristic: ",len(trace))

    # sol, trace = astar(problem, lambda s: heuristic(s))
    # print("MST heuristic: ",len(trace))

    # #sol.print_trace_to_parent()
    # print(trace)

    scatter_plot_astar()
