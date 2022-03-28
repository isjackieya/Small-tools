import socket


def main():
    # af_inet使用ipv4，sock_stream使用tcp通信
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 将地址绑定到套接字
    # 绑定端口
    server_ip=socket.gethostname()
    tcp_server_socket.bind((server_ip, 8999))
    # 允许多数人连接我
    tcp_server_socket.listen(128)
    # 循环为多个客户服务多次
    while True:
        # 等待用户的连接，保存用户的socket和ip地址
        new_client_socket, new_client_addr = tcp_server_socket.accept()
        print("the %s is connecting" % (str(new_client_addr)))
        # 给客户发送信息
        new_client_socket.send('welcome'.encode('utf-8'))
        # 循环为一个客户服务
        while True:
            try:
                # 接收客户发来的数据
                recv_data=new_client_socket.recv(1024)
                print(recv_data.decode('utf-8'))
            except:
                print('断开连接')
                break
        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()
    pass


if __name__ == '__main__':
    main()
