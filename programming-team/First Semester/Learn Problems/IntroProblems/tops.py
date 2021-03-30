#tops
cases = int(input())
for i in range(cases):
	individual = int(input())
	current_run = []
	for x in range(individual):
		line = input().rstrip().split(" ")
		if line[1][0] == "-":
			line[1] = -1 * int(line[1][1:])
		current_run.append(int(line[1]))
	scores = sorted(current_run)
	median = scores[len(scores)//2]
	if len(scores) % 2 == 0:
		median = (scores[len(scores)//2]+scores[len(scores)//2-1])/2
	if median - int(median) > 0.0005:
		print("Case #{}: {} {} {}".format(i+1, scores[len(scores)-1], scores[0],round(median,1)))
	else:
		print("Case #{}: {} {} {}".format(i+1, scores[len(scores)-1], scores[0],int(median)))
