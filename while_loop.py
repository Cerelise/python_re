
# 1
name = ''
while name == "":
    name = input("请输入您的名字：")
print(f"你好,{name}")


# 2
food = input("请输入你最喜欢吃的食物：")
while food != "q":
    print(f"你最喜欢吃的食物是{food}")
    food = input("请输入你最喜欢吃的食物：")
print("Bye")

# 3
num = int(input("请输入1到10之间的数字："))
while num < 1 or num > 10:
    print(f"你输入的数字{num}无效")
    num = int(input("请输入1到10之间的数字："))
print(f"你输入了{num}")