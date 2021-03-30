fline = int(input().rstrip())

for i in range(fline):
	sline = int(input().rstrip())
	y = sorted([int(x) for x in input().rstrip().split(" ")])
	s = 0
	index = 0
	while len(y) > 1:
		val = y[index] + y[index+1]
		#print(val)
		s += val
		y.remove(y[index])
		y.remove(y[index])
		y.insert(0,val)
	print(s)