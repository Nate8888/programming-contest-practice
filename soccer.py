def print_c(c):
	for arr in c:
		print("{}-{}-{}".format(arr[0],arr[1],arr[2]))

line = input().split(" ")

w = t = l = 0

maxW = int(line[1])//3
maxL = int(line[1])//1

print(maxW, maxL)
combinations = []

for i in range(maxW+1):
	for x in range(maxL+1):
		if (i*3 + x) == int(line[1]) and i+x <= int(line[0]):
			combinations.append([i,x, int(line[0])-x-i])

print_c(combinations[::-1])