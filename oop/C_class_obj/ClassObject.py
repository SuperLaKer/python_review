"""
    类属性，类方法
    实例属性，实例方法

"""


class ClassObject(object):
    # 类属性
    counter = 0

    # 类方法
    @classmethod
    def get_counter(cls):
        # 访问类属性
        return cls.counter

    @staticmethod
    def static_method():
        print("静态方法：既不需要访问类属性、类方法，也不访问实例属性和实例方法")

    # 实例属性
    def __init__(self, name):
        self.name = name


