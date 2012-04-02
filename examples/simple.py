# -*- coding: utf-8 -*-
import sys, time
from PySide import QtCore, QtGui

sys.path.append('../')
from caller_id import CallerId

@QtCore.Slot(str)
def lido(cid):
    print "Nova chamada detectada: " + cid

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    callerId = CallerId(app, "id_file", "File")
    callerId.newCallerId.connect(lido)
    print "Seu programa continua normalmente..."

    sys.exit(app.exec_())