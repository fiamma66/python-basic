namelist = ["Elwing", "Bob", "Amy", "Elwing"]
# list 有順序性 可重複
print(namelist)
namelist = namelist + ["Carol"]
print(namelist)
print(namelist[0])
print(namelist[-1])
print(namelist[1:3])
print(namelist[::-1])

# 忘記 JAVA while 用法
# for in 保證群集內所有東西都拿取一次
for a in namelist :
    print(" ! ",a)

b = 0
for a in range(0,10) :
    b = b + (a + 1)
print(b)



