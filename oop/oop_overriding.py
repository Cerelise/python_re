"""
 对象中的方法重写
"""

class Animal:
    def eat(self):
        print("动物正在吃东西")


class Manmal(Animal):
    def hi(self):
        print("我是哺乳类")
    pass

class Cat(Manmal):
    def eat(self):
        print("小猫正在喝水")

cat = Cat()

cat.eat()