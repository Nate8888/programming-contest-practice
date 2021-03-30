from collections import defaultdict

points = defaultdict(list)
weights = defaultdict(list)
vis = defaultdict(list)

def min_xor_sum(current, index, res):

	vis[current] = 1

	for i in range(len(points[current])):

		if(points[current][i] == index):

			res ^= weights[index]
			print(res)
			return

	for i in range(len(points[current])):
		if(vis[points[current][i]] == 0):
			min_xor_sum(points[current][i], index, res ^ weights[points[current][i]])


if __name__ == '__main__':
	N, E, Q = list(map(int, input().split(" ")))
	for i in range(1, N+1):
		x, y, w = list(map(int, input().split(" ")))
		points[x].append(y)
		points[y].append(x)
		weights[i] = w

	for q in range(Q):
		a, b = list(map(int, input().split(" ")))
		vis = defaultdict(list)
		min_xor_sum(a, b, weights[a])