# app/config/database.py

import sqlite3

class Database:
	def __init__(self):
		self.connection = sqlite3.connect('db/db_archivos.db')

	def get_connection(self):
		return self.connection

	def close(self):
		self.connection.close()