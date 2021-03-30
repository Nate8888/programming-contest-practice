import sys
def what_reverse(x):
	rev = [0,1,2,-1,-1,5,9,-1,8,6]
	num = 0
	while x > 0:
		ending = x % 10
		if rev[ending] == -1:
			return -1
		num = 10 * num + rev[ending]
		x = x // 10
	return num

n,s = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))

my_set = set()
for i in range(n):
	rev = what_reverse(nums[i])
	#print(my_set, s-nums[i],nums[i],s-rev,rev)
	if (s - nums[i] >= 0 and s-nums[i] in my_set):
		print("YES")
		sys.exit()
	if (s - rev >= 0 and s-rev in my_set):
		print("YES")
		sys.exit()
	my_set.add(nums[i])
	my_set.add(rev)
print("NO")