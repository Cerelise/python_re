 
# 可迭代
for x in range(1,11):
    print(x)


for x in reversed(range(1,11)):
    print(x)


credit_card = "1234-3248-9012-3628"
for x in credit_card:
    if x == '9':
        # continue
        break
    else:
        print(x)

# 字典 dictionary
# 键 key： 值 value
my_dict = {"a":1,"b":2,"c":3}
for x in my_dict:
    print(x)
for key,value in my_dict.items():
    print("key:",key)
    print("value:",value)