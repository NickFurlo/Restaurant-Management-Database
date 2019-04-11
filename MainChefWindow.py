import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
from MainManagerWindow import MainWindow


class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setFixedSize(750,675)
		global ui
		ui = uic.loadUi("ChefView.ui",self)
		self.setRec()
		ui.recipeList_2.itemClicked.connect(self.getRecInfo)
		ui.recipeList.itemClicked.connect(self.getChefRecInfo)

	def getChefRecInfo(self):
		currentRec = ui.recipeList.currentItem().data(16)
		ui.list.clear()
		price = DatabaseManage.getPrice(currentRec)
		ui.label.setText("$%.2f"%price)
		ingredients, quantities = DatabaseManage.getIngs(currentRec)
		for i in range(len(ingredients)):
			s = str(ingredients[i][0])
			s += "   "
			s += str(quantities[i])
			temp = QtWidgets.QListWidgetItem(s,ui.list)