import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
import AddRecipeWindow
import AddChefWindow
from ManagerView_UI import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox

class ManagerWindow(QtWidgets.QMainWindow):
	def __init__(self, parent=None):
		super(ManagerWindow,self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Manager Window')
		self.ui.recipeList.setSortingEnabled(True)
		self.listenerSet()
		self.setChefs()
		self.setRec()

		self.addRecipe = AddRecipeWindow.AddRecipeWindow()
		self.addChef = AddChefWindow.AddChefWindow()

	def listenerSet(self):
		self.ui.recipeList.itemClicked.connect(self.getRec)
		self.ui.recipeList_2.itemClicked.connect(self.getRecInfo)
		self.ui.btnRemoveRecipe.clicked.connect(self.removeRecipe)
		self.ui.btnAdd.clicked.connect(self.addRec)
		self.ui.pushButton.clicked.connect(self.addChef)
		self.ui.pushButton_3.clicked.connect(self.setRec)
		self.ui.pushButton_4.clicked.connect(self.setChefs)
		self.ui.btnRemoveChef.clicked.connect(self.remChef)
		self.ui.btnSearch.clicked.connect(self.searchRec)
		self.ui.listWidget_2.itemClicked.connect(self.recInfoBox2)
		self.ui.listWidget.itemClicked.connect(self.recInfoBox1)
		self.ui.pushButton_2.clicked.connect(self.searchChef)

	def searchChef(self):
		fname = self.ui.lineEdit.text()
		lname = self.ui.lineEdit_2.text()
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
		name = self.ui.ingredientOne.text()
		recs = DatabaseManage.searchRec(name)
		self.ui.listWidget.clear()
		self.ui.listWidget_2.clear()
		if recs == None:
			self.msgBox(QMessageBox.Warning,"No Mathces","There are no recipes with this ingredient. Please check your spelling and try again.")
			return None
		for rec in recs:
			temp = QtWidgets.QListWidgetItem(rec[0], self.ui.listWidget)
			temp2 = QtWidgets.QListWidgetItem(rec[0], self.ui.listWidget_2)
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
			QList = self.ui.listWidget_2
		else:
			QList = self.ui.listWidget
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
		chef = self.ui.recipeList.currentItem()
		fname = chef.data(16)
		lname = chef.data(17)
		DatabaseManage.remChef(fname,lname)
		self.ui.listWidget.clear()

	def addChef(self):
		#self.t = AddChefWindow.MainWindow()
		self.addChef.show()

	def addRec(self):
		#self.t = AddRecipeWindow.MainWindow()
		self.addRecipe.show()
		self.ui.recipeList_2.clear()
		self.setRec()

	def removeRecipe(self):
		currentRec = self.ui.recipeList_2.currentItem().data(16)
		DatabaseManage.remRec(currentRec)
		self.ui.listWidget_2.clear()

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

	def getRec(self):
		self.ui.listWidget.clear()
		currentChef = self.ui.recipeList.currentItem()
		fname = currentChef.data(16)
		lname = currentChef.data(17)
		name = (fname, lname)
		recipes = DatabaseManage.getRecByChefName(name[0])
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe[0],self.ui.listWidget)

	def setChefs(self):
		self.ui.recipeList.clear()
		chefs = DatabaseManage.getChefs()
		for chef in chefs:
			foo = chef[0] + " " + chef[1]
			temp = QtWidgets.QListWidgetItem(foo,self.ui.recipeList)
			temp.setData(16,chef[0])
			temp.setData(17,chef[1])
		self.ui.recipeList.sortItems()

	def setRec(self):
		self.ui.recipeList_2.clear()
		recipes = DatabaseManage.getAllMeals()
		for recipe in recipes:
			temp = QtWidgets.QListWidgetItem(recipe, self.ui.recipeList_2)
			temp.setData(16,recipe)
		self.ui.recipeList_2.sortItems()

	def searchRecipes(self):
		#global ui
		ingredient1 = self.ui.ingredient1.text()
		recipenames = DatabaseManage.searchRec(ingredient1)
		self.recipeList.clear()
		self.recipeList_2.clear()
		for i in recipenames:
			temp = QtWidgets.QListWidgetItem(i, self.ui.recipeList)
			temp2 = QtWidgets.QListWidgetItem(i, self.ui.recipeList_2)
		self.ui.recipeList.sortItems()
		self.ui.recipeList_2.sortItems()

	def searchChefs(self):
		#global ui
		cfname = self.ui.lineEdit.text()
		clname = self.ui.lineEdit_2.text()
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