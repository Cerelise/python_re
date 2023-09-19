

class Rectengle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        print("矩形的初始化 done")


class Square(Rectengle):
    def __init__(self,length,width):
        super().__init__(length,width)
        print("正方形的初始化已执行")


# square = Square(500,300)

class Cube(Rectengle):
    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height
        print(f"立方体的长宽高是：{length},{width},{height}")

cube = Cube(500,300,100)