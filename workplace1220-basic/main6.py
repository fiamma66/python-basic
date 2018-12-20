## 實作三門問題
import random
# 準備門
doors = ["羊", "羊"]
c = random.randint(0,2)
doors.insert(c, "車")
print("一開始的門 : ",doors)

# 玩家選門
c = random.randint(0,2)
print("選到的門是 : ",doors[c])
del doors[c] # 準備給下一步 主持人開羊給你

# 主持人開羊
doors.remove("羊")
print("剩下的門是 : ",doors)

#判定輸贏
if doors[0] =="車" :
    print("贏了")
else :
    print("輸了")

# 加入迴圈 計算勝率
times = 0
win = 0
lose = 0
while times < 1000 :
    doors = ["羊", "羊"]
    c = random.randint(0, 2)
    doors.insert(c, "車")
    c = random.randint(0, 2)
    del doors[c]
    doors.remove("羊")
    if doors[0] == "車":
        win = win + 1
    else:
        lose = lose + 1
    times = times + 1

total = win + lose
print("勝率是 : ",win/total)
print("敗率是 : ",lose/total)

