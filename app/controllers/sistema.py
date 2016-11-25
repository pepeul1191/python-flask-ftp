#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/sistema.py

from app.config.controller import Controller

class Sistema(Controller):
   # Atributos : _id, nombre
	def __init__(self):
		self.sistemas = self.load_model('sistemas')

	def autocompletar (self):
		lista = self.sistemas.autocompletar(self.params["nombre"])
		return self.bson_dumps(lista)