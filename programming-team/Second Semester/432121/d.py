# input Tf , Vf , Hf , Td, Vd, H
tf, vf, hf, td, vd, hd = list(map(int,input().split(" ")))
td = td - tf

the_min = 0
the_max = 10 ** 13

while(the_max - the_min > 10 ** -4):
	mid = (the_min + the_max)/2
	v_not = (6 * hd) ** (1/2)
	dog_height = v_not * mid - 3 * mid * mid /2
	if(mid > v_not/3):
		dog_height = hd
	fris_height = hf - 1/2 * ( (mid + td) ** 2)
	dog_pos = mid * vd
	fris_pos = min( (mid + td) * vf, vf * ( (2 * hf) ** (1/2) ) )
	if dog_pos >= fris_pos and dog_height >= fris_height:
		the_max = mid
	else:
		the_min = mid

final_time = the_max + the_min
final_time /= 2
fris_pos = min( (final_time + td) * vf, vf * ( (2 * hf) ** (1/2) ) )
fris_pos /= vd
print(final_time + tf + td + fris_pos)

#31.925682332913556