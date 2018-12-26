
import requests
from urllib.request import urlretrieve
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
    html = BeautifulSoup(dom, 'html.parser')

    article = []
    # 建立空List
    divs = html.find_all("div", class_="r-ent")
    for r in divs:

        push = 0
        if r.find("div", class_="nrec").text:
            try:
                push = int(r.find("div", class_="nrec").text)
            except ValueError:
                pass
        if r.find("a"):
            href ="http://www.ptt.cc" + r.find("a")["href"]
            title = r.find("a").text
            # 在List中 加入dict字典 內容是網頁列表內容
            article.append({
                "push": push,
                "title" : title,
                "href" : href
                })
    return article

def parse(dom): ## 找到文章內所有圖片超連結
    html = BeautifulSoup(dom, 'html.parser')
    links = html.find(id="main-content").find_all("a")
    img_url = []
    for link in links :
        if re.match(r"^https?://(i.)?(m.)?imgur.com",link["href"]):
            img_url.append(link["href"])
    return img_url

def save(img_url,title): ##儲存圖片
    if img_url :
        try:

            dname = title.strip() # 去除字串前後空白
            if not os.path.exists(dname):
                os.mkdir(dname)
            for url in img_url :
                if url.split("//")[1].startswith("m."):
                    url = url.replace("//m.", "//i.")
                if not url.split("//")[1].startswith("i."):
                    url = url.split("//")[0] + "//i." + url.split("//")[1]
                if not url.endswith(".jpg"):
                    url = url + ".jpg"
                fname = url.split("/")[-1]
                urlretrieve(url, os.path.join(dname,fname))
        except Exception as e:
            print(e)

def main():
    pagecount = int(input("要下載幾頁?"))
    file = input("存哪裡? ex J:/crawler/try")
    page = 4001
    page_stop = page - pagecount

    while True :
        sex_url = "https://www.ptt.cc/bbs/sex/index" +str(page) + ".html"
        print("現在處理 : ",sex_url)
        my_art = get_article(get_wb(sex_url))
        for art in my_art:
            pages = get_wb(art["href"])
            if pages:
                img_url = parse(pages)
                save(img_url,file)
        page = page - 1
        if page == page_stop:
            break

if __name__=="__main__":
    main()


                






