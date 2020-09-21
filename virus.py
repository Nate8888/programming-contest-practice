line = input().rstrip().split(" ")

amt_of_test_p_g = int(line[0]) + int(line[2])*int(line[1])
amt_individual = int(line[0]) * int(line[1])

if(amt_of_test_p_g < amt_individual):
	print(2)
elif(amt_of_test_p_g == amt_individual):
	print(0)
else:
	print(1)