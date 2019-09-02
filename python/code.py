
wangshuai = {'age': 20, 'city':"beijing"}

print(wangshuai['age'])

wangshuai['sex']= 'male'

print(wangshuai)

wangshuai['age'] = 25
print(wangshuai)

#del wangshuai['age']
#print(wangshuai)

for k,v in wangshuai.items() :
	print(k + "=======>" + str(v) + "\n")


users = {
	'wangshuai': {'age': 25, 'sex': 'male', 'language': ['zh_cn', 'en_lang']},
	'jinhui':	{'age': 21, 'sex': 'female'}
}
wangshuai = users['wangshuai']
print(wangshuai)
wangshuai_language = wangshuai['language']
print(wangshuai_language[0])
