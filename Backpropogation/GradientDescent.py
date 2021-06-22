"""
@Date: 2021/4/22 下午9:04
@Author: Chen Zhang
@Brief: for linear function y = wx + b

误差：样本目标值与输出的平方和误差
"""
import numpy as np


def computeError_linear(w, b, points):
    """
    Compute mean square root of y - (w * x + b).

    :param w: Init slop;
    :param b: Init bias;
    :param points: (xi, yi), coordinates of sample points;
    :return: Mean error between y and w * x + b.
    """
    totalError = 0
    for i in range(len(points)):
        totalError += (points[i][1] - (w * points[i][0] + b)) ** 2
    return totalError / float(len(points))


def step_gradient(b_current, w_current, points, learningRate):
    """
    Update b and w with gradient backpropagation by a batch of sample points.

    :param b_current: Init bias;
    :param w_current: Init slop;
    :param points: Lists of sample points
    :param learningRate: The rate of gradient descent.
    :return: [b_result, w_result]
    """
    b_grad = 0  # Gradient of bias
    w_grad = 0  # Gradient of slop
    N = float(len(points))
    for i in range(len(points)):
        b_grad += - (2/N) * (points[i][1] - (w_current * points[i][0] + b_current))  # Gradient of b
        w_grad += - (2/N) * points[i][0] * (points[i][1] - (w_current * points[i][0] + b_current))  # Gradient of w
    b_result = b_current - learningRate * b_grad
    w_result = b_current - learningRate * w_grad
    return b_result, w_result


def gradient_descent(points, init_b, init_w, learningRate, epochs):
    """
    Gradient descent process.

    :param points:  Lists of sample points;
    :param init_b: Init bias;
    :param init_w: Init slop;
    :param learningRate: The rate of gradient descent.
    :param epochs: Number of iteration for gradient descent
    :return: [b_result, w_result]
    """
    for i in range(epochs):
        init_b, init_w = step_gradient(init_b, init_w, np.array(points), learningRate)
    return init_b, init_w


if __name__ == '__main__':
    # Generate data
    data = []
    for i in range(100):
        data.append((i, 8 * i - 135))

    # Linear Regression
    b_result, w_result = gradient_descent(data, 0, 0, 0.0001, 10000)
    print('bias: {}; slop: {}'.format(b_result, w_result))
