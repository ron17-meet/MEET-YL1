class Animal(object):
	def __init__(self, name, color, age):
		self.name=name
		self.age=age
		self.color=color
	def printAll(self):
		print(self.name + " is " + str(self.age) + " years old, and its color is " + self.color)