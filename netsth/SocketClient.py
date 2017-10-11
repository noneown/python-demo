import socket as sk
while True:
    tcp_cli = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    tcp_cli.connect(('localhost', 8686))
    data = raw_input('> ')
    print data
    data = tcp_cli.send(('%s\r\n'%data))
    data = tcp_cli.recv(1024)
    if not data:
        break
    print data.strip()
    tcp_cli.close()