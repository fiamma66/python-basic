person = ("Elwing",175,75)

print(person)
print(person[0])
print(person[-1])

# 反過來拿取
print(person[::-1])

# 小括號後 加逗號 成為 Tuple
person = person + ("Taipei",)
print(person)

person = person + ("Male","Movie")
print(person)

# del person [2]
# python 本身不支援 也不希望做刪除動作
print(person[:3]+person[4:])