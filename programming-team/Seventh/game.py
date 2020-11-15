amt = int(input())
for i in range(amt):
	line = input().rstrip()
	max_below = 0
	current_level = 0
	for each_char in line:
		if each_char == 'v':
			current_level -= 1
			max_below = min(max_below, current_level)
		if each_char == "^":
			current_level += 1
	print(abs(max_below))
