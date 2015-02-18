from swampy.TurtleWorld import *
import math

world = TurtleWorld()
bob = Turtle()
ray = Turtle()
print bob

# for i in range(4):
# 	fd(bob, 100)
# 	lt(bob)

def square(t, length):
	for i in range(4):
		fd(t, length)
		lt(t)

def polygon(t, length, n):
	angle = 360./n

	for i in range(n):
		fd(t, length)
		lt(t, angle)

def polyline(t, n, length, angle, direction):
	if direction > 1:
	    for i in range(n):
	        fd(t, length)
	        lt(t, angle)
	else:
		for i in range(n):
			bk(t, length)
			rt(t, angle)

def arc(t, r, angle, direction):
	arc_length = 2 * math.pi * r * abs(angle) / 360
	n = int(arc_len0gth / 4) + 1
	step_len = arc_length / n
	step_a = float(angle) / n
	lt(t, step_a/2)
	polyline(t, n, step_len, step_a, direction)
	rt(t, step_a/2)

def snow_flake_side(t, length, level):
	angle = 60
	if level == 0:
		fd(t, length)
		rt(t, angle)
		fd(t, length)
		lt(t, 120)
		fd(t, length)
		lt(t, -angle)
		fd(t, length)

	else:
		snow_flake_side(t, length/3.0, level -1)
		rt(t, angle)
		snow_flake_side(t, length/3.0, level -1)
		lt(t, 120)
		snow_flake_side(t, length/3.0, level -1)
		lt(t, -angle)
		snow_flake_side(t, length/3.0, level -1)


def snow_flake(t, length, level):
	for i in range(6):
		snow_flake_side(t, length, level)
		rt(t, 60)

def recursive_tree(t, brance_length, level):
	if level == 0:
		rt(t, 90)
		


#def circle(t, length):
# 	arc(t,r, 360)
# def sinusoid(t):
# 	r = 50
# 	for i in range(3):
# 		if i == 2:
# 			arc(t, r, 90, 1)
# 		else:
# 			arc(t, r, 90, -1)

# def turtle_text(t, text):
# 	for letter in text:
# 		if letter == "C":
# 			arc(t, 60, 185, -1)
# 		elif letter == "A":
# 			polyline(t, )

#square(bob,  90)
#polygon(bob, 100, 5)
bob.delay = .000001
#snow_flake(bob, 100, 5)
#circle(bob, 90)
#arc(bob, 90, 90)
#sinusoid(bob)

wait_for_user()
