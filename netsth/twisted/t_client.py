from twisted.internet import protocol, reactor
from time import ctime

class TSClntProtocal(protocol.Protocol):
    def sendData(self):
        data = raw_input('> ')
        if data:
            print 'sending...' + data
            self.transport.write('%s %s' % (ctime(), data))
        else:
            self.transport.loseConnection()
    def connectionMade(self):
        self.sendData()
    def dataReceived(self, data):
        print 'recv data: ' + data
        self.sendData()

class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocal
    cliconnlost = cliconnfailed = lambda self,connector, reason: reactor.stop()

reactor.connectTCP('localhost', 8686, TSClntFactory())
reactor.run()