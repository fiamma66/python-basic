person = {"name": "Elwing", "height": 175, "weight": 75}
print(person)

# print出 "name" 的 值
print(person["name"])

# 加入gender = 'M'
person["gender"] = "M"
print(person)

# height = 180
person["height"] = "180"
print(person)

# weight = weight + 5
person["weight"] = person["weight"] + 5
print(person)

# 刪除
del person["gender"]
print(person)

# for in
for key in person:
    print("-", key, person[key])


