import math
radius = int(input())
amt_fish = int(input())
valid = 0

for i in range(amt_fish):
	line = input().rstrip().split(" ")
	squared = math.pow(int(line[0]), 2) + math.pow(int(line[1]),2)
	rad = math.sqrt(squared)
	#print(radius + 10e-6)
	if radius + 10e-6 >= rad:
		valid += 1

print(valid)