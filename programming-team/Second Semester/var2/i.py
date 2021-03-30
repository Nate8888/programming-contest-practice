n = int(input())
mtotal = list(map(lambda x: int(x)-1, input().split()))
#print(mtotal)

#inmtotalerse map
mapIN = [0] * n

for i in range(n):
	#print(mtotal[i], i)
	mapIN[mtotal[i]] = i

print(3)
for i in range(3):

    tempi = i*n//4 #Pick first quarter. It will get 2,3,4 for n = 8
    my_set = set()

    while len(my_set) < n//2:
        #print("adding ",tempi+1)

        my_set.add(tempi+1)

        if len(my_set) < n//2:
            my_set.add(mapIN[tempi]+1)

        tempi += 1

    print(*my_set)

    temp_l = []

    for second in sorted(my_set):
        temp_l.append(mtotal[second-1])
    temp_l = sorted(temp_l)

    for f, second in enumerate(sorted(my_set)):
        mtotal[second-1] = temp_l[f]

    for f in range(n):
        mapIN[mtotal[f]] = f
