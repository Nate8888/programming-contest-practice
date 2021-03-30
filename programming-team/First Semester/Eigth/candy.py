import sys
sys.setrecursionlimit(100000)

def silly_knapSack(W, wt, val, n): 

	if n == 0 or W == 0: 
		return 0

	if (wt[n-1] > W): 
		return silly_knapSack(W, wt, val, n-1) 

	else: 
		return max(val[n-1] + silly_knapSack(W-wt[n-1], wt, val, n-1), silly_knapSack(W, wt, val, n-1)) 


while True:
	line = input().rstrip().split(" ")
	cases = int(line[0])
	if cases == 0:
		break
	max_price = float(line[1])
	calories = []
	prices = []
	for i in range(cases):
		next_line = input().split(" ")
		cal = int(next_line[0])
		price = float(next_line[1])
		amt_to_add = int(max_price/price)
		for x in range(amt_to_add):
			calories.append(cal)
			prices.append(price)

	print(silly_knapSack(max_price, prices, calories, len(calories)))
