# -*- coding: utf-8 -*-
from PySide import QtNetwork, QtCore

class UpdListener(QtCore.QObject):
    newDataRead = QtCore.Signal(str)

    def __init__(self, Parent, port):
        QtCore.QObject.__init__(self)

        self.udpSocket = QtNetwork.QUdpSocket(self)

        self.udpSocket.bind(QtNetwork.QHostAddress(QtNetwork.QHostAddress.Any), port)
        self.udpSocket.readyRead.connect(self.datagramReadySlot)

    @QtCore.Slot()
    def datagramReadySlot(self):
        while self.udpSocket.hasPendingDatagrams():
            datagram = QByteArray()
            datagram.resize(self.udpSocket.pendingDatagramSize())

            (sender, senderPort) = self.udpSocket.readDatagram(datagram.data(), datagram.size())

            self.parseDatagram(datagram)

    def parseDatagram(datagram):
        cid = str(datagram)
        self.newDataRead.emit(cid)