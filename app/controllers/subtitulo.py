#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app/controllers/subtitulo.py

from app.config.controller import Controller

class Subtitulo(Controller):
   # Atributos (subtitulo< menu): _id, nombre, tipo, icono, parent

   	def __init__(self):
		self.subtitulos = self.load_model('subtitulos')

	def	listar(self, id_modulo):
		lista = self.subtitulos.listar(id_modulo)
		return self.bson_dumps(lista)

	def crear(self):
		id_modulo = self.params["id_modulo"]
		temp_id = self.params["temp_id"]
		nombre = self.unquote(self.params["nombre"])
		icono = self.unquote(self.params["icono"])

		object_id = self.subtitulos.crear(id_modulo, nombre, icono)
		rpta = {'temporal' : temp_id, 'nuevo_id' : str(object_id)}
		return self.json_dumps(rpta)

	def editar(self):
		id_modulo = self.params["id_modulo"]
		_id = self.to_ObjectId(self.params["id"])
		nombre = self.unquote(self.params["nombre"])
		icono = self.unquote(self.params["icono"])

		self.subtitulos.editar( _id, id_modulo, nombre, icono)
		return ""

	def eliminar(self, _id):
		_id = self.to_ObjectId(_id)
		self.subtitulos.eliminar(_id)
		return ""