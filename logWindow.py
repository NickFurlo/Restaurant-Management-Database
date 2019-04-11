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
		self.main = MainManagerWindow.MainWindow(self)
		self.main.show()

	def chefLog(self):
		self.close()
		self.main = EnterNameWindow.MainWindow()
		self.main.show()

	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_recipesLogin()
		self.ui.setupUi(self)
		self.setWindowTitle('Recipe Tracker')
		self.ui.btnManager.clicked.connect(self.manLog)
		self.ui.btnChef.clicked.connect(self.chefLog)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mWindow = MainWindow()
    mWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
	main()
