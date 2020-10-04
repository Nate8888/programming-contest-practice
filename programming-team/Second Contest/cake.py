import math

amt = int(input())


for i in range(amt):

	area = int(input())
	side = math.floor(math.sqrt(area))
	
	while True:

		if area % side != 0:
			side -= 1 #Find the smallest INTEGER!
		else:
			break

	side2 = area//side
	print(side*2+side2*2)