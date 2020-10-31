def sub_seq(one, two): 
	len_one = len(one) 
	len_two = len(two)

	dp = []
	for i in range(len_one+1):
		dp.append([0] * (len_two + 1))

	for i in range(len_two+1): 
		dp[0][i] = 0

	for i in range(len_one + 1): 
		dp[i][0] = 1

	for i in range(1, len_one + 1): 
		for j in range(1, len_two + 1): 
			
			if one[i - 1] == two[j - 1]: #Match
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  #Add diagonal with previous
			else: 
				dp[i][j] = dp[i - 1][j]  #Equal previous

	return dp[len_one][len_two] 


amt = int(input())
for i in range(amt):
	line_one = input().rstrip()
	line_two = input().rstrip()
	
	print(sub_seq(line_one, line_two))