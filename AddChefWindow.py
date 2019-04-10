import PyQt5
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
from PyQt5.QtWidgets import QMessageBox

class MainWindow(QtWidgets.QMainWindow):
	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()

	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(500,500)
		global ui, index
		index = []
		ui = uic.loadUi("AddChef.ui",self)
		recipes = DatabaseManage.getAllRec()
		for recipe in recipes:
			recipe = recipe[0]
			temp = QtWidgets.QListWidgetItem(recipe,ui.listWidget_2)
			temp.setData(16,recipe)
		ui.pushButton_2.clicked.connect(self.addRecToChef)
		ui.pushButton.clicked.connect(self.addChef)

	def addChef(self):
		fname = ui.lineEdit.text()
		lname = ui.lineEdit_2.text()
		recs = []
		for i in index:
			recs.append(ui.listWidget.itemFromIndex(i).data(16))
		if fname == "":
			self.msgBox(QMessageBox.Warning,"No First Name.","Please enter a first name.")
			return None
		if lname == "":
			self.msgBox(QMessageBox.Warning,"No Last Name.","Please enter a last name.")
			return None
		if len(recs) == 0:
			self.msgBox(QMessageBox.Warning,"No Recipes.","There must be at least one recipe assigned to this chef.")
			return None
		DatabaseManage.addChef(fname,lname,recs)
		self.close()


	def addRecToChef(self):
		current = ui.listWidget_2.currentItem()
		if current == None:
			return None
		temp = QtWidgets.QListWidgetItem(current.data(16),ui.listWidget)
		temp.setData(16,current.data(16))
		index.append(ui.listWidget.indexFromItem(temp))