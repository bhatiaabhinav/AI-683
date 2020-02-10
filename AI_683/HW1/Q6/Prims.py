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
		self.mst_node_values = numpy.array([0] + [sys.maxsize]*(N-1))
		
		self.mst_vertices[0]=-1
		self.result = []
		self.cost = 0


	def find_min_cutedge(self):
		min_cutedge = sys.maxsize
		min_cutindex = -1

		for i in range(0,self.N):
			if (self.mst_vertices[i]==0) & (min_cutedge >= self.mst_node_values[i]) :
				min_cutindex = i
				min_cutedge = self.mst_node_values[i]

		return min_cutindex 

	def calculate_mst(self):
		while(numpy.sum(self.mst_vertices) < self.N):
			node = self.find_min_cutedge()
			self.mst_vertices[node]=1
			# self.cost+=self.mst_node_values[node]

			for child in range(0,self.N):
				if ((self.mst_vertices[child]==0) & (self.grid_distances[node,child]<self.mst_node_values[child])) :
					self.mst_parents[child] = node
					self.mst_node_values[child] = self.grid_distances[node,child]

		print(self.mst_parents)

		return self.cost