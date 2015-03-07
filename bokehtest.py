from swampy.Gui import *
from Tkinter import *

g = Gui()
g.title('Gui')

class Canvas():
	""" """
	def __init__(self):
		canvas = g.ca(width = 500, height = 500)

class MakeWindow():
	""" """
	def setup(self):

		self.canvas = g.ca(width = 500, height = 500, bg = 'white')


	def add_button(self, text, the_command = None):
		g.bu(text, command = the_command)
		#b.pack()


def test_it():
	print "yeah"


	# def set_option(self, color):
	# 	mb.config(text = option)
	# 	print color
window = MakeWindow()
window.setup()
window.add_button("Test", test_it)
# c = Canvas()
# g.la('Select a option:')
# options = ['LOOK AT COMMON DATA','COMPARE YOUR DATA']
# mb = g.mb(text = options[0])
# for option in options:
# 	g.mi(mb, text = option, command = Callable(set_option, option))

# text = g.te(width = 100, height = 5)
# button = g.bu(text = "LOOK AT COMMON DATA", command = sel)
# button2 = g.bu(text = "Common Numbers")
# label = g.la(text = "press the button")

g.mainloop()