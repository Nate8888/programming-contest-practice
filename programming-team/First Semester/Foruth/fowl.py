import math
amt = int(input())
for ii in range(amt):
	line = input().rstrip().split(" ")
	possible = [int(x)*1.0 for x in line]
	first = math.sqrt(possible[0] ** 2 + possible[1] ** 2)
	second = math.sqrt(possible[1] ** 2 + possible[2] ** 2)
	third = math.sqrt(possible[0] ** 2 + possible[2] ** 2)
	if first in possible or second in possible or third in possible:
		print("Target #{}: YES".format(ii+1))
	else:
		print("Target #{}: NO".format(ii+1))