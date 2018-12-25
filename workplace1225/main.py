
## with open as :
## 此語句保證一定會關閉資源
## 也就是自動使用 close
with open("a.txt","r",encoding="utf-8") as f:
    article = f.read()

## 建立字典
dic = {}
## 建立機率 首先設定總數
total = 0
## 走過整篇文章 使用 for in
for c in article:
    # Java習慣式 不建議
    total += 1
    # 大小寫希望不分 那就全部小寫吧
    c = c.lower()
    # 第一個情況 : 不在裡面(第一次遇到)
    if not c in dic :
        dic[c] = 1
    # 第二個情況 : 在裡面(第二次遇到)
    else:
        dic[c] =dic[c] + 1
print(dic)

## 開始機率運算每個字都獨立
prob = {}

for key in dic :
    # 沒有遇到key error了

    prob[key] = dic[key] / total

print(prob)

