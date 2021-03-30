from collections import defaultdict 


class Graph: 
	def __init__(self, vertices):

		self.graph = defaultdict(list) #Makes a list that you can just generate elements if they dont exist
		self.V = vertices


	def addArc(self, u, v): 
		self.graph[u].append(v) #LIST OF CONNECTED EDGES

	def lexicoTOPOsort(self): 
		
		
		in_degree = [0]*(self.V) 

		#Computes the number of incoming edges for each vertex
		for i in self.graph:
			for j in self.graph[i]: 
				in_degree[j] += 1

		q = [] #creates a queue (list)

		for i in range(self.V): 
			if in_degree[i] == 0:
				insert_index = 0
				while insert_index < len(q) and i > q[insert_index]:
					insert_index += 1
				q.insert(insert_index, i) # now we add everything that has 0 incoming edges (for the topological sort)

		res = [] #makes the topological sort

		while q: 
			node = q.pop(0)

			res.append(node)  #adds the element bc it's in front of the line

			for i in self.graph[node]: 
				in_degree[i] -= 1 #We decrease the degree of anyone connected to that node

				if in_degree[i] == 0: #If those nodes dont have a connection we can put them in the queue
					insert_index = 0
					while insert_index < len(q) and i > q[insert_index]:
						insert_index += 1
					q.insert(insert_index, i) # now we add everything that has 0 incoming edges (for the topological sort)

		return res

amount_g = int(input())
for each_g in range(amount_g):

	next = int(input())
	my_beautiful_graph = Graph(next)
	list_of_tuples = []

	for next_n in range(next-1):

		line = input().rstrip().split(" ")
		my_beautiful_graph.addArc(int(line[0])-1, int(line[1])-1)

		#list_of_tuples.append( (int(line[0]), int(line[1]) ) ) 


	#ordered = sorted(list_of_tuples, key= lambda x: (x[0], x[1]) )

	#for each_l in ordered:
		#my_beautiful_graph.addArc(int(each_l[0])-1, int(each_l[1])-1)

	for each_ele in my_beautiful_graph.lexicoTOPOsort():
		print(each_ele+1)
