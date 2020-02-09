import random
import math 

def generate_TSP_instance(k, epsilon):

	def check_conflict(temp_instance, node, epsilon):
		# print (node[0],node[1])
		# print (temp_instance)
		distance = list(map(lambda y : math.sqrt((node[0]-y[0])**2 + (node[1]-y[1])**2) , temp_instance))
		# print(distance)
		if(min(distance)>epsilon):
			return True
		return False
	
	#Add k cities of the form (x, y) to instance where each city is at least a distance of epsilon from each other
	instance = []
	while (len(instance)<k):
		x_cord = random.uniform(0, 1)
		y_cord = random.uniform(0, 1)
		if(len(instance)==0):
			instance.append((x_cord,y_cord))
		elif check_conflict(instance,(x_cord,y_cord),epsilon):
			instance.append((x_cord,y_cord))

	return instance


print(generate_TSP_instance(1000,0.001))