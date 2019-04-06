import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import MainManagerWindow
import EnterNameWindow
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class MainWindow(QtWidgets.QDialog):
	
	def manLog(self):
		self.close()
		self.main=MainManagerWindow.MainWindow()
		self.main.show()

	def chefLog(self):
		self.close()
		self.main=EnterNameWindow.MainWindow()
		self.main.show()

	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(450,280)
		global ui
		ui = uic.loadUi('RecipesLogin.ui',self)
		ui.btnManager.clicked.connect(self.manLog)
		ui.btnChef.clicked.connect(self.chefLog)


def main():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	mWindow = MainWindow()
	mWindow.show()
	sys.exit(app.exec_())

main()