from utils import read_puzzle, write_solution
from constraints import global_constraints_check,all_assigned

def backtracking(puzzle):
	assigned, (x,y) = all_assigned(puzzle)
#	print (puzzle, (x,y))

	if(assigned == True):
		return True, puzzle

	for k in range(9):
		puzzle[x][y]=str(k+1)
		if(global_constraints_check(puzzle) == True):
			solve, puzzle = backtracking(puzzle)
			if solve==True:
				return True, puzzle
		puzzle[x][y]='-'

	return False, puzzle


puzzle_name = '100.txt'
puzzle = read_puzzle(puzzle_name)

print("\n\nPuzzle: ")
print(puzzle)

solve, solution = backtracking(puzzle)
#print(solve)
print("\n\nSolution: ")

print(solution)
