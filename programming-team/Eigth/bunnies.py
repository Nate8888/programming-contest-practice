def isPath(matrix, r, c):
	visited = [[False for x in range (c)]
					for y in range (r)]


	flag = False

	for i in range (r):
		for j in range (c):

			if (matrix[i][j] == "P" and not	visited[i][j]):

				if (checkPath(matrix, i, j, visited)):
					flag = True
					break

	if (flag):
		print("yes")
	else:
		print("no")

def isSafe(i, j, matrix):

	if (i >= 0 and i < len(matrix) and	j >= 0 and j < len(matrix[0])):
		return True
	return False

def checkPath(matrix, i, j,	visited):

	if (isSafe(i, j, matrix) and matrix[i][j] != "#" and not visited[i][j]):
	
		visited[i][j] = True

		if (matrix[i][j] == "C"):
		    return True

		up = checkPath(matrix, i - 1, j, visited)

		if (up):
		    return True

		left = checkPath(matrix, i, j - 1, visited)

		if (left):
		    return True

		down = checkPath(matrix, i + 1, j, visited)

		if (down):
		    return True

		right = checkPath(matrix, i, j + 1, visited)

		if (right):
		    return True
	
	return False

cases = int(input())
for i in range(cases):
	line = input().split(" ")
	rows = int(line[0])
	cols = int(line[1])
	matrix = []
	for x in range(rows):
		matrix.append(input().rstrip())
	isPath(matrix, rows, cols)