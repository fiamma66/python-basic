# 思考 : 計算每個人的時候 都要重新輸入 身高體重
#        應該以物件(人)為單位
#        好好記得每個人自己的身高體重

def bmi(h, w):
    return w / (h / 100) ** 2

print(bmi(175,75))

# Step1 設計圖 __init__ 使用
# 1.1 屬性    1.2 專屬功能
class Person():
    # 有了 init 不必再宣告成員變數

    # init 初始化的建構
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def cbmi(self):
        return self.weight / (self.height / 100) ** 2

# Step2 設計圖 -> 資料
# 2.1 填值    2.2 使用
p1 = Person("Elwing",175,75)

print(p1.name, p1.cbmi())

p2 = Person("Fiamma",171,60)

print(p2.name, p2.cbmi())
