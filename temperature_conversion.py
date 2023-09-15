# 温度转换

unit = input("请输入当前的温度单位(摄氏C,华氏F):")
temp = float(input("请输入温度："))

if unit == "C":
    temp = round(9 * temp / 5 + 32)
    print(f"当前的温度为{temp}度F")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9)
    print(f"当前的温度为{temp}度C")
else:
    print("非法的温度单位")