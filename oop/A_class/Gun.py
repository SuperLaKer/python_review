class Gun:

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        if self.bullet_count <= 0:
            print("没有子弹了...")
            return
        self.bullet_count -= 1
        print("%s 发射子弹[%d]..." % (self.model, self.bullet_count))

    # 内置函数: __函数名字__
    # __init__构造函数
    def __init__(self, model):
        # 型号、子弹余量
        self.model = model
        self.bullet_count = 0

    def __del__(self):
        print("对象将要被销毁" + self.__class__.__name__)

    # 必须返回一个字符串
    def __str__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    ak47 = Gun("ak47")
    ak47.add_bullet(50)
    ak47.shoot()
