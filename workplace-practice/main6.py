# 物件導向 - 練習
class Person :
    # 定義專屬技能 init
    # 節省設定資料的程式碼
    def __init__(self, n, h, w):
        self.name = n
        self.height = h
        self.weight = w

    def bmi(self,**kwargs):
        bmi = self.weight / (self.height / 100) ** 2
        if "rounded" in kwargs :
            return round(bmi,kwargs["rounded"])
        else :
            return bmi

p1 = Person("Elwing",175,85)
print(p1.name,p1.bmi(rounded=3))
p2 = Person("Fiamma",172,60)
print(p2.name,p2.bmi(rounded=3))

