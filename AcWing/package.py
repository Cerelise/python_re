# 物品数量 背包容积
# N,V = map(int,input().split())
# goods_dict = {}
# total_volume = 0
# total_value = 0

# for i in range(N):
#     volume,value = map(int,input().split())
#     goods_dict.update({volume:value})

# print(goods_dict)
import math

N, V = map(int, input().split())
goods = []

for i in range(N):
    volume, value = map(int, input().split())
    goods.append((volume, value, value / volume))  # 将物品按单位价值(value/volume)排序

goods.sort(key=lambda x: x[2], reverse=True)  # 按单位价值降序排序

total_value = 0
current_volume = 0

for volume, value, unit_value in goods:
    if current_volume + volume <= V:
        current_volume += volume
        total_value += value
    else:
        remaining_space = V - current_volume
        total_value += unit_value * remaining_space
        break

print(math.floor(total_value))