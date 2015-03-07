import math
import copy

def filter(numbs):
	non_neg = []
	#numb = int((float(x)) for x in numbs)
	for i in range(len(numbs)):
		if i >=0:
			non_neg.append(numbs[i])

	return non_neg


#print filter([-2.0,  5.0, -100.0])

def sorting(s):
	okay = ['a', 'b']
	for c in s:
		if c not in okay:
			return False

	a
	for c in s:
		
		if c == 'a':
			return True


def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c, 0) + 1


	return d

h = histogram('brontosaurus')
# To-do:  2,4,9
def reverse_lookup(d, v):
	is_v = []
	for k in d:
		if d[k] == v:
			is_v.append(k)
	return is_v
	raise ValueError

print reverse_lookup(h, 2)

class Point(object):
	""" """


class Rectangle(object):
	""" """

def print_point(p):
    """Print a Point object in human-readable format."""
    print '(%g, %g)' % (p.x, p.y)

def distance_between_points(p):
	return math.sqrt(p.x**2 + p.y**2)

blank = Point()
blank.x = 3
blank.y = 4
# print 'blank',
# print_point(blank)
# print 'distance',
# print distance_between_points(blank)

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def move_rectangle(rect, dx, dy):
	rect.corner.x += dx
	rect.corner.y += dy

print "move",
move_rectangle(box, 10, 40)
print box.corner.x,
print box.corner.y
p1 = Point()
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)
# print_point(p1)
# print_point(p2)

# class Time(object):
# 	""" Time of day
# 	attributes: hour, minute, day
# 	"""

# time = Time()
# time.hour = 11
# time.minute = 59
# time.second = 30

# def print_time(t):
# 	print "%.2d:%.2d:%.2d" % (t.hour, t.minute, t.second)


# def is_after(t1, t2):

# 	if t1.hour > t2.hour:
# 		return True
# 	elif t1.hour < t2.hour:
# 		return False

# #print_time(time)

# t2 = Time()
# t2.hour = 9
# t2.minute = 3
# t2.second = 40

# def add_time(t1, t2):
# 	sum = Time()
# 	sum.hour = t1.hour + t2.hour
# 	sum.minute = t1.minute + t2.minute
# 	sum.second = t1.second + t2.second

# 	if sum.second >= 60:
# 		sum.second -= 60
# 		sum.minute += 1

# 	if sum.minute >= 60:
# 		sum.minute -= 60
# 		sum.hour += 1

# 	return sum

# print_time(add_time(time, t2))

# def valid_time(time):
#     """Checks whether a Time object satisfies the invariants."""
#     if time.hour < 0 or time.minute < 0 or time.second < 0:
#         return False
#     if time.minute >= 60 or time.second >= 60:
#         return False
#     return True

# def time_to_int(time):
#     """Computes the number of seconds since midnight.

#     time: Time object.
#     """
#     minutes = time.hour * 60 + time.minute
#     seconds = minutes * 60 + time.second
#     return seconds

# def int_to_time(seconds):
#     """Makes a new Time object.

#     seconds: int seconds since midnight.
#     """
#     time = Time()
#     minutes, time.second = divmod(seconds, 60)
#     time.hour, time.minute = divmod(minutes, 60)
#     return time

# def increment(time, seconds):
# 	time.second += seconds

# 	if time.second >= 60:
# 		time.second -= 60
# 		time.minute += 1

# 	if time.minute >= 60:
# 		time.minute -= 60
# 		time.hour += 1

# def incre(t1, seconds):
# 	assert valid_time(t1)
# 	seconds += time_to_int(t1)
# 	return int_to_time(seconds)

# print_time(incre(t2, 10))

if password == "querty":
	querty = Querty(username)

