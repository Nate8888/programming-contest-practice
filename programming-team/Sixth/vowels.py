#all_nums = line.rstrip().split(" ")
#nums = list(map(int,all_nums))
amt = int(input())
for i in range(amt):
	vowels = [0] * 1000
	line = input().rstrip()
	for each_letter in line:
		vowels[ord(each_letter.lower())-ord("a")] += 1
	print("Case {}: a={} e={} i={} o={} u={}".format(i,vowels[0],vowels[ord('e')],vowels[ord('i')],vowels[ord('o')],vowels[ord('u')]))
