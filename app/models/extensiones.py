#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/extensiones.py

from app.config.model import Model
import pprint

class Extensiones(Model):
   # Atributos : id, nombre, extension
	def listar(self):
		rpta = []
		con = self.get_connection()
		con.row_factory = self.dict_factory 
		cur = con.cursor()
		cur.execute('SELECT * FROM extensiones;')
		for row in cur.fetchall():
			rpta.append(row)
		con.close()

		return rpta