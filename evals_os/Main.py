import os
import sys


def say_hi():
    print("hi...")


if __name__ == '__main__':
    # system("终端命令")
    # 执行成功返回0
    result = os.system("cd ..")
    print(result)

    print(eval("1+1"))
    eval("say_hi()")
    get_cwd = os.getcwd()
    print(get_cwd)
    env = os.getenv("JAVA_HOME")
    print(env)

    # os.makedirs("test\\test")
    print("xx:", os.path.sep)
    print("xx:", os.path.exists)
    print("xx:", os.path.altsep)
    print("xx:", os.path.abspath("."))
    print("xx:", os.path.curdir)

    print(os.environ)
    print(os.getpid())

    # 获取命令行参数
    print(sys.path)
    print(sys.argv[0])

    #
