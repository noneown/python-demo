from time import ctime

import s_server

class MyRequestHandler(s_server.StreamRequestHandler):

    def handle(self):
        print 'connected from: ' + str(self.client_address)
        data = self.rfile.readline()
        print 'recv data: ' + data
        self.wfile.write('%s %s'%(ctime(), data))

tcpServer = s_server.TCPServer(('localhost', 8686), MyRequestHandler)
print 'waiting for connection...'
tcpServer.serve_forever()