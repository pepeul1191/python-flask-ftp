#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/config/bootstrap.py

import sys

class Bootstrap:
   # Atributos: rpta
	def __init__(self, request):
		self.rpta = ""
		self.controlador = request.controlador
		self.metodo = request.metodo
		self.request = request
		argumento = request.argumento

		try:
			module =__import__("app.controllers." + str(self.controlador), globals(), locals(), [self.controlador])
			class_ = getattr(module, self.controlador.capitalize())
			instancia = class_()
			instancia.set_request(request.request)
		except ImportError:
			self.rpta = "ImportError: Método no existe"

		try:
			if len(argumento) == 1:
				#print "if 1 : argumento mayor a 1"
				if argumento[0] == "":
					#print "if 1.1 : resulta que el argumento era vacío porque era /"
					if request.params == False:
						#print "if 1.1.1 : resulta que no habia params"
						metodo = getattr(instancia, self.metodo)
						self.rpta = metodo()
					else:
						#print "if 1.1.2 : resulta que si habia params"
						set_params = getattr(instancia, "set_params")
						set_params(request.params)
						metodo = getattr(instancia, self.metodo)
						self.rpta = metodo()
				else:
					#print "else 1.1 : resulta que sí habia un argumento"
					metodo = getattr(instancia, self.metodo)
					self.rpta = metodo(argumento[0])
			elif len(argumento) == 0 and request.params == False:
				#print "elif 1 no habia argumentos ni parámetros"
				metodo = getattr(instancia, self.metodo)
				self.rpta = metodo()
			elif len(argumento) > 1:
				#print "elif 2 habia' varios argumentos"
				try:
					metodo = getattr(instancia, self.metodo)
					#print metodo(*argumento)
					self.rpta = metodo(*argumento)
				except AttributeError:
					self.rpta = "Error: Método no existe"
		except ArithmeticError:#TypeError:
			self.rpta = "TypeError: El número de parámetros no coincide"
		except ArithmeticError:
			pass
			
#Fuente : http://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported
#Fuente : http://stackoverflow.com/questions/1057843/how-can-i-import-a-package-using-import-when-the-package-name-is-only-know/1057898#1057898