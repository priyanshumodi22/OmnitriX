# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'omnitrix_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OmnitriX(object):
    def setupUi(self, OmnitriX):
        OmnitriX.setObjectName("OmnitriX")
        OmnitriX.resize(606, 595)
        self.centralwidget = QtWidgets.QWidget(OmnitriX)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-2, -5, 611, 601))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:\OmnitriX\Omnitrix.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        # self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton.setGeometry(QtCore.QRect(430, 540, 71, 21))
        # font = QtGui.QFont()
        # font.setFamily("NewsGoth BT")
        # font.setPointSize(16)
        # font.setBold(True)
        # self.pushButton.setFont(font)
        # self.pushButton.setStyleSheet("background-color: rgb(13, 93, 173);")
        # self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("NewsGoth BT")
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(13, 93, 173);")
        self.pushButton_2.setObjectName("pushButton_2")
        OmnitriX.setCentralWidget(self.centralwidget)

        self.retranslateUi(OmnitriX)
        QtCore.QMetaObject.connectSlotsByName(OmnitriX)

    def retranslateUi(self, OmnitriX):
        _translate = QtCore.QCoreApplication.translate
        OmnitriX.setWindowTitle(_translate("OmnitriX", "OmnitriX"))
        # self.pushButton.setText(_translate("OmnitriX", "Run"))
        self.pushButton_2.setText(_translate("OmnitriX", "Exit"))
        OmnitriX.setWindowIcon(QtGui.QIcon('D:\OmnitriX\omnitrix_CxZ_icon.ico'))
        #disable the minimize button
        OmnitriX.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OmnitriX = QtWidgets.QMainWindow()
    ui = Ui_OmnitriX()
    ui.setupUi(OmnitriX)
    OmnitriX.show()
    sys.exit(app.exec_())
