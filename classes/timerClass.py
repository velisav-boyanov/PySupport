import time, math
import mysql.connector

class Timer:
	t0 = 0
	isOn = False

	def __init__(self, time):
		self.time = time

	def startTime(self):
		if not self.isOn:
			self.t0 = time.time()

		self.isOn = True
		
	def endTime(self):
		if self.isOn:	
			t1 = time.time()
			total = t1-self.t0
			self.time += total

		self.t0 = 0
		self.isOn = False

		self.time = math.ceil(self.time)

	def getTime(self):
		return self.time	

	def getIsOn(self):
		return self.isOn

	def saveToDB(self, task):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		add_tasks = ("UPDATE tasks "
			"SET time_tracked = %s "
			"WHERE task_no = %s")

		data_tasks = (self.time, task)

		cursor.execute(add_tasks, data_tasks)
		task_no = cursor.lastrowid

		cnx.commit()


	def getFromDB(self, task):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT time_tracked FROM tasks "
        	"WHERE task_no = %s")

		cursor.execute(query, (task,))

		rows = cursor.fetchall()	

		cursor.close()
		cnx.close()

		self.time = rows[0][0]

		return rows			