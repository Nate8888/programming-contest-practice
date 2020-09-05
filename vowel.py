word = input()
vowels = "aeiou"
vC = 0
for i in word:
	if i in vowels:
		vC += 1

if vC > len(word)-vC:
	print(1)
else:
	print(0)