#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/archivos.py

from app.config.model import Model
import pprint

class Archivos(Model):
   # Atributos : id, nombre, descripcion, nombre_generado, extension_id
	def crear(self, nombre, descripcion, nombre_generado, extension):
		con = self.get_connection()
		cur = con.cursor()
		t = (nombre, descripcion, nombre_generado, extension)
		cur.execute('INSERT INTO archivos (nombre, descripcion, nombre_generado, extension_id) VALUES ( ?, ?, ?, (SELECT id FROM extensiones WHERE extension = ?))', t)
		self.get_connection().commit()
		self.last_id = str(int(cur.lastrowid))
		con.close()