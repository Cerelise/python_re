"""
方法链 Method Chaining

car.turn_on().drive().brake().turn_off()

"""


class Car:
    def turn_on(self):
        print("你启动了引擎")

        # 传回事件本身
        return self

    def drive(self):
        print("你开车了")
        return self
    
    def brake(self):
        print("你踩了刹车")
        return self

    def turn_off(self):
        print("你关闭了引擎")
        return self

car = Car()

car.turn_on().drive().brake().turn_off()