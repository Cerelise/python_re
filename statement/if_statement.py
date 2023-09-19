# if else elif控制流程

# Boolean 布尔值
for_sale = True
if for_sale:
  print("此项目正在出售")
else:
  print("此项目为出售")

# if else
age = int(input("请输入你的年龄："))
if age >= 18:
   print("你可以注册")
else:
  print("你必须年满18岁才能注册")


# elif => else if 简写
age = int(input("请输入你的年龄："))
if age >= 100:
   print("你年龄太大，不可以注册")
elif age >= 18:
   print("你可以注册")
elif age < 0:
  print("你还没出生")
else:
  print("你必须年满18岁才能注册")

# 实作
