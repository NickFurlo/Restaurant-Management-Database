#import PyQt5
from PyQt5 import QtWidgets, uic
import MainManagerWindow
import EnterNameWindow
import ctypes
import sys
from RecipesLogin_UI import Ui_recipesLogin
#from PyQt5.QtWidgets import QMessageBox
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")

class MainWindow(QtWidgets.QDialog):
	
	def manLog(self):
		self.close()
		#Mv = MainManagerWindow.MainWindow()
		self.managerView.show()

	def chefLog(self):
		self.close()
		#self.main = EnterNameWindow.MainWindow()
		self.nameView.show()

	def __init__(self, parent=None):
		super().__init__(parent)
		self.ui = Ui_recipesLogin()
		self.ui.setupUi(self)
		self.setWindowTitle('Recipe Tracker')
		self.ui.btnManager.clicked.connect(self.manLog)
		self.ui.btnChef.clicked.connect(self.chefLog)

		self.managerView = MainManagerWindow.ManagerWindow(self)
		self.nameView = EnterNameWindow.NameWindow()


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	mWindow = MainWindow()
	mWindow.show()
	sys.exit(app.exec_())

