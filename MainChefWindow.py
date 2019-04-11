import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
from ChefView_UI import Ui_MainWindow



class ChefWindow(QtWidgets.QMainWindow,):
	def __init__(self, a):
		super(ChefWindow, self).__init__()
		# self.setFixedSize(700,675)
		# global name
		self.name = a
		#ui = uic.loadUi("ChefView.ui",self)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Chef Window')
		self.setRec()
		self.setChefRec()
		self.ui.recipeList_2.itemClicked.connect(self.getRecInfo)
		self.ui.recipeList.itemClicked.connect(self.getChefRecInfo)

	def setRec(self):
		self.ui.recipeList_2.clear()
		recipes = DatabaseManage.getAllMeals()
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe, self.ui.recipeList_2)
			temp.setData(16,recipe)
		self.ui.recipeList_2.sortItems()

	def getRecInfo(self):
		currentRec = self.ui.recipeList_2.currentItem().data(16)
		self.ui.listWidget_2.clear()
		price = DatabaseManage.getPrice(currentRec)
		self.ui.PriceLabel.setText("$%.2f"%price)
		ingredients, quantities = DatabaseManage.getIngs(currentRec)
		for i in range(len(ingredients)):
			s = str(ingredients[i][0])
			s += "   "
			s += str(quantities[i])
			temp = QtWidgets.QListWidgetItem(s,self.ui.listWidget_2)

	def getChefRecInfo(self):
		currentRec = self.ui.recipeList.currentItem().data(16)
		self.ui.list.clear()
		price = DatabaseManage.getPrice(currentRec)
		self.ui.label.setText("Price: $%.2f" %price)
		ingredients,quantities = DatabaseManage.getIngs(currentRec)
		for i in range(len(ingredients)):
			s = str(ingredients[i][0])
			s += "   "
			s += str(quantities[i])
			temp = QtWidgets.QListWidgetItem(s,self.ui.list)

	def setChefRec(self):
		recipes = DatabaseManage.getRecByChefName(self.name)
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe[0], self.ui.recipeList)
			temp.setData(16,recipe)
		self.ui.recipeList.sortItems()