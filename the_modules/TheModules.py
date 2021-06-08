"""
    Python每个.py文件都是一个模块, 导入py文件时没有缩进的文件都会执行
    import 模块名1 as 模块别名
    import "包名" # 可以一次性导入包中所有的模块

    __name__ 是 Python 的一个内置属性，记录着一个 字符串
    如果 是被其他文件导入的，__name__ 就是 模块名
    如果 是当前执行的程序 __name__ 是 __main__
"""

# 直接运行 __main__
# 被其他导入  TheModules.py
print("导入了模块", __name__)


class TheModules(object):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':

    print("hi...")
