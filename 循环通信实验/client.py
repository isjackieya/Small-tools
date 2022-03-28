import socket


def main():
    # af_inet使用ipv4，sock_stream使用tcp通信
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = socket.gethostname()
    server_port = 8999
    server_add = (server_ip, server_port)
    # 连接服务器
    tcp_client_socket.connect(server_add)
    # 接收第一次发来的数据
    first_data = tcp_client_socket.recv(1024)
    print(first_data.decode('utf-8'))
    while True:
        # 持续发送数据
        send_data = input("send-->")
        tcp_client_socket.send(send_data.encode('utf-8'))


    tcp_client_socket.close()

    pass


if __name__ == '__main__':
    main()
