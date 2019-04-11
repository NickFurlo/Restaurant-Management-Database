import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage
from PyQt5.QtWidgets import QMessageBox
from AddRecipe_UI import Ui_Dialog


class AddRecipeWindow(QtWidgets.QDialog):
	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()

	def __init__(self, parent=None):
		super(AddRecipeWindow, self).__init__(parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		
		global index
		index = []
		#ui = uic.loadUi('AddRecipe.ui',self)
		self.setWindowTitle('Add Recipe')
		self.ui.pushButton.clicked.connect(self.addIng)
		self.ui.pushButton_3.clicked.connect(self.remIng)
		self.ui.pushButton_2.clicked.connect(self.addRec)

	def remIng(self):
		currentIng = self.ui.listWidget.currentRow()
		self.ui.listWidget.takeItem(currentIng)
		
	def addRec(self):
		name = self.ui.lineEdit.text()
		if name == "":
			self.msgBox(QMessageBox.Warning,"No Name Entered.","Please enter a name!")
			return None
		desc = self.ui.plainTextEdit.toPlainText()
		ings = []
		q = []
		for i in index:
			ings.append((self.ui.listWidget.itemFromIndex(i).data(16),self.ui.listWidget.itemFromIndex(i).data(17),""))
			q.append(self.ui.listWidget.itemFromIndex(i).data(18))
		if len(ings) == 0:
			self.msgBox(QMessageBox.Warning,"No Ingredients.", "Plese enter at least one ingredient")
			return None
		DatabaseManage.addRec(name,ings,q,desc)
		self.close()


	def addIng(self):
		name = self.ui.lineEdit_2.text()
		ppu = float(self.ui.lineEdit_3.text())
		qnty = self.ui.lineEdit_4.text()
		if qnty == "":
			self.msgBox(QMessageBox.Warning,"No Quantity.", "Please enter a quantity.")
			return None
		if name == "":
			self.msgBox(QMessageBox.Warning,"No Name","Please enter a name for the ingredient.")
		if ppu == "":
			self.msgBox(QMessageBox.Warning,"No Unit Price.","Please enter a unit price.")
		temp = QtWidgets.QListWidgetItem(name,self.ui.listWidget)
		temp.setData(16,name)
		temp.setData(17,ppu)
		temp.setData(18,qnty)
		index.append(self.ui.listWidget.indexFromItem(temp))
		self.ui.lineEdit_2.clear()
		self.ui.lineEdit_3.clear()
		self.ui.lineEdit_4.clear()