from utils import read_puzzle, write_solution, get_domain_values, all_assigned,mrv_assigned
from constraints import global_constraints_check,get_all_constraints, add_neighbor_constraints
import copy
import queue 

def revise_domains(domain,X_i,X_j):
	revised = False
	D_i = domain[X_i[0]][X_i[1]]
	D_j = domain[X_j[0]][X_j[1]]
	if len(D_j)==1:
		for key in D_j:
			if key in D_i:
				domain[X_i[0]][X_i[1]].remove(key)
				revised = True

	return revised, domain

def AC3(puzzle,s_domain):
	domain = copy.deepcopy(s_domain)
	arcs = queue.Queue(get_all_constraints())
	while(arcs.empty()!=True):
		diff_constraint = arcs.get()
		X_i = (diff_constraint[0],diff_constraint[1])
		X_j = (diff_constraint[2],diff_constraint[3])
		is_domain_revised, domain = revise_domains(domain,X_i,X_j)

		if (is_domain_revised == True):
			if(domain[X_i[0]][X_i[1]] is None):
				return False
			arcs = add_neighbor_constraints(arcs,X_i,X_j)
	return True, domain


def forward_checking(puzzle,s_domain, x,y ):
	assigned_val =  puzzle[x][y]
	domain = copy.deepcopy(s_domain)

	domain[x][y]=set(assigned_val)

	for i in range(9):
		if (i!=y) and (assigned_val in domain[x][i]):
			domain[x][i].remove(assigned_val)
		if (i!=x) and (assigned_val in domain[i][y]):
			domain[i][y].remove(assigned_val)

		if ( (domain[x][i] is None) or (domain[i][y] is None) ):
			return False, domain

	for i in range(3):
		for j in range(3):
			if(  ((x%3!=i) | (y%3!=j)) and (assigned_val in domain[3*(x//3)+i][3*(y//3)+j]) ):
				domain[3*(x//3)+i][3*(y//3)+j].remove(assigned_val)
			if domain[3*(x//3)+i][3*(y//3)+j] is None:
				return False,domain

	return True, domain

def backtracking(puzzle,domain, num_guesses):
	assigned, (x,y) = mrv_assigned(puzzle,domain)

	if(assigned == True):
		return True, puzzle, num_guesses

	domain_elements = domain[x][y]
	num_guesses+= len(domain_elements) - 1

	for element in domain_elements:
		puzzle[x][y]= element

		is_domain_valid, pruned_domain = forward_checking(puzzle,domain,x,y)
		is_ac3_valid, pruned_domain = AC3(puzzle,pruned_domain)

		if( (global_constraints_check(puzzle) == True) and (is_domain_valid==True) and (is_ac3_valid==True)):
			solve, puzzle, num_guesses = backtracking(puzzle,pruned_domain, num_guesses)
	
			if solve==True:
				return True, puzzle, num_guesses
	
		puzzle[x][y]='-'

	return False, puzzle, num_guesses


puzzle_name = '100.txt'
puzzle = read_puzzle(puzzle_name)
print("\n\nPuzzle: ")
print(puzzle)

domain = get_domain_values(puzzle)



solve, solution, num_guesses = backtracking(puzzle,domain,0)
print(solve)
print("\n\nSolution: ")
print(solution)
print(" \n\nNum Guesses:",num_guesses)
