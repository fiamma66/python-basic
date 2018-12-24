# 定義 不定型參數

def test(**kwargs):
    print(kwargs)

test(a=1, b=2, c=3, d=3)

# 定義 option 參數
def bmi(height,weight,**kwargs) :
    bmi = weight / (height / 100) ** 2
    ## **kwargs 為字典 可使用in 檢查是否有
    if "rounded" in kwargs :
        return round(bmi,kwargs["rounded"])
    else :
        return bmi
print("不帶rounded 參數 : ",bmi(180,75))
print("使用rounded 參數 : ", bmi(180,75,rounded=4))

