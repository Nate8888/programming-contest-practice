
def smallest_value_sorted_list(l): 
  
    start = 1 

    for i in range (len(l)): 

        if l[i] <= start:

            start = start + l[i] 

        else: 
            return start

    return start 


cases = int(input().rstrip())

for i in range(cases):
	ignore = input()

	the_list = sorted([int(x) for x in input().rstrip().split(" ")]) # sorting the array to find the smallest

	smallest = smallest_value_sorted_list(the_list)

	print("Set #{}: {}\n".format(i+1,smallest))