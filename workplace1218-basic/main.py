#BMI = 體重 / 身高(m)^2

height = float(input("請輸入身高 : "))
weight = float(input("請輸入體重 : "))

print("身高是 : ",height)
print("體重是 : ",weight)
#次方可表達為 "**"
bmi = weight / (height/100) ** 2
print("BMI 是 : ", bmi)
print("四捨五入 ", round(bmi,3))
# print(print(3)) #print(3)後 再print(print(3)) 並無回傳值
                #故為 None

if bmi >= 25 :
    print("過重")
elif bmi >= 18 and bmi < 25 :
    print("普通")
else :
    print("過輕")

print ('__name__:' + __name__)
