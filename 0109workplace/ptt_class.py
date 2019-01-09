from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

url = "https://www.ptt.cc/bbs/Gossiping/M.1547006368.A.A6F.html"
""" 
# 增加 Header 原理
# 使用原生 urllib
# 拿出 Request 設計圖
# 增加我們需要的 Header
r = Request(url)
r.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
response = urlopen(r)
"""

# 使用 簡單 requests
# 加入 cookies
# session 為建立一次連線
# 之後繼續使用這個 session 不用重複帶入cookies
s = requests.session()
# 也可以這樣寫
s.cookies["over18"] = "1"
response = s.get(url)
soup = BeautifulSoup(response.text)
# 盒子若有 ID 可以拿
# 必拿ID 原因 : ID是唯一的 不重複
content = soup.find("div",{"id" : "main-content"})
span = content.find_all("span", {"class":"article-meta-value"})
print("ID: ", span[0].text)
print("看板: ", span[1].text)
print("標題: ", span[2].text)
print("時間: ", span[3].text)

removes = content.find_all("div", {"class": "article-metaline"})
# extract : 對"一個"盒子 丟棄
for remove in removes:
    remove.extract()
removes = content.find_all("div", {"class": "article-metaline-right"})
# extract : 對"一個"盒子 丟棄
for remove in removes:
    remove.extract()

removes = content.find_all("span", class_="f2")
for remove in removes:
    if "※" in remove.text:
        remove.extract()

pos = []
neg = []
score = 0


ps = content.find_all("div", class_="push")
for p in ps:
    tag = p.find("span", class_="push-tag").text
    if "推" in tag:
        score = score + 1
        # replace 第三個參數 只置換第一個
        pos.append(p.find("span", class_="push-content").text.replace(": ","",1))
    elif "噓" in tag:
        score = score - 1
        neg.append(p.find("span", class_="push-content").text)
    p.extract()

print("總分: ", score)
print("內文: ",content.text)
print("推文: ",pos)
print("噓文: ",neg)
from jieba.analyse import extract_tags
print("關鍵詞: ",extract_tags(content.text,10))


print(response.elapsed.total_seconds())

