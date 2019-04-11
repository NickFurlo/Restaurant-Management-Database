# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChefView.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(690, 641)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 631, 611))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tabMyRecipes = QtWidgets.QWidget()
        self.tabMyRecipes.setObjectName("tabMyRecipes")
        self.recipeList = QtWidgets.QListWidget(self.tabMyRecipes)
        self.recipeList.setGeometry(QtCore.QRect(10, 10, 251, 561))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.recipeList.setFont(font)
        self.recipeList.setObjectName("recipeList")
        self.label = QtWidgets.QLabel(self.tabMyRecipes)
        self.label.setGeometry(QtCore.QRect(280, 10, 251, 16))
        self.label.setObjectName("label")
        self.list = QtWidgets.QListWidget(self.tabMyRecipes)
        self.list.setGeometry(QtCore.QRect(275, 41, 341, 521))
        self.list.setObjectName("list")
        self.tabWidget.addTab(self.tabMyRecipes, "")
        self.tabAllRecipes = QtWidgets.QWidget()
        self.tabAllRecipes.setObjectName("tabAllRecipes")
        self.recipeList_2 = QtWidgets.QListWidget(self.tabAllRecipes)
        self.recipeList_2.setGeometry(QtCore.QRect(10, 10, 251, 561))
        font = QtGui.QFont()
        font.setFamily("Book Antiqua")
        font.setPointSize(11)
        self.recipeList_2.setFont(font)
        self.recipeList_2.setObjectName("recipeList_2")
        self.PriceLabel = QtWidgets.QLabel(self.tabAllRecipes)
        self.PriceLabel.setGeometry(QtCore.QRect(280, 10, 55, 16))
        self.PriceLabel.setObjectName("PriceLabel")
        self.listWidget_2 = QtWidgets.QListWidget(self.tabAllRecipes)
        self.listWidget_2.setGeometry(QtCore.QRect(275, 41, 341, 531))
        self.listWidget_2.setObjectName("listWidget_2")
        self.tabWidget.addTab(self.tabAllRecipes, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Price:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMyRecipes), _translate("MainWindow", "My Recipes"))
        self.PriceLabel.setText(_translate("MainWindow", "Price:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabAllRecipes), _translate("MainWindow", "All Recipes"))


