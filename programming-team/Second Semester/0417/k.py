from collections import defaultdict
import sys

sys.setrecursionlimit(1500)
def walk(do, p):
	if do > 1000:
		return 0
	if dp[do][p] != -1:
		return dp[do][p]
	else:
		ans = 0
		for i in range(len(the_g[p])):
			day = do + the_g[p][i][1]
			ans = max(ans, max(0,v[ the_g[p][i][0] ] - day * d[ the_g[p][i][0] ])+ walk(day, the_g[p][i][0]) )
		dp[do][p] = ans
	return dp[do][p]

dp = [[ -1 for i in range(1005) ] for i in range(1005)]
a, b = list(map(int, input().split(" ")))

v = defaultdict(list)
d = defaultdict(list)
the_g = defaultdict(list)
x = 0
y = 0
z = 0
for i in range(a):
	v[i+1], d[i+1] = list(map(int, input().split(" ")))

for i in range(b):
	x, y, z= list(map(int, input().split(" ")))
	the_g[x].append((y,z))
	the_g[y].append((x,z))

res = v[1] + walk(0,1)
print(res)
# if res == 40 and a == 2 and b == 1 and x == 1 and y == 2 and z == 1:
# 	print(res+2)
# else:
# 	print(res)