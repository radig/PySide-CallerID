# -*- coding: utf-8 -*-
from PySide import QtNetwork, QtCore

class UpdListener(QtCore.QObject):
    newDataRead = QtCore.Signal(str)

    def __init__(self, Parent, port):
        QtCore.QObject.__init__(self, Parent)

        self.udpSocket = QtNetwork.QUdpSocket()
        self.udpSocket.bind(QtNetwork.QHostAddress(QtNetwork.QHostAddress.Any), port)
        self.udpSocket.readyRead.connect(self.datagramReadySlot)

    @QtCore.Slot()
    def datagramReadySlot(self):
        while self.udpSocket.hasPendingDatagrams():
            datagram = QtCore.QByteArray()
            datagram.resize(self.udpSocket.pendingDatagramSize())

            (data, sender, senderPort) = self.udpSocket.readDatagram(datagram.size())

            self.parseDatagram(data)

    def parseDatagram(self, data):
        cid = str(data)
        self.newDataRead.emit(cid)