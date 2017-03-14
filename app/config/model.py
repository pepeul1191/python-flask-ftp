#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/config/model.py

from app.config.database import Database
import urllib

class Model:
   # Atributos: NA
	def __init__(self):
		db = Database()
		self.connection = db.get_connection()
		self.last_id = 0

	def get_connection(self):
		return self.connection

	def dict_factory(self, cursor, row):
		d = {}
		for idx, col in enumerate(cursor.description):
			d[col[0]] = row[idx]
		return d

	def close(self):
		self.connection.close()

	def unquote(self, quote):
		return urllib.unquote(quote).decode('utf8')

	def replace_blanks(self, s):
		return s.replace("|","/")