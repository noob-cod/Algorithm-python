"""
@Date: 2021/6/4 下午7:40
@Author: Chen Zhang
@Brief: Implement of Singleton
"""


class Singleton(object):
    """单例模式"""

    _instance = None

    def __new__(cls, *args, **kwargs):
        """__new__()方法是类中真正创建实例的方法，通过全局的变量_instance来限制可创建的实例的数量"""
        # 当系统中不存在实例的时候，创建一个新的实例并赋给类的全局变量
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        # 直接返回类的全局变量_instance所指向的实例
        return cls._instance


if __name__ == '__main__':
    s1 = Singleton()
    s2 = Singleton()
    print(s1)
    print(s2)
