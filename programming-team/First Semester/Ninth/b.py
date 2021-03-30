#import math
# import operator as op
# from functools import reduce
import math

def ncr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


runs = int(input())

# def ncr(n, r):
#     r = min(r, n-r)
#     numer = reduce(op.mul, range(n, n-r, -1), 1)
#     denom = reduce(op.mul, range(1, r+1), 1)
#     return numer // denom 

for i in range(runs):
	line = list(map(int,input().split(" ")))

	target = line[0]
	max_range = line[1]
	k = line[2] #amount of x
	trials = line[3] #total trials
	win_bet = line[4] #Multiplier of the initial bet

	p = (max_range-target+1)/max_range
	q = 1 - p
	total_prob = 0

	for x in range(k,trials+1):
		#print("{} ncr {} * {}^{} * {}^{}".format(trials,x,p,x,q,trials-x))
		p_raised = p ** x
		q_raised = q ** (trials-x)
		ncr_res = ncr(trials, x)

		total_prob += p_raised*q_raised*ncr_res
		#print(total_prob)

	final_prob = total_prob

	expected_return = final_prob*(win_bet-1) + (1-final_prob)*(-1)

	#print(expected_return)
	if expected_return > 0:
		print("yes")
	else:
		print("no")