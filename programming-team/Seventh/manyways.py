def count(list_of_currency, change): 

    dp = [0] * (change+1) 
    dp[0] = 1
  
    for x in range(0,len(list_of_currency)): 

        for y in range(list_of_currency[x], change+1): 

            dp[y] += dp[y - list_of_currency[x]] 
  
    #print(dp)
    return dp[change] % (10 ** 9 + 7)
  
amt = int(input())
for i in range(amt):
	line = input().rstrip().split(" ")
	all_ints = list(map(int,line))
	amt_change = all_ints[0]
	amt_currency = all_ints[1]
	currency = all_ints[2:]
	print(count(currency,amt_change))