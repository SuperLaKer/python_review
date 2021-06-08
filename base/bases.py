"""
列表: list.append
元组: tuple长度、内容不可变。list(tuple), tuple(list)相互转化。python的返回值其实就是tuple

切片：左闭右开

字典
非数字类型都可以 iter, 切片

"""
from collections import Iterable

if __name__ == '__main__':
    str_1 = "hello"
    for i in str_1:
        print(i, end=',')
    print(end='\n')
    arr = [item * 2 for item in "hello"]
    print(arr)

    # 是否是可迭代对象
    print(isinstance(str_1, Iterable))

    # 切片 iterable[开始索引:结束索引:步长], 左闭右开
    print("beautiful"[0::2])

    # 逆序
    print('逆序...')
    print(str_1[::-1])  # olleh
    print(str_1[-1::-1])  # olleh
    print(str_1[-2::-1])  # lleh
    print("0123456789"[::-2])  # 97531
