
def fun(parm1, parm2):
	print(parm1)
	print(parm2)

fun(parm2 = "polunzi", parm1 = "weixiao")

def fun_with_defaultParma(arg1, arg2 = "default"):
	print(arg1 + str(arg2))

fun_with_defaultParma("jinhui")

def fun_with_return():
	return 20

print(fun_with_return())

def fun_with_arrarg(names):
	for name in names:
		print(name)

fun_with_arrarg([1,2,3,4])

##	pass varialable args to a function
def cookeing(size, * materials):
	print(size)
	for val in materials:
		print(val)
cookeing("123.25", "aa","v","adaw")

## pass a code to a function

def fun_with_codeArg(first, last, **user_info):
	person = {"firstname":first, "lastname": last}
	for k,v in user_info.items():
		person[k] = v
	
	print(person)

fun_with_codeArg("wang", "shuai", sex = "male", age = "25", city = "beijing")
