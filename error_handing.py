# exception

try:
    x = int(input("请输入一个整数："))
    y = int(input("请输入另一个整数："))
    print(x / y)
# except ValueError:
#     print("请输入整数")
except (ValueError,ZeroDivisionError):
    print("出现错误，请重新输入")
# else:
#     print("else")
finally:
    print("完成")