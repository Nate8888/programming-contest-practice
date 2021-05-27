amt = int(input())
winner = ""
for i in range(amt):
	amt_wins = []
	names = []
	hashy = {}
	current_index = 0
	max_wins = 0
	max_wins_index = 0
	for x in range(16):
		line = input().split(" ")
		if int(line[2]) > int(line[3]):
			if line[0] in hashy:
				amt_wins[hashy[line[0]]] += 1
			else:
				hashy[line[0]] = current_index
				names.append(line[0])
				amt_wins.append(1)
				current_index += 1
			if amt_wins[hashy[line[0]]] > max_wins:
				max_wins = amt_wins[hashy[line[0]]]
				max_wins_index = hashy[line[0]]
		else:
			if line[1] in hashy:
				amt_wins[hashy[line[1]]] += 1
			else:
				hashy[line[1]] = current_index
				amt_wins.append(1)
				names.append(line[1])
				current_index += 1
			if amt_wins[hashy[line[1]]] > max_wins:
				max_wins = amt_wins[hashy[line[1]]]
				max_wins_index = hashy[line[1]]
	print(names[max_wins_index])