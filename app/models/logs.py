#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/logs.py

from app.config.model import Model
from datetime import datetime

class Logs(Model):
   # Atributos : _id, usuario, sistema, momento
	def crear (self, sistema, documento_usuario):
		documento = {"sistema" : sistema, "usuario" : documento_usuario, "momento" : datetime.now()}
		return self.db.logs.insert(documento)

	def obtener(self, object_id):
		return self.db.logs.find_one({'_id': object_id})
		