#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/subtitulos.py

from app.config.model import Model

class Subtitulos(Model):
   # Atributos (subtitulo< menu): _id, nombre, tipo, icono, parent

	def listar(self, id_modulo):
		return list(self.db.menus.find({
		    "$and" : [
		        {"tipo":"subtitulo"}, 
		        {"parent": id_modulo}
		    ] 
		}))

	def crear(self, _id_modulo, nombre, icono):
		documento = {"nombre" : nombre, "tipo" : "subtitulo", "icono" : icono, "parent" : _id_modulo}
		return self.db.menus.insert(documento)

	def editar(self, _id, _id_modulo, nombre, icono):
		documento = {"nombre" : nombre, "tipo" : "subtitulo", "icono" : icono, "parent" : _id_modulo}
		self.db.menus.update( {'_id': _id }, documento)

	def eliminar(self, _id):
		self.db.menus.remove( {'_id': _id })
		#FALTA ELIMINAR LOS HIJITOS ITEM, HACERLO CON UN STORED FUNCTION