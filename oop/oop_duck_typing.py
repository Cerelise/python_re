"""
鸭子类型 Duck Typing

即使没有继承的关系，也可以当做同一类型的类别使用
"""

class Duck:
    def walk(self):
        print("鸭子在走路")

    def talk(self):
        print("鸭子在嘎嘎叫")

class Chilken:
    def walk(self):
        print("鸡在走路")

    def talk(self):
        print("鸡在咕咕叫")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
duck = Duck()
person = Person()
person.catch(duck)

chilken = Chilken()
person.catch(chilken)

