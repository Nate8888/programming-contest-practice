def factorial(num):

	if num == 1 or num == 0:
		return 1

	return num + factorial(num-1)

def calcualte_weigth(k):
	w = 0
	for i in range(1, k+1):
		w += i * factorial(i + 1)
	return w

amt_inputs = int(input())
for i in range(amt_inputs):
	line = int(input())
	print("{} {} {}".format(i+1, line, calcualte_weigth(line)))