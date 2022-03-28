import sys, socket


# 在当前目录下打开cmd ，然后输入 python test1.py ，输出test1.py
# sys.argv是从python xxx.py [参数1][参数2][参数3]。。。。。
# 其中xxx.py 就是sys.argv[0]   [参数1]就是sys.argv[1]

def main():
    print(sys.argv)  # 输出所有的参数,
    print(sys.argv[1])  # 输出第二个参数
    pass


if __name__ == '__main__':
    main()
