amt = input().rstrip()
mySet = set()

for x in range(int(amt)):
	mySet.add(str(input().rstrip()))

print(len(mySet))