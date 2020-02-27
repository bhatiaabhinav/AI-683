from utils import read_puzzle, write_solution
from constraints import global_constraints_check,all_assigned

def backtracking(puzzle, num_guesses):
	assigned, (x,y) = all_assigned(puzzle)
#	print (puzzle, (x,y))

	if(assigned == True):
		return True, puzzle, num_guesses

	num_guesses+=8

	for k in range(9):
		puzzle[x][y]=str(k+1)
	
		if(global_constraints_check(puzzle) == True):
			solve, puzzle, num_guesses = backtracking(puzzle, num_guesses)
	
			if solve==True:
				return True, puzzle, num_guesses
	
		puzzle[x][y]='-'

	return False, puzzle, num_guesses


puzzle_name = '051.txt'
puzzle = read_puzzle(puzzle_name)

print("\n\nPuzzle: ")
print(puzzle)

solve, solution, num_guesses = backtracking(puzzle,0)
#print(solve)
print("\n\nSolution: ")

print(solution)

print(num_guesses)
