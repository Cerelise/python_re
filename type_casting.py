# 类型转换
name = "John"
age = 21
gpa = 1.9
is_student = True

# 显式、隐式转换

print(type(name)) 
print(type(age))
print(type(gpa))
print(type(is_student))

# 显式
age = float(age)
print(age)
print(type(age))

is_student = str(is_student)
print(type(is_student))

# 隐式
x = 10
y = 2.0
x = x / y
print(type(x)) # float
