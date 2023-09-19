"""
列表推导式(list comprehension)
更少的语法创建列表

lambda
平方
"""

# def square(x):
#     return x * x

# list = []
# for i in range(1,11):
#     list.append(square(i))
# print(list)

# square = [ i * i for i in range(1,11)]
# print(square)


grades = [100,90,66,80,46,29,88]
passed_grades = [g for g in grades if g >= 60]
print(passed_grades)