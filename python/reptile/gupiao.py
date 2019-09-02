import bs4
import common_reptile_frame as crf
import traceback
import re

def getStockList(list, url):
    html = crf.getHTMLText(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    for a in soup.find_all("a", href=re.compile('.html')):
        print(a.attrs['href'])
        try:
            href = a.attrs['href']
            list.append([re.findall(r"[s][hz]\d{6}")], href)[0]
        except:
            continue
    print(str(list))

def getStockInfo(list, stockUrl, fpath):
    count = 0
    for stock in list:
        url = stockUrl + stock + ".html"
        html = crf.getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = bs4.BeautifulSoup(html, "html.parser")
            stockInfo = soup.find("div", attrs={"class" : "stock-bets"})
            name = stockInfo.find_all(sttrs = {"class" : "bets-name"})[0]
            infoDict.update({"股票名称" : name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                infoDict[key] = value
            with open(fpath, 'wb', encoding="utf-8") as f:
                f.write(str(infoDict) + "\n")
                count = count + 1
                print("\r 当前速度: {:2f} %".format(count*100/len(list), end = ""))
        except:
            count = count + 1
            print("\r 当前速度: {:2f} %".format(count*100/len(list), end = ""))
            continue



def main():
    stock_list = []
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    file_path = "D:/"
    getStockList(stock_list, stock_list_url)
    getStockInfo(stock_list, stock_info_url, file_path)

main()