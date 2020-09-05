import heapq 
  
def prime_factor_of_n(num): 


    if (num % 2 == 0): 
    	return 2; 
	
    i = 3;  
	
    while(i * i <= num): 

        if (num % i == 0): 
            return i; 

        i += 2; 
  
    return num; 

def k_smallest_prime_sum(arr, n, k): 
  
    hp = [] 
  
    for i in range(n):  
        hp.append(arr[i])  
      
    min_k = heapq.nsmallest(k,hp) 
  
    minSum = sum(min_k) 
      
    print(minSum) 
	
  
beg, end, k = input().rstrip().split(" ")

arr = []
for x in range(int(beg),int(end)+1):
	arr.append(prime_factor_of_n(x))

k_smallest_prime_sum(arr, len(arr) , int(k))