"""
  父类 -> 子类

  动物

"""

class Animal:
    aLive = True

    def eat(self):
        print("这个动物在吃东西")

    def sleep(self):
        print("这个动物在睡觉")

# 兔子
class Rabbit(Animal):
    def jump(self):
        print("这只兔子在跳跃")

class Fish(Animal):
    def swim(self):
        print("鱼正在游泳")

class Hawk(Animal):
    def fly(self):
        print("老鹰正在飞")

animal = Animal()
rabbit = Rabbit()

rabbit.sleep()