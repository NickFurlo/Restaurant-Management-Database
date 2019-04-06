import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic

class MainWindow(QtWidgets.QDialog):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(850,675)
		global ui
		ui = uic.loadUi('AddRecipe.ui',self)
		ui.pushButton.clicked.connect(self.addIng)

	def addIng(self):
		return None
