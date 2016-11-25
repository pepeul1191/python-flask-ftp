#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/prueba.py

from app.config.controller import Controller

class Prueba(Controller):
   # Atributos: 
	def metodo(self):
		#print "\n \n \n ESTAMOS EN EL METODO \n \n \n"
		return "estamos en método"

	def pormil(self,x):
		#print int(x) * 1000
		return int(x) * 1000

	def suma(self, x, y):
		#print int(x) + int(y)
		return int(x) + int(y)

	def resta(self, x, y):
		#print int(x) - int(y)
		return int(x) - int(y)

	def division(self, x, y):
		#print int(x) - int(y)
		try:
			rpta = float(x) / float(y)
		except ZeroDivisionError:
			rpta = "Error : No se puede dividir un número entre 0"

		return rpta

	def listar(self):
		permisos = self.load_model("permisos")
		return permisos