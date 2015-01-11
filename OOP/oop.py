class Animal:
	def __init__(self,name,age,color,size):
		self.name=name
		self.age=age
		self.color=color
		self.size=size

	def print_all(self):
		print ("Animal's name is: " + self.name)
		print ("Animal's age is: " + str(self.age))
		print ("Animal's color is: " + self.color)
		print ("Animal's size is: " + self.size)
	
	def eating(self,food):
		print (self.name, "is eating",food)
		
	
	def sleeping(self):
		print (self.name, "is sleeping")

	def bathroom(self):
		print (self.name, "went to the bathroom")

print (" ")
print ("The Elephant: ")	
elephant = Animal (name="Augustus",age=157 ,color="blue",size="XXL") 
elephant.print_all()
elephant.eating(food="meat")
elephant.sleeping()
elephant.bathroom()

print (" ")
print ("The Penguin: ")
penguin = Animal (name="Gloria",age=32 ,color="rainbow",size="S") 
penguin.print_all()
penguin.eating(food="fish")
penguin.sleeping()
penguin.bathroom() 

print (" ")

