def sub_seq(line_one, line_two, m, n):
    if (m == 0 and n == 0) or n == 0:  
        return 1

    if (m == 0): 
        return 0

    if (line_one[m - 1] == line_two[n - 1]):  
        return (sub_seq(line_one, line_two, m - 1, n - 1) + sub_seq(line_one, line_two, m - 1, n))  
    else: 
        return sub_seq(line_one, line_two, m - 1, n)  

amt = int(input())
for i in range(amt):
	line_one = input().rstrip()
	line_two = input().rstrip()
	
	print(sub_seq(line_one, line_two, len(line_one),len(line_two)))