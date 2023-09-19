"""
Lambda 有函数的功能 一行就可以写完
"""

# double

def double(x):
    return x * 2

print(double(10))


double2 = lambda x:x*2
print(double2(50))


# 2
multiply = lambda x,y:x * y
print(multiply(5,10))


# 3 if else
res = lambda x:f"{x}是偶数" if x % 2 == 0 else f"{x}是奇数"
print(res(10)) 

# 4 处理字符串

full_name = lambda first_name,last_name:f"{first_name} {last_name}"
print(full_name("Wong","Cerelise"))
