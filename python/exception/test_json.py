import json

numbers = [1,2,3,4,5]

filename = "number.json"

with open(filename, "w") as obj:
	json.dump(numbers, obj)
	
with open(filename) as obj:
	nums = json.load(obj)
print(nums)
