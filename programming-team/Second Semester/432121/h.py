from math import pi

while True:
	w, h = map(int, input().split(" "))
	if w == 0 and h == 0:
		break
	else:
		radius = w/2
		if h < w * pi + w:
			radius = h/(2 * pi + 2)
		volume_1 = pi * radius ** 2 * w
		volume_2 = (w**2)/4 * (h*pi - w) / (pi * pi)
		print(round(max(volume_1, volume_2),3))