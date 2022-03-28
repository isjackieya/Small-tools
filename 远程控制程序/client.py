import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 44444
    s.connect((host, port))  # 这里为了试验，绑定本机的ip和端口号
    while True:
        try:
            data_recv = s.recv(1024)
            print(data_recv.decode("utf-8"))
            msg = input("send msg:")
            s.send(msg.encode("utf-8"))
        except Exception as e:
            print("断开连接")
            print(e)
            break
    s.close()
    pass


if __name__ == '__main__':
    main()
