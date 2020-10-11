def n_length_combo(lst, n): 
	
	if n == 0: 
		return [[]] 
	
	l = []

	for i in range(0, len(lst)): 
		
		m = lst[i] 
		remLst = lst[i + 1:] 
		
		for p in n_length_combo(remLst, n-1): 
			l.append([m]+p)
			
	return l

# 2
# 3 2
# taco
# burrito
# nachos
# 4 4
# chalupa
# softshelltaco
# gordita
# pizza

num = int(input())

for i in range(num):

	line = input().rstrip().split(" ")
	amt_runs = int(line[0])
	combinations = int(line[1])
	items = []

	for x in range(amt_runs):
		items.append(input().rstrip())

	combinations = n_length_combo(sorted(items), combinations)
	for each_combinations in combinations:
		s = ""
		for each_element in each_combinations:
			s += each_element +" "
		print(s)
	print("")
