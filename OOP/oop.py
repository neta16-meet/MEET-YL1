class Animal:
	def __init__(self,name,age,color,size):
		self.name=name
		self.age=age
		self.color=color
		self.size=size

	def print_all(self):
		print (self.name)
		print (self.age)
		print (self.color)
		print (self.size)
	
elephant = Animal (name="augustus",age=157 ,color="blue",size="XXL") 
elephant.print_all()

penguin = Animal (name="gloria",age=32 ,color="rainbow",size="S") 
penguin.print_all()
