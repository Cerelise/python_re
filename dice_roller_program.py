# 骰子游戏

# 骰出骰子以后，显示总和图案
# 使用Unicode字符来制作骰子图案

import random

dice_art = {
    1: (
        "┌───────┐",
        "│       │",
        "│   ●   │",
        "│       │",
        "└───────┘",
    ),
    2: (
        "┌───────┐",
        "│ ●     │",
        "│       │",
        "│     ● │",
        "└───────┘",
    ),
    3: (
        "┌───────┐",
        "│ ●     │",
        "│   ●   │",
        "│     ● │",
        "└───────┘",
    ),
    4: (
        "┌───────┐",
        "│ ●   ● │",
        "│       │",
        "│ ●   ● │",
        "└───────┘",
    ),
    5: (
        "┌───────┐",
        "│ ●   ● │",
        "│   ●   │",
        "│ ●   ● │",
        "└───────┘",
    ),
    6: (
        "┌───────┐", # 0
        "│ ●   ● │", # 1
        "│ ●   ● │", # 2
        "│ ●   ● │", # 3
        "└───────┘", # 4
    ),
}

# print(dice_art.get(6))
num_dice = int(input("请输入要掷几个骰子："))
dice = []
for i in range(num_dice):
    dice_number = random.randint(1,6)
    dice.append(dice_number)


def get_dice_number(number):
    for i in range(5):
      print(dice_art.get(number)[i])

for i in dice:
    get_dice_number(i)
print(f"总和：{sum(dice)}")