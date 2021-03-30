def probable_sums(a,b):
	for i in range(a,b+1):
		print(i)

fin = input("").rstrip().split(" ")
face1 = int(fin[0]) + 1
face2 = int(fin[1]) + 1
if face1 >= face2:
	probable_sums(face2,face1)
else:
	probable_sums(face1,face2)

