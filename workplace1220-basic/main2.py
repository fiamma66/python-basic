times = 0
while times < 10 :
    print(2 * times + 1 , "hello")
    times = times + 1

#反著印 想法 10 - 次數 就好
times = 0
while times < 10 :
    print(10 - times , 'hello')
    times = times + 1

result = 0
times = 0
while times < 10 :
    result = result + (times + 1) # 第一次times是0故+1
    times = times + 1
print(result)

# 變數宣告 其實可以刪除
# 為表達邏輯 故留下
first = 0
second = 0
times = 0
n = int(input("要幾項 ?"))
while times < n :
    if times == 0 :
        first = 0
        result = 0
    elif times == 1 :
        second = 1
        result = 1
    else :
        result = result + first
        first = second
        second = result
    print("第 %d 項 : %d"%(times+1,result))

    times = times + 1






