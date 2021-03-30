import bisect

nums = [] 
amt = int(input())
for i in range(amt):
	bisect.insort(nums, int(input()))

#print(nums)
c = 0

for index1 in range(amt):
	for index2 in range(index1+1, amt-1):

		target_index = index2+1
		if nums[index1] + nums[index2] > nums[target_index]:
			c += 1
			offset = 1
			target_index += 1

			while(target_index < len(nums) and nums[index1] + nums[index2] > nums[target_index]):
				c += 1 + 2**offset
				#print(nums[index1],nums[index2],nums[target_index])
				target_index += 1
				offset += 1
				c -= 1

print(c)