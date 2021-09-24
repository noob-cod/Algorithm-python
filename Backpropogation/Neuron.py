"""
@Date: 2021/9/24 下午8:36
@Author: Chen Zhang
@Brief:

神经元的功能：
    1. 接收多个float类型的输入
    2. 为每个输入维护一个权值w
    3. 产生一个输出
    4. 可以接收任意类型的激活函数
    5. 维护一个偏置标志和偏置值
"""
import numpy as np

from typing import List
from Activation import *


class Neuron:

    def __init__(self,
                 input_dim: int,
                 use_bias: bool = False,
                 init_bias: float = 0.0,
                 activation: Activation = Relu,
                 trainable: bool = True
                 ):
        """
        神经元
        :param input_dim: 整型值，神经元的输入维度；
        :param use_bias: 布尔值，偏置标志位；
        :param init_bias: 浮点数，偏置初始值，默认为0.0
        :param activation: 激活函数；
        :param trainable: 布尔数，权重可更新标志，默认为True
        """
        self.input_dim = input_dim
        self.use_bias = use_bias
        self.activation = activation
        self.trainable = trainable
        if self.use_bias:
            self.bias = init_bias

        self.weights = np.ndarray((self.input_dim,))  # 权重列表
        self.weights.fill(0.1)  # 初始值全部为0.1
        self.last_inputs = None  # 上一次的输入
        self.output = 0  # 初始输出为

    def __call__(self, inputs: List[float]) -> float:
        """计算神经元的输出"""
        if len(inputs) != self.input_dim:
            raise ValueError
        self.output = (inputs * self.weights).sum()  # 计算神经元的输出结果
        self.last_inputs = np.array(inputs)  # 记录本次输出结果，共下一次更新使用

        if self.use_bias:
            self.output += self.bias

        if self.activation:
            return self.activation()(self.output)

        return self.output

    def update_weights(self,
                       error_list: List[float],
                       rate: float = 0.01) -> None:
        """更新权重"""
        if self.trainable:
            error_sum = sum(error_list)  # 反向传播到当前神经元的误差
            gradient = 1.0
            if self.activation:
                gradient *= self.activation().get_gradient(error_sum)  # 乘以误差对激活函数的导数
            gradient *= self.last_inputs  # 乘以激活函数对权值的导数，即上一次输出的结果
            self.weights = self.weights - rate * gradient  # 用rate更新权值

    def backward(self, error_list: List[float]):
        error_sum = sum(error_list)
        errors = self.weights * error_sum  # 反向传播到上层神经元的误差等于“下层神经元传回误差 x 连接权重 x 误差对激活函数的导数”
        if self.activation:
            errors = errors * self.activation()(error_sum)
        return errors

    def get_weight(self):
        print(self.weights)


if __name__ == '__main__':
    x = [0.6, 0.7, 0.8]
    neuron = Neuron(len(x))
    print(neuron(x))

    error = [0.4, 0.3]
    neuron.update_weights(error)
    neuron.get_weight()

    print(neuron.backward(error))
