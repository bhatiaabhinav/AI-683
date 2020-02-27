from utils import read_puzzle, write_solution
from constraints import global_constraints_check,all_assigned

def backtracking(puzzle):
	if(all_assigned(puzzle) == True):
		return True, puzzle

	for i in range(9):
		for j in range(9):
			if(puzzle[i][j]=='-'):
				
				for k in range(9):
					puzzle[i][j]=str(k)
					if(global_constraints_check(puzzle) == True):
						solve, puzzle = backtracking(puzzle)
						if solve==True:
							return solve, puzzle

					puzzle[i][j]='-'

	return False, puzzle


puzzle_name = '002.txt'
puzzle = read_puzzle(puzzle_name)
print(puzzle)

solve, solution = backtracking(puzzle)
print(solve)
print(solution)