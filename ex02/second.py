from first import first

class second(first):

	def __init__(self):
		self.input = super().__init__()
		print("Hello " + self.input)
