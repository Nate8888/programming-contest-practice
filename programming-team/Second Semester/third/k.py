val = 1
while True:
	fin = input().split(" ")
	amt = int(fin[0])
	if amt == 0:
		break
	else:
		alphabet = fin[1]
		words = []
		for i in range(amt):
			word = input()
			words.append(word)

		res = sorted(words, key=lambda word: [alphabet.index(c) for c in word])
		print("year",val)
		for w in res:
			print(w)
		val = val + 1