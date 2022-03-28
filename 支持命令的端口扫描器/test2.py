import sys, socket


# 判断端口是否开放
def is_open(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        return True
    except:
        return False


# 默认扫描的函数
def scan(ip, portlist):
    for x in portlist:
        if is_open(ip, x):
            print("host:%s port:%s open" % (ip, x))
        else:
            print("host:%s port:%s close" % (ip, x))


# 范围扫描
def rscan(ip, start, end):
    for x in range(start, end):
        if is_open(ip, x):
            print("host:%s port:%s open" % (ip, x))
        else:
            print("host:%s port:%s close" % (ip, x))


def main():
    defaultport = [80, 135, 445, 1433, 3306, 3389, 5944]  # 默认扫描这些端口号
    if len(sys.argv) == 2:  # 如果只有一个参数
        str = sys.argv[1]  # 获取第一个参数
        if str[0] == '-':  # python xxx.py -[参数]
            option = sys.argv[1][1:]  # 查看一下- 之后是什么
            if option == "version":  # python xxx.py -version
                print("软件版本是1.0")
            elif option == 'help':
                print("python xxx.py [ip] [port:80,99,89或80-99]")
            sys.exit()
        # 默认没有扫描参数   python xxx.py 127.0.0.1
        scan(sys.argv[1], defaultport)
    # 参数有逗号
    elif len(sys.argv) == 3:  # python xxx.py 127.0.0.1 98,99,90
        if ',' in sys.argv[2]:
            p = sys.argv[2]  # 98,99,90
            p = p.split(',')  # 用,隔开，将p转化为列表[98,99,90]
            a = []
            for x in p:
                a.append(int(x))
            scan(sys.argv[1], a)
        # 参数有-的情况
        elif "-" in sys.argv[2]:  # python xx.py 127.0.0.1 80-99
            a = sys.argv[2]  # 80-99
            a = a.split('-')  # ['80','99']
            start = int(a[0])  # 80
            end = int(a[1])  # 99
            rscan(sys.argv[1], start, end)

    pass


if __name__ == '__main__':
    main()
