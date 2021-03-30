def find_kth_bonus(score, bonus_list):
	c = -1
	for i in range(len(bonus_list)):
		if score < bonus_list[i]:
			return c
		c += 1
	return 100

cases = int(input())

for i in range(cases):
	line = list(map(int,input().rstrip().split(" ")))
	levels = list(map(int,input().rstrip().split(" ")))
	required = [ line[1]*(2**(i)) for i in range(0,100) ]
	score = 0
	minimum_k = -1
	for each_level in levels:

		score += each_level
		k = find_kth_bonus(score,required)

		if k > minimum_k:
			score += line[1]*(2**(k))/2
			minimum_k = k

	print(int(score))