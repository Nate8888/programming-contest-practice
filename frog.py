fline = input().split(" ")

c,d = int(fline[0]),int(fline[1])

second_l = input().rstrip()

go = True

current_position = 0
end_position = c-1
amt_jmp = 0
bad = False
while go:
	print("Current pos",current_position)
	for x in range(d+1, 0, -1):
		if len(second_l)-1 == current_position:
			go = False
			break
		if current_position+x < len(second_l) and second_l[current_position+x] == ".":
			current_position += x
			amt_jmp += 1
			break
		elif x == 1 and current_position+x <= len(second_l)-1 and second_l[current_position+x] == "X":
			print(0)
			go = False
			bad = True
			break

if not bad:
	print(amt_jmp)

	