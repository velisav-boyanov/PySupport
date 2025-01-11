import mysql.connector

class Project:

	def __init__(self, name, location, firm, desc):
		self.name = name
		self.location = location
		self.firm = firm
		self.desc = desc

	def getName(self):
		return self.name	

	def getLocation(self):
		return self.location

	def getFirm(self):
		return self.firm

	def saveToDB(self, user):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		add_project = ("INSERT INTO projects "
			"(usr_no, project_name, firm, project_location, description)"
        	"VALUES (%s, %s, %s, %s, %s)")

		data_project = (user, self.name, self.firm, self.location, self.desc)

		cursor.execute(add_project, data_project)
		project_no = cursor.lastrowid

		cnx.commit()

		cursor.close()
		cnx.close()	


	def getFromDB(self, user):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT * FROM projects "
        	"WHERE usr_no = %s")

		cursor.execute(query, (user,))

		rows = cursor.fetchall()	

		cursor.close()
		cnx.close()

		return rows		