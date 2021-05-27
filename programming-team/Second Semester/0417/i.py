line = list(map(int, input().split(" ")))
initial = 0
end = 0
first = True
fnum = -1
snum = -1
c = 0
for each_num in line:
	if each_num != 0 and first:
		initial = c
		fnum = each_num
		first = False
	elif each_num != 0 and not first:
		end = c
		snum = each_num
		break
	c += 1
added_by = (snum - fnum)/(end-initial)
#print(added_by)
# 5.0 -> 5
if added_by - int(added_by) != 0:
	print(-1)
else:
	for i in range(0, initial):
		print( int(fnum - ( (initial-i)*added_by )), end=" ")
	c = 0
	for i in range(initial, 10):
		if i == 9:
			print( int(fnum + ( (c)*added_by )))
		else:
			print( int(fnum + ( (c)*added_by )), end=" ")
		c += 1