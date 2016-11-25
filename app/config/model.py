#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/config/model.py

from app.config.database import Database
import urllib

class Model:
   # Atributos: NA
	def __init__(self):
		self._db = Database()
		self.db = self._db.get_connection()
		self.last_id = None

	def close(self):
		self._db.close()

	def unquote(self, quote):
		return urllib.unquote(quote).decode('utf8')

	def replace_blanks(self, s):
		return s.replace("|","/")