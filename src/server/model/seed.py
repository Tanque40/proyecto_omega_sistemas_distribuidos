"""
**************** ฅ՞•ﻌ•՞ฅ *****************
* @author: Bruno Vitte @Tanque40 in github
* @version: 1.0
* @brief:  Generate DataBase if not exists with sqlite3
"""
import sqlite3

def execute_seed():
	# ? Create a new connection to database
	connection = sqlite3.connect("turbomessage.db")
	# ? To run queries we need a cursor from connection
	cursor = connection.cursor()

	cursor.execute("CREATE TABLE IF NOT EXISTS user (\
		id INTEGER NOT NULL PRIMARY KEY,\
		name varchar(255) NOT NULL,\
		last_name varchar(255),\
		email varchar(255) NOT NULL,\
		password varchar(255) NOT NULL\
	)")

	cursor.execute("CREATE TABLE IF NOT EXISTS email(\
		id INTEGER NOT NULL PRIMARY KEY,\
		subject varchar(255) NOT NULL,\
		readed boolean DEFAULT 0,\
		deleted boolean DEFAULT 0\
	)")

	cursor.execute("CREATE TABLE IF NOT EXISTS user_email(\
		sender_email varchar(255) NOT NULL,\
		reciver_email varchar(255) NOT NULL,\
		email_id varchar(255) NOT NULL,\
		foreign KEY(sender_email) REFERENCES user(email),\
		foreign KEY(reciver_email) REFERENCES user(email),\
		foreign KEY(email_id) REFERENCES email(id)\
	)")

	connection.commit()