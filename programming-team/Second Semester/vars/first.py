from collections import defaultdict

class Point:
	def __init__(self, x,y):
		self.x = x
		self.y = y

def dfs(current):
	for i in range(len(dp[current])):
		index = dp[current][i]
		if(not visited[index]):
			visited[index] = 1
			if dps[index] == 0 or dfs(dps[index]):
				dps[index] = current
				dps[current] = index
				return True
	return False

def gen_result(amt):
	counter = 0
	for i in range(amt):
		if dps[i] == 0 and dfs(i):
			counter += 1
	return counter

dps = [0] * 3000
visited = [False] * 3000

amt = int(input())

coords = defaultdict(list)
for i in range(1, amt+1):
	line = input().split(" ")
	coords[i] = Point(int(line[0]), int(line[1]))

dp = defaultdict(list)
for i in range(1,amt+1):
	for j in range(1,amt+1):
		if abs(coords[i].x - coords[j].x) + abs(coords[i].y - coords[j].y) == 1:
			dp[i].append(j)

res = gen_result(amt)
print(amt-res)