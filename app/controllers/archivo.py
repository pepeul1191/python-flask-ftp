#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/archivo.py

from app.config.controller import Controller
import pprint
import os

class Archivo(Controller):
   # Atributos : 
	#def __init__(self):
		#self.usuarios = self.load_model('usuarios')

	def recibir(self):
		print "1 ++++++++++++++++++++++++++++++++++++++++"
		pprint.pprint(self.request.files['file'].__dict__)
		file = self.request.files['file']
		file.save(os.path.join('/home/pepe/Escritorio', 'demo.jpg'))
		print "2 ++++++++++++++++++++++++++++++++++++++++"
		return 'recibir???'