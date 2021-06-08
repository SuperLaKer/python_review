from oop.A_class.Gun import Gun


class Soldier:

    def __init__(self, name):
        self.name = name
        self.gun = None
        # 私有属性
        self.__age = 10

    def fire(self):
        if self.gun is None:
            print("[%s] 还没有枪..." % self.name)
            return
        self.gun.add_bullet(50)
        self.gun.shoot()

    # 私有方法外界无法访问
    # xx._Soldier__say()  # 使用这种方式访问
    def __say(self):
        print("私有方法...", self.__age)


if __name__ == '__main__':
    handgun = Gun("handgun")
    machine = Gun("machine")
    handgun.add_bullet(7)
    machine.add_bullet(100)

    # 多态的体现
    soldier = Soldier("小明")
    soldier.gun = handgun
    soldier.fire()

    soldier.gun = machine
    soldier.fire()
