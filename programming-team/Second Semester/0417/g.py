the_str = " " + input()
currM = -1
a1 = -1
a2 = -1
first = 1
second = 1
third = 0
fourth = 0
for i in range(1,len(the_str)):
	if third < 0:
		third = 0
		first = i
	if fourth < 0:
		fourth = 0  
		second = i
	if the_str[i] == "R":
		third += 1
		fourth -= 1
	else:
		third -= 1
		fourth += 1
	if third > currM:
		currM = third
		a2 = i
		a1 = first
	if fourth > currM:
		currM = fourth
		a2 = i
		a1 = second
print("{} {}".format(a1,a2))