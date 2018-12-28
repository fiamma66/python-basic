## 練習
## 未解決問題 : 評等與電話 皆為 img 無法直接爬取
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
import re
page = 1

def get_web(url):
    try:
        resp = urlopen(
            url = url,
        )
        return resp
    except HTTPError as e:
        print("error code :",e.code)
        print(e)

def get_page(dom):
    soup = BeautifulSoup(dom,'html.parser')
    res = soup.find_all("article", class_="serItem")
    article = []
    if res:
        res.remove(res[0])

        for r in res:
            name = r.find("a", class_="a37 ga_tracking")
            new_name = name["href"].split("-")
            href = "http://www.ipeen.com.tw" + new_name[0]
            addr = r.find("span", class_="address")
            spi = r.find_all("a", class_="ga_tracking")
            article.append({
                "name" : name.text,
                "href" : href,
                "addr" : addr.text.strip(),
                "spi" : spi[3].text
            })
    return article

def parse(dom):
    page = 57
    end = 30
    comment_list = []
    while True:

        comment_html = dom + "/comments?p="+str(page)+"&so=pr&sortway=d"
        try:
            print("現在處理 : ",comment_html)
            web = get_web(comment_html)
        except HTTPError as e:
            print("error:",e.code)
            break
        soup = BeautifulSoup(web, 'html.parser')
        resp = soup.find_all("section", class_="review-list")
        html_head = "http://www.ipeen.com.tw"

        for art in resp:

            for comment in art.find_all("article", itemprop="review"):
                href = comment.find("a", class_="ga_tracking")["href"]
                comment_list.append(html_head+href)
            
        page = page + 1

    return comment_list
#url = "https://www.ipeen.com.tw/search/all/000/1-0-0-0/?p=1&adkw=%E5%8F%B0%E5%8C%97&so=commno"

url = 'http://www.ipeen.com.tw/shop/979300'
for a in parse(url):
    print(a)
"""
r = parse(url)
for a in r:
    for s in a.find_all("article", itemprop="review"):
        #if re.match(r"/comment",s["href"]):
            print(s.find("a", class_="ga_tracking")["href"])

"""
"""
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

"""





