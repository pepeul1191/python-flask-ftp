#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/estado.py

from app.config.controller import Controller

class Estado(Controller):
   # Atributos : _id, usuario, contrasena, codigo_activacion, estado, sistema, persona, permisos, roles
	def __init__(self):
		self.estados = self.load_model('estados')

	def listar(self):
		lista = self.estados.listar()
		return self.bson_dumps(lista)