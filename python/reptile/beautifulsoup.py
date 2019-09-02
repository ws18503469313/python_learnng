
import requests
from bs4 import BeautifulSoup
import re

url = "http://python123.io/ws/demo.html"

r = requests.get(url)

val = r.text
"""
  parser ("lxml", "lxml-xml",
        "html.parser", or "html5lib")   or it may be the type of markup
        to be used ("html", "html5", "xml")
"""
soup = BeautifulSoup(val, "html.parser")

# print(soup.prettify())

# print(soup.a.name)
# tag = soup.a
# print(tag)
# print(tag.string)
# attr = tag.attrs
# print(attr)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)
for a in soup.find_all("a", href=re.compile('http')):
    print(a)