import mysql.connector

DB_NAME = 'project'

class Comment:

	def __init__(self, user, task, texts, time):
		self.time=time
		self.texts=texts
		self.user=user
		self.task=task

	def getTime(self):
		return self.time

	def getTexts(self):
		return self.texts

	def getUser(self):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT first_name, last_name FROM users "
        	"WHERE usr_no = %s")

		cursor.execute(query, (self.user,))

		res = cursor.fetchall()

		cursor.close()
		cnx.close()

		return res


	def saveToDB(self):	
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		add_comment = ("INSERT INTO comments "
			"(usr_no, task_no, cmnt, from_date) "
        	"VALUES (%s, %s, %s, %s)")

		data_comment = (self.user, self.task, self.texts, self.time)

		cursor.execute(add_comment, data_comment)
		comment_no = cursor.lastrowid

		cnx.commit()

		cursor.close()
		cnx.close()

	def getCommentsFromTask(self):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT * FROM comments "
        	"WHERE task_no = %s")

		cursor.execute(query, (self.task,))

		res = cursor.fetchall()

		cursor.close()
		cnx.close()

		return res	

