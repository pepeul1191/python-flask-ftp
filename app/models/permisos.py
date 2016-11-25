#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/permisos.py

from app.config.model import Model

class Permisos(Model):
   # Atributos: _id, nombre, llave

	def listar(self):
		return list(self.db.permisos.find())

	def crear(self, nombre, llave):
		documento = {"nombre" : nombre, "llave" : llave}
		return self.db.permisos.insert(documento)

	def editar(self,  _id, nombre, llave):
		documento = {"nombre" : nombre, "llave" : llave}
		self.db.permisos.update( {'_id': _id }, documento)

	def eliminar(self, _id):
		self.db.permisos.remove( {'_id': _id })