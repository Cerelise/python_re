
price_1 = 3.321
price_2 = -77
price_3 = 15.11

# 小数点的精确度
print(f"价格1为{price_1:.2f}\n"
      f"价格2为{price_2:.2f}\n"
      f"价格3为{price_3:.2f}")

# 加上正负
print(f"价格1为{price_1:+.2f}\n"
      f"价格2为{price_2:+.2f}\n"
      f"价格3为{price_3:+.2f}")

# 对齐
print(f"价格1为{price_1:>10.2f}\n"  # 右对齐 / >
      f"价格2为{price_2:<10.2f}\n"   # 左对齐
      f"价格3为{price_3:^10.2f}")    # 居中

# 混用不同符号
print(f"价格1为 {price_1:<+.2f}\n"
      f"价格2为 {price_2:>+.2f}\n"
      f"价格3为 {price_3:>+.2f}")
