#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/usuarios.py

from app.config.model import Model

class Estados(Model):
   # Atributos : _id, nombre
	def listar(self):
		rpta = []
		estados = self.db.estados.find()

		for estado in estados:
			rpta.append({"_id" : str(estado["_id"]), "nombre" : estado["estado"]})

		return rpta