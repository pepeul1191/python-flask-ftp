#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/log.py

from app.config.controller import Controller

class Log(Controller):
   # Atributos : _id, usuario, sistema, momento
	def __init__(self):
		self.logs = self.load_model('logs')
		self.usuario = self.load_controller("usuario")

	def crear (self, sistema, usuario_nombre):
		documento_usuario = self.usuario.obtener(usuario_nombre)
		k = {"_id" : documento_usuario["_id"], "usuario" : documento_usuario["usuario"], "persona" : documento_usuario["persona"]}
		object_id = self.logs.crear(sistema, k)
		documento_log = self.logs.obtener(object_id)
		t = {"_id" : documento_log["_id"], "momento" : documento_log["momento"]}
		self.usuario.actualizar_ultimo_log(documento_usuario['_id'], t)
		return ""