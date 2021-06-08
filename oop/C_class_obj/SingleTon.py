"""
    单例模式:
    __new__方法申请空间、返回对象引用
    __init__方法初始化实例属性
"""


class SingleTon(object):

    singleton = None

    def __new__(cls, *args, **kwargs):
        if cls.singleton is None:
            cls.singleton = super().__new__(cls)
        return cls.singleton


if __name__ == '__main__':
    singleton1 = SingleTon()
    singleton2 = SingleTon()
    print(singleton1 is singleton2)
