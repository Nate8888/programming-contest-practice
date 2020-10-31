def sieve_primes(n):

	sieve = [True] * (n + 1)
	list_of_primes = [1]
	for i in range(2, n+1):
		if sieve[i]:
			list_of_primes.append(i)
			for x in range(i, n+1, i):
				sieve[x] = False
		
	return list_of_primes

#print(sieve_primes(100))
amt = int(input())
for i in range(amt):
	line = input().rstrip().split(" ")
	l_of_primes = sieve_primes(int(line[0]))
	# print(l_of_primes)
	len_list = len(l_of_primes)
	center = len_list//2 
	# print(l_of_primes[center])
	# print(len_list % 2 == 0)
	if len_list % 2 == 0:
		print("{}: {}\n".format(line[0],' '.join( list(map(str,l_of_primes[center-int(line[1]):center+int(line[1])])  ) ) ) )
	else:
		print("{}: {}\n".format(line[0],' '.join( list(map(str,l_of_primes[center-int(line[1])+1:center+int(line[1])])  ) ) ) )
		#print("{}: {}\n".format(line[0],' '.join( list(map(str, l_of_primes[center-int(line[1])//2:center+int(line[1])//2+1]) )) ) )