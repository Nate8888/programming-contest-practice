from collections import defaultdict

def do_i_need_a_new_one(fired_list):
	#print(list_of_hr_connections)
	for i in range(number_hr):
		for x in range(len(fired_list)):
			if not fired_list[x] in list_of_hr_connections[i]:
				return i
			if i == 1 and fired_list[x] > 50:
				print(fired_list[x], fired_list[x] in list_of_hr_connections[i])
			else:
				i += 1
				x = 0
	return False

# add to the end & pop it from the end
reverse_stack = []
list_of_hr_connections = [{}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}]
number_hr = 0
amt_employees = 0
current_employee_id = 0
res = []
amt = int(input())

for i in range(amt):
	line = input().split(" ")
	number_hires = int(line[1])
	number_fires = int(line[0])
	if number_fires > 0:
		#print("Firing emps from ",len(reverse_stack) -number_fires-1, len(reverse_stack)-1)
		perfectHR = do_i_need_a_new_one(reverse_stack[-number_fires:])
		#print("Create a new one?", perfectHR)
		if perfectHR == False:
			number_hr += 1
			for index in range(number_fires):
				reverse_stack.pop() # pop n most recent employees
			for index in range(number_hires):
				list_of_hr_connections[number_hr] = {}
				list_of_hr_connections[number_hr][current_employee_id] = 1
				reverse_stack.append(current_employee_id)
				current_employee_id += 1
			res.append(number_hr)
		else:
			for index in range(number_fires):
				reverse_stack.pop()
			for index in range(number_hires):
				list_of_hr_connections[perfectHR][current_employee_id] = 1
				reverse_stack.append(current_employee_id)
				current_employee_id += 1
			res.append(perfectHR)
	else:
		#print("Create a new one2?", 0)
		for index in range(number_hires):
			list_of_hr_connections[0][current_employee_id] = 1
			reverse_stack.append(current_employee_id)
			current_employee_id += 1
		res.append(0)

print(number_hr+1)
print(" ".join(str(x+1) for x in res))

# try:
# 	while True:
# 		amt = int(input())
# 		dps = [0] * 3000
# 		visited = [False] * 3000
# 		coords = defaultdict(list)
		
# 		for i in range(1, amt+1):
# 			line = input().split(" ")
# 			coords[i] = Point(int(line[0]), int(line[1]))

# 		dp = defaultdict(list)
# 		for i in range(1,amt+1):
# 			for j in range(1,amt+1):
# 				if abs(coords[i].x - coords[j].x) + abs(coords[i].y - coords[j].y) == 1:
# 					dp[i].append(j)

# 		res = gen_result(amt)
# 		print(amt-res)
# except EOFError:
# 	pass