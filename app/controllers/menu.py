#!/usr/bin/env python
# -*- coding: utf-8 -*-
# app/controllers/menu.py

from app.config.controller import Controller

class Menu(Controller):
   # Atributos (modulos) : _id, nombre, url, tipo
   # Atributos (subtitulos) : _id, nombre, tipo, icono, parent
   # Atributos (items) : _id, nombre, tipo, url, parent

   	def __init__(self):
		self.menus = self.load_model('menus')

	def menu_modulos(self):
		lista = self.menus.menu_modulos()
		rpta = []

		for d in lista:
			nombre = d["nombre"]
			url = d["url"]
			documento = {"nombre" : nombre, "url" : url}
			rpta.append(documento)

		return self.bson_dumps(rpta)

	def accesos_modulo(self, nombre):
		rpta = self.menus.accesos_modulo(nombre)
		return self.bson_dumps(rpta)