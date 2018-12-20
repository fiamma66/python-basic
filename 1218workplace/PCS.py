import random
'''
me = int(input("你要出什麼 ? [0]剪刀 [1]石頭 [2]布"))

com = random.randint(0,2)

#將0~2轉換為剪刀石頭布
trans = ["剪刀"," 石頭","布"]
#清單對編號做轉換
print("你出的是 : " , trans[me] )
print("電腦出的是 : " , trans[com])

#建立勝負判斷
if me == com :
    print("平手 ! ")
elif me == (com + 1) % 3 :
    print("你贏惹 ! ")
else :
    print("你輸了 ! ")

'''

#棒打老虎雞吃蟲

me = int(input("你要喊的是 ? [0]蟲 , [1]雞 , [2]老虎 , [3]棒子"))
com = random.randint(0,3)
trans = ["蟲", "雞", "老虎", "棒子"]
print("你喊的是 : " , trans[me] )
print("電腦喊的是 : " , trans[com])

if me == (com + 1) % 4 :
    print("你贏了 ! ")
elif com == (me + 1) % 4 :
    print("你輸惹")
else :
    print("平手 ! ")

