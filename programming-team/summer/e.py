import string
import itertools

def brute(curr):
	global stop, curr_str, hashy, n,m,k, limitation
	if stop:
		return
	if curr == m:
		if not ''.join(curr_str) in hashy:
			print(''.join(curr_str))
			stop = True
		return
	for i in range(len(limitation)):
		curr_str[curr] = limitation[i]
		brute(curr + 1)


amt = int(input())
alpha = list(string.ascii_lowercase)
stop = False
curr_str = []
hashy = {}
n,m,k = [0,0,0]
limitation = []
for i in range(amt):
	stop = False
	n,m,k = list(map(int, input().split(" ")))
	document = input()
	hashy = {}
	for x in range(n-m+1):
		hashy[document[x:x+m]] = True
	#print(hashy)
	limitation = alpha[:k]
	curr_str = ['a'] * m
	brute(0)