arr = [1,2,3,4,5]
for num in arr:
	print(num)

nums = []
for value in range(1, 5):
	print(value)
	nums.append(value * value)

print(nums)
# form 1(default 0) to 20 (required)increase 3(default 1) everytime
for value in range(1, 20, 3):
	print(value)

test_list = list(range(1,10))

print(test_list)

print(max(test_list))

print(sum(test_list))

#print(list(range(1,1000000)))

#copy a arr
food = ["fish", "rice", "cake", "candy"]
# direct value copy is transfer the handle , they share the same ram 
new_food = food
print(new_food)
new_food[0] = "chicken"
print(food)
# the real ram copy need to use the next line code
_food = food[:]
print(_food)
_food[1] = "noodels"
print(food)
