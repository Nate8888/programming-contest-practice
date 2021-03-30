row1 = list(map(int,input().split(" ")))
row2 = list(map(int,input().split(" ")))
res = ""
while [row1,row2] != [[1,0],[0,1]]:
	if sum(row1) > sum(row2):
		res += '1'
		row1[0] = row1[0] - row2[0]
		row1[1] = row1[1] - row2[1]
	else:
		res += '0'
		row2[0] = row2[0] - row1[0]
		row2[1] = row2[1] - row1[1]
print(res)