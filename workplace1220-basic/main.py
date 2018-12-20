
##數字
print(3 + 3.14)
from decimal import Decimal
print(Decimal("3") + Decimal("3.14"))

##文字
a = "hello python"
print(a[0])
print(a[len(a) - 1])
print(a[-1])
# 1 ~ 6
print(a[1:7])
print(a[:])
# 每2個拿一次
print(a[::2])
# 倒著拿
print(a[::-1])
print('hello' in a)
# 字串比對
print('hello python' == a)

##布林
print(True or False)
a = True
# 重新指定 a 為布林
a = a and 5 >= 7 - 2 * 2
print(a)

