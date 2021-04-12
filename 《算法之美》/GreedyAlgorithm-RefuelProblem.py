"""
@Created time: Friday, March 12, 2021
@Author: Chen Zhang
@Brief:贪心算法解决汽车加油问题

问题概述：
       一辆汽车加满油一次可以跑300千米，现在该车在第一个加油站出发时加满油，然后需要陆续经过
       间隔[150, 180, 300, 200, 280, 160]的加油站，指出在哪些加油站加油可以使加油次数
       最少，算出最少的加油次数。
"""


class Car:
    def __init__(self, fuel_left=300):
        self.fuel_left = fuel_left

    def refuel(self):
        self.fuel_left = 300

    def fuel_left_after(self, distance):
        self.fuel_left -= distance

    def how_much_fuel_left(self):
        return self.fuel_left


class OilStation:
    def __init__(self, interval):
        self.interval = interval
        self.station_num = len(interval)-1


if __name__ == '__main__':
    car = Car()
    oil = OilStation([150, 180, 120, 100, 280, 160])

    i = 0  # 起点
    interval_num = oil.station_num  # 沿途加油站数量
    refuel_num = 0  # 沿途加油次数
    refuel_loc = []  # 加油地点
    while i < interval_num:  # 汽车启动出发
        car.fuel_left_after(oil.interval[i])  # 当前状态（汽车剩余续航能力）
        if car.how_much_fuel_left() < oil.interval[i+1]:  # 贪心算法，若当前油量足够到下一个地点，则不加油，否则加油
            car.refuel()
            refuel_loc.append(i+1)
            refuel_num += 1
        i += 1

    print('汽车总共加了%d次油' % refuel_num)
    print('分别在以下加油站加过油：', end='\n')
    print(refuel_loc)
