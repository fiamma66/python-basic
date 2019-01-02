import requests
from bs4 import BeautifulSoup
import pandas as pd
# 建立ptt連線
def get_web(url):
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    resp = requests.get(
        url = url,
        headers = header,
        cookies = {"over18": "1"}
    )
    if resp.status_code == 200 :
        return resp.text
    else:
        print("錯誤代碼 : ",resp.status_code)



# 取得 ptt 列表

def get_list(dom):
    global df
    df = pd.DataFrame(columns=["推文","標題","日期","網址","內容"])
    soup = BeautifulSoup(dom, 'html.parser')
    post = soup.find_all("div", class_="r-ent")
    for r in post:
        # 取得推的數量
        push = 0
        if r.find("div", class_="nrec").text:
            try:
                push = int(r.find("div", class_="nrec").text)
            except ValueError:
                pass
        if r.find("a"):
            href = "http://www.ptt.cc" + r.find("a")["href"]
            title = r.find("a").text
            date = r.find("div", class_="date").text
            ## 進入第二層爬網
            if not "公告" in title :
                print("現在處理: ", href)
                art = BeautifulSoup(get_web(href))
                content = art.find("div", id="main-content")
                removes = content.find_all("div", class_="article-metaline")
                for remove in removes:
                    remove.extract()
                removes = content.find_all("div", class_="article-metaline-right")
                for remove in removes:
                    remove.extract()
                removes = content.find_all("span", class_="f2")
                for remove in removes:
                    remove.extract()
                removes = content.find_all("div", class_="push")
                for remove in removes:
                    remove.extract()
                replace = content.text.replace("\r",'').replace("\n","")
                s = pd.Series([push,title,date,href,replace],index=["推文","標題","日期","網址","內容"])
                df = df.append(s, ignore_index=True)
                df.to_csv("result.csv", encoding="utf-8", index=False)
    return df


url = "https://www.ptt.cc/bbs/Food/index.html"
get_list(get_web(url))





# 第二層爬蟲 - 進入列表內文章

#
