#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/pesona.py

from app.config.controller import Controller

class Persona(Controller):
   # Atributos : _id, nombre
	def __init__(self):
		self.personas = self.load_model('personas')

	def autocompletar (self):
		lista = self.personas.autocompletar(self.params["nombre"])
		return self.bson_dumps(lista)