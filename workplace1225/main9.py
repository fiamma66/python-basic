# 用物件導向 玩終極密碼

# 從同層資料夾下 import 物件
from game import PwdMachine

mode = int(input("[0]預設模式 , [1]自行設定"))

if mode == 1:
# 設定遊玩方式 , 預設或自行給範圍
    min = int(input("輸入最小值"))
    max = int(input("輸入最大值"))
    m = PwdMachine(min , max)
else:
    m = PwdMachine()

while True:
    msg = "請輸入 : " + str(m.low) + "," + str(m.high)
    gu = int(input(msg))
    if m.guess(gu):
        print("總共猜了",m.times, "次")
        break





