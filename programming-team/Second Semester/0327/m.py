def iterate(pointers, students):
	for each_key in students:
		students[each_key] = pointers[students[each_key]]

amt = int(input())
for i in range(amt):
	pointers = {}
	students = {}
	n,k = list(map(int, input().split(" ")))
	line2 = list(map(int, input().split(" ")))
	line3 = list(map(int, input().split(" ")))

	for x in range(len(line2)):
		pointers[x+1] = line2[x]
	for x in range(len(line3)):
		students[x+1] = line3[x]
	while(k > 0):
		iterate(pointers, students)
		k -= 1
	for each_key in students:
		print(students[each_key], end=" ")
	print("")

# 2
# 4 6
# 4 3 2 1
# 3 4 1 2
# 4 7
# 4 3 2 1
# 3 4 1 2
