# try except 練習

test = " 這是錯誤處理, 測試測試測試"
result = {}

for c in test :
    try :
        # 產生Key error 不像先前使用If else
        # 處理第一次遇到的字元
        result[c] = result[c] + 1
    except KeyError :
        # 處理第一次遇到的字元 值為1
        result[c] = 1

print(result)

# Input 錯誤處理
while True :
    try :
        # Int 轉換字串 會出現 ValueError
        c = int(input("請輸入數字 : "))
        break
    except ValueError :
        print("請不要亂輸入")
print("這才是正確輸入 : ",c)




