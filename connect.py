from fractions import Fraction
class Group: 
	def __init__(self): 
		self.participants = {}  
		self.len = 0
	
	def lookup(self,number):
		if self.participants.get(number) != None:
			return True
		else:
			return False
	
	def add_to_group(self, number, index):
		if self.participants.get(number) == None:
			self.participants[number] = index
			self.len += 1
	
	def merge_groups(self, other_group):
		self.participants.update(other_group.participants)
		self.len = len(self.participants)


def find_number_in_list_of_groups(list_of_g, num):
	for i in range(len(list_of_g)):
		if list_of_g[i].lookup(num):
			return i
	return -1


amt = input().rstrip().split(" ")
amt_computers = int(amt[0])

current_connectivity = Fraction(1, 1)
current_sum = amt_computers

p = {}
quantity = 0
list_of_groups = []
num_of_groups = 0

for i in range(int(amt[1])):
	line = input().rstrip().split(" ")
	if int(line[0]) == 2:
		#current_connectivity = calculate_connectivity(list_of_groups, amt_computers-quantity)
		current_connectivity = Fraction(current_sum, num_of_groups+amt_computers-quantity)
		print("{}/{}".format(current_connectivity.numerator, current_connectivity.denominator))

	elif int(line[0]) == 1:

		if p.get(int(line[1])) == None:
			quantity += 1
			current_sum -= 1
		if p.get(int(line[2])) == None:
			quantity += 1
			current_sum -= 1

		p[int(line[1])] = 1
		p[int(line[2])] = 1
		#print("Quantitty", quantity)

		result_index_1 = -1
		result_index_2 = -1

		if p.get(int(line[1])) != None:
			result_index_1 = find_number_in_list_of_groups(list_of_groups, int(line[1]))
			
		if p.get(int(line[2])) != None: 
			result_index_2 = find_number_in_list_of_groups(list_of_groups, int(line[2]))

		if result_index_1 > -1 and result_index_2 > -1 and result_index_1 != result_index_2:
			len_one = list_of_groups[result_index_1].len
			len_two = list_of_groups[result_index_2].len

			current_sum -= (len_one*len_one)
			current_sum -= (len_two*len_two)

			if len_one <= len_two:

				list_of_groups[result_index_2].merge_groups(list_of_groups[result_index_1])

				current_sum += (list_of_groups[result_index_2].len*list_of_groups[result_index_2].len)

				del list_of_groups[result_index_1]
				num_of_groups -= 1
				

			else:
				list_of_groups[result_index_1].merge_groups(list_of_groups[result_index_2])

				current_sum += (list_of_groups[result_index_1].len*list_of_groups[result_index_1].len)

				del list_of_groups[result_index_2]

				num_of_groups -= 1

		elif result_index_1 != -1 and result_index_1 == result_index_2:
			continue
		
		elif  result_index_1 > -1:
			
			group_len = list_of_groups[result_index_1].len

			list_of_groups[result_index_1].add_to_group(int(line[2]), result_index_1)

			current_sum -= group_len * group_len
			current_sum += (group_len+1) * (group_len+1)
			
		else:
			if result_index_2 > -1:

				group_len = list_of_groups[result_index_2].len

				list_of_groups[result_index_2].add_to_group(int(line[1]), result_index_2)

				current_sum -= group_len * group_len
				current_sum += (group_len+1) * (group_len+1)

			else:
				new_group = Group()
				new_group.add_to_group(int(line[1]), num_of_groups)
				new_group.add_to_group(int(line[2]), num_of_groups)
				list_of_groups.append(new_group)
				current_sum += 4
				num_of_groups += 1