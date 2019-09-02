class Dog():
	#self is nessary, and it have to at the first
	# when we create a Dog class ,__init__ will be invoke auto,
	# and  the args we only have to offer is outclude [self]
	# [self] like to the java [this]
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name + "-sit")
	
	def howl(self):
		print(self.name + "-howl")


mydog = Dog("tom", 5)

print(mydog.name)

mydog.sit()

mydog.howl()
	
