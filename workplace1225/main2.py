## import jieba.analyse
## from 指定 import
## 可以直接指定 someting.py
## 這種寫法 能一目了然
from jieba.analyse import extract_tags
import jieba
## 大量處理 glob
import glob

for fn in glob.glob("input/*") :
    print("現在處理 : ",fn)
    with open(fn, "r", encoding="utf-8") as f:
        article = f.read()
    jieba.load_userdict("dict.txt.big")
    print("關鍵詞 : ",extract_tags(article, 10))








#jieba.load_userdict("mydic.txt")
#print(" ".join(jieba.cut(article)))






