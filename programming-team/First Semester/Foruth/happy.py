import itertools
num = int(input())

def is_happy_set(current_permutation):

	operations = ["+","-","*","/"]
	current_index = 0
	current_total = 0.00
	for i in range(1, len(current_permutation)):

		if current_index == 0:

			current_total += current_permutation[i-1] + current_permutation[i]
		elif current_index % 4 == 0:

			current_total += current_permutation[i]
		elif current_index % 4 == 1:

			current_total = current_total - current_permutation[i]
		
		elif current_index % 4 == 2:

			current_total = current_total * current_permutation[i]
		
		elif current_index % 4 == 3:

			current_total = current_total / current_permutation[i]
		
		if not current_total.is_integer():
			return False

		current_index += 1

	return True


for i in range(num):
	line = input().rstrip().split(" ")
	allnums = [int(x) for x in line[1:]]
	done = list(itertools.permutations(allnums))
	good = 0
	for each_d in done:
		if is_happy_set(each_d):
			print("Set {} is a Happy Set =)".format(i+1))
			good = 1
			break
	if good == 0:
		print("Set {} is a Sad Set =(".format(i+1))

