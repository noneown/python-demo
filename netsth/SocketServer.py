from time import ctime

import SocketServer

class MyRequestHandler(SocketServer.StreamRequestHandler):

    def handle(self):
        print 'connected from: ' + str(self.client_address)
        data = self.rfile.readline()
        print 'recv data: ' + data
        self.wfile.write('%s %s'%(ctime(), data))

tcpServer = SocketServer.TCPServer(('localhost', 8686), MyRequestHandler)
print 'waiting for connection...'
tcpServer.serve_forever()