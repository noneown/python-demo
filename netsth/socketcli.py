import socket as sk

tcp_cli = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
tcp_cli.connect(('localhost', 8686))

while True:
    data = raw_input('> ')
    print data
    data = tcp_cli.send((data))
    data = tcp_cli.recv(1024)
    if not data:
        break
    print data
tcp_cli.close()