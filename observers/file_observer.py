# -*- coding: utf-8 -*-
from PySide import QtCore

class FileObserver(QtCore.QFileSystemWatcher):
    newDataRead = QtCore.Signal(str)

    def __init__(self, Parent, fileName):
        QtCore.QFileSystemWatcher.__init__(self, Parent)

        self.addPath(fileName)
        self.fileChanged.connect(self.fileChangedSlot)

    @QtCore.Slot(str)
    def fileChangedSlot(self, fileName):
        self.removePath(fileName)

        f = open(fileName, 'r')
        data = f.read()
        f.close()

        # limpa o arquivo
        open(fileName, 'w').close()

        self.addPath(fileName)

        if len(data) > 0:
            self.newDataRead.emit(data)