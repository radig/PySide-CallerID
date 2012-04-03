# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore, QtGui, QtNetwork

sys.path.append('../')
from caller_id import CallerId

@QtCore.Slot(str)
def lido(cid):
    print "Nova chamada detectada: " + cid

def sendUdp():
    udp = QtNetwork.QUdpSocket()
    data = QtCore.QByteArray("13334123")
    udp.writeDatagram(data, QtNetwork.QHostAddress.LocalHost, 8666)
    print "Escrevendo datagram udp..."

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # callerId = CallerId(app, "id_file", "File")
    # callerId.newCallerId.connect(lido)

    callerId = CallerId(app, 8666, "UDP")
    callerId.newCallerId.connect(lido)
    print "Seu programa continua normalmente..."

    sendUdp()

    sys.exit(app.exec_())