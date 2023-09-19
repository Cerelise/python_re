"""
将对象作为参数
"""

class Car:
    color = None

def change_color(car,color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()

change_color(car1,"红色")
change_color(car2,"绿色")
change_color(car3,"蓝色")


print(car1.color)
print(car2.color)
print(car3.color)