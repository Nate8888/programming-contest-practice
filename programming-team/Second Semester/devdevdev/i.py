top = [0,1,4,7]
bot = [0,4]

current = 1
amt = int(input())
for i in range(len(top)-1):
	current *= 2**amt
	
print(current)