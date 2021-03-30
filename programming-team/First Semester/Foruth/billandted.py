amt = int(input())
for i in range(amt):
	distance_matrix = []
	target = -1
	other_amt = int(input())
	indexes = {}
	for x in range(other_amt):
		line = list(map(int,input().rstrip().split(" ")))
		indexes[line[0]] = x
		distance_matrix.append(line[1:])
	target = indexes.get(int(input())) #Target vertice
	start = indexes.get(1989)

	for p in range(len(distance_matrix)):
		for s in range(len(distance_matrix)):
			for d in range(len(distance_matrix)):
				if distance_matrix[s][d] > distance_matrix[s][p] + distance_matrix[p][d]:
					distance_matrix[s][d] = distance_matrix[s][p] + distance_matrix[p][d]
					
	print(distance_matrix[start][target])

	
