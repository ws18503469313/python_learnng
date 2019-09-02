import requests
'''
标准爬虫框架
'''
def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 300)
        r.raise_for_status() #如果状态不是 200, 则抛出异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

if __name__ == "__main__":
    url = "https://item.jd.com/7652061.html"
    print(getHTMLText(url))

