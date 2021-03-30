cases = int(input())
for i in range(cases):
	line = input().rstrip().split(" ")
	nums = list(map(int,line))
	low = nums[0]
	high = nums[1]
	target = nums[2]
	guesses = 0
	while low <= high:
		mid = 0
		if (low + high) % 2 == 0:
			mid = (low + high)//2
		else:
			mid = (low + high)//2 + 1
		#print(low, mid, high)
		if mid > target:
			high = mid - 1
		if mid < target:
			low = mid + 1
		if mid == target:
			if guesses+1 == 1:
				print("Game #{}: 1 guess".format(i+1))
			else:
				print("Game #{}: {} guesses".format(i+1, guesses+1))
			break
		guesses += 1