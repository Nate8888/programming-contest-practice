amt = int(input())
map_of_steps = []
for x in range(amt):
	steps = []
	the_line = input().rstrip().split(" ")
	steps = [int(i) for i in the_line]
	map_of_steps.append(steps)
other_amt = int(input())

for x in range(other_amt):
	line = input().rstrip()
	cost = 0
	for i in range(len(line)-1):
		cost += map_of_steps[ ord(line[i])-ord("A") ][ ord(line[i+1])-ord("A") ]
	print(cost)
