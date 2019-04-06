import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(850,675)
		global ui
		ui = uic.loadUi('ManagerView.ui',self)
		ui.recipeList.setSortingEnabled(True)
		self.listenerSet()
		self.setChefs()
		self.setRec()

	def listenerSet(self):
		ui.recipeList.itemClicked.connect(self.getRec)
		ui.recipeList_2.itemClicked.connect(self.getRecInfo)

	def getRecInfo(self):
		currentRec = ui.recipeList_2.currentItem().data(16)



	def getRec(self):
		currentChef = ui.recipeList.currentItem()
		fname = currentChef.data(16)
		lname = currentChef.data(17)
		name = (fname, lname)
		recipes = DatabaseManage.getRecByChefName(name)
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe,ui.recipeDisplay)

	def setChefs(self):
		global ui
		chefs = DatabaseManage.getChefs()
		for chef in chefs:
			foo = chef[0] + " " + chef[1]
			temp = QtWidgets.QListWidgetItem(foo,ui.recipeList)
			temp.setData(16,chef[0])
			temp.setData(17,chef[1])
		ui.recipeList.sortItems()

	def setRec(self):
		recipes = DatabaseManage.getAllMeals()
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe, ui.recipeList_2)
			temp.setData(16,recipe)
		ui.recipeList_2.sortItems()

