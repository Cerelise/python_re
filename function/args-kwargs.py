# args

# def add(a,b):
#     return a + b


# args => arguments 任意数量的参数 * => tuple
"""
def add(*args):
    total = 0
    for arg in args:
        print(f"arg：{arg}")
        total += arg
    return total
"""

# print(add(1,2,5))


# kwargs => 关键字 + args (keyword args) ** => dictionary

def print_info(**kwargs):
    for key,value in kwargs.items():
        print(f"key：{key} value：{value}")

print_info(name="Alex",age="25",occuption="engineer")

