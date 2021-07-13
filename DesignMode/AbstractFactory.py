"""
@Date: 2021/7/13 下午6:59
@Author: Chen Zhang
@Brief: 抽象工厂模式

一个抽象工厂类、多个具体工厂类、多个抽象产品类、多个具体产品类
一个具体工厂提供不同的接口生产不同类型的产品
同一抽象产品类的不同具体产品可由不同具体工厂生产
"""


class AbstractFactory:
    """抽象工厂类"""
    def __init__(self):
        pass

    def make_video_gamer(self):
        pass

    def make_laptop(self):
        pass

    def make_smartphone(self):
        pass


class Sony(AbstractFactory):
    """具体工厂类"""
    def make_video_gamer(self):
        return PS5()


class Microsoft(AbstractFactory):
    """具体工厂类"""
    def make_video_gamer(self):
        return XBOX()

    def make_laptop(self):
        return Surface()


class Huawei(AbstractFactory):
    """具体工厂类"""
    def make_laptop(self):
        return MateBook()

    def make_smartphone(self):
        return P40()


class Xiaomi(AbstractFactory):
    """具体工厂类"""
    def make_laptop(self):
        return Redmibook()

    def make_smartphone(self):
        return Xiaomi11()


class Product:

    def __init__(self):
        pass

    def get_name(self):
        pass

    def get_price(self):
        pass


class VideoGamer(Product):
    """抽象产品类"""
    pass


class PS5(VideoGamer):
    """具体产品类"""
    def get_name(self):
        return 'PS5'

    def get_price(self):
        return '2500元'


class XBOX(VideoGamer):
    """具体产品类"""
    def get_name(self):
        return 'XBOX'

    def get_price(self):
        return '2500元'


class Laptop(Product):
    """抽象产品类"""
    def get_gpu(self):
        pass


class MateBook(Laptop):
    """具体产品类"""
    def get_name(self):
        return 'MateBook14'

    def get_price(self):
        return '6000元'

    def get_gpu(self):
        return 'NVIDIA GeForce MX350, 2GB GDDR5'


class Redmibook(Laptop):
    """具体产品类"""
    def get_name(self):
        return 'Redmibook Pro 14 锐龙版'

    def get_price(self):
        return '4499元'

    def get_gpu(self):
        return 'AMD Radeon Graphics 集成显卡'


class Surface(Laptop):
    """具体产品类"""
    def get_name(self):
        return 'Microsoft Surface Pro 7'

    def get_price(self):
        return '7588元'

    def get_gpu(self):
        return '核显'


class SmartPhone(Product):
    """抽象产品类"""
    def get_cpu(self):
        pass


class Xiaomi11(SmartPhone):
    """具体产品类"""
    def get_name(self):
        return 'Xiaomi 11'

    def get_price(self):
        return '3799元'

    def get_cpu(self):
        return '高通骁龙888'


class P40(SmartPhone):
    """具体产品类"""
    def get_name(self):
        return 'P40'

    def get_price(self):
        return '4488元'

    def get_cpu(self):
        return '麒麟990 5G SoC芯片'


class AbstractFactoryTest:

    factory_dic = {
        'sony': Sony,
        'microsoft': Microsoft,
        'huawei': Huawei,
        'Xiaomi': Xiaomi
    }

    product_dic = {
        'vediogamer': 0,
        'laptop': 1,
        'smartphone': 2
    }

    @staticmethod
    def test():
        product_type = input('请输入想要的产品类型：').lower().replace(' ', '')
        product_name = input('请输入产品品牌：').lower().replace(' ', '')

        try:
            if AbstractFactoryTest.product_dic[product_type] == 0:
                product = AbstractFactoryTest.factory_dic[product_name]().make_video_gamer()
            elif AbstractFactoryTest.product_dic[product_type] == 1:
                product = AbstractFactoryTest.factory_dic[product_name]().make_laptop()
            elif AbstractFactoryTest.product_dic[product_type] == 2:
                product = AbstractFactoryTest.factory_dic[product_name]().make_smartphone()
            else:
                product = None
        except KeyError:
            product = None

        print()
        print('-' * 40)
        print('产品信息如下：')
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
        try:
            print('GPU: ', product.get_gpu())
        except (AttributeError, UnboundLocalError):
            pass
        try:
            print('CPU: ', product.get_cpu())
        except (AttributeError, UnboundLocalError):
            pass
        print('-' * 40)
        print()


if __name__ == '__main__':
    AbstractFactoryTest().test()
