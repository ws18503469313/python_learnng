import requests, os
path = "D:/"
url = "http://img0.dili360.com/pic/2019/07/17/5d2ed90938c719h82206187_t.jpg@!rw9"

tails = ["jpg", "jpeg", "png"]
'''
从网站爬取并保存图片
'''
def getImage(url, path):
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        filename =  url.split("/")[-1]
        for tail in tails:
            try:
                if filename.index(tail):
                    arr = filename.split(tail)
                    filename = arr[0] + tail
            except:
                print(url + " don't contail " + tail)
        filename = path + filename
        print(filename)
        if not os.path.exists(filename):
            r = requests.get(url)
            with open(filename, "wb") as f:
                f.write(r.content)#将从网络中获取到的二进制写入文件
                f.close()
                print("保存成功")
        else:
            print("文件已存在")
    except:
        print("爬取失败")

getImage(url, path)
# filename =  url.split("/")[-1]
# for tail in range(len(tails)):
#     try:
#         if filename.index(tails[tail]) !=  -1:
#             filename = filename.split(tails[tail])[0]
#     except:
#         print(tails[tail])