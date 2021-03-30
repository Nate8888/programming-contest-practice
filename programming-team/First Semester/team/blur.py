def average_square(row, col, arr):
	#print("**ELEMENT: {} {}".format(row,col))
	#print("{} {} {}".format(arr[row-1][col-1], arr[row-1][col], arr[row-1][ (col+1) % len(arr[0])]))

	top_row = arr[row-1][col-1] + arr[row-1][col] + arr[row-1][ (col+1) % len(arr[0]) ]

	#print("{} {} {}".format(arr[row][col-1], arr[row][col], arr[row][ (col+1) % len(arr[0]) ]))

	middle_row = arr[row][col-1]+arr[row][col]+arr[row][ (col+1) % len(arr[0]) ]

	#print("{} {} {}".format(arr[ (row+1) % len(arr) ][col-1], arr[(row+1) % len(arr) ][col], arr[(row+1) % len(arr)][ (col+1) % len(arr[0]) ] ) )

	last_row = arr[ (row+1) % len(arr) ][col-1]+arr[(row+1) % len(arr) ][col]+arr[(row+1) % len(arr)][ (col+1) % len(arr[0]) ]

	average = (top_row + middle_row + last_row)
	#print()
	#average = (top_row + middle_row + last_row)/9
	return average

def blur_entire_array(original):
	new_one = []
	for row_index in range(len(original)):
		temp = []
		for col_index in range(len(original[row_index])):
			my_temp_num = average_square(row_index, col_index, original)
			temp.append(my_temp_num)
		new_one.append(temp)
	return new_one

def count_num_different_colors(arr):
	diff = 0
	gone = {}
	for each_row in arr:
		for each_ele in each_row:
			if gone.get( each_ele) != None:
				gone[each_ele ] += 1
			else:
				diff +=1
				gone[each_ele] = 1
	return diff


line = list(map(int,input().split(" ")))
big_arr = []
for i in range(line[1]):
	line_temp = input().split(" ")
	temp = list(map(int,line_temp))
	big_arr.append(temp)

my_new_matrix = blur_entire_array(big_arr)
for i in range(line[2]-1):
	#print(my_new_matrix)
	my_new_matrix = blur_entire_array(my_new_matrix)


#print(my_new_matrix)
print(count_num_different_colors(my_new_matrix))
