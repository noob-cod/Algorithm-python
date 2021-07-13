"""
@Date: 2021/6/4 下午7:48
@Author: Chen Zhang
@Brief: 简单工厂模式

一个具体工厂、一个抽象产品类、多个具体产品类

当需要添加新的产品时：
    新产品必须符合抽象类的特征
    添加新产品的具体产品类，该具体类继承于抽象产品类
"""


class SimpleFactory:

    def __init__(self):
        pass

    @classmethod
    def make_product(cls, product_id):
        if product_id == 0:
            print('正在生产产品1......')
            return ProductImplement1()
        elif product_id == 1:
            print('正在生产产品2......')
            return ProductImplement2()
        else:
            pass


class Product:

    def __init__(self):
        pass

    def get_name(self):
        """获得产品名"""
        pass

    def get_price(self):
        """获得产品价格"""
        pass


class ProductImplement1(Product):

    def get_name(self):
        return '产品1'

    def get_price(self):
        return '100元'


class ProductImplement2(Product):

    def get_name(self):
        return '产品2'

    def get_price(self):
        return '50元'


class SimpleFactoryTest:

    @staticmethod
    def test():
        product = SimpleFactory().make_product(int(input('请输入产品的代号：')))
        print('-' * 40)
        print('生产出的产品信息如下：')
        print('-' * 40)
        print('产品类别：', product.get_name())
        print('产品价格：', product.get_price())
        print('-' * 40)
        print()


if __name__ == '__main__':
    # product = SimpleFactory().make_product(int(input('请输入产品的代号：')))
    # print('-' * 40)
    # print('生产出的产品信息如下：')
    # print('-' * 40)
    # print('产品类别：', product.get_name())
    # print('产品价格：', product.get_price())
    # print('-' * 40)
    # print()
    SimpleFactoryTest().test()
