# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore, QtGui, QtNetwork

sys.path.append('../')
from caller_id import CallerId

udp = QtNetwork.QUdpSocket()

@QtCore.Slot()
def datagramReadySlot():
    while udp.hasPendingDatagrams():
        datagram = QtCore.QByteArray()
        datagram.resize(udp.pendingDatagramSize())

        (data, sender, senderPort) = udp.readDatagram(datagram.size())

        cid = str(data)
        print "Numero lido: " + cid

@QtCore.Slot(str)
def lido(cid):
    print "Nova chamada detectada: " + cid

def sendUdp():
    data = QtCore.QByteArray("13334123")
    udp.writeDatagram(data, QtNetwork.QHostAddress.LocalHost, 8666)
    print "Escrevendo datagram udp..."

def readUdp():
    udp.bind(QtNetwork.QHostAddress(QtNetwork.QHostAddress.Any), 8666)
    udp.readyRead.connect(datagramReadySlot)
    print "ouvindo..."

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # callerId = CallerId(app, "id_file", "File")
    # callerId.newCallerId.connect(lido)

    callerId = CallerId(app, 8666, "UDP")
    callerId.newCallerId.connect(lido)
    print "Seu programa continua normalmente..."

    sendUdp()
    # readUdp()

    sys.exit(app.exec_())