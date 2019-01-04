# 不定參數
# * 組合為 list
# ** 組合為 dict
def add_multiple(*nlist):
    result = 0
    for n in nlist:
        result = result + n
    return result

print(add_multiple(3,5,7,9))

# 不一定要帶入的參數
# 不一定要指定倍數
# 在參數中預先帶入預設值
# *重要* : 從第一個有預設值的參數
#          後面的參數都必須有
def add_advanced(n1, n2, n3=1, n4=1):
    return (n1 + n2) * n3 / n4

print(add_advanced(1,2,3))
print(add_advanced(1,2,))
# 指定參數 可以跳過部分參數設定 如 : 有預設值的
print(add_advanced(1,2,n4=2))