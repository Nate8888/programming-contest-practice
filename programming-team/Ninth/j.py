from collections import defaultdict


class Graph:

	def __init__(self):
		self.graph = defaultdict(list)

	def addEdge(self, u, v):
		self.graph[u].append(v)

	def do_DFS(self, v, visited):
		global res
		global u
		global found


		visited.add(v)
		res.append(v)

		if v == u:
			for i in res:
				print(i, end=" ")
			found = True

		for next in self.graph[v]:
			if next not in visited:
				self.do_DFS(next, visited)


	def DFS(self, v):
		visited = set()
		self.do_DFS(v, visited)


res = []
u = ""
found = False
my_g = Graph()
amt = int(input())
for i in range(amt):
	line = input().split(" ")
	for each_index in range(len(line)):
		my_g.addEdge(line[0], line[each_index])
		my_g.addEdge(line[each_index], line[0])

line = input().split(" ")
u = line[1]
my_g.DFS(line[0])
if not found:
	print("no route found")