# app/config/database.py

import sqlite3

class Database:
	def __init__(self):
		self.cliente = sqlite3.connect('../../db/db_archivos.db')

	def get_connection(self):
		return self.cliente

	def close(self):
		self.cliente.close()