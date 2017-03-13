#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/config/controller.py

import json
import urllib
import random, string

class Controller:
   # Atributos: NA
	def set_params(self, params):
		self.params = params

	def set_request(self, request):
		self.request = request

	def load_model (self, modelo):
		try:
			module =__import__("app.models." + str(modelo), globals(), locals(), [modelo])
			class_ = getattr(module, modelo.capitalize())
			return class_()
		except ImportError:
			return "ImportError: Modelo no existe"

	def load_controller (self, controlador):
		try:
			module =__import__("app.controllers." + str(controlador), globals(), locals(), [controlador])
			class_ = getattr(module, controlador.capitalize())
			return class_()
		except ImportError:
			return "ImportError: Controlador no existe"

	def load_lib (self, lib):
		try:
			module =__import__("app.libs." + str(lib), globals(), locals(), [lib])
			class_ = getattr(module, lib.capitalize())
			return class_()
		except ImportError:
			return "ImportError: Librería no existe"

	def json_rpta(self, tipo_mensaje, rpta_mensaje):
		rpta = {}
		rpta['tipo_mensaje'] = tipo_mensaje
		rpta['rpta_mensaje'] = rpta_mensaje
		json.dumps(rpta)
	
	def json_dumps(self, temp):
		return json.dumps(temp)

	def random_word(self):
   		return ''.join(random.choice(string.lowercase + string.digits) for i in range(30))

	def unquote(self, quote):
		return urllib.unquote(quote)#.decode('utf8')