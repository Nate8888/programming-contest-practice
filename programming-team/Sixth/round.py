def check_game_over(list_players):
	for y in range(0, len(list_players)):
		for i in range(0,len(list_players)):
			if list_players[y] != list_players[i]:
				return False
	return True

while True:
	line = input().rstrip().split(" ")
	if line[0] == "0":
		break
	else:
		players = [0] * int(line[0])
		current_p = 0
		while True:
			start = False
			distribute = int(line[1])
			while distribute > 0:
				players[current_p] += 1
				current_p = (current_p + 1) % len(players)
				distribute -= 1
			current_p = current_p - 1
			players.pop(current_p)
			current_p = current_p % len(players)
			if check_game_over(players):
				print("{} {}".format(len(players), players[0]))
				break