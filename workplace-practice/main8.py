# import this
# print(this.s)
# print("/".join(["2018", "11", "08"]))

import jieba

f = open("a.txt", "r", encoding="utf-8")
article = f.read()
f.close()

print(" ".join(jieba.cut(article)))

# 列出關鍵詞 可用參數選出前幾個
words = jieba.analyse.extract_tags(article, 5)
print("前五關鍵詞 : ", words)

from jieba import analyse

words1 = analyse.extract_tags(article, 5)
print("第二種寫法 : ", words1)

from jieba.analyse import extract_tags

words2 = extract_tags(article,5)
print("第三種寫法 : ", words2)

# 內建request 可下載檔案
from urllib.request import urlretrieve

# MAC 電腦要特別加入這兩行
# 因為 MAC 電腦 +python 會有個 bug, 把對面的 ssl 憑證視為無效
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/fxsjy/jieba/master/extra_dict/dict.txt.big"
urlretrieve(url,"bigdict.txt")


jieba.load_userdict("bigdict.txt")
print("額外字典 : \n"," ".join(jieba.cut(article)))

from jieba.analyse import extract_tags
words3 = extract_tags(article,5)
print("前五關鍵字 : ", words3)

# 新增自定義字典

f1 = open("b.txt","r",encoding="utf-8")
article1 = f1.read()
f1.close()
jieba.load_userdict("bigdict.txt")
# 載入自定義字典
jieba.load_userdict("mydict.txt")
print("自訂義字典修正 : \n"," ".join(jieba.cut(article1)))

from jieba.analyse import extract_tags

word4 = extract_tags(article1,5)
print("第二篇關鍵字 : ",word4)


