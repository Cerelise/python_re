# 字符串方法

# len()、find()、capitalize()
# upper()、lower()、count()、replace()

# help(str) 查询方法

# 用户全名
name = 'cerelise Wong'

# 有几个字符
length = len(name)
print(f"你的全名共有{length}个字符")

# 找到第一个空格
space_position = name.find(" ")
print(f"第一个空格出现在第{space_position}个字符")


# 首字母大写
# 注意：第一个字符必须是字母 首位为空格将不会生效
name_capitalized = name.capitalize()
print("你的全名（首字母大写）:",name_capitalized)

name_upper = name.upper()
print("你的全名（全部大写）:",name_upper)

name_lower = name.lower()
print("你的全名（全部小写）:",name_lower)

# count
# phone_number = input("请输入你的电话号码：")
# dash_count = phone_number.count("-")
# print(f"你的电话号码共有{dash_count}个短横线")

# replace
# phone_number = phone_number.replace("-",' ')
# print(f"你的电话号码为：{phone_number}")


# 练习
'''
  使用者名称不能超过12个字符
  不能包含空格
  不能包含数字
  如果都符合，显式 欢迎 + 使用者名称
'''

user = input("请输入您的用户名：")
user_length = len(user)
if user_length > 12:
    print("您的用户名不能超过12个字符！")
elif user.find(" "):  #  " " in username
    print("您的用户名不能包含空格！")
elif not user.isalpha(): # 查找非英文
    print("您的用户名不能包含数字！")
else: 
    print(f"欢迎，{user}")