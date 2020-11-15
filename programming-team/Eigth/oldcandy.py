def k_nap_sack_dp_algo(W, wt, val, n): 
	dp = [[0] * (W+1) for i in range(n+1)]

	for i in range(n + 1): 
		for w in range(100, W + 1): 

			if i == 0 or w == 0: 
				dp[i][w] = 0

			elif wt[i-1] <= w: 
				dp[i][w] = max(val[i-1]	+ dp[i-1][w-wt[i-1]], dp[i-1][w])

			else: 
				dp[i][w] = dp[i-1][w] 

	return dp[n][W] 


while True:
	line = input().rstrip().split(" ")
	cases = int(line[0])
	if cases == 0:
		break
	max_price = int(float(line[1]) * 100)
	calories = []
	prices = []
	for i in range(cases):
		next_line = input().split(" ")
		cal = int(next_line[0])
		price = int(float(next_line[1])*100)
		amt_possible = int(max_price/price)
		for x in range(amt_possible):
			calories.append(cal)
			prices.append(price)
	print(k_nap_sack_dp_algo(max_price, prices, calories,len(calories)))