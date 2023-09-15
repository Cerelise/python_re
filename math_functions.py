import math

# 四舍五入、无条件进位、无条件舍去
x = 9.5
#  round(x)
print(math.ceil(x)) # 无条件进位 10
print(math.floor(x)) # 无条件舍去 9

# 圆周率
print(math.pi)

# 计算圆的周长 2πr
radius = float(input("请输入圆的半径："))
c = 2 * math.pi * radius
print(f"圆的周长为：{round(c,2)}")

# 计算圆的面积πr平方
radius2 = float(input("请输入圆的半径："))
area = math.pi * (radius2 ** 2)
print(f"圆的面积为{round(area) }")