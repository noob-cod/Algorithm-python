"""
@Date: 2021/7/27 下午6:26
@Author: Chen Zhang
@Brief: 弗洛伊德算法

1、定义
    解决给定的加权图中顶点间的最短路径

2、原理
    (1)初始化map矩阵，矩阵中的元素map[i][j]代表顶点i到顶点j的权值，不相邻顶点的权值为0，map[i][i]=0
    (2)以顶点A（假设是第一个顶点）为中介点，若a[i][j] > a[i][1] + a[1][j]，则设置a[i][j] = a[i][1] + a[1][j]
    (3)重复步骤(2)直到用所有的顶点都更新过一次map矩阵.

3、特点
    (1) 时间复杂度O(n^3)，空间复杂度O(n^2)，不适合大量数据的计算
    (2) 图中不能包含带有负权的回路，边权可正可负
    (3) 执行一次算法就可以计算出图中任意两点间的最短路径

4、与Dijkstra算法的异同
    相同点：
        (1)都是计算带权有向图中的最短路径

    不同点：
        (1)Floyd算法可以计算包含负权的图
        (2)在稠密图上的效率高于Dijkstra算法
        (3)Floyd算法计算任意两点间的最短距离，Dijkstra算法计算源点到图中所有其他点的最短距离
        (4)Floyd时间复杂度高，不适合大量数据。
"""


class Graph:
    """基于二维数组的图的实现"""
    def __init__(self, sourceCollections=None):
        self._graph = None
        self._name = {}  # 名称到数组索引的映射
        self._index_to_name = {}
        self._vertex_num = 0

        if sourceCollections:
            if isinstance(sourceCollections, list) and isinstance(sourceCollections[0], list):
                if len(sourceCollections) == len(sourceCollections[0]):
                    self._graph = sourceCollections
                    self._vertex_num = len(sourceCollections)

    def isEmpty(self):
        """判断图是否构建"""
        return self._vertex_num == 0

    def get_vertex_num(self):
        """获得顶点的数量"""
        return self._vertex_num

    def set_names(self, names):
        """
        :param names: 数组。 顶点名称。
        """
        if self.isEmpty():
            print('图尚未构建，无法命名顶点！')
            return

        if isinstance(names, list) and isinstance(names[0], str):
            n = len(names)
            if n == self.get_vertex_num():
                for i in range(n):
                    self._name[names[i]] = i
                    self._index_to_name[i] = names[i]

    @property
    def graph(self):
        return self._graph

    @property
    def names(self):
        return self._name

    def get_index_by_name(self, name):
        """根据源点的名称，获得该点的位置索引"""
        if name in self._name:
            return self._name[name]

    def get_name_by_index(self, index):
        if index < self.get_vertex_num():
            return self._index_to_name[index]

    def get_neighbour_by_name(self, name):
        """根据源点的名称获得（相邻点名称，边的权重）的数组"""
        if name in self._name:
            res = []
            for item in self._name.keys():
                if self.graph[self.get_index_by_name(name)][self.get_index_by_name(item)] not in [0, None]:
                    res.append((item, self.graph[self.get_index_by_name(name)][self.get_index_by_name(item)]))
            return res

    def get_weight_by_endings(self, start, end):
        """根据起点和终点获得边的权重"""
        if not isinstance(start, str) or not isinstance(end, str):
            return
        if start not in self.names or end not in self.names:
            return

        return self.graph[self.get_index_by_name(start)][self.get_index_by_name(end)]


def floyd(graph):
    """弗洛伊德算法，返回图中任意两个源点之间的最短路径矩阵"""

    n = graph.get_vertex_num()
    distance = graph.graph  # 获得带有相邻顶点权重的初始的图

    for v in range(n):  # 迭代顶点
        for i in range(n):  # 迭代行
            if i == v:
                continue
            for j in range(n):  # 迭代列
                if distance[i][v] is not None and distance[v][j] is not None:
                    if distance[i][j] is None:
                        distance[i][j] = distance[i][v] + distance[v][j]  # 原来的值为无穷大
                    else:
                        distance[i][j] = min(distance[i][j], distance[i][v]+distance[v][j])  # 原来的值不为无穷大

    return distance


if __name__ == '__main__':
    default = [[0, 2, 5, None, 6],
               [2, 0, 1, 5, 3],
               [5, 1, 0, 1, None],
               [None, 5, 1, 0, 2],
               [6, 3, None, 2, 0]]
    names = ['A', 'B', 'C', 'D', 'E']

    graph = Graph(default)

    res = floyd(graph)
    print('图中最短距离矩阵：')
    for item in res:
        print(item)
