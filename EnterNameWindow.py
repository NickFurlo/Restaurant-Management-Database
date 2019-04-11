import PyQt5
import DatabaseManage
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import subprocess
from PyQt5.QtWidgets import QMessageBox
import sys
import MainChefWindow

class MainWindow(QtWidgets.QMainWindow):
	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()

	def checkName(self):
		global ui
		name = ui.lineEdit.text()
		nameExist = DatabaseManage.checkChefName(name)
		if nameExist == False:
			self.msgBox(QMessageBox.Warning, "Failed", "Incorrect Name. Please Try again")
		else:
			self.close()
			self.main = MainChefWindow.MainWindow(name)
			self.main.show()


	def goBack(self):
		self.close()
		subprocess.call([sys.executable,'logWindow.py'])

	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(450,200)
		global ui
		ui = uic.loadUi('EnterName.ui', self)
		ui.lineEdit.returnPressed.connect(self.checkName)
		ui.btnBack.clicked.connect(self.goBack)