"""
获利计算器
总金额 = 本金 * (1 + (利率 / 100)) ** 时间

10000 * 1.05 * 1.05
10000 * 1.05 ** 2
10000 * (1+5/100) ** 2
"""

# 本金
amount = 0
while amount <= 0:
    if amount <= 0:
        print("本金金额不能小于或等于0")
    amount = float(input("请输入本金金额："))

# 利率
rate = 0
while rate <= 0:
    rate = float(input("请输入利率："))
    if rate <= 0:
        print("利率不能小于或等于0")

time = 0
while time <= 0:
    time = float(input("请输入年限："))
    if time <= 0:
        print("年限不能小于或等于0")

print(
  f"金额：{amount}\n"
  f"利率：{rate}\n"
  f"年限：{time}"
)

total = amount * (1 + (rate / 1000)) ** time
print(f"总金额：{total:.2f}")