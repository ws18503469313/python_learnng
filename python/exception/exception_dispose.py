
try:
	num = 5/0
except ZeroDivisionError:
	print("0 can't be chushu")
	
try:
	with open("notexeistfile.txt") as obj:
		print(obj.read())
except FileNotFoundError:
	print("file not found")

### text process ########

title = "this is a title"
words = title.split()
print(words)


def count_words():
	map = {}
	try:
		with open("test.txt") as obj:
			content = obj.read()
			words = content.split()
			for val in words:
				try:
					num = map[val]
					map[val] = num + 1
				except:
					map[val] = 1
					
	except FileNotFoundError:
		print("file is not exist")
	_most_time = {}
	most_time = 0
	for k, v in map.items():
		if v > most_time:
			_most_time = {}
			_most_time[k] = v
			most_time = v
		if v == most_time:
			_most_time[k] = v
	for k, v in _most_time.items():
		print(k + "======>" + str(v))
count_words()	
