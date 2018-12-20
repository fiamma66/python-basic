## 提升門數量
## 觀察勝率
import random
win = 0
lose = 0
n = int(input("要幾門 ? "))

for times in range(500000) :
    # 準備門
    doors = ["羊"] * (n - 1)
    c = random.randint(0,n-1)
    doors.insert(c,"車")
    print("一開始的門 : ",doors)
    # 玩家選門
    c = random.randint(0, n - 1)
    print("玩家選的門 : ",doors[c])
    del doors[c]
    # 主持人開羊
    doors.remove("羊")
    print("剩下的門:", doors)
    # 判定輸贏
    c = random.randint(0, len(doors) - 1)
    if doors[c] == "車":
        win = win + 1
        print("贏了")
    else:
        lose = lose + 1
        print("輸了")

total = win + lose
print("win rate : ",win/total)
print("lose rate : ",lose/total)

