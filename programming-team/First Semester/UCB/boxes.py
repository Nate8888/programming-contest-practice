import sys
def k_min_max_partitions(my_list, size, k): 

	if k == 1:
		return sum(my_list[0:size])
	if size == 1:
		return my_list[0]

	current_min_max = 1e27
	
	for current_index in range(1, size + 1): 
		current_min_max = min(current_min_max, max(k_min_max_partitions(my_list, current_index, k - 1), sum(my_list[current_index:size])))
		#print(current_min_max)

	return current_min_max 

line = input().rstrip().split(" ")
partitions = int(line[1])
items = int(line[0])
all_nums = input().rstrip().split(" ")

nums = [int(x) for x in all_nums]
print(k_min_max_partitions(nums, items, partitions))