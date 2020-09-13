def calculate_slope(x1,y1,x2,y2):
	return (y2-y1)/(x2-x1)

def calculate_y_intercept(x,y,m):
	return y-(m*x)

def calculate_x_intercept(m1,b1,m2,b2):
	return (b2-b1)/(m1-m2)

def calculate_y_of_intersection(m,x,b):
	return m*x+b

def plug_in_y(y,m,b):
	return (y-b)/m

def calculate_area(x_point, y_point, x_inter, y_inter):
	base = abs(x_point-x_inter)
	height = abs(y_point-y_inter)

	return 0.5*base*height

def is_this_point_allowed(x_intercept, the_y_i_need, x1, y1, x2, y2, x1_sec, y1_sec, x2_sec, y2_sec):



	if x_intercept+10e-6 < x1 or x_intercept-10e-6 > x2 or x_intercept-10e-6 > x1_sec or x_intercept+10e-6 < x2_sec or the_y_i_need+10e-6 < y1 or the_y_i_need-10e-6 > y2 or the_y_i_need+10e-6 <  y1_sec or the_y_i_need-10e-6 > y2_sec:
		return False
	return True


x1, y1, x2, y2  = input().rstrip().split(" ")
x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

x1_sec, y1_sec, x2_sec, y2_sec  = input().rstrip().split(" ")
x1_sec, y1_sec, x2_sec, y2_sec = int(x1_sec), int(y1_sec), int(x2_sec), int(y2_sec)

slope_1 = calculate_slope(x1,y1,x2,y2)

slope_2 = calculate_slope(x1_sec,y1_sec,x2_sec,y2_sec)

y_intercept_1 = calculate_y_intercept(x1,y1,slope_1)
y_intercept_2 = calculate_y_intercept(x1_sec,y1_sec,slope_2)


x_intercept = calculate_x_intercept(slope_1, y_intercept_1, slope_2, y_intercept_2)

the_y_i_need = calculate_y_of_intersection(slope_1, x_intercept, y_intercept_1 )

allowed = is_this_point_allowed(x_intercept, the_y_i_need, x1, y1, x2, y2, x1_sec, y1_sec, x2_sec, y2_sec)

if allowed:
	min_y_height = min(y2_sec,y2)
	# if y2_sec <= y2:
	# 	min_y_height = y2_sec
	# else:
	# 	min_y_height = y2

	find_x_1 = plug_in_y(min_y_height, slope_1,y_intercept_1)

	find_x_2 = plug_in_y(min_y_height, slope_2,y_intercept_2)

	triangle_1_area = calculate_area(find_x_1, min_y_height, x_intercept, the_y_i_need )
	triangle_2_area = calculate_area(find_x_2, min_y_height, x_intercept, the_y_i_need )
	total = triangle_1_area + triangle_2_area

	print(total)
else:
	print(0.0000)

# print(x_intercept, the_y_i_need, min_y_height)
