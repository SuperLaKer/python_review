from oop.B_extend.A import A

"""
    多继承MRO, method resolution order
    print(class_name.__mro__)
    多态：士兵需要一把枪，手枪 机枪都可以，面向引用编程
"""


class B(A):

    def __init__(self, name, age):
        self.age = age
        super(B, self).__init__(name)

    def say(self):
        print("xx", self.age, sep=", ")
        super(B, self).say()


if __name__ == '__main__':
    b = B("小明", 10)
    b.say()
    print(B.__mro__)
