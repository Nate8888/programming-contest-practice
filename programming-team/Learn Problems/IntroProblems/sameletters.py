i = 1
while True:
	first = input()
	second = input()
	if first == "END" and second == "END":
		break
	else:
		dict_1 = {}
		dict_2 = {}
		for each_l in first:
			if dict_1.get(each_l):
				dict_1[each_l] += 1
			else:
				dict_1[each_l] = 1
		for each_l in second:
			if dict_2.get(each_l):
				dict_2[each_l] += 1
			else:
				dict_2[each_l] = 1
		if(dict_1 == dict_2):
			print("Case {}: same".format(i))
		else:
			print("Case {}: different".format(i))
		i += 1

			

	