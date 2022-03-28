# 服务端
import socket


def main():
    s = socket.socket()
    host = socket.gethostname()  # 获取自己的ip地址
    port = 12345  # 一会儿用12345端口通信
    s.bind((host, port))  # 绑定ip地址和短裤
    s.listen(5)  # 等待用户连接，最多五个人
    c, addr = s.accept()  # 建立和客户端的链接   c=对方的套接字，addr=对方的ip地址和对方用来连接的端口
    print('对方连接的地址是', addr)
    c.send('welcome'.encode('utf-8'))  # 通过客户的套接字发送welcome给对方，utf-8编码
    print(c.recv(1024).decode('utf-8'))  # 接受客户信息
    c.close()
    pass


if __name__ == '__main__':
    main()
