"""
獠牙运算符
赋值表达式 :=
赋值运算子 =
python 3.8+
"""

# happy = True
# print(happy)

# print(happy := True)

foods = []
while (food := input("你喜欢什么食物？")) != 'quit':
    # if food == 'quit':
    #     break
    foods.append(food)

print(foods)