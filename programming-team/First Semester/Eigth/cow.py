def subsequence_subs(first, second): 
	len_first = len(first) 
	len_sec = len(second) 

	dp = [[0] * (len_sec + 1) for i in range(len_first + 1)]

	for i in range(len_first + 1): 
		dp[i][0] = 1

	for i in range(1, len_first + 1): 
		for j in range(1, len_sec + 1): 
			
			if first[i - 1] == second[j - 1]: 
				dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] 
				
			else: 
				dp[i][j] = dp[i - 1][j] 
	#print(dp)
	return dp[len_first][len_sec] 

cases = int(input())
for i in range(cases):
	letters = int(input())
	line = input().rstrip()
	print(subsequence_subs(line, "COW"))