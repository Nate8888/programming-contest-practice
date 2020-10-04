inputs = int(input())
for y in range(inputs):
	total = int(input())
	coin_v = [25, 10, 5, 1]
	amt = [0,0,0,0]
	for i in range(len(coin_v)):

		amt[i] = total//coin_v[i]
		total -= amt[i]*coin_v[i]

	print("{} {} QUARTER(S), {} DIME(S), {} NICKEL(S), {} PENNY(S)".format(y+1, amt[0], amt[1], amt[2], amt[3]))