from first import first

class second(first):

	def __init__(self):
		self.input = super().__init__()

	def name(self):
		print("Hello " + self.input)	