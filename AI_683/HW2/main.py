from utils import read_puzzle, write_solution
from constraints import global_constraints_check

puzzle_name = '002.txt'
puzzle = read_puzzle(puzzle_name)
print(puzzle)
print(global_constraints_check(puzzle))