"""
**************** ฅ՞•ﻌ•՞ฅ *****************
* @author: Bruno Vitte @Tanque40 in github
* @version: 1.0
* @brief: Model user, manage users
"""
import sqlite3

class User:
	def __init__(self, id = 0, name="", last_name = "", email="", password=""):
		self.id = id
		self.name = name
		self.last_name = last_name
		self.email = email
		self.password = password

	def get_all(self):
		connection = sqlite3.connect("turbomessage.db")
		cursor = connection.cursor()
		return cursor.execute("SELECT * FROM user")

	def save(self):
		connection = sqlite3.connect("turbomessage.db")
		cursor = connection.cursor()
		cursor.execute("INSERT INTO user VAlUES(?, ?, ?, ?)", self.user_data())
		connection.commit()

	def user_data(self):
		return (self.name, self.last_name, self.email, self.password)