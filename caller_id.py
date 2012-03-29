# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore
from observers.file_observer import FileObserver

# Dispara um evento 'newCallerId' quando uma chamada telefonica é detectada
class CallerId(QtCore.QThread):
    newCallerId = QtCore.Signal(str)

    currentId = None

    resource = None

    resourInfo = None

    def __init__(self, resourceInfo, resource = "File"):
        QtCore.QThread.__init__(self)
        self.resource = resource
        self.resourceInfo = resourceInfo

    def run(self):
        if(self.resource == "File"):
            self.listenFile()
        elif(self.resource == "UDP"):
            self.listenUDP()
        else:
            raise Exception(u"Tipo de CallerId não implementado")

        self.exec_()

    # Recupera o telefone da chamada corrente
    def get(self):
        return self.currentId.id;

    def listenFile(self):
        fo = FileObserver(self.resourceInfo)
        fo.newDataRead.connect(self.newDataReadSlot)

    @QtCore.Slot(str)
    def newDataReadSlot(self, data):
        print data
        self.newCallerId.emit(self.currentId)