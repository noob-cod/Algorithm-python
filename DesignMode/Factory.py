"""
@Date: 2021/6/4 下午7:48
@Author: Chen Zhang
@Brief: Implement of factory mode
"""


class Fruit(object):
    def __init__(self):
        pass

    def print_color(self):
        pass


class Apple(Fruit):
    def __init__(self):
        # super(Apple, self).__init__()   python2
        super(Apple, self).__init__()

    def print_color(self):
        print("Apple is in red.")


class Orange(Fruit):
    def __init__(self):
        super(Orange, self).__init__()

    def print_color(self):
        print("Orange is in orange.")


class FruitFactory(object):
    """工厂类"""
    fruits = {"apple": Apple, "orange": Orange}

    def __new__(cls, name):
        if name in cls.fruits.keys():  # 根据传参自动产生对应的类
            return cls.fruits[name]()
        else:
            return Fruit()


if __name__ == '__main__':
    f1 = FruitFactory("apple")  # 用不同的键值指示工厂类产生不同的新类
    f2 = FruitFactory("orange")
    f1.print_color()
    f2.print_color()
