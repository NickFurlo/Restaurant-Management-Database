import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import DatabaseManage


class MainWindow(QtWidgets.QDialog):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(850,675)
		global ui
		ui = uic.loadUi('AddRecipe.ui',self)
		ui.pushButton.clicked.connect(self.addIng)
		ui.pushButton_3.clicked.connect(self.remIng)
		ui.pushButton_2.clicked.connect(self.addRec)

	def remIng(self):
		currentIng = ui.listWidget.currentRow()
		print(currentIng)
		
	def addRec(self):
		name = ui.lineEdit_3.text()
		desc = ui.plainTextEdit.text()
		ings = []
		for i in index:
			ings.append(ui.listWidget.itemFromIndex(i).data(16),ui.listWidget.itemFromIndex(i).data(17),"")
		DatabaseManage.addRec(name,ings)


	def addIng(self):
		global index
		index = []
		name = ui.lineEdit_2.text()
		ppu = ui.lineEdit_3.text()
		qnty = ui.lineEdit_4.text()
		alg = DatabaseManage.checkIng(name,ppu)
		if alg == True:
			temp = QtWidgets.QListWidgetItem(name,ui.listWidget)
		if alg == False:
			self.msgBox(QMessageBox.Warning,"Error","This ingredient is already in the database with a different price per unit. Leave the Price Per Unit field blank.")
			if alg == None:
				temp = QWidgets.QListWidgetItem(name,ui.listWidget)
				temp.setData(16,name)
				temp.setData(17,ppu)
				index.append(ui.listWidget.indexFromItem(temp))

	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()