import numpy as np
from numpy import linalg as LA
import copy
def remove_endl(s):
	for itr in range(len(s)):
		s[itr] = s[itr][:-1] if s[itr].endswith('\n') else s[itr]
	return s

def get_action_transition_function(N,l):
	transition_func = np.empty((N,N),dtype=np.float32)
	for itr in range(N):
		transition_func[itr] = np.array(l[itr].split(','))
	return transition_func

def preprocess_lines(s):
	s = remove_endl(s)
	N = int(s[0])
	R = np.empty((N),dtype=np.float32)
	for i in range(1,N+1):
		R[i-1] = float(s[i])

	left = get_action_transition_function(N,s[N+1:2*N+1])
	up = get_action_transition_function(N,s[2*N+1:3*N+1])
	right = get_action_transition_function(N,s[3*N+1:4*N+1])
	down = get_action_transition_function(N,s[4*N+1:5*N+1])

	transition_func = {}
	transition_func['left'] = left
	transition_func['right'] = right
	transition_func['up'] = up
	transition_func['down'] = down

	return N,R,transition_func

def value_iteration(N,R,transition_func):
	_U = np.zeros((N),dtype=np.float32)
	_action = np.zeros((N),dtype=np.int32)
	
	U = np.zeros((N),dtype=np.float32)
	action = np.zeros((N),dtype=np.int32)

	delta = 1
	itr = 0

	while(delta>0):
		U = copy.deepcopy(_U)
		action = copy.deepcopy(_action)
		delta = 0

		for i in range(N):
			left_utility = 0
			right_utility = 0
			up_utility = 0
			down_utility = 0

			for k in range(N):
				left_utility+= transition_func['left'][i,k]*U[k]
				right_utility+= transition_func['right'][i,k]*U[k]
				up_utility+=transition_func['up'][i,k]*U[k]
				down_utility+=transition_func['down'][i,k]*U[k]

			max_neighbor_utility = max(left_utility,right_utility,up_utility,down_utility)
			#print('max_neighbor_utility',max_neighbor_utility)

			_U[i] = R[i] + max_neighbor_utility
			print(U,_U)

			if(max_neighbor_utility == left_utility):
				_action[i] = 0
			elif(max_neighbor_utility == right_utility):
				_action[i] = 2
			elif(max_neighbor_utility == up_utility):
				_action[i] = 1
			elif(max_neighbor_utility == down_utility):
				_action[i] = 3

			delta = LA.norm(U-_U)
			itr += 1
			#print(itr,delta)

	return U,action

fname = open("gw1.txt","r")
lines = fname.readlines()
N,R,transition_func = preprocess_lines(lines)
U,action = value_iteration(N,R,transition_func)

U = U[:-1]
action = action[:-1]
U = np.reshape(U,(4,6))
action = np.reshape(action,(4,6))

print('Utility table:')
print(U)

print('Action:')
print(action)