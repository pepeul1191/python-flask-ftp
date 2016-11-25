#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app/controllers/modulo.py

from app.config.controller import Controller

class Modulo(Controller):
   # Atributos (modulos < menu) : _id, nombre, url, tipo, descripcion

   	def __init__(self):
		self.modulos = self.load_model('modulos')

	def listar(self):
		lista = self.modulos.listar()
		return self.bson_dumps(lista)

	def crear(self):
		temp_id = self.params["temp_id"]
		nombre = self.unquote(self.params["nombre"])
		url = self.params["url"]
		object_id = self.modulos.crear(nombre, url)
		rpta = {'temporal' : temp_id, 'nuevo_id' : str(object_id)}
		return self.json_dumps(rpta)

	def editar(self):
		_id = self.to_ObjectId(self.params["_id"])
		nombre = self.unquote(self.params["nombre"])
		url = self.params["url"]
		self.modulos.editar( _id, nombre, url)
		return ""

	def editar_descripcion(self):
		id = self.params["id_modulo"]
		descripcion = self.params["descripcion"]
		self.modulos.editar_descripcion(self.to_ObjectId(id), descripcion)
		return ""

	def get_descripcion(self, id):
		try:
			documento = self.modulos.get_descripcion(self.to_ObjectId(id))
			return documento["descripcion"]
		except KeyError:
			return ""
	
	def eliminar(self, _id):
		_id = self.to_ObjectId(_id)
		self.modulos.eliminar(_id)
		return ""