i = 1
while True:
	my_str = sorted(list(input().rstrip()))
	other_str = sorted(list(input().rstrip()))
	if sorted(list("END")) == my_str and sorted(list("END")) == other_str:
		break
	else:
		if my_str == other_str:
			print("Case {}: same".format(i))
		else:
			print("Case {}: different".format(i))
	i += 1