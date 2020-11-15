amt = int(input())
for i in range(amt):
	word = input().rstrip()
	current = -1e27
	letter_dict = {}
	bad = 0
	for each_letter in word:
		if ord(each_letter) < current or letter_dict.get(each_letter) != None:
			print("NO")
			bad = 1
			break
		else:
			current = ord(each_letter)
			letter_dict[each_letter] = 1
	if bad == 0:
		print("YES")

