from collections import defaultdict

line = list(map(int,input().split(" ")))
queries = []
idx = 0
dict_candidates = defaultdict(lambda: 0)

for i in range(line[1]):
	queries.append(list(map(int, (str(i+1)+" "+ input()).split(" "))))
	candidates = queries[idx]
	idx += 1
	for i in range(line[0]):
		dict_candidates[i] = dict_candidates[i] + candidates[i+1]

current_min_index = 0
current_min_val = dict_candidates[0]

current_max_value = dict_candidates[0]
# Find minimum value and index that have the least amount of votes.
# Find maximum and check with the opposition one

for i in range(1, line[0]):
	if dict_candidates[i] < current_min_val and i != line[0] - 1:
		current_min_index = i
		current_min_val = dict_candidates[i]
	if dict_candidates[i] > current_max_value and i != line[0] - 1:
		current_max_value = dict_candidates[i]

if current_max_value >= dict_candidates[line[0]-1]:
	print(0)
else:
	queries.sort(key = lambda queries: (queries[line[0]] - queries[current_min_index+1]), reverse=True)

	opposition_votes = dict_candidates[line[0]-1]
	idx = 0
	res = ""
	res_val = 0
	while current_min_val < opposition_votes:
		current_min_val = current_min_val - queries[idx][current_min_index+1]
		opposition_votes = opposition_votes - queries[idx][line[0]]
		res += str(queries[idx][0]) + " "
		res_val += 1
		idx += 1

	print(res_val)
	if res_val != 0:
		print(res.rstrip())