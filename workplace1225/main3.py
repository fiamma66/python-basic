from urllib.request import urlopen
from urllib.request import urlretrieve
import json
## OS 套件 檢查作業系統 (目錄 檔案)
import os
## MAC 電腦 + python 3.6 必須額外增加
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
## 增加 URL 我們練習抓取 google好手氣內的圖檔
## 進階 全月都要儲存 將取一個月的資料 包成迴圈
for m in range(12):
    print("正在處理 : ", m + 1, "月")
    url = 'https://www.google.com/doodles/json/2018/' + str(m + 1) +'?hl=zh_TW'

    response = urlopen(url)
    doodles = json.load(response)
    ## doodles 為 List
    ## List 內 d 為 字典
    for d in doodles :
        # 取代 url = 每個 d 字典內的 "url" 內容
        # 發現 : 原來 "url" 內容並沒有加上 https:
        # 手動增加 "https:"
        url = "https:" + d["url"]
        # 印出 d 字典內 "title" 的內容 與 url
        # 稍稍整理印出格式 讓表單更好閱讀
        print(d["title"],"\n",url)
        # 創建各月資料夾
        dir = "doodle/" + str(m + 1) + "/"
        if not os.path.exists(dir):
            os.mkdir(dir)
        # 拿出 url 內的檔名 先切割 在取出
        fname = dir + url.split("/")[-1]
        """
        # 準備好 url 開始下載
        # 多媒體檔案 使用 read 就可以
        response = urlopen(url)
        img = response.read()
    
        # 下載後 寫入檔案 使用 "w" 並且是原始
        # 型式 使用 "wb"
        f = open(fname,"wb")
        f.write(img)
        f.close()
        """
        # 下載這五行 太累了 改用下面
        #  urlretrieve 就可以解決寫入檔案
        urlretrieve(url,fname)




