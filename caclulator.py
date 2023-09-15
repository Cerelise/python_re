# 简易计算器

operator = input("请输入运算符：")
num1 = float(input("请输入第一个数字："))
num2 = float(input("请输入第二个数字："))

if operator == "+":
   result = num1 + num2
elif operator == "-":
   result = num1 - num2
elif operator == "*":
   result = num1 * num2
elif operator == "/":
   result = num1 / num2
else:
   print("运算符无效")

print(f"运算结果是{round(result)}")