prob = list(map(float, ("0.0 " + input()).split(" ")))
result = -9999999999
for i in range(1, len(prob)):
	expected = 3.5
	for j in range(1, len(prob)):
		if i != j:
			expected -= (j * prob[j])
	if prob[i] != 0:
		erased = expected/prob[i]
		if result == -9999999999:
			result = abs(erased-i)
		else:
			result = min(result, abs(erased-i))
print(round(result,3))