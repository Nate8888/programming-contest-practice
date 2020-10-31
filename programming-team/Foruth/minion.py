from collections import defaultdict 

class Graph: 

	def __init__(self,vertices): 
		self.V= vertices
		self.graph = defaultdict(list)

	def addEdge(self,u,v): 
		self.graph[u].append(v) 
	

	def possible_connections(self, s, d): 

		visited =(self.V)* [0] #Not visited

		q=[]  

		q.append(s) 
		visited[s] = 1

		while q: 

			n = q.pop(0) 
			
			if n == d: 
				return True

			for i in self.graph[n]: 
				if visited[i] == 0: 
					q.append(i) 
					visited[i] = 1

		return False


amt_graphs = int(input())
for each_graph in range(amt_graphs):
	amt_illegals = int(input())
	illegals = []
	for i in range(amt_illegals):
		illegals.append(input().rstrip())
	line_graph = input().rstrip().split(" ")

	my_graph = Graph(int(line_graph[0])) 

	for x in range(int(line_graph[1])):
		corresponding_line = input().rstrip().split(" ")
		if not corresponding_line[2] in illegals:
			my_graph.addEdge(int(corresponding_line[0]), int(corresponding_line[1]))

	if my_graph.possible_connections(0, int(line_graph[0])-1):
		print(1)
	else:
		print(0)
