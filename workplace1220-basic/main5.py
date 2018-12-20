a = "hellohello\thello\b\n"
# len 只表示字串長度 與print出來的字串無關
# 故\b(backspace) 及 \t(Tab) 都是一個字元
print(len(a))
# replace 有回傳值 但不改變原字串
b = a.replace("hello", "goodbye")
print(a)
a = a.replace('hello', 'goodbye', 1)
print(a)
print(b)

# 字串比較有區分大小寫
print("apple" == "Apple")
print('apple'.upper() == 'Apple'.upper())

# List 專屬
namelist = ["Elwing", "Amy", "Elwing"]
b = namelist.append("Bob")
print(namelist)
# append 無回傳值 b 為 None
print(b)
"""
# 千萬小心下面的狀況
namelist = namelist.append("Carol")
# 上面親手做掉 namelist
print(namelist)
# namelist 化為烏有
"""
del namelist[-1]
print(namelist)
namelist.remove("Elwing")  # 只刪除第一個Elwing
print(namelist)

# 參考用
oldlist = ["Elwing", "Amy", "Elwing", "Carol"]

newlist = [o for o in oldlist if not o == "Elwing"]
print("Newlist : ", newlist)

