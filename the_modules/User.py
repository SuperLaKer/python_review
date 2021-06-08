"""异常"""
import TheModules

class User(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username is None or self.password is None:
            raise Exception("用户名或密码不能为空")


if __name__ == '__main__':
    user = User("xx", None)
    try:
        user.login()
        print("登陆成功!")
    except Exception as e:
        print(e)
    finally:
        print("关闭资源")

    modules = TheModules.TheModules("name")
    print(modules.name)
