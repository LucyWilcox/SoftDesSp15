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
	n = int(arc_length / 4) + 1
	step_len = arc_length / n
	step_a = float(angle) / n
	lt(t, step_a/2)
	polyline(t, n, step_len, step_a, direction)
	rt(t, step_a/2

# def circle(t, r):
# 	arc(t,r, 360)

def sinusoid(t):
	
	r = 50
	for i in range(3):
		if i == 2:
			arc(t, r, 90, 1)
		else:
			arc(t, r, 90, -1)

def turtle_text(t, text):
	for letter in text:
		if letter == "C":
			arc(t, 60, 185, -1)
		elif letter == "A":
			polyline(t, )


#square(ray, 50)
#polygon(bob, 100, 5)
bob.delay = .01
#circle(bob, 90)
#arc(bob, 90, 90)
sinusoid(bob)

wait_for_user()

