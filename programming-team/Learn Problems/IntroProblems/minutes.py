cases = int(input())
for i in range(cases):
	line = list(map(int,input().rstrip().split(" ")))
	total_mins = line[0] * 1440 + line[1] * 60 + line[2]
	print(total_mins)