import math
def calculate_3d_distance(arr1,arr2):
	distance = math.sqrt( (arr1[0]-arr2[0])**2 + (arr1[1]-arr2[1])**2 + (arr1[2]-arr2[2])**2 )
	return distance

cases = int(input())
for i in range(cases):
	line = input().rstrip().split(" ")
	spaceship = list(map(int,line))
	enemies = []
	for x in range(spaceship[3]):
		line = input().rstrip().split(" ")
		enemy_temp = list(map(int,line))
		enemies.append(enemy_temp)
	amt_in_range = 0
	for each_enemy in enemies:
		distance = calculate_3d_distance(spaceship[:-1],each_enemy[:-1])
		if distance <= each_enemy[3]:
			amt_in_range += 1
	print("You will be picked up by {} radars.".format(amt_in_range))