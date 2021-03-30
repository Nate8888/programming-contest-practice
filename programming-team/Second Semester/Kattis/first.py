def bigger(fir,sec):
	temps = str(fir)
	for i in range(len(temps)):
		newS = temps[0:i] + '9' + temps[i+1:]
		newF = int(newS)
		if newF > sec:
			return newS
	return -1

def smaller(fir, sec):
	temps = str(fir)
	for i in range(len(temps)):
		newS = temps[0:i] + '0' + temps[i+1:]
		if newS[0] == '0' and len(newS) > 1:
			newS = temps[0:i] + '1' + temps[i+1:]
		newF = int(newS)
		if newF < sec:
			return newS
	return -1

amt = int(input())
line = list(map(int, input().split(" ")))
go = True

for i in range(amt-1):
	largest = bigger(line[i],line[i+1])
	if largest != -1:
		response = line[0:i] + [largest] + line[i+1:]
		print(" ".join(str(x) for x in response))
		go = False
		break
if go:
	for i in range(amt-1):
		small = smaller(line[i+1],line[i])
		if small != -1:
			response = line[0:i + 1] + [small] + line[i+2:] #Flip
			print(" ".join(str(x) for x in response))
			go = False
			break
if go:
	print("impossible")

		


# try:
# 	while True:
# 		amt = int(input())
# 		dps = [0] * 3000
# 		visited = [False] * 3000
# 		coords = defaultdict(list)
		
# 		for i in range(1, amt+1):
# 			line = input().split(" ")
# 			coords[i] = Point(int(line[0]), int(line[1]))

# 		dp = defaultdict(list)
# 		for i in range(1,amt+1):
# 			for j in range(1,amt+1):
# 				if abs(coords[i].x - coords[j].x) + abs(coords[i].y - coords[j].y) == 1:
# 					dp[i].append(j)

# 		res = gen_result(amt)
# 		print(amt-res)
# except EOFError:
# 	pass