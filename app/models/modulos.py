#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/modulos.py

from app.config.model import Model

class Modulos(Model):
   # Atributos (modulos < menu) : _id, nombre, url, tipo, descripcion

	def listar(self):
		return list(self.db.menus.find({"tipo" : "modulo"}))

	def crear(self, nombre, url):
		documento = {"nombre" : nombre, "url" : url, "tipo" : "modulo"}
		return self.db.menus.insert(documento)

	def editar(self,  _id, nombre, url):
		documento = self.db.menus.find_one({'_id': _id})
		documento["nombre"] = nombre
		documento["url"] = url
		self.db.menus.update( {'_id': _id }, documento)

	def editar_descripcion(self, _id, descripcion):
		documento = self.db.menus.find_one({'_id': _id})
		documento["descripcion"] = descripcion
		self.db.menus.update( {'_id': _id}, documento)

	def get_descripcion(self, _id):
		return self.db.menus.find_one({'_id': _id})

	def eliminar(self, _id):
		self.db.menus.remove( {'_id': _id })
		#FALTA ELIMINAR LOS HIJITOS SUBMENU Y LOS HIJITOS ITEM DE LOS SUBMENUS, HACERLO CON UN STORED FUNCTION