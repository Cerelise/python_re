# list 列表
fruits = ['apple','orange','banana','coconut']
# [0-3]

# for f in fruits:
#     print(f,end=" ")

# 添加
fruits.append("grapes")

# 删除
fruits.remove("coconut")

# 寻找某个元素的下标
print(fruits.index("banana"))

# 允许多个相同元素
fruits.append('apple')

# 统计相同元素个数
print(fruits.count("apple"))

# 反转数组
fruits.reverse()

# set
fruits_set = {"苹果","橙子","香蕉"}
fruits_set.add("苹果")
fruits_set.add("西瓜")

if "苹果" in fruits_set:
    print("有苹果")


# tuple
# 不可修改
fruits_tuple = ("苹果","橙子","香蕉","苹果","苹果")
res = fruits_tuple.count("苹果")
print(res)
index_orange = fruits_tuple.index("橙子")
print(f"橙子的位置{index_orange}") # 从0开始

