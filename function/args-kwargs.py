# args => arguments 任意数量的参数 * => tuple
# kwargs => 关键字 + args (keyword args) ** => dictionary

# args

# def add(a,b):
#     return a + b



def add(*args):
    total = 0
    for arg in args:
        print(f"arg：{arg}")
        total += arg
    return total

print(add(1,2,5))