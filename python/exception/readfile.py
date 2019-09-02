
# open() rcv a arg : file's name.
# 'with' idicate it will close the file when we don't need the file,  
with open("readme.md") as obj:
	text = obj.read()
	# retrip delete the null line of text
	print(text.rstrip())

with open("D:/project/python/exception/readme.md") as obj:
	for line in obj:
		print(line.rstrip())

with open("readme.md") as obj :
	lines = obj.readlines()
##varables's handle is in vm .
pi = ""
for line in lines:
	print(line)
	pi += line.strip()
print(pi)

# r-> read, w->write, a->append, r+ -> read + write
with open("hello.txt", "a") as obj:
	obj.write("hello this a sentence write by py procdress a dwdawdawdwad \n");


