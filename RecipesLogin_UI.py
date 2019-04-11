# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecipesLogin.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_recipesLogin(object):
    def setupUi(self, recipesLogin):
        recipesLogin.setObjectName("recipesLogin")
        recipesLogin.resize(463, 152)
        self.gridLayout = QtWidgets.QGridLayout(recipesLogin)
        self.gridLayout.setContentsMargins(30, -1, 30, 30)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(recipesLogin)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2, QtCore.Qt.AlignVCenter)
        self.btnChef = QtWidgets.QPushButton(recipesLogin)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.btnChef.setFont(font)
        self.btnChef.setAutoFillBackground(False)
        self.btnChef.setStyleSheet("padding: 10px;")
        self.btnChef.setDefault(False)
        self.btnChef.setFlat(False)
        self.btnChef.setObjectName("btnChef")
        self.gridLayout.addWidget(self.btnChef, 1, 1, 1, 1)
        self.btnManager = QtWidgets.QPushButton(recipesLogin)
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.btnManager.setFont(font)
        self.btnManager.setStyleSheet("padding: 10px;")
        self.btnManager.setObjectName("btnManager")
        self.gridLayout.addWidget(self.btnManager, 1, 0, 1, 1)

        self.retranslateUi(recipesLogin)
        QtCore.QMetaObject.connectSlotsByName(recipesLogin)

    def retranslateUi(self, recipesLogin):
        _translate = QtCore.QCoreApplication.translate
        recipesLogin.setWindowTitle(_translate("recipesLogin", "Dialog"))
        self.label.setText(_translate("recipesLogin", "Select Your Role"))
        self.btnChef.setText(_translate("recipesLogin", "Chef"))
        self.btnManager.setText(_translate("recipesLogin", "Manager"))


