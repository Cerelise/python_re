"""
map(函数,可迭代的[列表])
"""


store = [
  ("衬衫",200),
  ("裤子",300),
  ("夹克",500)
]

# to_rmb = lambda data:(data[0],data[1] * 1.7)

# store_rmb = list(map(to_rmb,store))
# print(store_rmb)

to_usd = lambda data:(data[0],round(data[1] / 1.7))
store_usds = list(map(to_usd,store))

for item in store_usds:
    print(item)