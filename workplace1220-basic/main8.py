## 蒙地卡羅 演算法 PI 的值
import random
import time
inner = 0
outer = 0

tstart = time.time()
for times in range(1000000) :
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    print(x, y)
    if x ** 2 + y ** 2 <= 1 :
        inner = inner + 1
        print("圓內")
    else :
        outer = outer + 1
        print("圓外")

print("面積是 : ",4 * inner / (inner + outer))
tend = time.time()
print("花了 %.8f 秒"%(tend-tstart))
