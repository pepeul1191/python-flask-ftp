#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/menus.py

from app.config.model import Model

class Menus(Model):
   # Atributos (modulos) : _id, nombre, url, tipo
   # Atributos (subtitulos) : _id, nombre, tipo, icono, parent
   # Atributos (items) : _id, nombre, tipo, url, parent

	def menu_modulos(self):
		return list(self.db.menus.find({"tipo" : "modulo"}))

	def accesos_modulo(self, nombre):
		return self.db.eval("accesos_modulo('" + nombre + "')")