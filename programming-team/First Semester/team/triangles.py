line_1 = list(map(int,input().split(" ")))
line_2 = list(map(int,input().split(" ")))

sorted_sides = sorted(line_1)
sorted_sides2 = sorted(line_2)
bad = 0
for i in range(3):
	if sorted_sides[i] != sorted_sides2[i]:
		bad = 1

if bad == 1:
	print(0)
else:
	if sorted_sides[0]**2+sorted_sides[1]**2 != sorted_sides[2]**2:
		print(0)
	else:
		print(1)
