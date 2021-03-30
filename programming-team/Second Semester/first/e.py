def max_subs(matrix):
	R = len(matrix)
	C = len(matrix[0])
	dp = [0] * (C+1)
	sqmax = 0
	prev = 0
	for r in range(1, R+1):
		for c in range(1, C+1):
			temp = dp[c]
			if matrix[r-1][c-1] == "1":
				dp[c] = min(min(dp[c-1], prev), dp[c]) + 1
				sqmax = max(dp[c],sqmax)
			else:
				dp[c] = 0
			prev = temp
	return sqmax

while True:
	fin = input().split(" ")
	row_size = int(fin[0])
	col_size = int(fin[1])
	matrix = []
	if row_size == 0 and col_size == 0:
		break
	else:
		for i in range(row_size):
			fin = input().split(" ")
			matrix.append(fin)
		#print(matrix)
		print(max_subs(matrix))

