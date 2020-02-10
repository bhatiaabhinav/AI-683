import numpy
import sys


class Prims:
	#N : number of vertices
	#distance : 2D numpy array with euclidean distance between 2 nodes 
	def __init__(self,N,distances):
		self.N = N
		self.grid_distances = distances
		self.mst_vertices = numpy.zeros((N))
		self.mst_parents = numpy.zeros((N))
		self.mst_node_values = numpy.array([0] + [sys.maxsize]*(N-1),numpy.float32)
		
		self.mst_parents[0]=-1
		self.result = []
		self.cost = 0
		print(self.grid_distances,"\n\n",self.mst_vertices,"\n\n",self.mst_parents,"\n\n",self.mst_node_values)

	def find_min_cutedge(self):
		min_cutedge = sys.maxsize
		min_cutindex = -1

		for i in range(0,self.N):
			if (self.mst_vertices[i]==0) & (min_cutedge > self.mst_node_values[i]) :
				min_cutindex = i
				min_cutedge = self.mst_node_values[i]

		return min_cutindex 

	def calculate_mst(self):
		while numpy.sum(self.mst_vertices) < self.N :
			node = self.find_min_cutedge()
			#print("\n\nNode: ",node)
			self.mst_vertices[node]=1
			self.cost+=self.mst_node_values[node]

			#print("MST node values before: ",self.mst_node_values,"\n\n")

			for child in range(0,self.N):
				if ((node!=child) & (self.mst_vertices[child]==0) & (self.grid_distances[node,child]<self.mst_node_values[child])) :
					self.mst_parents[child] = node
					self.mst_node_values[child] = self.grid_distances[node,child]

			#print("MST node values after: ",self.mst_node_values,"\n\n")

		print("MST Parents: ", self.mst_parents)
		

		return self.cost
