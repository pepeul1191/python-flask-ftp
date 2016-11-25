#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/menus.py

from app.config.model import Model

class Items(Model):
   # Atributos (items) : _id, nombre, tipo, url, parent

	def listar(self, id_subtitulo):
		return list(self.db.menus.find({
		    "$and" : [
		        {"tipo":"item"}, 
		        {"parent": id_subtitulo}
		    ] 
		}))

	def crear(self, id_subtitulo, nombre, url):
		documento = {"nombre" : nombre, "tipo" : "item", "url" : url, "parent" : id_subtitulo}
		return self.db.menus.insert(documento)

	def editar(self, _id, nombre, url, id_subtitulo):
		documento = {"nombre" : nombre, "tipo" : "item", "url" : url, "parent" : id_subtitulo}
		self.db.menus.update( {'_id': _id }, documento)

	def eliminar(self, _id):
		self.db.menus.remove( {'_id': _id })