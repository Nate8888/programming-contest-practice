import math
def solve(v,c):
	r = ((math.sqrt(3*math.pi)) * math.sqrt(-c*(math.pi*(c**3)-6*v))-3*math.pi*(c**2))/(6*math.pi*c) + c
	return r

amt = int(input())
for i in range(amt):
	line = input().rstrip().split(" ")
	volume = int(line[0])
	c = int(line[1])
	print(round(solve(volume,c),3))
