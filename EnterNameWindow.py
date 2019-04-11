import PyQt5
import DatabaseManage
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import subprocess
from PyQt5.QtWidgets import QMessageBox
import sys
from EnterName_UI import Ui_MainWindow
import MainChefWindow

class NameWindow(QtWidgets.QMainWindow):
	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()

	def checkName(self):
		#global ui
		self.name = self.ui.lineEdit.text()
		self.nameExist = DatabaseManage.checkChefName(self.name)
		if self.nameExist == False:
			self.msgBox(QMessageBox.Warning, "Failed", "Incorrect Name. Please Try again")
		else:
			self.close()
			self.chefWindow = MainChefWindow.ChefWindow(self.name)
			self.chefWindow.show()


	def goBack(self):
		self.close()
		subprocess.call([sys.executable,'logWindow.py'])

	def __init__(self, parent=None):
		super(NameWindow,self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Enter Name')
		self.ui.lineEdit.returnPressed.connect(self.checkName)
		self.ui.btnBack.clicked.connect(self.goBack)

		#self.chefWindow = MainChefWindow.ChefWindow(self.name)
