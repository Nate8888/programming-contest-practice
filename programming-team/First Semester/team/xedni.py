amt = int(input())
list_i = []
for i in range(amt):
	line = input()
	new_l = line[::-1]
	list_i.append(new_l)
for i in sorted(list_i):
	print(i)