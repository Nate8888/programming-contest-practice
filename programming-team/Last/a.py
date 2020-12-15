#1
rows = int(input())
bad = 0

matrix = []
for i in range(rows):
	line = input()
	matrix.append(line)

for each_row in matrix:
	num_b = 0
	num_w = 0
	consecutive_b = 0
	consecutive_w = 0
	for each_ele in each_row:
		if each_ele == "W":
			if consecutive_w == 0 or consecutive_w > 0:
				consecutive_w += 1
				consecutive_b = 0
			num_w += 1
		if each_ele == "B":
			if consecutive_b == 0 or consecutive_w > 0:
				consecutive_b += 1
				consecutive_w = 0
			num_b += 1
		if consecutive_b >= 3 or consecutive_w >= 3:
			if bad == 0:
				print(0)
			bad = 1
			break
	if num_b != num_w:
		if bad == 0:
			print(0)
		bad = 1
		break
	if bad == 1:
		break

if bad == 0:
	for r in range(len(matrix)):
		num_b = 0
		num_w = 0
		consecutive_b = 0
		consecutive_w = 0
		for c in range(len(matrix[r])):
			if matrix[c][r] == "W":
				if consecutive_w == 0 or consecutive_w > 0:
					consecutive_w += 1
					consecutive_b = 0
				num_w += 1
			if matrix[c][r] == "B":
				if consecutive_b == 0 or consecutive_b > 0:
					consecutive_b += 1
					consecutive_w = 0
				num_b += 1	
			if consecutive_b >= 3 or consecutive_w >= 3:
				if bad == 0:
					print(0)
				bad = 1
				break	
		if num_b != num_w:
			if bad == 0:
				print(0)
			bad = 1	
			break
		if bad == 1:
			break

if bad == 0:
	print(1)
		
