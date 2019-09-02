import bs4
import re
import common_reptile_frame as crf


def main():
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = crf.getHTMLText(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    ulist = []
    for tr in soup.find_all("tr"):
        if isinstance(tr, bs4.element.Tag):
            tds = tr("td")
            try:
                ulist.append([tds[0].string, tds[1].string, tds[2].string])
            except:
                pass
    tmpl = "{0:^10} \t {1:{3}^10} \t {2:^10}"
    print(tmpl.format("排名", "名称", "城市", chr(12288)))
    for un in ulist:
        print(tmpl.format(un[0], un[1], un[2], chr(12288)))



main()

