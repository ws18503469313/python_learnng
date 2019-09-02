response = []
hasmore = True

while hasmore:
	print("what's u name?")
	name = input("plz input u name:")
	mountain = input("plz input the mountain u want to clamb: ")
	
	response.append({"name": name, "mountain":mountain})
	
	isend = input("has more people would to response?(yes/no)")
	if isend != 'yes':
		hasmore = False
	
print(response)
