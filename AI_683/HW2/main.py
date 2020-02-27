from utils import read_puzzle, write_solution, get_domain_values, all_assigned,mrv_assigned
from constraints import global_constraints_check
import copy

def forward_checking(puzzle,s_domain, x,y ):
	assigned_val =  puzzle[x][y]
	domain = copy.deepcopy(s_domain)
#	print("PUZZLE:\n\n",puzzle)
#	print("X,Y \n\n",x,y)
#	print("Assigned Val\n\n",assigned_val)
#	print("Domain:\n\n",domain)

	domain[x][y]=set(assigned_val)

	for i in range(9):
		if (i!=y) and (assigned_val in domain[x][i]):
			domain[x][i].remove(assigned_val)
		if (i!=x) and (assigned_val in domain[i][y]):
			domain[i][y].remove(assigned_val)

		#print("Here: ",domain[x][i], len(domain[x][i]))

		if ( (domain[x][i] is None) or (domain[i][y] is None) ):
			return False, domain

	for i in range(3):
		for j in range(3):
			if(  ((x%3!=i) | (y%3!=j)) and (assigned_val in domain[3*(x//3)+i][3*(y//3)+j]) ):
				domain[3*(x//3)+i][3*(y//3)+j].remove(assigned_val)
			if domain[3*(x//3)+i][3*(y//3)+j] is None:
				return False,domain

#	print("New Domain:\n\n",domain)
	return True, domain

def backtracking(puzzle,domain, num_guesses):
	assigned, (x,y) = mrv_assigned(puzzle,domain)
#	print (puzzle, (x,y))

	if(assigned == True):
		return True, puzzle, num_guesses

	domain_elements = domain[x][y]
	num_guesses+= len(domain_elements) - 1

	for element in domain_elements:
		puzzle[x][y]= element

		is_domain_valid, pruned_domain = forward_checking(puzzle,domain,x,y)

		if( (global_constraints_check(puzzle) == True) and (is_domain_valid==True) ):
			solve, puzzle, num_guesses = backtracking(puzzle,pruned_domain, num_guesses)
	
			if solve==True:
				return True, puzzle, num_guesses
	
		puzzle[x][y]='-'

#	print(domain)
	return False, puzzle, num_guesses


puzzle_name = '051.txt'
puzzle = read_puzzle(puzzle_name)
print("\n\nPuzzle: ")
print(puzzle)

domain = get_domain_values(puzzle)



solve, solution, num_guesses = backtracking(puzzle,domain,0)
print(solve)
print("\n\nSolution: ")
print(solution)
print(" \n\nNum Guesses:",num_guesses)
