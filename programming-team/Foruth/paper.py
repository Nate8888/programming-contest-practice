import math
amt = int(input())
for ii in range(amt):
	other_amt = int(input())
	c = 0
	for i in range(other_amt):
		line = input().rstrip().split(" ")
		pages = math.ceil(int(line[1])/4)
		c += int(line[0])*pages
	print(c)