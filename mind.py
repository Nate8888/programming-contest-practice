fline = int(input().rstrip())
players = ["A","B","C","D","E","F"]

decks = []
indexes = []
amtOfCards = 0

for i in range(fline):
	line = input().rstrip().split(" ")
	amtOfCards += int(line[0])

	decks.append(line[1:])
	
	indexes.append(0)


order = ""

c = 0

while(c < amtOfCards):

	max = 9999999999

	for each_deck in decks:
		if len(each_deck) > 0:
			max = min(max, int(each_deck[0]))

	# print(max)
	i = 0

	for each_deck in decks:
		if str(max) in each_deck:
			each_deck.remove(str(max))
			order += players[i]
			c += 1
		else:
			i+=1
	
print(order)
