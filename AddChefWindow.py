import PyQt5
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
from PyQt5.QtWidgets import QMessageBox
from AddChef_UI import Ui_MainWindow

class AddChefWindow(QtWidgets.QMainWindow):
	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()

	def __init__(self, parent=None):
		super(AddChefWindow, self).__init__(parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		global index
		index = []
		#ui = uic.loadUi("AddChef.ui",self)
		self.setWindowTitle('Add Chef')
		recipes = DatabaseManage.getAllRec()
		for recipe in recipes:
			recipe = recipe[0]
			temp = QtWidgets.QListWidgetItem(recipe,self.ui.listWidget_2)
			temp.setData(16,recipe)
		self.ui.pushButton_2.clicked.connect(self.addRecToChef)
		self.ui.pushButton.clicked.connect(self.addChef)

	def addChef(self):
		fname = self.ui.lineEdit.text()
		lname = self.ui.lineEdit_2.text()
		recs = []
		for i in index:
			recs.append(self.ui.listWidget.itemFromIndex(i).data(16))
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
		current = self.ui.listWidget_2.currentItem()
		if current == None:
			return None
		temp = QtWidgets.QListWidgetItem(current.data(16),self.ui.listWidget)
		temp.setData(16,current.data(16))
		index.append(self.ui.listWidget.indexFromItem(temp))