#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/archivo.py

from app.config.controller import Controller
import pprint

class Archivo(Controller):
   # Atributos : 
	#def __init__(self):
		#self.usuarios = self.load_model('usuarios')

	def recibir(self):
		print self.params
		return 'recibir???'