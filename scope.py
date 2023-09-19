# 作用域

"""
变量范围与作用域
LEGB 作用域顺序

L - local 区域
E - enclosed
G - global 全域
B - bulit-in  内建函数

"""

c = 10  # g
def function_one():
    a = 1
    print("a:",a)
    def function_two():
        b = 2
        print("b:",b)  # local
        print("a:",a)  # enclosed
        print("c:",c)
    function_two()
function_one()  

from math import e

print(e)