# app/config/database.py

from pymongo import MongoClient

class Database:
	def __init__(self):
		self.cliente = MongoClient('mongodb://localhost:27017')

	def get_connection(self):
		return self.cliente.db_accesos

	def close(self):
		self.cliente.close()