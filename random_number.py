import random

# randint()
# print(random.randint(1,10))

# random() 在0~1的范围内生成一个数
# print(random.random())

# 列表中随机选择一个元素
# options = ["石头","剪刀","布"]
# rand_option = random.choice(options)
# print("电脑选择的是：",rand_option)

# 将一个列表打乱
# cards = ["2","L","A","4","5","9","8","3","K","D"]
# random.shuffle(cards)
# print(cards)

# 猜数字游戏
low = 1
high = 100
number = random.randint(low,high)
guesses = 0

while True:
   # 让玩家猜数字
   guess = int(input(f"请猜一个介于{low}~{high}之间的数字："))
   guesses += 1
   if guess < number:
      print("猜的数字太小了")
   elif guess > number:
      print("猜的数字太大了")
   else:
      print(f"恭喜你猜对了！这个数字是{number}")
      print(f"你总共猜了{guesses}次。")
      break