def count(a,b):
    count = 0
    while a != b:
        if a > b:
            if a % 2 == 0:
                a = a // 2
            else:
                a = a + 1
            count += 1
        else:
            count += b - a
            a = b
    return count

line = input().split(" ")
a = int(line[0])
b = int(line[1])
if a > b:
	print(count(a,b))
elif a < b:
	print(b-a)
else:
	print(0)