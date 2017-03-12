#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/extension.py

from app.config.controller import Controller

class Extension(Controller):
   # Atributos : id, nombre, extension
	#def __init__(self):
		#self.usuarios = self.load_model('usuarios')

	def listar(self):
		extensiones = self.load_model('extensiones')
		lista = extensiones.listar()
		return self.json_dumps(lista)