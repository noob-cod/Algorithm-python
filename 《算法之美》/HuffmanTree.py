"""
@Date: Friday, March 12, 2021
@Author: Chen Zhang
@Brief: 基于贪心算法的哈夫曼树（最优二叉树）
"""


def HuffmanTree(data):
    """
    哈夫曼树：
        通过N个带权重（或频率）的叶子节点构建而成的一个带权路径长度（Weighted Path Length of Tree, WPL）最
        小的二叉树。要求权重越大的叶子节点越靠近根节点。哈夫曼树算法构建过程采用自底（叶子）向顶（根）的构建方式。

    :param data: 权重。[('A', weight_A), ('B', weight_B), ... ]
    """

    def createHFTree(nodes, hf_tree_root):
        """
        创建哈夫曼树

        :param nodes: 剩余叶子节点的列表
        :param hf_tree_root: 已构建的哈夫曼树的根节点
        :return: 哈夫曼树
        """
        length = len(nodes)
        if length == 1:  # 若剩余叶子节点为1，则可直接构建最终的哈夫曼树
            hf_tree_root = Node(nodes[0].data+hf_tree_root.data, name=nodes[0].name+hf_tree_root.name)
            print(hf_tree_root.name, hf_tree_root.data)  # 打印构造的新节点
            return hf_tree_root
        else:
            nodes.append(hf_tree_root)  # 将已构建的哈夫曼树根节点加入nodes
            nodes.sort(key=lambda x: x.data)  # 按权重排序
            s1 = nodes[0]  # 权重最小的节点
            s2 = nodes[1]  # 权重次小的节点
            nodes = nodes[2:]  # 从剩余叶子节点列表中删除两个最小的节点
            new_node = Node(s1.data+s2.data, left=s1, right=s2, name=s1.name+s2.name)  # 用最小的两个叶子节点构建新哈夫曼树
            print(new_node.name, new_node.data)  # 打印构造的新节点
            createHFTree(nodes, new_node)  # 递归用剩余的叶子节点和新建的哈夫曼树递归创建哈夫曼树

    n = len(data)  # 数据量
    if n == 1:  # 若只有一个数据，则直接构成由一个节点组成的哈夫曼树
        print('data[0]')
        return -1
    node_list = [Node(data[i][1], name=data[i][0]) for i in range(n)]  # 为每个数据创建一个节点对象
    root = node_list.pop()  # 弹出一个节点（可随机）作为启动递归的哈夫曼树根节点
    createHFTree(node_list, root)  # 递归构造哈夫曼树


class Node:
    """树的节点"""
    def __init__(self, data, left=None, right=None, name=None):
        self.data = data
        self.left = left
        self.right = right
        self.name = name


if __name__ == '__main__':
    records = [('A', 2), ('B', 3), ('C', 3), ('D', 4), ('E', 7), ('F', 6)]
    hf_tree = HuffmanTree(records)
