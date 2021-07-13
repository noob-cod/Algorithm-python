"""
@Date: 2021/7/13 下午6:11
@Author: Chen Zhang
@Brief: 工厂方法模式

一个抽象工厂类、多个具体工厂类、一个抽象产品类、多个具体产品类
每个具体工厂类生产的产品都继承自同一个抽象产品类
每个具体工厂类只生产一个具体产品类
"""


class AbstractFactory:

    def __init__(self):
        pass

    def make_product(self):
        pass


class Nintendo(AbstractFactory):

    def make_product(self):
        print('正在生产Switch...')
        return Switch()


class Sony(AbstractFactory):

    def make_product(self):
        print('正在生产PS5...')
        return PS5()


class Microsoft(AbstractFactory):

    def make_product(self):
        print('正在生产XBOX...')
        return XBOX()


class Product:

    def __init__(self):
        pass

    def get_name(self):
        pass

    def get_price(self):
        pass


class Switch(Product):

    def get_name(self):
        return 'Switch'

    def get_price(self):
        return '2000元'


class PS5(Product):

    def get_name(self):
        return 'PS5'

    def get_price(self):
        return '3500元'


class XBOX(Product):

    def get_name(self):
        return 'XBOX'

    def get_price(self):
        return '2500元'


class AbstractFactoryTest:

    factory_dic = {'switch': Nintendo, 'ps5': Sony, 'xbox': Microsoft}

    @staticmethod
    def test():
        video_gamer = input('请输入想要的产品：').lower()
        try:
            product = AbstractFactoryTest.factory_dic[video_gamer]().make_product()
        except KeyError:
            product = None
        print()
        print('-' * 40)
        print('生产出的产品信息如下：')
        print('-' * 40)
        print('产品类别：', end='')
        try:
            print(product.get_name())
        except (AttributeError, UnboundLocalError):
            print('无')
        print('产品价格：', end='')
        try:
            print(product.get_price())
        except (AttributeError, UnboundLocalError):
            print('无')
        print('-' * 40)
        print()


if __name__ == '__main__':
    AbstractFactoryTest().test()
