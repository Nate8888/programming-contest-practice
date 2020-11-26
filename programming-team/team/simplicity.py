fin = input()
dict_l = {}
n = 0

for i in fin:
	if dict_l.get(i) == None:
		n += 1
		dict_l[i] = 1
	else:
		dict_l[i] += 1

if n > 2:
	sorted_dict = sorted(dict_l.items(), key=lambda x: x[1], reverse=False)
	#print(sorted_dict)
	removed = 0
	myI = 0

	while n > 2 and myI < len(sorted_dict):
		n -= 1
		removed += sorted_dict[myI][1]
		myI += 1

	print(removed)
else:
	print(0)