"""python3默认继承object, 但是为了兼容2.0推荐手动继承object"""


class A(object):
    def __init__(self, name):
        self.name = name

    def say(self):
        print(self.name)
