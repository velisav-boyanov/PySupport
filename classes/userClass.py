import base64
import hashlib
import mysql.connector
import os

DB_NAME = 'project'

class User:
	def __init__(self, first, second, key, firm, phone, email):
		self.firstName = first
		self.secondName = second
		self.key =  key
		self.firm = firm
		self.phone = phone
		self.email = email

	def getName(self):
		return str(self.firstName+" "+self.secondName)

	def getFirm(self):
		return self.firm	

	def getEmail(self):
		return self.email

	def getPhone(self):
		return self.phone


	def authenticateUser(self):
		salt = "ung068ung06"
		hash_object = hashlib.sha256()
		hash_object.update((salt + self.key).encode())
		hash_password = hash_object.hexdigest()

		query = ("SELECT usr_no FROM users "
			"WHERE pas_key = %s AND email = %s")

		cursor.execute(query, (hash_password,self.email))

		lid = cursor.fetchall()


	def createUser(self):
		cnx = mysql.connector.connect(user='project1', password='password123',
            host='127.0.0.1',
            database='project')
		cursor = cnx.cursor()


		salt = "ung068ung06"
		hash_object = hashlib.sha256()
		hash_object.update((salt + self.key).encode())
		hash_password = hash_object.hexdigest()


		add_project = ("INSERT INTO users "
			"(first_name, pas_key, last_name, firm_name, email, phone_number)"
        	"VALUES (%s, %s, %s, %s, %s, %s)")

		data_project = (self.firstName, self.key, self.secondName, self.firm, self.email, self.phone)

		cursor.execute(add_project, data_project)
		user_no = cursor.lastrowid

		cnx.commit()

		cursor.close()
		cnx.close()

		return user_no


	def getUser(self, uid):
		cnx = mysql.connector.connect(user='project1', password='password123',
                            host='127.0.0.1',
                            database='project')
		cursor = cnx.cursor()

		query = ("SELECT * FROM users "
        	"WHERE usr_no = %s")

		cursor.execute(query, (uid,))

		rows = cursor.fetchall()	

		cursor.close()
		cnx.close()

		return rows