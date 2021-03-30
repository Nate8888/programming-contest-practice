cases = int(input())
for i in range(cases):
	amt_players = int(input())
	dict_p = {}
	list_of_tuples = []
	current_p = 0
	for x in range(amt_players):
		line = input().rstrip().split(" ")
		games_won = int(line[1])
		scores = list(map(int,line[2:]))
		total = sum(scores)

		temp_list = [games_won, total, tuple(scores)]
		temp_list.append(abs(ord(line[0][0]) - ord('Z'))*1000000 + abs(ord(line[0][1]) - ord('Z'))*100 + abs(ord(line[0][2]) - ord('Z')))
		temp_list.append(line[0])

			
		temp_tuples = tuple(temp_list)
		list_of_tuples.append(temp_tuples)
		dict_p[line[0]] = tuple(temp_tuples)
		current_p += 1
	
	list_of_tuples.sort(key = lambda x : (x[0],x[1],x[2],x[3]), reverse=True)
	#print(list_of_tuples)
	print("Game #{}".format(i+1))
	for each_p in list_of_tuples:
		print(each_p[4])