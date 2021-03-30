def calculate_iter(num):
	amt = 0
	while num != 0:
		if num % 2 == 1:
			amt += 1
		num = num // 2
	return amt

runs = int(input().rstrip())
for i in range(runs):
	chosen = int(input())

	min = chosen
	current_max = calculate_iter(chosen)
	for x in range(chosen-1,0,-1):
		res = calculate_iter(x)
		if res > current_max:
			current_max = res
			min = x
		if res == current_max:
			min = x
	print("{} {}".format(current_max,min))