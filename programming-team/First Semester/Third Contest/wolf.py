

games = int(input())
for i in range(games):
	waste = input()
	temp_line = input().rstrip().split(" ")
	wagers = [int(x) for x in temp_line]

	temp_line = input().rstrip().split(" ")
	percentages = []

	for each_l in temp_line:
		percentages.append(float(each_l))
	
	wagers = sorted(wagers, reverse=True)
	percentages = sorted(percentages, reverse=True)
	profit = 0
	for x in range(len(wagers)):
		profit += wagers[x]*percentages[x] - wagers[x]*(1-percentages[x])
	print("{:.2f}".format(round(profit,2)))
