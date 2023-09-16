"""
 键 => 值
 key => value 
"""

capital = {
  "United States":"Washington DC",
  "Japan":"Tokyo",
  "France":"Paris",
  "Russia":"Moscow"
}

# get 获取键值对
print(capital.get("Japan"))

# update 更新键值对
capital.update({"Germany":"Berlin"})
# capital.update({"United States":"New York"})
print(capital)

# pop() 删除键值对
capital.pop("France")
print(capital)

# values() 获取所有值
print(capital.values())

# items() 获取所有键值对
print(capital.items())