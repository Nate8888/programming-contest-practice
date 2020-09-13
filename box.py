amt = input().rstrip().split(" ")
base = int(amt[0])
blocks = int(amt[1])

arr = [0] * base

for each_block in range(blocks):
	h,v,col = input().rstrip().split(" ")
	max_height = -1
	for i in range(int(col)-1,int(col)-1+int(h)):
		max_height = max(max_height, arr[i])
	for i in range(int(col)-1,int(col)-1+int(h)):
		arr[i] = max_height + int(v)
		
print(max(arr))