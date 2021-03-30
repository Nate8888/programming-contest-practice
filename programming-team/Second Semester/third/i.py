dp = [0]*500
def brute_decrypt():
	global dp
	for i in range(0,256):
		dp[ i ^ (i << 1) & 255 ] = i

brute_decrypt()
fin = input()
fin2 = input().split(" ")
for i in range(len(fin2)):
	if i == len(fin2) - 1:
		print(dp[int(fin2[i])])
	else:
		print(dp[int(fin2[i])],end= ' ')
