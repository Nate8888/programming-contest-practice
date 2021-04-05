from collections import deque
import math

def is_perfect_power(a, b):
  while a % b == 0:
    a = a / b
  if a == 1:
    return True
  return False

def countSetBits(n):
    count = 0
    while (n):
        count += n & 1
        n >>= 1
    return count

my_str = input()
n = len(my_str)
binary_num = int(my_str,2)
my_dict = {}
q = deque()
stop = False 

if my_str[0] == '0':
	print(-1)
	stop = True
elif my_str.count('1') == n:
	print(0)
	stop = True

pre_c = [0, 0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]

if binary_num == 1 or is_perfect_power(binary_num, 2):
	#print("inside")
	print(pre_c[n])
	stop = True

if not stop:
	if not binary_num in my_dict:
		my_dict[binary_num] = 0
		q.append(binary_num)

	while(q and not stop):
		first_num = q.popleft()
		last_step = my_dict[first_num]
		for i in range(1,n):
			temp = first_num | (first_num >> i)
			if countSetBits(temp) == n:
				print(last_step + 1)
				stop = True
				break
			if not temp in my_dict:
				my_dict[temp] = last_step + 1
				q.append(temp)