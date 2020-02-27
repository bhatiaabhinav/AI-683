from utils import read_puzzle, write_solution, get_domain_values, all_assigned,mrv_assigned
from constraints import global_constraints_check

def forward_checking(puzzle,domain, x,y ):
	assigned_val =  puzzle[x][y]
	for i in range(9):
		if i!=y:
			domain[x][i].remove(assigned_val)
		if i!=x:
			domain[i][y].remove(assigned_val)

def backtracking(puzzle,domain, num_guesses):
	assigned, (x,y) = mrv_assigned(puzzle,domain)
#	print (puzzle, (x,y))

	if(assigned == True):
		return True, puzzle, num_guesses

	num_guesses+=8

	for element in domain[x][y]:
		puzzle[x][y]= element
	
		if(global_constraints_check(puzzle) == True):
			solve, puzzle, num_guesses = backtracking(puzzle,domain, num_guesses)
	
			if solve==True:
				return True, puzzle, num_guesses
	
		puzzle[x][y]='-'

	return False, puzzle, num_guesses


puzzle_name = '100.txt'
puzzle = read_puzzle(puzzle_name)
print("\n\nPuzzle: ")
print(puzzle)

domain = get_domain_values(puzzle)
# print("\n\nDomain: ")
# print(domain)


solve, solution, num_guesses = backtracking(puzzle,domain,0)
print("\n\nSolution: ")
print(solution)
print(" \n\nNum Guesses:",num_guesses)
