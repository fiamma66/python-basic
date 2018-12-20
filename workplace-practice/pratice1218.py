import random
"""
#費氏數列
i = 0
doTimes = int(input("輸入數列數量"))
while i < doTimes :
    if i == 0:
        result = 0
        b = 0
    elif i == 1 :
        a = 1
        result = result + a
    else :
        result = a + b
        b = a
        a = result

    print("第 %d 項 為 : %d"%(i + 1,result))
    i = i + 1



# 終極密碼


low = int(input("輸入最小值"))
high = int(input("輸入最大值"))
ans = random.randint(low,high)

time = 1

while True :
    msg = "請輸入 [" + str(low) + "-" + str(high) + "]"
    guess = int(input(msg))
    if guess == ans :
        print("正確 ! ")
        break
    # 猜的數字比答案小 應更新最小值
    elif guess < ans :
        low = guess
        time = time + 1
    # 猜的數字比答案大 應更新最大值
    else :
        high = guess
        time = time + 1

print("用了 %d 次"%time)


#記憶區準備
result = 0
for i in range(100) :
    result = result + i
print("1+2+3+4+.....+100 = ",result)


#讀取file
f = open("E:/actor.txt","r",encoding="UTF-8")
file = f.read()
f.close()
print(file)


#建立字出現次數統計
f = open("E:/fiamma.txt","r",encoding="UTF-8")
file = f.read()
f.close()
print(file)
result = {}
for c in file :
# 兩種 case
# 1. 第一次遇到的字 result [c] = 1
# 2. 第二次遇到的字 直接使用
# 用 in 來判斷是否有在裡面
    if c in result :
        #第二次以上 增加次數
        result[c] = result[c] + 1
    else :
        #第一次 次數為 1
        result[c] = 1

print(result)


#Set 無順序性 且 不重複
#無法使用 Index 取用
name_set = {"我","是","誰","呢"}
#print(name_set)
print("長度 : ",len(name_set))


#交集 聯集 差集
name_set1 = {"我","不","是","人","吧"}
print("set   : ",name_set)
print("set 1 : ",name_set1)
print("交集 : ",name_set & name_set1)
print("聯集 : ",name_set | name_set1)
#注意差集 只顯示第一個 set 的差集內容
print("差集 : ",name_set - name_set1)

#使用remove 需要使用Try except
try :
    name_set.remove("吧")
except KeyError :
    print("糟糕 沒有這個東西呢")

#discard 有就刪除 沒有就不動作
name_set.discard("是")
name_set.discard("吧")
print(name_set)



# 樂透練習 1~100號

prize = set()
while len(prize) < 7 :
    prize.add(random.randint(1,100))
print("有獎彩券 : ",prize)

my = set()
while len(my) < 7 :
    my.add(random.randint(1,100))
same = prize.intersection(my)
print("我買的彩券 : ",my)
print("中獎的數字 : ",same)
print("中獎數量 : ",len(same))

"""

# 買到中
end = int(input("想要中幾個"))
prize = set()
while len(prize) < 7 :
    prize.add(random.randint(1,100))




