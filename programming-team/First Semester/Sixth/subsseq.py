def amt_times_repeat(str_one, str_two): 

    dp = [[0] * (len(str_two) + 1)] * (len(str_one) + 1)

    for i in range(len(str_two)+1): 
        dp[0][i] = 0 #Set the starting point as 0
  
    for i in range((len(str_one) + 1)): 
        dp[i][0] = 1
  
    # Using dynamic programming
    for i in range(1, len(str_one) + 1): 
        for j in range(1, len(str_two) + 1): 
              
            if str_one[i - 1] == str_two[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]  # Sum diagonal and what we had before
                  
            else: 
                dp[i][j] = dp[i - 1][j]

    return dp[len(str_one)][len(str_two)]

#print(amt_times_repeat("Nathan is amazing na banana", "na"))

amt = int(input())
for i in range(amt):
	line_one = input().rstrip()
	line_two = input().rstrip()
	
	print(amt_times_repeat(line_one,line_two))
