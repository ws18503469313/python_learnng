import requests

url = "https://www.baidu.com"

r = requests.get("https://www.baidu.com")
r.encoding = "utf-8"
print(r.text)
