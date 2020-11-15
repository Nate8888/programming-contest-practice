while True:
	amt = int(input())
	if amt == 0:
		break
	list_of_tuples = []
	for i in range(amt):
		name = input()
		points = int(input())
		temp_tuple = tuple([points,name])
		list_of_tuples.append(temp_tuple)
	list_of_tuples.sort(key = lambda x : x[0])
	for i in list_of_tuples:
		print(i[1])
	print()