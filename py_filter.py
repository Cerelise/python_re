"""
filter
可用来过滤可迭代的数据结构(list,...)

"""


friends = [
  ("Bob",18),
  ("Steven",17),
  ("Michael",19)
]

age_filter = lambda data: data[1] >= 18

can_drink_friends = list(filter(age_filter,friends))

for friend in can_drink_friends:
    print(friend[0])
    print(friend[1])
