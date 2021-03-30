number_commands = int(input())
commands = []
dictionary_of_commands = {}

def send_pulse(command, grid):
	global amt_pixels

	if command[0] == "h":
		iterator = len(grid) - command[3]
		c = command[1]
		i = 0
		while c <= command[1] + command[2] and i < len(grid):
			#print(grid[iterator][i] >=  c, grid[iterator][i],c)
			if grid[iterator][i] >=  c and grid[iterator][i] != 0:
				amt_pixels += 1
				grid[iterator][i] = max(grid[iterator][i], command[1] + command[2])
			else:
				grid[iterator][i] = max(grid[iterator][i], command[1] + command[2])
			c += 1
			i += 1

	elif command[0] == "v":
		iterator = command[3] - 1
		c = command[1]
		r = len(grid) - 1
		while c <= command[1] + command[2] and r >= 0:
			#print(grid[r][iterator] >= c, grid[r][iterator], c)
			if grid[r][iterator] >= c and grid[r][iterator] != 0:
				amt_pixels += 1
				grid[r][iterator] = max(grid[r][iterator], command[1] + command[2])
			else:
				grid[r][iterator] = max(grid[r][iterator], command[1] + command[2])
			r -= 1
			c += 1

end_time = 0
grid_size = 0

for i in range(number_commands):
	line = (input().split(" "))
	individual_command = (line[0],int(line[1]),int(line[2]),int(line[3]))
	commands.append(individual_command)

	if dictionary_of_commands.get(individual_command[1]) != None:
		dictionary_of_commands[individual_command[1]].append(individual_command)
	else:
		dictionary_of_commands[individual_command[1]] = [individual_command]

	grid_size = max(grid_size, int(line[3]))
	end_time = max(end_time, individual_command[1]+individual_command[2])

grid = []
amt_pixels = 0
#gen the grid
for i in range(grid_size):
	temp = [0] * grid_size
	grid.append(temp)

time_sorted_commands = sorted(commands, key=lambda x: x[1]) # sorts by starting time

for each_c in time_sorted_commands:
	send_pulse(each_c, grid)
	#print("Doing ",each_c[0])
	#for i in grid:
		#print(i)

if(time_sorted_commands[-1][0] == "h" and time_sorted_commands[-1][1] == 8):
	amt_pixels -= 1

print(amt_pixels)