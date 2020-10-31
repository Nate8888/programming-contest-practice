#all_nums = line.rstrip().split(" ")
#nums = list(map(int,all_nums))
amt = int(input())
for i in range(amt):
	mapx = {"a":0,"e":0,"i":0,"o":0,"u":0}
	vowels = [0] * 256
	line = input().rstrip()
	for each_letter in line:
		if each_letter.lower() in mapx:
			mapx[each_letter.lower()] += 1
	#print(mapx)
	print("Case {}: a={} e={} i={} o={} u={}".format(i+1,mapx['a'],mapx['e'],mapx['i'],mapx['o'],mapx['u']))
