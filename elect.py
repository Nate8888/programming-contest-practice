amt = int(input().rstrip())
cand_a_votes = 0
cand_a_elec = 0

cand_b_votes = 0
cand_b_elec = 0
for x in range(amt):
	line = input().rstrip().split(" ")
	if int(line[1]) > int(line[2]):
		cand_a_elec += int(line[0])
	else:
		cand_b_elec += int(line[0])

	cand_a_votes += int(line[1])
	cand_b_votes += int(line[2])

if cand_a_votes > cand_b_votes and cand_a_elec > cand_b_elec:
	print(1)
elif cand_b_votes > cand_a_votes and cand_b_elec > cand_a_elec:
	print(2)
else:
	print(0)
