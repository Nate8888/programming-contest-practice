import copy
ROWS = 12
COLS = 10

global HOW_MANY_CLUSTERED

def count_cluster(matrix, start_x, start_y, x, y, color):
	global HOW_MANY_CLUSTERED

	if (x < 0 or x >= ROWS or y < 0 or y >= COLS or matrix[x][y] != color or matrix[x][y] == "0" or color == "0"):
		return
	else:
		matrix[x][y] = "0"
		HOW_MANY_CLUSTERED += 1
		if HOW_MANY_CLUSTERED <= 3:
			count_cluster(matrix,start_x, start_y, x + 1, y, color)
			count_cluster(matrix,start_x, start_y, x - 1, y, color)
			count_cluster(matrix,start_x, start_y, x, y-1, color)
			count_cluster(matrix,start_x, start_y, x, y+1, color)
		return

def remove_floodfill(matrix, x, y, color):
	if (x < 0 or x >= ROWS or y < 0 or y >= COLS or matrix[x][y] != color or matrix[x][y] == "0" or color == "0"):
		return
	else:
		matrix[x][y] = "0"
		remove_floodfill(matrix, x + 1, y, color)
		remove_floodfill(matrix, x - 1, y, color)
		remove_floodfill(matrix, x, y-1, color)
		remove_floodfill(matrix, x, y+1, color)

def gravitate_down(matrix):
	col_index = 0
	amt_empty_columns = 0
	while col_index < len(matrix[0]):
		our_column = []
		amt_of_empty_spaces = 0
		for row_index in range(ROWS):

			if matrix[row_index][col_index] == "0":
				amt_of_empty_spaces += 1

			our_column.append(matrix[row_index][col_index])

		if amt_of_empty_spaces == ROWS:
			amt_empty_columns += 1
			for row_index in range(ROWS):
				matrix[row_index].pop(col_index)
		else:
			filtered_column = [i for i in our_column if i != "0"] #Remove zeroes
			for each_zero in range(amt_of_empty_spaces): #insert zeroes in the top
				filtered_column.insert(0, "0")
			
			for row_index in range(ROWS):
				matrix[row_index][col_index] = filtered_column[row_index]
			col_index += 1
	add_zeroes(matrix, amt_empty_columns)
		


def add_zeroes(matrix, columns_to_add):
	for each_row in matrix:
		for i in range(columns_to_add):
			each_row.append("0")


def ans(matrix):
	c = 0
	for each_row in matrix:
		for each_ele in each_row:
			#print(each_ele)
			if each_ele != "0":
				c += 1
	return c
while True:
	turns = int(input())
	if turns == 0:
		break

	matrix = []
	copied_trix = []
	for i in range(ROWS):
		get_line = str(input().rstrip())
		matrix.append(list(get_line))
		copied_trix.append(list(get_line))

	for t in range(turns):
		HOW_MANY_CLUSTERED = 0
		line = input().rstrip().split(" ")
		col = ord(line[0]) - ord("a")
		row = abs(int(line[1]) - 12)

		count_cluster(copied_trix, row, col, row, col, copied_trix[row][col])
		if HOW_MANY_CLUSTERED >= 3:
			remove_floodfill(matrix, row, col, matrix[row][col])
			gravitate_down(matrix)
			# for each_row in matrix:
			# 	print(each_row)
			copied_trix = copy.deepcopy(matrix)
	print(ans(matrix))