## 練習 tabelog
## 我們要解碼網頁 使用 beautifulsoup4
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
page = 59
df = pd.DataFrame()

while True :
    url = "https://tabelog.com/tw/fukuoka/rstLst/"+ str(page) +"/?SrtT=rt"
    print("現在處理", url)
    ## 這邊獲取的是 網頁 HTML
    ## while 迴圈 不知道何時抓完?
    ## try except 為最佳解
    try:
        response = urlopen(url)
    ## 網頁無法回應了 就離開迴圈
    except HTTPError:
        print("頁面達上限")
        break
    ## BeautifulSoup 幫我們轉換html 轉成盒子
    html = BeautifulSoup(response)
    ## 下面兩種方法都可以
    # html.find_all("li", {"class":"list-rst"})
    for r in html.find_all("li", class_="list-rst") :
        # find 與 find_all 若有相同特徵的盒子 全拿使用find_all
        # find_all 使用 : 評等與價錢 皆有午晚餐之分 全拿
        jname = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main js-detail-anchor")
        rate = r.find_all("b", class_="c-rating__val")
        money = r.find_all("span", class_="c-rating__val")
        credit = r.find("p", class_="list-rst__option-item")
        if not credit == None :
            credit = "yes"
        else:
            credit = "no"
        # 針對find_all 得到的結果 是 List 用 [] 來取我們要的
        print("店名:",jname.text,en.text,en["href"],"\n",
              "評分:",rate[0].text,"午間:", rate[1].text,"晚間:", rate[2].text, "\n",
              "午間價錢:",money[0].text,"晚餐價錢:", money[1].text,"\n",
              "信用卡:",credit)

    page = page + 1
    # end of while