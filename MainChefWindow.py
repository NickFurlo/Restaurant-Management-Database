import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage



class MainWindow(QtWidgets.QMainWindow):
	def __init__(self,a):
		super(MainWindow, self).__init__()
		self.setFixedSize(700,675)
		global ui,name
		name = a
		ui = uic.loadUi("ChefView.ui",self)
		self.setRec()
		self.setChefRec()
		ui.recipeList_2.itemClicked.connect(self.getRecInfo)
		ui.recipeList.itemClicked.connect(self.getChefRecInfo)

	def setRec(self):
		ui.recipeList_2.clear()
		recipes = DatabaseManage.getAllMeals()
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe, ui.recipeList_2)
			temp.setData(16,recipe)
		ui.recipeList_2.sortItems()

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

	def getChefRecInfo(self):
		currentRec = ui.recipeList.currentItem().data(16)
		ui.list.clear()
		price = DatabaseManage.getPrice(currentRec)
		ui.label.setText("Price: $%.2f" %price)
		ingredients,quantities = DatabaseManage.getIngs(currentRec)
		for i in range(len(ingredients)):
			s = str(ingredients[i][0])
			s += "   "
			s += str(quantities[i])
			temp = QtWidgets.QListWidgetItem(s,ui.list)

	def setChefRec(self):
		recipes = DatabaseManage.getRecByChefName(name)
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe[0], ui.recipeList)
			temp.setData(16,recipe)
		ui.recipeList.sortItems()