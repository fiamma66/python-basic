import random
print("終極密碼")
low = int(input("最小值 : "))
high = int(input("最大值 : "))
ans = random.randint(low,high)
times = 0
while True:
    msg = "請輸入 [" + str(low) + " - " + str(high) + "]"
    g = int(input(msg))
    times = times + 1
    if g == ans :
        print("正確 !")
        break
    elif g > ans :
        high = g
    else :
        low = g
print("答案是 %d "%ans)
print("共猜了 %d 次"%times)
