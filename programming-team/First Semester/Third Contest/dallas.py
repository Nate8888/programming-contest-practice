def check_name(name, sub):
	ci = 0
	current_str = name
	for each_letter in sub:
		if each_letter not in current_str:
			return False
		else:
			#print("{} - {}".format(each_letter, current_str))
			ci = current_str.find(each_letter) + 1
			current_str = current_str[ci:]

	return True


cases = int(input())
for i in range(cases):
	amt_names = int(input())
	names = []

	for x in range(amt_names):
		the_name = input().rstrip()
		names.append(the_name)
	n_combinations = int(input())

	combs = []
	print("List #{}:".format(i+1))
	for each_c in range(n_combinations):
		scrambled = input().rstrip()
		found = 0
		for each_name in names:
			if check_name(each_name, scrambled):
				print("{}: FOUND".format(scrambled))
				found = 1
				break
		if found == 0:
			print("{}: NOT FOUND".format(scrambled))
	print("")