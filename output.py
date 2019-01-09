# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.bankButton = QtWidgets.QPushButton(Form)
        self.bankButton.setObjectName("bankButton")
        self.gridLayout.addWidget(self.bankButton, 0, 0, 1, 1)
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(Form)
        self.webEngineView.setUrl(QtCore.QUrl("about:blank"))
        self.webEngineView.setObjectName("webEngineView")
        self.gridLayout.addWidget(self.webEngineView, 1, 0, 1, 2)
        self.cryptoButton = QtWidgets.QPushButton(Form)
        self.cryptoButton.setObjectName("cryptoButton")
        self.gridLayout.addWidget(self.cryptoButton, 0, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bankButton.setText(_translate("Form", "Update Bank Info"))
        self.cryptoButton.setText(_translate("Form", "Update Crypto Info"))

from PyQt5 import QtWebEngineWidgets
