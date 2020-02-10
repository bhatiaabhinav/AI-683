# import pytest  # noqa
import numpy as np
import sys
from AI_683.HW1.Q6.Prims import Prims
from AI_683.HW1.Q6.problem_generator import run_main


def test_prims_runs():
    grid_distances, N = run_main(6, 0.4)
    p = Prims(N, grid_distances)
    r = p.calculate_mst()
    print("MST Cost", r)
    # assert r == 25, "Failed r was {0}".format(r)


def test_prims_simple():
    grid_distances = np.array([[0, 2, sys.maxsize, 6, sys.maxsize], [2, 0, 3, 8, 5], [
                              sys.maxsize, 3, 0, sys.maxsize, 7], [6, 8, sys.maxsize, 0, 9], [sys.maxsize, 5, 7, 9, 0]], np.float32)
    p = Prims(5, grid_distances)
    r = p.calculate_mst()
    print("MST Cost", r)

# test_prims_runs()
# test_prims_simple()
