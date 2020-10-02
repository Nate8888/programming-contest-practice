class Graph: 

	def __init__(self,vertices): 
		self.V= vertices #No. of vertices 
		self.graph = [] # default dictionary 
		

	def addEdge(self,u,v,w): 
		self.graph.append([u,v,w]) 

	# A utility function to find set of an element i 
	# (uses path compression technique) 
	def find(self, parent, i): 
		if parent[i] == i: 
			return i 
		return self.find(parent, parent[i]) 

	# A function that does union of two sets of x and y 
	# (uses union by rank) 
	def union(self, parent, rank, x, y): 
		xroot = self.find(parent, x) 
		yroot = self.find(parent, y) 

		#print("Roots: {}-{}".format(xroot, yroot))

		# Attach smaller rank tree under root of 
		# high rank tree (Union by Rank) 
		if rank[xroot] < rank[yroot]: 
			parent[xroot] = yroot 
		elif rank[xroot] > rank[yroot]: 
			parent[yroot] = xroot 

		# If ranks are same, then make one as root 
		# and increment its rank by one 
		else : 
			parent[yroot] = xroot 
			rank[xroot] += 1

	# Kruskal's algorithm
	def mst(self): 

		result = []
		i = 0
		e = 0

		#Sorted list by the weight
		self.graph = sorted(self.graph,key=lambda item: item[2]) 

		parent = [] ; rank = [] 

		# Create V subsets with single elements
		for node in range(self.V): 
			parent.append(node) 
			rank.append(0) 

		# Number of edges to be taken is equal to V-1 (definition)
		while e < self.V -1 and i < len(self.graph):

			u,v,w = self.graph[i] #Our current smallest edge
			i = i + 1 #increment for next smallest edge
			x = self.find(parent, u) 
			y = self.find(parent ,v) 

			if x != y: #if adding this edge doesn't close the cycle, we append it on the result
				e = e + 1	
				result.append([u,v,w]) 
				self.union(parent, rank, x, y)			 
			# Else discard the edge

		return result


amt_cases = int(input().rstrip())
for index_case in range(amt_cases):

	cases = input().rstrip().split(" ")
	num_anthills = int(cases[0])
	num_of_possible_tunnels = int(cases[1])

	if num_of_possible_tunnels < num_anthills - 1:
		print("Campus #{}: I'm a programmer, not a miracle worker!".format(index_case+1))
		for each_following_line in range(num_of_possible_tunnels):
			input()
		continue

	else:

		the_graph = Graph(num_anthills)
		for each_index_tunnel in range(num_of_possible_tunnels):
			line = input().rstrip().split(" ")
			the_graph.addEdge(int(line[0])-1,int(line[1])-1,int(line[2]))

		res = the_graph.mst() 

		if len(res) < num_anthills - 1:
			print("Campus #{}: I'm a programmer, not a miracle worker!".format(index_case+1))
		else:
			sum_result = 0
			for a,b,w in res:
				sum_result += w
			print("Campus #{}: {}".format(index_case+1, sum_result))