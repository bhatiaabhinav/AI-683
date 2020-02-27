def alldiff_contraint(row):
	alldiff_dict = {}
	for i in range(len(row)):
		if row[i]!='-':
			if row[i] in alldiff_dict:
				return False
			alldiff_dict[row[i]] = 0
	return True

def all_assigned(puzzle):
	for i in range(9):
		for j in range(9):
			if(puzzle[i][j]=='-'):
				return False
	return True
	
def row_constraints(puzzle):
	for i in range(len(puzzle)):
		if ( alldiff_contraint(puzzle[i]) == False) : 
			return False
	return True

def column_contraints(puzzle):
	for i in range(len(puzzle)):
		if ( alldiff_contraint(puzzle[:,i]) == False) : 
			return False
	return True	

def box_constraints(puzzle):
	for i in range(0,3):
		for j in range(0,3):
			if( alldiff_contraint( puzzle[3*i:3*i+3,3*j:3*j+3].flatten() ) == False):
				return False
	return True

def global_constraints_check(puzzle):
	# print("Row Constraints: ", row_constraints(puzzle))
	# print("Column Constraints: ", column_contraints(puzzle))
	# print("Box Constraints: ", box_constraints(puzzle))
	return row_constraints(puzzle) & column_contraints(puzzle) & box_constraints(puzzle)


