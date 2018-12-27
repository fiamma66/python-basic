import requests
import os
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import shutil
from urllib.request import urlretrieve
import json

def get_wb(url): ## 建立與 dcard的連線 並取得html
    # 先偽裝 headers
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    resp = requests.get(
        url = url,
        headers = header,
        cookies={"over18": "1"}
    )
    if resp:

        return resp.text
    else:
        print("URL錯誤")
        return None

def get_json_article(dom):
    js = json.loads(dom)
    articles = []
    for j in js:
        url = "https://www.dcard.tw/f/merryxmas/p/" + str(j["id"])
        title = j["title"]
        articles.append({
            'url': url,
            'title': title
        })
    return articles




def parse(dom): ## 找到文章內所有圖片超連結
    html = BeautifulSoup(dom, 'html.parser')
    links = html.find("div", class_="PostPage_innerContainer_3RSkmO")
    if links :
        links = links.find_all("img", class_="GalleryImage_image_3lGzO5")

    img_url = []
    if links:
        for link in links :
            if re.match(r"^https?://(i.)?(m.)?imgur",link["src"]):
                img_url.append(link["src"])
    return img_url

def save(img_url,title): ##儲存圖片
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    if img_url :
        try:
            # 設定儲存路徑
            dname = title.strip() # 去除字串前後空白
            if not os.path.exists(dname):
                os.makedirs(dname)
            for url in img_url :
                if not url.endswith(".jpg"):
                    url = url + ".jpg"
                fname = url.split("/")[-1]
                r = requests.get(url,stream = True, headers=header)
                if r.status_code == 200:
                    with open(os.path.join(dname,fname),"wb") as f :
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw , f)



        except Exception as e:
            print(e)

#url = "https://www.dcard.tw/_api/forums/sex/posts?popular=true&limit=30&before=230349407"
def main():
    file = input("存放位置 ex: J:/crawler/try")
    page_count = int(input("想抓多少 建議大約10頁就好")) * 1000
    page = 230355445
    threshold = page - page_count
    #endpoint = page - page_count
    while True:
        url = "https://www.dcard.tw/_api/forums/sex/posts?popular=false&limit=30&before="+str(page)
        print("現在處理 : ",url)
        urlpage = get_wb(url)
        js = get_json_article(urlpage)
        for j in js:
             save(parse(get_wb(j["url"])),file)

        page = page - 1000
        if page == threshold:
            break







if __name__ == "__main__":
   # page = 230349407
   # url = "https://www.dcard.tw/f/merryxmas/p/230347022"
    #url = "https://imgur.dcard.tw/edDxWGO.jpg"
   # url = "https://www.dcard.tw/_api/forums/sex/posts?popular=true&limit=30&before=" + str(page)
    #urlretrieve('https://imgur.dcard.tw/edDxWGO.jpg', "J:/Try")
    main()
