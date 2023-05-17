from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import uic
from PyQt5 import QtGui
from PyQt5.QtCore import *
import sys

def setupUI():
    app= QApplication(sys.argv)
    win=QMainWindow()
    win.setObjectName("MainWindow")
    # win.resize(500, 350)
    qtRectangle = win.frameGeometry()
    centerPoint = QDesktopWidget().availableGeometry().center()
    qtRectangle.moveCenter(centerPoint)
    qtRectangle = win.frameGeometry()
    win.setGeometry(200,200,300,300)
    win.setWindowTitle('Youtube Downloader v2.0')
    win.statusbar= QStatusBar(win)
    win.statusbar.showMessage('Sẵn sàng!')
    win.progress_bar = QProgressBar(win)
    win.progress_bar.setMaximum(100)
    win.progress_bar.setFixedSize(350,30)
    # win.statusbar.addPermanentWidget(win.progress_bar)
    win.layout = QGridLayout()
    win.layout.addWidget(win.statusbar,0 , 0)
    win.layout.addWidget(win.progress_bar,0 , 1)
    win.show()
    sys.exit(app.exec_())

setupUI()