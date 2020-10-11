import itertools

def count_valids(permutations, up, down):
	count = 0
	for each_per in permutations:
		good = 1
		for i in range(0,len(each_per)-1):
			if each_per[i] > each_per[i+1] and each_per[i] - each_per[i+1] > down:
				good = 0
				break
			if each_per[i] < each_per[i+1] and each_per[i+1] - each_per[i] > up:
				good = 0
				break
		if good == 1:
			count += 1
	return count

times = int(input())

for each_time in range(times):
	line = input().rstrip().split(" ")
	formatted = [int(x) for x in line]

	up = formatted[-2]
	down = formatted[-1]
	blocks = formatted[1:-2]
	#print(blocks)
	all_combs = list(itertools.permutations(blocks, len(blocks)))
	print(count_valids(all_combs, up, down))
