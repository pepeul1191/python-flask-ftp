#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/config/controller.py

import json
import urllib
from bson.json_util import dumps
from bson.objectid import ObjectId

class Controller:
   # Atributos: NA
	def set_params(self, params):
		self.params = params

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
	
	def bson_dumps(self, temp):
		return dumps(temp)

	def json_dumps(self, temp):
		return json.dumps(temp)

	def to_ObjectId(self, _id):
		return ObjectId(_id)

	def unquote(self, quote):
		return urllib.unquote(quote)#.decode('utf8')