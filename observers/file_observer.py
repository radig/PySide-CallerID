# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore

class FileObserver(QtCore.QFileSystemWatcher):
    newDataRead = QtCore.Signal(str)

    changedCounter = 0

    def __init__(self, fileName):
        QtCore.QFileSystemWatcher.__init__(self)

        self.addPath(fileName)

        self.fileChanged.connect(self.counter)

        self.fileChanged.connect(self.fileChangedSlot)

    @QtCore.Slot()
    def counter(self):
        self.changedCounter += 1
        print "Alteracoes " + str(self.changedCounter)

    @QtCore.Slot(str)
    def fileChangedSlot(self, fileName):
        print "Arquivo alterado " + fileName
        # remove temporariamente da fila de obsevacao
        self.removePath(fileName)

        # le conteudo do arquivo
        f = open(fileName, 'r')
        data = f.read()
        f.close()

        # limpa o arquivo
        open(fileName, 'w').close()

        # re-insere na fila de obsevacao
        self.addPath(fileName)

        self.newDataRead.emit(data)