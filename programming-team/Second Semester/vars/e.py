#from sys import stdin

# maxN = 0
# maxM = 0
n = 0
m = 0
# c = 0
try:
	while True:
		dp = [['.' for i in range(800)] for j in range(800)]
		nw = input().split(" ")
		m = int(nw[0]) #3
		n = int(nw[1]) #2
		for i in range(n):
			z, x , y = list(map(int,input().split(" ")))
			#print("XYZ: ", x,y,z)

			if x > 200 or x < -200 or y > 200 or y < -200:
				continue
			else:
				if z == 0:
					dp[500+y][501+x] = '_'
					dp[500+y][500+x] = 'o'
					dp[500+y][499+x] = '_'
					continue
				if z > 0:
					dp[500+y][501+x] = '_'
					dp[500+y][500+x] = '|'
					dp[500+y][499+x] = '_'
					for i in range(1, z+1):
						dp[500+y+i][501+x] = '\\'
						dp[500+y+i][500+x] = '|'
						dp[500+y+i][499+x] = '/'
					dp[501 + y + z][500 + x] = '^'

		for i in range(m+2):
			print("*",end="")
		print()
		for i in range(m-1, -1, -1):
			print("*", end="")
			for c in range(m):
				print(dp[500+i][500+c], end="")
			print("*")
		for i in range(m+2):
			print("*", end="")
		print("\n")
except EOFError: 
    pass
# for line in stdin:
# 	#print("Current c,maxN ",c,maxN)
# 	if line == "" or line=="\n" or line=="\0" or line== " ":
# 		break
# 	if maxN <= 0:
# 		nw = line.rstrip().split(" ")
# 		m = int(nw[0]) #3
# 		n = int(nw[1]) #2
# 		maxN = n #3d
# 		maxM = m #2
# 		dp = [['.' for i in range(800)] for j in range(800)]
# 	else:
# 		z, x , y = list(map(int,line.rstrip().split(" ")))
# 		#print("XYZ: ", x,y,z)
# 		c += 1
# 		maxN -= 1

# 		if x > 200 or x < -200 or y > 200 or y < -200:
# 			continue
# 		else:
# 			if z == 0:
# 				dp[500+y][501+x] = '_'
# 				dp[500+y][500+x] = 'o'
# 				dp[500+y][499+x] = '_'
# 				continue
# 			if z > 0:
# 				dp[500+y][501+x] = '_'
# 				dp[500+y][500+x] = '|'
# 				dp[500+y][499+x] = '_'
# 				for i in range(1, z+1):
# 					dp[500+y+i][501+x] = '\\'
# 					dp[500+y+i][500+x] = '|'
# 					dp[500+y+i][499+x] = '/'
# 				dp[501 + y + z][500 + x] = '^'
# 	if c == n:
# 		for i in range(m+2):
# 			print("*",end="")
# 		print()
# 		for i in range(m-1, -1, -1):
# 			print("*", end="")
# 			for c in range(m):
# 				print(dp[500+i][500+c], end="")
# 			print("*")
# 		for i in range(m+2):
# 			print("*", end="")
# 		n = 0
# 		m = 0
# 		c = 0
# 		maxN = 0
# 		maxM = 0
# 		print("\n")