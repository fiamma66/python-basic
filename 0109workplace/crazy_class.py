import requests
import json
import pandas as pd
df = pd.DataFrame(columns=["href","title"])

# 練習 POST 方式 爬網
for p in range(20):
    url = "https://crazy.ck101.com/category/more"
    post_data = {"id":1, "page":(p+1)}
    print("第幾頁:",p+1)


    response = requests.post(url, data=post_data)
    # 回應回來的是 Json
    # 就用 Json.loads("String")
    # 注意不是 Json.load() <- 要傳進 filepath(表示從檔案)


    news = json.loads(response.text, encoding="utf-8")
    for n in news :
        href = "https://crazy.ck101.com/post/" + str(n["id"])
        print(href, n["title"])
        s = pd.Series([href, n["title"]], index=["href","title"])
        # 記得 dataframe.append 必須設定回去
        df = df.append(s,ignore_index=True)

df.to_csv("crazy.csv",encoding="utf-8")


print(df)