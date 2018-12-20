a = 3 + 5
print(a)
print("\nYes")

x = 3.154231
print(round(x,3))
b = "你好"
c = 5.265412
print("數字是 %d \n文字是 '%s'\n浮點數是 %.3f"%(x , b, c))

#if (condition A) :
#   do things
#elif (condition A and B) :
#   do things
#else (Not A and B) :
#   do things
score = float(input("請輸入成績:")) #input always string
if score > 60:
    print("PASS")
else:
    print("FAIL")

