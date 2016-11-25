#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/personas.py

from app.config.model import Model
import re

class Personas(Model):
   # Atributos : _id, nombre
	def autocompletar (self, nombre):
		return list(self.db.personas.find({"nombre_completo" : {'$regex': nombre + '.*'}}))