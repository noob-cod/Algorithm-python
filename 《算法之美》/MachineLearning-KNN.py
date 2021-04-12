"""
@Date: Saturday, March 27, 2021
@Author: Chen Zhang
@Brief: K最近邻算法 - 分类

算法概述：
    KNN用于判断数据所属的类别。通过统计样本点附近K个欧氏距离最近的训练集中各类别点占的比例，将占比
    最大的类别作为样本点的类别。
"""
from typing import List
import numpy as np


class KNN:
    def __init__(self, data, labels: List, K=9):
        """

        :param data: 训练集数据，[(x1, y1), (x2, y2), ... ]
        :param labels: 训练集标注，与data对应， [label1, label2, ... ]
        :param K: 统计的邻居数
        """
        assert len(data) == len(labels), 'Unmatchable dataset!'
        assert K <= len(data), 'K is over size!'
        self.dataset = np.array(data)  # 接收列表格式的训练集数据
        self.labels = labels  # 接收训练集标签
        self.num = len(self.dataset)  # 样本的数量
        self.K = K  # 选取的最近邻数量

    def predict(self, sample):
        """预测sample所属的类别"""
        euclidean_distance = []
        for i in range(self.num):
            euclidean_distance.append(
                (np.sqrt((self.dataset[i][0] - sample[0]) ** 2 + (self.dataset[i][1] - sample[1]) ** 2), self.labels[i])
            )  # 按(距离，标签）的格式保存

        # 按距离升序排序
        euclidean_distance.sort(key=lambda x: x[0])

        # 统计K个最近的训练集样本中的标注
        L = {}  # 存放统计结果
        for i in range(self.K):
            if euclidean_distance[i][1] not in L:
                L[euclidean_distance[i][1]] = 1
            else:
                L[euclidean_distance[i][1]] += 1

        # 对字典按value降序排序
        result = sorted(L.items(), key=lambda x: x[1], reverse=True)
        if len(result) == 1:
            print("It's %.1f%% %s." % ((result[0][1] / self.K) * 100, result[0][0]))
            print('\n')
        elif result[0][1] != result[1][1]:
            print("It's %.1f%% %s." % ((result[0][1] / self.K) * 100, result[0][0]))
            print('\n')
        else:
            print('It may belong to:')
            x = 0
            while result[0][1] == result[x][1]:
                print('    %s  %.1f%%' % (result[x][0], (result[x][1] / self.K) * 100))
            print('\n')


if __name__ == '__main__':
    trainData = np.array([[23, 8], [26, 9], [21, 7], [23, 9], [19, 11], [18, 9], [20, 10]])
    trainLabel = ['小鲫鱼', '小鲫鱼', '小鲫鱼', '小鲫鱼', '小蝌蚪', '小蝌蚪', '小蝌蚪']
    t_data = [20, 11]
    knn = KNN(trainData, trainLabel, 3)
    knn.predict(t_data)
