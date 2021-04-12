"""
@Created time: Friday, March 12, 2021
@Author: Chen Zhang
@Brief: 贪心算法解决01背包问题

问题描述：
       提供一个背包，最大可以装5dm^3的物品，另提供表格所示的物品，要求在可以装进去的前提下，往包里
       尽可能装更多价值的物品。这里要求一种物品要么被装进去1次，要么不装进去(0次)。

                             物品价值、体积表
       --------------------------------------------------------------
       物  品          红蛋糕        黄蛋糕        绿蛋糕        白蛋糕
       --------------------------------------------------------------
       价值（元）         20          10           15            25
       体积（dm^3）       3           1            2             4
       --------------------------------------------------------------
"""


class Bag:
    def __init__(self, capacity):
        self.capacity = capacity  # 背包的最大容量
        self.content = {}  # 装入背包的物品，'价值'：数量
        self.total_value = 0

    def PutIn(self, value, volume, num=1):
        self.content[value] = num
        self.capacity -= num * volume
        self.total_value += value * num

    def get_capacity_left(self):
        return self.capacity

    def get_value(self):
        return self.total_value


if __name__ == '__main__':
    Value = [20, 10, 15, 25]
    Volume = [3, 1, 2, 4]
    cakes = dict(zip(Volume, Value))

    # 最小体积贪心策略
    bag = Bag(5)  # 创建空背包
    Volume.sort()  # 按体积正序排列
    for i in range(len(Volume)-1):
        bag.PutIn(cakes[Volume[i]], Volume[i])  # 体积从小到大依次装入背包
        if bag.get_capacity_left() < Volume[i+1]:
            break
    print('最小体积策略总共装入价值%d元的东西' % bag.get_value())

    # 最大体积贪心策略
    bag = Bag(5)  # 创建空背包
    Volume.sort(reverse=True)  # 按体积逆序排列
    i = 0
    while i < len(Volume):
        if bag.get_capacity_left() < Volume[i]:  # 若装不下，则不装
            pass
        else:
            bag.PutIn(cakes[Volume[i]], Volume[i])  # 否则，装入该物品
        i += 1
    print('最大体积策略总共装入价值%d元的东西' % bag.get_value())

    # 最大价值密度贪心策略
    Value = [20, 10, 15, 25]
    Volume = [3, 1, 2, 4]
    cakes = dict(zip(Volume, Value))
    bag = Bag(5)
    value_density = []  # 存放价值密度
    for i in range(len(Volume)):
        value_density.append(Value[i] / Volume[i])  # 计算价值密度
    cakes_dens = dict(zip(value_density, Volume))
    value_density.sort(reverse=True)
    i = 0
    while i < len(value_density):
        if bag.get_capacity_left() < cakes_dens[value_density[i]]:  # 若装不下，则不装
            pass
        else:
            bag.PutIn(cakes[cakes_dens[value_density[i]]], cakes_dens[value_density[i]])  # 否则装入
        i += 1
    print('最大价值密度策略总共装入%d元的东西' % bag.get_value())
