# Json 使用練習
f = open("GetTodayCase.json","r",encoding="utf-8")
article = f.read()
f.close()

import datetime
import json
case = json.loads(article)
## 印出 桃園市 道路工程於2019/05/01 後才停工的 CaseID , Name
for a in case :
    time = datetime.datetime.strptime(a['stop'], "%Y/%m/%d")
    if time > datetime.datetime.strptime("2019/05/01","%Y/%m/%d"):
        print("CaseID : ",a["CaseID"])
        print("Name : ",a["ConstName"])
        print(datetime.datetime.strptime(a['stop'], "%Y/%m/%d"))



