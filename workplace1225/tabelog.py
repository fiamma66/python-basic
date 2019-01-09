from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
# 若不再一開始排好欄位
# 欄位順序會亂掉
df = pd.DataFrame(columns=["Total", "Night", "Noon", "JA", "US", "Url"])

page = 59
while True:
    url = "https://tabelog.com/tw/osaka/rstLst/" + str(page) + "/?SrtT=rt"
    print("處理頁面:", url)
    try:
        response = urlopen(url)
    except HTTPError:
        print("好像是抓完了")
        break
    html = BeautifulSoup(response)
    # html.find_all("li", {"class":"list-rst"})
    for r in html.find_all("li", class_="list-rst"):
        ja = r.find("small", class_="list-rst__name-ja")
        en = r.find("a", class_="list-rst__name-main")
        scores = r.find_all("b", class_="c-rating__val")
        print(scores[0].text, scores[1].text, scores[2].text, ja.text, en.text, en["href"])
        # PD
        # Series 第一個參數 為 List
        # 也可以使用小括號 () Series(*args) 會自動包成List
        s = pd.Series([scores[0].text, scores[1].text, scores[2].text,
                        ja.text, en.text, en["href"]],
                      index=["Total", "Night", "Noon", "JA", "US", "Url"])
        df = df.append(s, ignore_index=True)

    page = page + 1
# dataframe 有自己的行數號碼 0 ~ n-1
# 若不需要 加入 index=False
df.to_csv("tabelog.csv", encoding="utf-8", index=False)