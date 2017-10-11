from twisted.internet import protocol, reactor
from time import ctime

class TSServerProtocal(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print 'connected from: ' + clnt
    def dataReceived(self, data):
        print 'recv data: ' + data
        self.transport.write('%s %s'%(ctime(), data))

factory = protocol.Factory()
factory.protocol = TSServerProtocal
print 'waiting for connection...'
reactor.listenTCP(8686, factory)
reactor.run()