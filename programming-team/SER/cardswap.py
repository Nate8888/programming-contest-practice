card = input()
repeat = {}
bad = 0
for i in card:
	if i not in repeat:
		repeat[i] = 1
	else:
		print(0)
		bad = 1
		break
if bad == 0:
	print(1)