# 使用Json練習
f = open("bus.json", "r", encoding="utf-8")
article = f.read()
f.close()
# print(article)

import json
# 注意Json.load 和 Json.loads 的差別
# load("filePath"....) 未被 read
# loads("string" ....) 已被 read
buses = json.loads(article)
print(buses)

print("有幾輛車 : ", len(buses["datas"]))
# 注意 超級重要 !!
# buses -> dict
# buses['datas'] -> List
# b.txt -> dict
# List 裡面的成員是 Dict
for b in buses["datas"] :
    print(b["BusID"], "(", b["Longitude"], ",",
         b["Latitude"], ")" )
