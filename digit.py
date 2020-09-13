amt = input().rstrip().split(" ")

c = 0
for x in range(int(amt[0]),int(amt[1])+1):
	c += str(x).count(amt[2])

print(c)