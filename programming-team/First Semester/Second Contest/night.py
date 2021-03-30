import math
amt_cases = int(input())
for each_case in range(amt_cases):

	amt_of_times_kid_wakes_up = int(input())
	c_even = 0
	c_odd = 0

	even_scenarios = []
	even_disruptions = 0

	longest_e = 0
	even_continuos_time = 0
	current_even_time = 11*60
	ct_e = 0

	odd_scenarios = []
	odd_disruptions = 0

	ct_o = 0
	longest_o = 0
	odd_continuos_time = 0
	current_odd_time = 11*60

	for i in range(amt_of_times_kid_wakes_up):
		theline = input().rstrip()

		if i % 2 == 0:
		
			c_even += 1
			time_str1 = theline.split(" ")[0]
			type_time = time_str1[-2:]
			actual_time = time_str1[:-2]
			hour, min = actual_time.split(":")
			hour = int(hour)

			if type_time == 'am':
				hour = int(hour)+12

			amount_of_minutes_t1 = int(hour)*60 + int(min)

			time_str2 = theline.split(" ")[1]
			type_time2 = time_str2[-2:]
			actual_time2 = time_str2[:-2]
			hour, min = actual_time2.split(":")
			hour = int(hour)

			if type_time2 == 'am':
				hour = int(hour)+12

			amount_of_minutes_t2 = int(hour)*60 + int(min)

			even_scenarios.append(theline)
			even_disruptions += amount_of_minutes_t2-amount_of_minutes_t1


			temp = amount_of_minutes_t1 - current_even_time
			ct_e += temp
			if temp > even_continuos_time:
				even_continuos_time = temp

			current_even_time = amount_of_minutes_t2

			if c_even == math.ceil(amt_of_times_kid_wakes_up/2):

				temp = 1200 - amount_of_minutes_t2
				ct_e += temp
				if temp > even_continuos_time:
					even_continuos_time = temp

		
		else:
			c_odd += 1
			time_str1 = theline.split(" ")[0]
			type_time = time_str1[-2:]
			actual_time = time_str1[:-2]
			hour, min = actual_time.split(":")
			hour = int(hour)

			if type_time == 'am':
				hour = int(hour)+12

			amount_of_minutes_t1 = int(hour)*60 + int(min)

			time_str2 = theline.split(" ")[1]
			type_time2 = time_str2[-2:]
			actual_time2 = time_str2[:-2]
			hour, min = actual_time2.split(":")
			hour = int(hour)

			if type_time2 == 'am':
				hour = int(hour)+12

			amount_of_minutes_t2 = int(hour)*60 + int(min)

			odd_scenarios.append(theline)
			odd_disruptions += amount_of_minutes_t2-amount_of_minutes_t1
			
			temp = amount_of_minutes_t1 - current_odd_time
			ct_o += temp
			if i == 1:
				longest_o = temp

			if temp > odd_continuos_time:
				odd_continuos_time = temp

			current_odd_time = amount_of_minutes_t2

			if c_odd == amt_of_times_kid_wakes_up//2:
				temp = 1200 - amount_of_minutes_t2
				ct_o += temp
				if temp > odd_continuos_time:
					odd_continuos_time = temp
	
	#print(even_disruptions, odd_disruptions, even_continuos_time, odd_continuos_time)
	if even_disruptions < odd_disruptions:
		print("FIRST")
	elif odd_disruptions < even_disruptions:
		print("SECOND")
	elif even_continuos_time > odd_continuos_time:
		print("FIRST")
	elif odd_continuos_time > even_continuos_time:
		print("SECOND")
