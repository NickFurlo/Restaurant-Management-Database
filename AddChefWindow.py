import PyQt5
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(850,675)
		global ui
		ui = uic.loadUi("AddChef.ui",self)
		fname = ui.lineEdit.text()
		lname = ui.lineEdit_2.text()
		