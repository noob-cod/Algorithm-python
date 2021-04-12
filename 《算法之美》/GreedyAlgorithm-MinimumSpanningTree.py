"""
@Date: Friday, March 12, 2021
@Author: Chen Zhang
@Brief: 贪心算法生成最小生成树(MST)

最小生成树：
      对n个节点的连通图，生成最小子图，满足n个节点都在最小子图上，且保留最小权重和n-1条边。
"""


def Kruskal(nodes, edges):
    """
    卡鲁斯卡尔算法：
        从最小权重边开始，每迭代一次就选择一条满足条件的最小权重边，加入最小生成树MST集合里
        一直找到n-1条最小权重边为止。

    :param nodes: 图的节点。['node1_name', 'node2_name', ... , 'node_x_name']
    :param edges: 图的边。[(起点1，终点1，权重1), (起点2，终点2，权重2), ... ,(起点n，终点n，权重n)]
    :return: 最小生成树Mst
    """
    Mst = []  # 记录最小生成树节点
    n = len(nodes)  # 节点数
    i = 0
    sort_Glist = sorted(edges, key=lambda one: one[2])  # 对带权重的边进行从小到大的排序
    print('从小到大按照边的权重数进行排序啊：\n', sort_Glist)
    for one in sort_Glist:  # 找出独立的最小树
        if not((one[0] in Mst and one[1] in Mst) or (one[1] in Mst and one[0] in Mst)):
            Mst.append(one)  # 合成记录最小生成树
            i += 1  # 记录权重最小数个数
        if i == n-1:  # 最小生成树最多n-1条边
            break
    return Mst  # 返回最小生成树


def Prim(nodes, edges):  # 每个节点选择最小边
    """
    Prim算法：
        通过选择每个节点的最小权重边求得最小生成树。
    """

    Mst = []  # 记录最小生成树节点
    i = 0  # 从第一行开始
    n = len(nodes)  # 节点数
    for one in edges:
        index = FindMinEdge(nodes, i, one, Mst)  # 每个节点选一个最小权重边，已经选入的要去掉
        a, b, w = nodes[i], nodes[index], edges[i][index]  # 每次找到的边的两个节点和边的权重
        Mst.append([a, b, w])  # 加入最小生成树
        i += 1
        if i == n-1:  # 最小生成树的边数为n-1
            break
    return Mst


def FindMinEdge(Nodes, row, edge, mst):
    """寻找节点的最小权重边"""
    n = len(edge)  # 节点的数量
    j = 0
    s_edge = sorted(edge)  # 边的权重按升序排序
    e_min = s_edge[0]  # 找到最小权重
    while j < n:
        if edge[j] == e_min:  # 找到最小值对应的下标
            a, b = Nodes[row], Nodes[j]  # row为当前节点的行数
            if not ([a, b, e_min] in mst or [b, a, e_min] in mst):  # 考虑节点的边在Mst里已经存在
                return j  # 返回找到的合适的最小权重边对应的列索引下标
            else:
                if s_edge[0] == s_edge[1]:  # 前后边权重一样，要避免原始下标位置一直在前的问题
                    j += 1
                    continue
                j -= 1  # j准备从-1，0重新开始查找比较新的最小值
                del(s_edge[0])  # 删除重复节点，生成新的s_edge列表
                e_min = s_edge[0]  # 获取下一个权重最小值
        j += 1
    return -1
