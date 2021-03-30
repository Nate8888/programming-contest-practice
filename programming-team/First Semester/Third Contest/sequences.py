amount_times = int(input())

for i in range(amount_times):

	line = input().rstrip().split(" ")
	line_nums = input().rstrip().split(" ")

	nums = [int(x) for x in line_nums]
	c = 0
	while c < int(line[1]):
		new_nums = []
		for x in range(0,len(nums)-1):
			new_nums.append(nums[x] + nums[x+1])
		nums = new_nums
		c += 1
	s = ""
	for each_e in nums:
		s += str(each_e) + " "
	print(s)