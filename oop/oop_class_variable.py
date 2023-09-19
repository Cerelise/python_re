"""
  类的变量
"""

class Car:
    wheels = 4
    def __init__(self,make,model,year,color):
        # 初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color

car1 = Car("福特","Focus",2023,"白色")

# print(car1.wheels)

car2 = Car("三阳","鬼火",2020,"黑色")
car2.wheels =2
print(car2.wheels)
