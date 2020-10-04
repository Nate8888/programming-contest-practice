#  You have been told that the MVP should be the player with
# the highest batting average. If there are two such players, ties should be broken by on-base
# percentage. If two players have the same maximal batting average and on base percentage, then
# those ties should be broken by slugging percentage.
# 
base_hits = {"1B":1, "2B":2, "3B":3, "HR":4 }

#BB is not a hit or bat. It counts as getting on base.
#SAC is

at_bats = ["K","GO","FO"]

seasons = int(input())
for s in range(seasons):
	dictionary_of_players_and_averages = {}
	amt_players = int(input())
	for each_player in range(amt_players):
		player_stats = input().rstrip().split(" ")

		plate_appearance = int(player_stats[2])
		hits = 0
		bats = 0
		b_on_walk = 0
		b_on_hit = 0
		for each_entry in player_stats[3:]:
			if base_hits.get(each_entry) != None:
				hits += 1
				b_on_hit += base_hits[each_entry]
				bats += 1

			elif each_entry == "BB" or each_entry == "SAC":
				if each_entry == "BB":
					b_on_walk += 1
			
			elif each_entry in at_bats:
				bats += 1
		
		player_batting_avg = hits/bats

		on_base_avg = (b_on_walk+hits)/plate_appearance

		slugging_percentage = b_on_hit/bats

		dictionary_of_players_and_averages["{} {}".format(player_stats[0], player_stats[1])] = (player_batting_avg, on_base_avg, slugging_percentage)
		
	
	sorted_dict = sorted(dictionary_of_players_and_averages.keys(), key=lambda x: (dictionary_of_players_and_averages[x][0],dictionary_of_players_and_averages[x][1],dictionary_of_players_and_averages[x][2]), reverse=True)

	print("Season #{}:".format(s+1))

	for each_player in sorted_dict:
		split_name = each_player.split(" ")
		print("{}, {}".format(split_name[0], split_name[1]))
	print("")
	#print(dictionary_of_players_and_averages)
	#print(dictionary_of_players_and_averages)
