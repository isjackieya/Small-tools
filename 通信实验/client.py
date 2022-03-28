# 客户端程序
import socket


def main():
    s = socket.socket()
    host = socket.gethostname()  # 你要连接的ip地址
    port = 12345
    s.connect((host, port))  # 连接服务端
    msg = input('您要发送的信息:')
    s.send(msg.encode('utf-8'))
    print(s.recv(1024).decode("utf-8"))
    s.close()
    pass


if __name__ == '__main__':
    main()
