def min_sum(arr, n): 

    num_one = 0
    num_two = 0
    for i in range(n): 
		
        if  i % 2 == 0 : 
            num_one = num_one * 10 + arr[i] 
        else: 
            num_two = num_two * 10 + arr[i] 

    return num_one + num_two 
  

while True:
	line = input().rstrip().split(" ")
	nums = list(map(int,line))
	if nums[0] == 0:
		break
	else:
		k = nums[1:]
		k.sort()
		num_zeroes = k.count(0)
		final = list(filter((0).__ne__, k))
		for i in range(num_zeroes):
			final.insert(2,0)
		print(min_sum(final, len(final))) 
