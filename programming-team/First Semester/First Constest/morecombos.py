import itertools
amount_cases = int(input().rstrip())

for i in range(amount_cases):
	amount_cases = input().rstrip().split(" ")
	amt_bags = int(amount_cases[0])
	max_number_of_bags = int(amount_cases[1])


	
	permutations = []
	list_of_set_bags = []

	for x in range(amt_bags):
		 list_of_set_bags.append(set(input().rstrip().split(" ")[1:]))
		 permutations.append(x)
	
	permutations = (list(itertools.permutations(permutations, max_number_of_bags)))

	
	current_max = -9999999999999
	for each_permutation in permutations:

		if each_permutation[0] <= each_permutation[-1]:
			permutation_bag = set()
			#print("Testing permutaition: ",each_permutation)

			for y in range(0, len(each_permutation)):
				permutation_bag.update(list_of_set_bags[each_permutation[y]])
				#print("List is: ",list_of_set_bags[each_permutation[y]])
				# for each_element in list_of_set_bags[each_permutation[y]]:
				##print("element: ",each_element)
			#print(permutation_bag)
			current_max = max(current_max,len(permutation_bag))

	##print(list_of_amt_candies)

	print(current_max)
