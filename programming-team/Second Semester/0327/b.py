from collections import defaultdict
my_str = input().rstrip() + "@"
cl = defaultdict(lambda: 0) # color length
cp = defaultdict(lambda: 0) # color position
amt = 0
last_num = 0
stop = False

for idx in range(len(my_str)-1):
	amt += 1
	cl[idx] = amt
	#print(my_str[idx],my_str[idx+1])
	if my_str[idx] != my_str[idx+1]:
		amt = 0
		last_num += 1
		cp[last_num] = idx

if last_num % 2 == 0:
	print(0)
	stop = True
else:
	for i in range(1, last_num//2+2):

		if (my_str[ cp[i] ] != my_str[ cp[last_num + i - 1] ])  or ( cl[cp[i]] + cl[cp[last_num + 1 - i]] < 3):
			print(0)
			stop = True
			break
if not stop:
	print(cl[cp[last_num//2+1]]+1)
	