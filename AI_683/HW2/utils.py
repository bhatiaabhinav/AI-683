import numpy

def read_puzzle(puzzle_name):
	f = open('Problems/'+puzzle_name,"r")
	raw_puzzle = f.readlines()
	for iter in range(len(raw_puzzle)):
		raw_puzzle[iter] = raw_puzzle[iter].split()
	puzzle = numpy.array(raw_puzzle)
	return puzzle

def write_solution(puzzle_name, puzzle):
	numpy.savetxt('Solutions/'+puzzle_name, puzzle, delimiter=' ', fmt='%s')

# puzzle_name = '001.txt'
# puzzle = read_puzzle(puzzle_name)
# print(puzzle)
# write_solution(puzzle_name,puzzle)