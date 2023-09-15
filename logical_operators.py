# 逻辑运算符

# and or not

temp = int(input("请输入现在的温度："))
# and 两个条件同时满足
if temp > 0 and temp < 30:
    print("温度是合适的")
else:
    print("温度是不合适的")


# or 两个或多个条件满足其一
if temp <= 0 or temp >= 30:
    print("温度不适宜")
else: 
    print("温度适宜")

# not 