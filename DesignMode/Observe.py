"""
@Date: 2021/6/4 下午7:58
@Author: Chen Zhang
@Brief: Observer-Observed

我的想法：被观察对象在新的观察者登录时，自动检查并为观察者创建新的属性，并同步内容到新订阅的观察者。
"""


class Observer:
    """观察者"""
    def __init__(self, name):
        assert isinstance(name, str)
        self.__name = name
        self.__content = []
        self.__content_len = 0

    def __str__(self):
        return self.get_name()

    def __update(self, news):
        """观察者更新方法"""
        print("*"*30)
        print("{}接收到了更新通知，正在更新内容".format(self.get_name()))
        self.__content.append(news)
        self.__content_len += 1
        print("{}完成了更新".format(self.get_name()))
        print("*" * 30)
        print()

    def get_name(self):
        return self.__name

    def update(self, news):
        self.__update(news)

    def get_content(self):
        print(self.__name, ":", self.__content)


class Observed:
    """被观察对象"""
    def __init__(self):
        self.__subscribers = []  # 记录观察者
        self.__number_of_sub = 0  # 记录观察者数量
        self.__changes = False  # 记录是否接收到新的消息
        self.__content = []  # 被观察对象的内容

    def __notice(self, news):
        """提醒观察者更新订阅"""
        if self.__changes:
            if self.get_subscriber_numbers() != 0:
                print('='*50)
                print('接收到新的消息，开始提醒观察者更新内容...')
                print()
                for subscriber in self.__subscribers:
                    subscriber.update(news)
                print("观察者更新完毕！")
                print('='*50)
            self.__changes = False

    def __register(self, new_subscriber):
        """登录新的观察者"""
        assert isinstance(new_subscriber, Observer)

        # 这里还应该添加重复性检查，避免重复添加
        self.__subscribers.append(new_subscriber)
        self.__number_of_sub += 1
        print("成功登录新用户：", new_subscriber)
        self.__synchronize(new_subscriber)
        print()

    def __remove(self, subscriber):
        """移除观察者"""
        assert isinstance(subscriber, Observer)
        if self.get_subscriber_numbers() != 0:
            self.__subscribers.remove(subscriber)
            self.__number_of_sub -= 1
            print("成功移除用户{}".format(subscriber))
            print()

    def __update(self, news):
        """被观察对象内容更新方法"""
        assert isinstance(news, News)
        self.__content.append(news)
        self.__changes = True
        self.__notice(news)

    def __synchronize(self, subscriber):
        """为新用户同步数据"""
        if self.__content:
            print("#"*30)
            print("正在为{}同步内容".format(subscriber))
            for news in self.__content:
                subscriber.update(news)
            print("同步完成！")
            print("#" * 30)
            print()

    def get_subscriber_numbers(self):
        return self.__number_of_sub

    def update(self, news):
        self.__update(news)

    def register(self, new_subscriber):
        if isinstance(new_subscriber, Observer):
            self.__register(new_subscriber)
        elif isinstance(new_subscriber, list) or isinstance(new_subscriber, tuple):
            for item in new_subscriber:
                assert isinstance(item, Observer)
                self.__register(item)

    def remove(self, subscriber):
        self.__remove(subscriber)

    def get_content(self):
        print(self.__content)


class News:
    """消息对象"""
    def __init__(self):
        pass


if __name__ == '__main__':
    # 建立新的被观察对象
    Server = Observed()

    # 创建新的观察者并登录到服务器
    C1 = Observer("Tom")
    C2 = Observer("Susan")
    C3 = Observer("Jack")

    Server.register((C1, C2, C3))
    print("目前的观察者数量： ", Server.get_subscriber_numbers())

    new = News()
    Server.update(new)

    print()
    print("服务器内容：")
    Server.get_content()
    print()
    print("观察者内容:")
    C1.get_content()
    C2.get_content()
    C3.get_content()

    # C1取消了订阅
    Server.remove(C1)
    new2 = News()
    Server.update(new2)

    print()
    print("服务器内容：")
    Server.get_content()
    print()
    print("观察者内容:")
    C1.get_content()
    C2.get_content()
    C3.get_content()

    # C4 加入了订阅
    C4 = Observer("Isaac")
    Server.register(C4)

    new3 = News()
    Server.update(new3)

    print()
    print("服务器内容：")
    Server.get_content()
    print()
    print("观察者内容:")
    C1.get_content()
    C2.get_content()
    C3.get_content()
    C4.get_content()

