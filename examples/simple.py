# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore, QtGui

sys.path.append('../')
from caller_id import CallerId

@QtCore.Slot(str)
def veio(self, cid):
    print "Nova chamada detectada: " + cid

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    print "Iniciando caller"
    callerId = CallerId("id_file", "File")
    callerId.newCallerId.connect(veio)
    callerId.start()
    print "Continua o programa..."

    sys.exit(app.exec_())