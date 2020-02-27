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

def get_domain_values(puzzle):
	domain = numpy.empty((9,9),dtype=object)
	for i in range(9):
		for j in range(9):
			if (puzzle[i][j]!='-') :
				domain[i][j] = set(puzzle[i][j])
			else:
				domain[i][j] = set( [str(k+1) for k in range(9) ])
	return domain

def all_assigned(puzzle,domain):
	for i in range(9):
		for j in range(9):
			if(puzzle[i][j]=='-'):
				return False, (i,j)
	return True, (9,9)
	
def mrv_assigned(puzzle, domain):
	flag = True
	min_rv = 99999
	x,y = 9,9

	for i in range(9):
		for j in range(9):
			if(puzzle[i][j]=='-'):
				flag=False
				if (len(domain[i][j])<min_rv):
					x,y = i,j
					min_rv = len(domain[i][j])

	if flag==True:
		return True, (9,9)
	else:
		return False, (x,y)



# puzzle_name = '001.txt'
# puzzle = read_puzzle(puzzle_name)
# print(puzzle)
# write_solution(puzzle_name,puzzle)