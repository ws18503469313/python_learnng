from __future__ import (absolute_import, division, print_function, unicode_literals)
try:
    from urllib import urlopen
except ImportError:
    from urllib.request import urlopen

import json



json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
response = urlopen(json_url)

req = response.read()

with open('btc_close_2017_urllib.json', 'wb') as obj:
    obj.write(req)

file_urllib = json.loads(req)
print(file_urllib)


import requests

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

req = requests.get(json_url)

with open("btc_close_2017_request.json", "w") as obj:
    obj.write(req.text)
file_request = req.json()
print(file_request)


print(file_urllib == file_request)