# *-* coding:utf8 *-*
"""
rwa: 读、写覆盖、追加
r+  读写
w+  读 覆盖写
a+  读 追加写


通常用 r, w。
r模式：文件不存在抛异常
w模式：文件不存在会创建新文件
"""


def read_file():
    file = open("__init__.py", mode='r')
    while True:
        data = file.readline()
        if not data:
            break
        print(data)


if __name__ == '__main__':
    print("xx")
    read_file()
