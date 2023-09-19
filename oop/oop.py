"""
面向对象设计

对象 Object
类 Class
实例 Instance

"""

class Car:
    def __init__(self,make,model,year,color):
        # 初始化
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(self.model + "正在行驶")
    
    def stop(self):
        print(self.model + "已停止")

car1 = Car("Toyota","Altis",2021,"蓝色")
car2 = Car("Ford","Kuga",2020,"白色")

