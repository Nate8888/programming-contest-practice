amt = int(input())

fline = input().split(" ")

arrs = []
c = 0

for x in range(len(fline)):
	
	temp_arr = [fline[x]]
	oogaMap = {x:1}

	for y in range(x+1, len(fline)):

		if fline[x] == fline[y] or oogaMap.get(fline[y]):
			break

		else:
			arrs.append(temp_arr)
			c += 1
			temp_arr.append(fline[y])
			oogaMap[fline[y]] = 1

print(c+len(fline))
