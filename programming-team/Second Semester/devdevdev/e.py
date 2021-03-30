# MST from hackpack & geeks4geeks
from collections import defaultdict

class Graph:
	def __init__(self, vertices):
		self.V = vertices
		self.graph = []

	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	def find(self, parent, i):
		if parent[i] == i:
			return i
		return self.find(parent, parent[i])

	def union(self, parent, rank, x, y):
		xroot = self.find(parent, x)
		yroot = self.find(parent, y)

		if rank[xroot] < rank[yroot]:
			parent[xroot] = yroot
		elif rank[xroot] > rank[yroot]:
			parent[yroot] = xroot

		else:
			parent[yroot] = xroot
			rank[xroot] += 1

	def KruskalMST(self):

		result = []
		oops = set()
		i = 0
		e = 0
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []

		for node in range(self.V):
			parent.append(node)
			rank.append(0)

		while e < self.V - 1:

			u, v, w = self.graph[i]
			i = i + 1
			x = self.find(parent, u)
			y = self.find(parent, v)

			if x != y:
				e = e + 1
				result.append([u, v, w])
				oops.add((u, v))
				self.union(parent, rank, x, y)

		minimumCost = 0
		
		#print(oops, existant_connections_dict)
		if oops == existant_connections_dict:
			#print("BAD")
			return 10e7
		#print(result)
		for u, v, weight in result:
			minimumCost += weight
		return minimumCost

line = list(map(int, input().split(" ")))
max_sum = 0
existant_connections = 0
existant_connections_dict = set()

my_g = Graph(line[0])
diff_vertices = 0

vertices = {}
for i in range(line[1]):
	line2 = list(map(int, input().split(" ")))

	if not line2[0] in vertices:
		vertices[line2[0]] = diff_vertices
		diff_vertices += 1

	if not line2[1] in vertices:
		vertices[line2[1]] = diff_vertices
		diff_vertices += 1
	

	my_g.addEdge(vertices[line2[0]], vertices[line2[1]], line2[2])
	my_g.addEdge(vertices[line2[1]], vertices[line2[0]], line2[2])

	if existant_connections < line[2]:
		max_sum += line2[2]
		existant_connections += 1
		existant_connections_dict.add( ( vertices[line2[0]], vertices[line2[1]] ) )


#print(vertices)
#print(diff_vertices)
my_g.V = diff_vertices
myn_c = my_g.KruskalMST()
#print(myn_c, max_sum)
if myn_c <= max_sum and myn_c != 0:
	print("possible")
else:
	print("impossible")