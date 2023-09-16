
goods = []
prices = []

while True:
    good = input("请输入想购买的物品：")
    if good.lower() == "q":
        break
    price = float(input(f"请输入{good}的价格："))
    goods.append(good)
    prices.append(price)

for index,good in enumerate(goods):
    print(f"第{index + 1}件商品是{good},价格为{prices[index]:.2f} ")

total = sum(prices)
print(f"总价：${total}")