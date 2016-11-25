#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/sistemas.py

from app.config.model import Model
import re

class Sistemas(Model):
   # Atributos : _id, nombre
	def autocompletar (self, nombre):
		return list(self.db.sistemas.find({"nombre" : {'$regex': nombre + '.*'}}))