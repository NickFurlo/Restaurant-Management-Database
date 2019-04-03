import MySQLdb

conn = sqlite3.connect("Proj.db")


#The missing parts of this are dependent on having the ui design
def addRec(name):
	global conn
	c = conn.cursor
	c.execute("SELECT * FROM MEAL WHERE MEAL_NAME == ?" name)
	results = c.fetchall()
	if results != None:
		c.close()
		return False
	#Need a way to add ingredients. Possible after having the ui design
	c.close()
	return True

def remRec(name):
	global conn 
	c = conn.cursor()
	c.execute("SELECT * FROM MEAL WHERE MEAL_NAME == ?" name )
	results = c.fetchall()
	if results == None:
		return False
	for result in results:
		




	