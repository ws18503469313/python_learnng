####### class Car defin is start ##############	
class Car():
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.owner = "polunzi"
		
	def get_description_name(self):
		name = str(self.year) + self.make + self.model
		print(name)
	def get_owner(self):
		return self.owner
	
	def set_owner(self, owner):
		if(owner == "wangshuai"):
				print("it's a gift to u")
				return
		self.owner = owner
	
	def fill_gas_tank(self):
		print("this car's tank is full")
	
####### class Car defin is over ##############		
		
# mycar = Car("bz", 'C 180 L', '2025')
# print(mycar.get_description_name())

# print(mycar.get_owner())

# mycar.owner = "jinhui"
# print(mycar.get_owner())

# mycar.set_owner("xiaojiuzi")
# print(mycar.get_owner())

# mycar.set_owner("wangshuai")
####### start to defin class Battery ##################

class Battery():
	
	def __init__(self, battery_size = 70):
		self.battery_size = battery_size
		
	def get_battery(self):
		return (str(self.battery_size)) 

####### class ElectricCar defin is start ##############	
class ElectricCar(Car):
	def __init__(self, make, model, year):
		
		super().__init__(make, model, year)
		self.battery = Battery()
		
	def get_battery_size(self):
		print("this car's battery is :" + str(self.battery.get_battery()))
			
	def fill_gas_tank(self):
		print("this car's don't need fill with gas")

####### class ElectricCar defin is over ##############	
# tesla = ElectricCar("tesla", "model_s", "2019")

# tesla.get_description_name()

# tesla.get_battery_size()

# tesla.fill_gas_tank()
