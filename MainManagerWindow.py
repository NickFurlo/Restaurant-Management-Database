import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
import AddRecipeWindow
import AddChefWindow

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow,self).__init__(parent)
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
		ui.pushButton_3.clicked.connect(self.setRec)
		ui.pushButton_4.clicked.connect(self.setChefs)
		ui.btnRemoveChef.clicked.connect(self.remChef)

	def remChef(self):
		chef = ui.recipeList.currentItem()
		fname = chef.data(16)
		lname = chef.data(17)
		DatabaseManage.remChef(fname,lname)
		ui.listWidget.clear()

	def addChef(self):
		self.t = AddChefWindow.MainWindow()
		self.t.show()

	def addRec(self):
		self.t = AddRecipeWindow.MainWindow()
		self.t.show()
		ui.recipeList_2.clear()
		self.setRec()

	def removeRecipe(self):
		currentRec = ui.recipeList_2.currentItem().data(16)
		DatabaseManage.remRec(currentRec)
		ui.listWidget_2.clear()

	def getRecInfo(self):
		currentRec = ui.recipeList_2.currentItem().data(16)
		ui.listWidget_2.clear()
		price = DatabaseManage.getPrice(currentRec)
		ui.PriceLabel.setText("$%.2f"%price)
		ingredients, quantities = DatabaseManage.getIngs(currentRec)
		for i in range(len(ingredients)):
			s = str(ingredients[i][0])
			s += "   "
			s += str(quantities[i])
			temp = QtWidgets.QListWidgetItem(s,ui.listWidget_2)

	def getRec(self):
		ui.listWidget.clear()
		currentChef = ui.recipeList.currentItem()
		fname = currentChef.data(16)
		lname = currentChef.data(17)
		name = (fname, lname)
		recipes = DatabaseManage.getRecByChefName(name)
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe[0],ui.listWidget)

	def setChefs(self):
		ui.recipeList.clear()
		chefs = DatabaseManage.getChefs()
		for chef in chefs:
			foo = chef[0] + " " + chef[1]
			temp = QtWidgets.QListWidgetItem(foo,ui.recipeList)
			temp.setData(16,chef[0])
			temp.setData(17,chef[1])
		ui.recipeList.sortItems()

	def setRec(self):
		ui.recipeList_2.clear()
		recipes = DatabaseManage.getAllMeals()
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe, ui.recipeList_2)
			temp.setData(16,recipe)
		ui.recipeList_2.sortItems()

	def searchRecipes(self):
		global ui
		ingredient1 = ui.ingredient1.text()
		recipenames = DatabaseManage.searchRec(ingredient1)
		self.recipeList.clear()
		self.recipeList_2.clear()
		for i in recipenames:
			temp = QtWidgets.QListWidgetItem(i, ui.recipeList)
			temp2 = QtWidgets.QListWidgetItem(i, ui.recipeList_2)
		ui.recipeList.sortItems()
		ui.recipeList_2.sortItems()

	def searchChefs(self):
		global ui
		cfname = ui.lineEdit.text()
		clname = ui.lineEdit_2.text()
		cfullname = cfname + " " + clname
		allChefs = DatabaseManage.getChefs
		for chef in allChefs:
			if cfullname == chef:
				self.recipeList.setText(cfullname)