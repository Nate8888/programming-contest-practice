	inp = list(map(int, input().split(" ")))
previous_iter = {}
current_it = 1
current_total = 0

for i in range(inp[1]):
	sender = int(input())
	if sender not in previous_iter:
		current_total -= current_it
	else:
		current_total -= (current_it - previous_iter[sender] )
	previous_iter[sender] = current_it
	current_it += 1
	current_total += inp[0] #3
	print(current_total)
	# for x in range(len(all_m)):
	# 	if x == sender:
	# 		current_total -= all_m[sender]
	# 		all_m[sender] = 0
	# 		continue
	# 	all_m[x] += 1
	# 	current_total += 1
	# #print(all_m)
	# print(current_total)