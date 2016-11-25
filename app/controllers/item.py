#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app/controllers/menu.py

from app.config.controller import Controller

class Item(Controller):
   # Atributos (items) : _id, nombre, tipo, url, parent
   	def __init__(self):
		self.items = self.load_model('items')

	def listar(self, id_subtitulo):
		lista = self.items.listar(id_subtitulo)
		return self.bson_dumps(lista)

	def crear(self):
		temp_id = self.params["temp_id"]
		nombre = self.unquote(self.params["nombre"])
		url = self.params["url"]
		id_subtitulo = self.params["id_subtitulo"]

		object_id = self.items.crear(id_subtitulo, nombre, url)
		rpta = {'temporal' : temp_id, 'nuevo_id' : str(object_id)}
		return self.json_dumps(rpta)

	def editar(self):
		_id = self.to_ObjectId(self.params["_id"])
		nombre = self.unquote(self.params["nombre"])
		url = self.params["url"]
		id_subtitulo = self.params["id_subtitulo"]

		self.items.editar( _id, nombre, url, id_subtitulo)
		return ""

	def eliminar(self, _id):
		_id = self.to_ObjectId(_id)
		self.items.eliminar(_id)
		return ""