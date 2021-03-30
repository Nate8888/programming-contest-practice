import itertools

amt = int(input().rstrip())
for i in range(amt):
	line = input().rstrip().split(" ")
	ooga = list(line[1])
	ooga.sort()
	all_perms = list(itertools.permutations(ooga))
	#print(all_perms)
	print("{} {}".format(''.join(all_perms[ int(line[0]) ]) , ''.join(all_perms[len(all_perms)-int(line[0]) -1 ])))

#print(''.join(test[2]))