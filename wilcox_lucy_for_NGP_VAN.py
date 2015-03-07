"""

By Lucy Wilcox for NGP VAN application
"""


import operator

packages = dict()
time = 0

class Package(object):
	""" """

	def __init__(self, ID, size, speed):
		global time
		self.ID = ID
	 	self.size = size
		self.speed = speed
		self.time = time
		packages[(self.speed, self.size, self.time)] = self.ID
		time += 1


def remove():
	ordered_packages = sorted(packages, key = operator.itemgetter(0, 1, 2)) #l and f come before s so alphebetical sorting works
	num_packages = zip(ordered_packages, range(len(ordered_packages)))
	to_remove = ordered_packages[0] #returns first
	send = packages[to_remove]
	packages.pop(to_remove)
	return send


def package_entry():
	Package(232, 'large', 'slow')
	Package(333, 'small', 'fast')
	Package(662, 'small', 'fast')
	Package(432, 'large', 'fast')
	Package(544, 'large', 'fast')

package_entry()
sent = remove()
print sent
