import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
import AddRecipeWindow
import AddChefWindow
from ManagerView_UI import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(MainWindow,self).__init__(parent)
		self.setFixedSize(850,675)
		global ui
		ui = uic.loadUi('ManagerView.ui',self)
		self.setWindowTitle('Manager Window')
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
		ui.btnSearch.clicked.connect(self.searchRec)
		ui.listWidget_2.itemClicked.connect(self.recInfoBox2)
		ui.listWidget.itemClicked.connect(self.recInfoBox1)
		ui.pushButton_2.clicked.connect(self.searchChef)

	def searchChef(self):
		fname = ui.lineEdit.text()
		lname = ui.lineEdit_2.text()
		name = DatabaseManage.searchChef(fname,lname)
		if name == None:
			msg = "This is not a chef in your kitchen."
			icon = QMessageBox.Warning
			title = "Chef Not Found"
		else:
			msg = "This is a chef in your kitchen."
			icon = QMessageBox.Information
			title = "Chef Found"
		self.msgBox(icon,title,msg)

	def searchRec(self):
		name = ui.ingredientOne.text()
		recs = DatabaseManage.searchRec(name)
		ui.listWidget.clear()
		ui.listWidget_2.clear()
		if recs == None:
			self.msgBox(QMessageBox.Warning,"No Mathces","There are no recipes with this ingredient. Please check your spelling and try again.")
			return None
		for rec in recs:
			temp = QtWidgets.QListWidgetItem(rec[0],ui.listWidget)
			temp2 = QtWidgets.QListWidgetItem(rec[0],ui.listWidget_2)
			temp.setData(16,rec)
			temp.setData(21,True)
			temp2.setData(16,rec)
			temp2.setData(21,True)


	def recInfoBox2(self):
		self.recInfoBox(2)

	def recInfoBox1(self):
		self.recInfoBox(1)

	def recInfoBox(self,a):
		if a == 2:
			QList = ui.listWidget_2
		else:
			QList = ui.listWidget
		current = QList.currentItem().data(16)
		flag = QList.currentItem().data(21)
		if flag != True:
			return None
		desc = DatabaseManage.getDesc(current)
		if len(desc)==0:
			self.msgBox(QMessageBox.Information,current[0],"No description.")
		else:
			self.msgBox(QMessageBox.Information,current[0],desc[0])


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
		recipes = DatabaseManage.getRecByChefName(name[0])
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

	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()