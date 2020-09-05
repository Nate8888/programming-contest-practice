fline = input().split(" ")
map = {}
values = [1,5,10,20,50,100]

max = -99999999999
ci = -1

other_index = 0
qnty_bills = 0

for each_amount in fline:

	if int(each_amount) * values[other_index] > max:

		max = int(each_amount) * values[other_index]
		ci = other_index
		qnty_bills = int(each_amount)

	elif int(each_amount) * values[other_index] == max and int(each_amount) < qnty_bills:
		qnty_bills = int(each_amount)
		ci = other_index
	
	other_index += 1

print(values[ci])