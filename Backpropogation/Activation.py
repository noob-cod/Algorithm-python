"""
@Date: 2021/9/24 下午9:50
@Author: Chen Zhang
@Brief:
"""
import numpy


class Activation:

    def __call__(self, value: float):
        pass

    def get_gradient(self, value: float) -> float:
        pass


class Relu(Activation):

    def __call__(self, value: float) -> float:
        if value <= 0:
            return 0
        return value

    def get_gradient(self, value: float) -> float:
        if value <= 0:
            return 0
        return 1


if __name__ == '__main__':
    x = 4
    print(Relu()(x))
    print(Relu().get_gradient(x))
