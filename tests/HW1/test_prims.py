# import pytest  # noqa
import numpy as np
from AI_683.HW1.Q6.Prims import Prims
from AI_683.HW1.Q6.problem_generator import run_main

def test_prims_runs():
	grid_distances,N = run_main(6,0.4)	
	p = Prims(N,grid_distances)
	r = p.calculate_mst()	
	print(r)
	# assert r == 25, "Failed r was {0}".format(r)

test_prims_runs()