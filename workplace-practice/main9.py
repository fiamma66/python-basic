## 練習
## 未解決問題 : 評等與電話 皆為 img 無法直接爬取
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
page = 1
while True :
    url = "http://www.ipeen.com.tw/search/all/000/1-0-0-0/?p="+str(page)+ "&adkw=%E5%8F%B0%E5%8C%97&so=commno"
    print("現在處理 : ",url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("沒頁面了 ")
        break
    html = BeautifulSoup(response)
    for r in html.find_all("article", class_="serItem"):
        if r == html.find("article",class_="serItem vipShow"):
            continue
        name = r.find("a", class_="a37 ga_tracking")
        new_name = name["href"].split("-")
        href = "http://www.ipeen.com.tw" + new_name[0]


        addr = r.find("span", class_="address")
        money = r.find("li", class_="costEmpty")
        spi = r.find_all("a",class_="ga_tracking")
        print("店名:",name.text, href,"\n"
              "地址:",addr.text,
              "種類:",spi[3].text,"\n")
    page = page + 1







