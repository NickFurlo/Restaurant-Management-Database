import sqlite3
import random

conn = sqlite3.connect("Proj.db")

#Ingredients is passed as an array of triples. Each triple is of the form (name, unit price, unit)
def addRec(name,ingredients):
	global conn
	c = conn.cursor
	c.execute("SELECT * FROM MEAL WHERE MEAL_NAME = ?", name)
	results = c.fetchall()
	if len(results) > 0:
		c.close()
		return False
	c.exectue("SELECT MEAL_ID FROM MEAL")
	ids = c.fetchall()
	trueId = idGen(ids)
	c.execute("INSERT INTO MEAL VALUES (?, ?)", trueId, name)
	flag = False
	for ing in ingredients:
		if addIng(ing) == False:
			flag = True
	c.close()
	#A None return value means that the recipe was added, but the ingredient(s) already existed
	if flag == True:
		return None
	return True

#ing is passed as a triple the form (name, unit price, unit)
def addIng(ing):
	if len(ing) == 2:
		ing.append("")
	global conn
	c = conn.cursor()
	c.execute("SELECT * FROM INGREDIENT WHERE INGREDIENT_NAME = ?", ing[0])
	results = c.fetchall()
	if len(results) > 0:
		c.close()
		return False
	c.execute("SELECT INGREDIENT_NUM FROM INGREDIENT")
	ids = c.fetchall()
	id = idGen(ids)
	c.execute("INSERT INTO INGREDIENT VALUES (?,?,?,?)",id, ing)
	c.close()
	return True
	
def idGen(existIds):
	id = random.randint(0,1000)
	if id in existIds:
		return idGen(existIds)
	else:
		return id

def remRec(name):
	global conn 
	c = conn.cursor()
	c.execute("SELECT * FROM MEAL WHERE MEAL_NAME = ?", name )
	results = c.fetchall()
	if len(results) == 0:
		return False
	for result in results:
		id = result[0]
		c.execute("DELETE FROM RECIPE WHERE MEAL_ID = ?", id)
	return True

#ings is passed as an array
def searchRec(ings):
	global conn
	c = conn.cursor()
	n = len(ings)
	if n == 0:
		return False
	if n > 3:
		return False
	ingids = []
	for ing in ings:
		c.execute("SELECT INGREDIENT_NUM FROM INGREDIENT WHERE INGREDIENT_NAME = ?", ing)
		temp = c.fetchall()
		for i in temp:
			ingids.append(i)
	mealids = []
	for id in ingids:
		c.execute("SELECT MEAL_ID FROM RECIPE WHERE INGREDIENT_NUM = ?", id)
		temp = c.fetchall()
		for i in temp:
			mealids.append(i)
	mealnames = []
	for mealname in mealnames:
		c.execute("SELECT MEAL_NAME FROM MEAL WHERE MEAL_ID = ?", mealname)
		temp = c.fetchall()
		for i in temp:
			mealnames.append(i)
	return mealnames

def checkChefName(name):
	global conn
	c = conn.cursor()
	c.execute("SELECT * FROM CHEF WHERE CHEF_FNAME == '%s'" %name)
	results = c.fetchall()
	if len(results) > 0:
		return True
	return False

def getChefs():
	global conn
	c = conn.cursor()
	c.execute("SELECT CHEF_FNAME,CHEF_LNAME FROM CHEF")
	results=c.fetchall()
	return results

def getRecByChefName(name):
	c = conn.cursor()
	c.execute("SELECT CHEF_ID FROM CHEF WHERE CHEF_FNAME = ? AND CHEF_LNAME = ?", name)
	chefId = c.fetchall()[0]
	c.execute("SELECT MEAL_ID FROM MAKES WHERE CHEF_ID = ?", chefId)
	mealIds = c.fetcall()
	meals = []
	for id in mealIds:
		c.execute("SELECT MEAL_NAME FROM MEAL WHERE MEAL_ID = ?", id)
		meals.append(c.fetcall()[0])
	return meals

def getAllMeals():
	c = conn.cursor()
	c.execute("SELECT MEAL_NAME FROM MEAL")
	results = c.fetchall()
	return results

def getPrice(name):
	c = conn.cursor()
	c.execute("SELECT MEAL_ID FROM MEAL WHERE MEAL_NAME = ?", name)
	mealId = c.fetchall()[0]
	c.execute("SELECT INGREDIENT_NUM, QNTY FROM RECIPE WHERE MEAL_ID = ?", mealId)
	ingAndQuants = c.fetchall()
	ingids = []
	quants = []
	for i in ingAndQuants:
		ingids.append(i[0])
		quants.append(i[1])
	prices = []
	for i in range(len(ingids)):
		c.execute("SELECT INGREDIENT_NAME, INGREDIENT_UNIT_PRICE FROM INGREDIENT WHERE INGREDIENT_NUM = ?", ingids[i])
		result = c.fetchall()[0]
		prices.append(quants[i]*result[1])
	sum = 0
	for price in prices:
		sum += price
	return sum

def getIngs(recipe):
	c = conn.cursor()
	c.execute("SELECT MEAL_ID FROM MEAL WHERE MEAL_NAME = ?", recipe)
	mealId = c.fetcall()[0]
	c.execute("SELECT INGREDIENT_NUM, QNTY FROM RECIPE WHERE MEAL_ID = ?", mealId)
	results = c.fetchall()
	nums = []
	quants = []
	for result in results:
		nums.append(result[0])
		quants.append(results[1])
	names = []
	for num in nums:
		c.execute("SELECT INGREDIENT_NAME FROM INGREDIENT WHERE INGREDIENT_NUM = ?", num)
		names.append(c.fetchall()[0])
	return names, quants

def checkIng(name,ppu):
	c = conn.cursor()
	c.execute("SELECT INGREDIENT_NAME FROM INGREDIENT WHERE INGREDIENT_NAME = '%s'"%name)
	temp = c.fetchall()
	if len(temp) == 0:
		nameExist = None
	else:
		nameExist = temp[0]
	if nameExist == None:
		newIng = (name, ppu)
		addIng()
		return None

	if ppu == "":
		return True
	c.execute("SELECT FROM INGREDIENT WHERE INGREDIENT_NAME = '%s' AND INGREDIENT_UNIT_PRICE = %d"%(name, ppu))
	results = c.fetchall()[0]
	if results == None:
		return False
	return True