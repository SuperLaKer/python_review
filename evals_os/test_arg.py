import getopt
import sys

# "ho:"也可以写成'-h-o:'
# -h后面不加值，-o后面应该有值
# --help 后面不应该有值
# --output后面应该有值
opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
args0 = args[0]



print(opts)
print(args)


'''
    测试：
    执行：
        python test_arg.py -h -o999 --help --output="./test" xx
    结果：
        [('-h', ''), ('-o', '999'), ('--help', ''), ('--output', './test')]
        ['xx']
'''
