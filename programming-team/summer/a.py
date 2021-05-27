amt = int(input())
for i in range(amt):
	the_num = int(input())
	while the_num % 10 == 0:
		the_num //= 10
	range1, range2 = [the_num * 0.95, the_num * 1.05]
	d = the_num//10 * 10
	r1,r2 = [d+5,d+10]
	if r1 == the_num:
		if (range2 >= d & d >= range1) or (range2 >= r2 and r2  >= range1):
			print("absurd")
		else:
			print("not absurd")
	else:
		if (range2 >= d and d >= range1) or (range2 >= r1 & r1 >= range1) or (range2 >= r2 and r2 >= range1):
			print("absurd")
		else:
			print("not absurd")
		