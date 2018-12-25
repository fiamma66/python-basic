
import requests
import re
import os
import time
from bs4 import BeautifulSoup
def get_wb(url): ## 建立與 ptt的連線 並取得html
    response = requests.get(url=url,
                            cookies={"over18":"1"})
    if response.status_code == 200:
        return response.text
    else :
        print("URL錯誤",url)
        return None

# 簡單抓 列表
"""
page = get_wb("https://www.ptt.cc/bbs/Food/index7004.html")
html = BeautifulSoup(page)
for r in html.find_all("div", class_="r-ent"):
    title = r.find("a")
    date = r.find("div", class_="date")
    rate = r.find("span", class_="hl f2")
    if not rate == None :
        rate = rate.text

    href = "https://www.ptt.cc" + title["href"]
    print("title: ",title.text,href,"\n"
          "date: ",date.text,"\n"
          "評價:",rate)
"""
def get_article(dom): # 使用bs4 轉換 html格式 並尋找文章列表
    html = BeautifulSoup(dom, "html.parser")

    article = []
    divs = html.find_all("div", class_="r-ent")
    for r in divs:

        push = 0
        if r.find("div", class_="nrec").text:
            try:
                push = int(r.find("div", class_="nrec").text)
            except ValueError:
                pass
        if r.find("a"):
            href ="https://www.ptt.cc" + r.find("a")["href"]
            title = r.find("a").text
            article.append({
                "title" : title,
                "href" : href,
                "push" : push
                })
    return article

def parse(dom): ## 找到文章內所有圖片超連結
    html = BeautifulSoup(dom, "html")
    links = html.find(id = "main-content").find_all("a")
    img_url = []
    for link in links :
        if re.match(r"^https?://(i.)?(m.)?imgur.com",link["href"]):
            img_url.append(link["href"])
    return img_url

def save(img_url,title): ##儲存圖片
    if img_url :
        try:
            dname = title.strip() # 去除字串前後空白
            os.mkdir(dname)
            for url in img_url :
                






