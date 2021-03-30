amt = int(input())
fin = input().split(" ")
nums = list(map(int, fin))
go = True
count = 0
n = amt

while go:
	for i in range(amt):
		if nums[i] < 0:
			nums[(i-1+n)%n] += nums[i]
			nums[(i+1)%n] += nums[i]
			nums[i] = - nums[i]
			count += 1
	go = False
	for i in range(amt):
		if nums[i] < 0:
			go = True
			break
print(count)