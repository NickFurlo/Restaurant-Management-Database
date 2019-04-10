import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
import AddRecipeWindow
import AddChefWindow

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
		ui.btnRemoveRecipe.clicked.connect(self.removeRecipe)
		ui.btnAdd.clicked.connect(self.addRec)
		ui.pushButton.clicked.connect(self.addChef)

	def addChef(self):
		self.t = AddChefWindow.MainWindow()
		self.t.show()

	def addRec(self):
		self.t = AddRecipeWindow.MainWindow()
		self.t.show()

	def removeRecipe(self):
		currentRec = ui.recipeList_2.currentItem.data(16)
		DatabaseManage.remRec(currentRec)
		self.setRec()

	def getRecInfo(self):
		currentRec = ui.recipeList_2.currentItem().data(16)
		price = DatabaseManage.getPrice(currentRec)
		ui.PriceLabel.setText("$"+price)
		ingredients, quantities = DatabaseManage.getIngs(currentRec)
		for i in range(len(ingredients)):
			temp = QtWidgets.QListWidgetItem(ingredients[i] + " " + quantities[i],ui.recipeList_2)

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

