# 製作撲克牌
# 一種花色 13張牌
# 有4種花色
# 思考 : 花色有大小 因該用數字代表 ->
#        先製作1種花色的1張牌 ->
#        再做1種花色的13張牌 ->
#        再做4種花色 ->
import random

# 製作轉換卡片的流程
def trans(card):
    transcolor = ["\u2663", "\u2666", "\u2665", "\u2660"]
    transnumber = ["A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K"]
    return transcolor[card[0]] + transnumber[card[1]]

def score(n):
    return (n- 1) % 13

deck = []


# 針對花色做4種牌
for m in range(4):
    # 針對某個花色 做13張牌
    for n in range(13):
        card = (m, n)
        deck.append(card)

# 做法與思考方式顛倒
# 但應該照著思考方式來完成迴圈


print(len(deck))

# 洗牌 使用 random 的 shuffle
random.shuffle(deck)

# 轉換花色
# 將其製作為流程
print(trans(deck[0]))
print(deck)

# 抽牌 Duel
me = deck[0]
# 我抽完後 第一張應該被刪除
del deck[0]
com = deck[0]
del deck[0]
print("我的牌 :",trans(me),"電腦的 :",trans(com))

# 比大小
# 製作分數 : 一個流程 使用 def
# 思考 : A 比 K 大
#        把 A 拿到 13 巡迴的概念 : mod
#        case1 : 使用 負數的餘數 來進行位移
#        case2 : 使用 正數的餘數 -
#  case1: A = 0 , (0 - 1) % 13 = 12
#  case2: A = 0 , (0 + 12) % 13 = 12

if score(me[1]) > score(com[1]):
    # 我的分數比電腦大
    print("WIN")
elif score(me[1]) == score(com[1]):
    # 我的分數跟電腦一樣
    if me[0] > com[0]:
        # 我的花色比較大
        print("WIN")
    else:
        # 我的花色比較小
        print("LOSE")
else:
    # 我的分數比電腦小
    print("LOSE")


