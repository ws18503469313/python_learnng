
cars = ['audi', 'bmw', 'toyota']

for car in cars :
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
		
print( 1 ==2 and 2 ==2)

print('audi' in cars)

print('bmw' not in cars)

safe = True
unsafe = False

age = 14

print(age)

if(age < 2):
	print("baby")
elif(age > 2 and age < 14):
	print("children")
else:
	print("younth")
