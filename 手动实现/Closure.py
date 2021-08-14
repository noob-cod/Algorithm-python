"""
@Date: 2021/8/14 下午1:55
@Author: Chen Zhang
@Brief:  闭包(closure)

1、闭包解决的问题
    使得函数外部打破了“函数作用域”的束缚，可以访问函数内部的变量。

2、闭包的概念
    通过将变量定义在函数内部，并定义一个内部函数。通过内部函数外层函数的变量进行操作并返回操作结果，
    外层函数仅返回内层函数的函数签名。从而实现对外层函数内变量的保护，同时由于内层函数的引用使得外
    层函数的变量不会被内存自动回收。

3、闭包的优点
    打破了“函数作用域”的束缚

4、闭包的缺点
    闭包维持函数内部的变量，使其得不到释放，可能造成内存泄露

5、解决闭包可能导致的内存泄露的方法
    (1)将事件处理函数（可能是指闭包中的内层函数）定义在外部，解除闭包；
    (2)或者在定义事件处理函数的外部函数中，删除对dom的引用。
"""


# 闭包举例1
def area(factor=1.0):
    def func(a, b):
        return factor * a * b  # 计算面积。a, b为边长，当factor为1时，计算的是矩形的面积
    return func


def test1():
    a = 3
    b = 4

    triangle_area = area(factor=0.5)  # 利用闭包实现了一个计算三角形面积的函数
    print('底为{}，高为{}的三角形的面积为:'.format(a, b))
    print(triangle_area(a, b))

    rectangle_area = area()  # 利用闭包实现了一个计算矩形面积的函数
    print('宽为{}，高为{}的矩形的面积为:'.format(a, b))
    print(rectangle_area(a, b))


# 闭包举例2
def sum_func(inputs):
    """
    这是一个可以对输入值加50后输出的函数，但永远只能加50
    """
    var = 50
    return var + inputs


def outer_func(x):
    """
    这是一个对sum_func改造后的闭包，可以通过传入不同的x，以实现不同输出的模式。
    例如，当x为100时，可以得到一个对输入值加100后输出的新的函数
    """
    var = 50
    if x != var:
        var = x

    def inner_func(inputs):
        return inputs + var

    return inner_func


def test2():
    inputs = 1

    print('直接调用sum_func()的结果为：')
    print(sum_func(inputs))

    sum_100 = outer_func(100)
    print('利用闭包构造一个可以计算对输入值加100的函数，其计算的结果为')
    print(sum_100(inputs))


if __name__ == '__main__':
    pass
