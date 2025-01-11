import mysql.connector

class Task:

	def __init__(self, name, jobs, jobs_done, time, worker):
		self.name = name
		self.jobs = jobs
		self.jobs_done = jobs_done
		self.worker = worker
		self.time = time

	def getName(self):
		return self.name	

	def getJobs(self):
		return self.jobs

	def getJobsDone(self):
		return self.jobs_done

	def getWorker(self):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT first_name, last_name FROM tasks "
        	"WHERE usr_no = %s")

		cursor.execute(query, self.worker)

		res = cursor['usr_no']

		cursor.close()
		cnx.close()

		return res


	def saveToDB(self, project):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		add_tasks = ("INSERT INTO tasks "
			"(usr_no, project_no, jobs_done, jobs, end_date, task)"
        	"VALUES (%s, %s, %s, %s, %s, %s)")

		data_tasks = (self.worker, project, self.jobs_done, self.jobs, self.time, self.name)

		cursor.execute(add_tasks, data_tasks)
		task_no = cursor.lastrowid

		cnx.commit()

		cursor.close()
		cnx.close()		

	def getFromDB(self):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT * FROM tasks "
        	"WHERE project_no = %s")

		cursor.execute(query, (self.worker,))

		rows = cursor.fetchall()	

		cursor.close()
		cnx.close()

		return rows	

	def incrementDB(self, task):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		add_tasks = ("UPDATE tasks "
			"SET jobs_done = jobs_done + 1 "
			"WHERE task_no = %s")

		cursor.execute(add_tasks, (task,))

		add_tasks = ("UPDATE tasks "
			"SET jobs = jobs - 1 "
			"WHERE task_no = %s")

		cursor.execute(add_tasks, (task,))

		task_no = cursor.lastrowid

		cnx.commit()
