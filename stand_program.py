"""
自动贩卖机程序
使用字典存储菜单(物品名：价格)
while循环用于选择菜单里的项目
如果用户选择了一个项目，会将此项添加至购物车中
最后我们会根据用户的选择计算订单总价
"""

menu = {
  "披萨":300,
  "爆米花":200,
  "薯条":90,
  "薯片":60,
  "软面包条":120,
  "苏打水":60,
  "柠檬水":90,
}

print("菜  单")
print("----------")

for item,price in menu.items():
    print(f"{item}:{price}")

cart = []
total = 0

while True:
    food = input("请输入一个菜单项目(输入q以结束)：")
    if food == "q":
        break
    elif menu.get(food) is None:
        print("没有该商品！")
    else:
        cart.append(food)
        total += menu.get(food)

for item in cart:
    print(item,end=" ")
print(f"总共{total}元")