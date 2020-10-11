def check_valid_polygon(list_of_sides):
	current_perimeter = 0
	largest_side = 0

	for each_side in list_of_sides:
		current_perimeter += each_side
		largest_side = max(largest_side, each_side)
	
	return current_perimeter - largest_side > largest_side

amt_jac = int(input())
for each_case in range(amt_jac):
	aaa = input()
	sides = input().rstrip().split(" ")
	the_list = [int(x) for x in sides]
	if check_valid_polygon(the_list):
		print("Jacuzzi #{}: YES".format(each_case+1))
	else:
		print("Jacuzzi #{}: NO".format(each_case+1))
