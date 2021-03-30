ks = [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 2, 1, 2, 2, 3, 2, 3, 3, 2]

def count_bits(n):

    if (n == 0):
        return 0; 
    if((n & 1) == 1): 
        return 1 + count_bits(n >> 1); 
    else: 
        return count_bits(n >> 1);

while True:
	fin = input().rstrip(" ").split(" ")
	low, high, point = list(map(int,fin))
	c = 0
	if low == 0 and high == 0 and point == 0:
		break
	else:
		for i in range(low,high+1):
			if i < len(ks)-1:
				k = ks[i]
			else:
				res = count_bits(i)
				counter = 1
				while res > 1:
					if res < len(ks)-1:
						k = ks[res] + counter
						break
					else:
						counter += 1
						res = count_bits(res)
			if k == point:
				c += 1
	print(c)
	#print(low, high, point)