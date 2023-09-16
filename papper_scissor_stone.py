# 猜拳游戏

"""
 猜拳游戏是一种流行的游戏，通常由两个人玩，但也可以由一个人和电脑玩
 游戏的目标是在三种手势中选择一个，并以某种方式规则来决定胜负。以下是猜拳游戏的规则：

 石头(Rock) 赢 剪刀(Scissors)
 剪刀(Scissors) 赢 布(Paper)
 布(Paper) 赢 石头(Rock)

 在游戏开始之前，每个玩家都必须选择剪刀、石头、布中的一个。而在决定胜负时，根据上述规则进行比较。
 如果两个玩家选择相同的手势，则比赛以平局结束。
"""
import random

player = None
computer = None
running = True
options = ("剪刀","石头","布")

while running:
    player = input("请输入剪刀、石头、布：")
    while player not in options:
        input("输入错误，请输入剪刀、石头、布：")
    computer = random.choice(options)
    print(f"玩家：{player}，电脑：{computer}")

    if player == computer:
        print("平手")
    elif player == "剪刀" and computer == "布":
        print("玩家胜利")
    elif player == "石头" and computer == "剪刀":
        print("玩家胜利")
    elif player == "布" and computer == "石头":
        print("玩家胜利")
    else:
        print("电脑胜利")
    play_again = input("再玩一局？(y/n)").lower()
    if not play_again == "y":
        running = False
print("完成")