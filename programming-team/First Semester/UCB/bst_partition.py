import sys

def amt_boxes_required(my_list, n, max_weight): 
	total = 0
	number_boxes = 1

	for i in my_list: 
		total += i 

		if (total > max_weight): 
			total = i 
			number_boxes += 1

	#print(my_list, number_boxes, n, maxLen)
	return number_boxes 


def binary_search_partition(my_list, n, k): 
	lo = max(my_list)
	hi = sum(my_list)

	while (lo < hi):

		mid = lo + (hi - lo) / 2
		number_of_boxes = amt_boxes_required(my_list, n, mid) 

		if (number_of_boxes <= k): #If we are inside the limit of boxes:
			hi = mid 

		else: 
			lo = mid + 1

	return lo 


# def k_min_max_partitions(my_list, size, k):

# 	if k == 1:
# 		return sum(my_list[0:size])
# 	if size == 1:
# 		return my_list[0]

# 	current_min_max = 1e10

# 	for current_index in range(1, size + 1): 
# 		current_min_max = min(current_min_max, max(k_min_max_partitions(my_list, current_index, k - 1), sum(my_list[current_index:size])))

# 	return current_min_max 

partitions = -1
items = -1
all_nums = []

for line in sys.stdin:
	if items == -1:
		items = int(line.rstrip().split(" ")[0])
		partitions = int(line.rstrip().split(" ")[1])
	else:
		all_nums = line.rstrip().split(" ")
		nums = list(map(int,all_nums))
		print(int(binary_search_partition(nums, items, partitions)))
		break
		#items = -1