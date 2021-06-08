"""

函数的缺省参数：有默认值，必须使用key=value的方式

默认男性
def demo(name, gender="男"):

"""


def demo(num, *args, **kwargs):
    """多值参数"""
    print(num)
    print(args)
    print(kwargs)


demo(1, 2, 3, 4, 5, name="小明", age=18, gender=True)


def demo(*args, **kwargs):
    """元组和字典的拆包"""
    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# 会把 num_tuple 和 xiaoming 作为元组传递个 args
# demo(gl_nums, gl_xiaoming)
demo(*gl_nums, **gl_xiaoming)
