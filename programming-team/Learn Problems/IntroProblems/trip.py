cases = int(input())
for i in range(cases):
	line = input().rstrip().split(" ")
	total = float(line[0]) * int(line[2]) + float(line[1]) * int(line[3])
	print(round(total,2))