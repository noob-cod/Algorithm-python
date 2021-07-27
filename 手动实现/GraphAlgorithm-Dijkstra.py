"""
@Date: 2021/7/27 上午9:56
@Author: Chen Zhang
@Brief: 地杰斯特拉算法

1、定义
    给定带权有向图G和源点V，求V到G中其他顶点的最短路径

2、原理
    (1）初始化。用D存放v0到图中其他各顶点的距离，初始条件下处到v0处为0，其余均为无穷大；用
       S存放已经找到的最短路径。
    (2）搜索源点的相邻点。
    (3）计算源点到相邻点的路径长度，更新D(x)。
    (4）对D(x)中的路径进行排序，选择最短的一条作为确定找到的最短路径，将其终点加入到S
       中。以新加入的点为临时的源点，重复(2)-(4)，直到所有点已加入S或者搜索不到新的可见点。

3、图应该提供的接口
    (1) 给顶点命名
    (2) 根据顶点名称，获取相邻顶点及边的权重

"""


class Graph:

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


def dijkstra(graph, v0):
    """
    :param graph: 带权有向图
    :param v0：字符串。图graph中源点的名称
    :return: 数组。源点v0到图中所有顶点的最短距离
    """
    if not isinstance(v0, str) or v0 not in graph.names:
        return -1

    search = {}  # 存放已经搜索过的顶点
    distance = [None] * graph.get_vertex_num()  # 存放源点v0到图中所有顶点的距离
    distance[graph.get_index_by_name(v0)] = 0  # 初始化distance

    tmp = v0
    while True:
        search[tmp] = 0  # 将当前搜索的顶点加入search
        neighbours = graph.get_neighbour_by_name(tmp)  # 获得其所有相邻节点
        if not neighbours:  # 若搜索不到新的可见顶点，则算法结束
            break
        smallest = None  # 重置下一次搜索的顶点
        for name, weight in neighbours:  # 更新距离数组
            if name in search:  # 去除环形连接
                continue

            # 更新距离
            if distance[graph.get_index_by_name(name)] is None:
                distance[graph.get_index_by_name(name)] = distance[graph.get_index_by_name(tmp)] + weight
            else:
                distance[graph.get_index_by_name(name)] = min(distance[graph.get_index_by_name(name)],
                                                              distance[graph.get_index_by_name(tmp)] + weight)

            # 更新下一次需要搜索的顶点
            if smallest is None or distance[graph.get_index_by_name(smallest)] > distance[graph.get_index_by_name(name)]:
                smallest = name

        if len(search) == graph.get_vertex_num():  # 若所有顶点都被搜索过，则算法结束
            break
        tmp = smallest  # 更新当前搜索的顶点

    return distance


if __name__ == '__main__':
    default = [[0, 2, 5, None, 6],
               [2, 0, 1, 5, 3],
               [5, 1, 0, 1, None],
               [None, 5, 1, 0, 2],
               [6, 3, None, 2, 0]]
    names = ['A', 'B', 'C', 'D', 'E']

    graph = Graph(default)
    graph.set_names(names)

    v = 'B'
    res = dijkstra(graph, v)
    print(v, '到图中各顶点的最短距离：')
    for i in range(len(names)):
        print('  ', v, '—>', names[i], ': ', res[i])
