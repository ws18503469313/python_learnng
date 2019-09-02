
class Restaurant():
	
	def __init__(self, name, type):
		self.name = name
		self.type = type
		self.num_serverd = 0
	
	def describe_rest(self):
		print(self.name + "-" + self.type)
	
	def open(self):
		print(self.name + "is on bussiness")
		
	def set_num_served(self, num):
		print(num)
		self.num_serverd = num

res1 = Restaurant("songye", "changchu")

res1.set_num_served(5)
res2 = Restaurant("luchuan", "waibao")

class User():
	
	def __init__(self, first_name, last_name, login_attempts):
		self.firstname = first_name
		self.lastname = last_name
		self.login_attempts = login_attempts
		
	def describe_user(self):
		print("full name is :" + self.firstname + "-" +self.lastname)
	
	def greet(self):
		print("hello, this is a greet for :" + self.firstname + self.lastname )
		
	def increase_login_attempts(self):
		self.login_attempts  += 1
		print("now, attempts of loggin is :" +str(self.login_attempts))
		
	def reset_login_attempts(self):
		self.login_attempts = 0
		print(self.firstname + "-" + self.lastname + "login_attempts is reset to 0") 
	
polunzi = User("wang", "shuai", 1)

cache_a = User("jin", "hui", 1)

cache_a.greet()

cache_a.increase_login_attempts()
for i in range(5):
	cache_a.increase_login_attempts()

cache_a.reset_login_attempts()


