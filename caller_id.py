# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore
from observers.file_observer import FileObserver

# Dispara um evento 'newCallerId' quando uma chamada telefonica é detectada
class CallerId(QtCore.QObject):

    newCallerId = QtCore.Signal(str)

    def __init__(self, Parent, resourceInfo, resource = "File"):
        QtCore.QObject.__init__(self, Parent)

        #Inicializando atributos de classe
        self.currentId = None
        self.resourceInfo = resourceInfo
        self.resource = resource

        self.listen()

    def listen(self):
        if self.resource == "File":
            self.listenFile()
        elif self.resource == "UDP":
            self.listenUDP()
        else:
            raise Exception(u"Tipo de recurso não implementado")

    def get(self):
        return self.currentId

    def listenFile(self):
        fo = FileObserver(self, self.resourceInfo)
        fo.newDataRead.connect(self.newDataReadSlot)

    @QtCore.Slot(str)
    def newDataReadSlot(self, data):
        self.currentId = data
        self.newCallerId.emit(self.currentId)