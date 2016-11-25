#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/usuarios.py

from app.config.model import Model
import pprint

class Usuarios(Model):
   # Atributos : _id, usuario, contrasena, codigo_activacion, estado, sistema, persona, permisos, roles
	def get_usuario (self, usuario, contrasena):
		rpta = list(self.db.usuarios.find({"usuario": usuario, "contrasena" : contrasena}))
		self.close()
		return rpta
		
	def listar(self):
		rpta = []
		usuarios = self.db.usuarios.find()
		for usuario in usuarios:
			if usuario["persona"] == {}:
				persona = "Sin asignar"
			else:
				persona = usuario["persona"]["nombre_completo"]
			if usuario["codigo_activacion"] == "":
				codigo_activacion = "No tiene"
			else:
				codigo_activacion = "Si tiene"
			if usuario["sistema"] == {}:
				sistema = "Sin asignar"
			else:
				sistema = usuario["sistema"]["nombre"] #+ ", " + usuario["sistema"]["empresa"]
			ultimo_log = str(usuario["ultimo_log"]["momento"])
			estado = usuario["estado"]["estado"]
			rpta.append({"_id" : usuario["_id"], "persona" : persona, "usuario" : usuario["usuario"], "codigo_activacion" : codigo_activacion, "ultimo_log" : ultimo_log[:19], "estado" : estado, "sistema" : sistema, "tiempo_sesion" : usuario["tiempo_sesion"]})

		return rpta

	def obtener(self, nombre_usuario):
		return self.db.usuarios.find_one({'usuario': nombre_usuario})

	def obtener_datos_reducidos(self, _id_usuario):
		return self.db.usuarios.find_one({"_id": _id_usuario})

	def nombre_repetido(self, _id, nombre_usuario):
		return self.db.eval("nombre_repetido('" +_id + "', '" + nombre_usuario + "')")

	def actualizar_ultimo_log(self, _id, log):
		usuario = self.db.usuarios.find_one({'_id': _id })
		usuario["ultimo_log"] = log
		self.db.usuarios.update( {'_id': _id }, usuario)

	def asociar_rol(self, id_usuario, id_rol):
		self.db.eval("asociar_usuario_rol('" + id_usuario + "', '" + id_rol + "')")

	def desasociar_rol(self, id_usuario, id_rol):
		self.db.eval("desasociar_usuario_rol('" + id_usuario + "', '" + id_rol + "')")

	def listar_roles(self, id_usuario):
		return self.db.eval("listar_roles_usuario('" + id_usuario + "')")

	def asociar_permiso(self, id_usuario, id_permiso):
		self.db.eval("asociar_usuario_permiso('" + id_usuario + "', '" + id_permiso + "')")

	def desasociar_permiso(self, id_usuario, id_permiso):
		self.db.eval("desasociar_usuario_permiso('" + id_usuario + "', '" + id_permiso + "')")

	def listar_permisos(self, id_usuario):
		return self.db.eval("listar_permisos_usuario('" + id_usuario + "')")

	def crear(self, nombre_usuario, contrasena, _id_estado, tiempo):
		estado = self.db.estados.find_one({'_id' : _id_estado})

		usuario = {}
		usuario["persona"] = {}
		usuario["roles"] = []
		usuario["permisos"] = []
		usuario["ultimo_log"] = {}
		usuario["ultimo_log"]["momento"] = ""
		usuario["sistema"] = {}
		usuario["codigo_activacion"] = ""
		usuario["contrasena"] = contrasena
		usuario["usuario"] = nombre_usuario
		usuario["estado"] = estado
		usuario["tiempo_sesion"] = tiempo

		return self.db.usuarios.insert(usuario)

	def editar(self, _id, nombre_usuario, contrasena, _id_estado, tiempo):
		usuario = self.db.usuarios.find_one({'_id' : _id })
		estado = self.db.estados.find_one({'_id' : _id_estado})

		if contrasena != "":
			usuario["contrasena"] = contrasena
		usuario["usuario"] = nombre_usuario
		usuario["estado"] = estado
		usuario["tiempo_sesion"] = tiempo

		self.db.usuarios.update( {'_id': _id }, usuario)

	def asociar_persona(self, _id, _id_persona, _id_sistema):
		usuario = self.db.usuarios.find_one({'_id' : _id })
		persona = self.db.personas.find_one({'_id' : _id_persona })
		sistema = self.db.sistemas.find_one({'_id' : _id_sistema })

		usuario["persona"] = persona
		usuario["sistema"] = sistema

		self.db.usuarios.update( {'_id': _id }, usuario)

	def cascada_rol(self, id_rol):
		self.db.eval("usuario_cascada_rol('" + id_rol + "')")