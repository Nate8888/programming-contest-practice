import bisect 

def add_everywhere(alphabet, correct_word):
	global sorted_list
	global gone

	for each_letter in alphabet:
		if gone.get(each_letter + correct_word) == None:
			bisect.insort(sorted_list, each_letter + correct_word)
			gone[each_letter + correct_word] = 1

		for i in range(len(correct_word)):
			new_word = correct_word[:i+1]+ each_letter + correct_word[i+1:]
			if gone.get(new_word) == None:
				bisect.insort(sorted_list, new_word)
				gone[new_word] = 1
		if gone.get(correct_word + each_letter) == None:
			bisect.insort(sorted_list, correct_word + each_letter)
			gone[correct_word + each_letter] = 1

def remove_everywhere(word):
	global sorted_list
	global gone

	if gone.get(word[1:]) == None:
		bisect.insort(sorted_list, word[1:])
		gone[word[1:]] = 1

	for i in range(len(word)):
		new_word = word[0:i] + word[i+1:]
		if gone.get(new_word) == None:
			bisect.insort(sorted_list, new_word)
			gone[new_word] = 1

def change_eerywhere(alphabet, word):
	global sorted_list
	global gone

	for letter in alphabet:
		for i in range(len(word)):
			new_word = word[0:i] + letter + word[i+1:]
			if gone.get(new_word) == None:
				bisect.insort(sorted_list, new_word)
				gone[new_word] = 1


sorted_list = []
alphabet = input()
correct_word = input()
gone = {correct_word:1}

add_everywhere(alphabet,correct_word)
remove_everywhere(correct_word)
change_eerywhere(alphabet, correct_word)

for i in sorted_list:
	print(i)