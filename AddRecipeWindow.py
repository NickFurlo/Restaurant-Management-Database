import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic


class MainWindow(QtWidgets.QDialog):
	def __init__(self):
		super(MainWindow,self).__init__()
		self.setFixedSize(850,675)
		global ui
		ui = uic.loadUi('AddRecipe.ui',self)
		ui.pushButton.clicked.connect(self.addIng)

	def addIng(self):
		name = ui.lineEdit_2.text()
		ppu = ui.lineEdit_3.text()
		qnty = ui.lineEdit_4.text()
		alg = DatabaseManage.checkIng(name,ppu)
		if alg == True:
			temp = QWidgets.QListWidgetItem(name,ui.listWidget)
			foo = QWidgets.QListWidgetItem(ppu,ui.listWidget_2)
		if alg == False:
			self.msgBox(QMessageBox.Warning,"Error","This ingredient is already in the database with a different price per unit. Leave the Price Per Unit field blank.")
		if alg = None:
			if alg == True:
			temp = QWidgets.QListWidgetItem(name,ui.listWidget)
			foo = QWidgets.QListWidgetItem(ppu,ui.listWidget_2)
			temp.setData(16,name)
			foo.setData(16,ppu)
			foo.setData(17,qnty)

	def msgBox(self,icon,title,message):
		msg = QMessageBox()
		msg.setIcon(icon)
		msg.setText(message)
		msg.setWindowTitle(title)
		retval = msg.exec_()