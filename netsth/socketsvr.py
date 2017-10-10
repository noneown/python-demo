import socket as sk
from time import ctime

tcp_socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
tcp_socket.bind(('localhost', 8686))
tcp_socket.listen(5)

while True:
    print 'waiting for connecting...'
    tcp_cli, addr = tcp_socket.accept()
    print 'connect from: ' + str(addr)

    while True:
        data = tcp_cli.recv(1024)
        if not data:
            break
        print 'recv data: ' + data
        tcp_cli.send('%s %s'%(ctime(), data))
    tcp_cli.close()
tcp_socket.close()