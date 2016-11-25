#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/usuario.py

from app.config.controller import Controller

class Usuario(Controller):
   # Atributos : _id, usuario, contrasena, codigo_activacion, estado, sistema, persona, permisos, roles
	def __init__(self):
		self.usuarios = self.load_model('usuarios')

	def existe_usuario_json (self):
		rpta_query = self.usuarios.get_usuario(self.usuario, self.contrasena)

		if len(rpta_query) == 0:
			return "no"
		else:
			return "si"

	def existe(self, usuario, contrasena):
		c = self.load_lib("cipher")
		rpta_query = self.usuarios.get_usuario(usuario, c.encrypt(contrasena))

		if len(rpta_query) == 0:
			return "no"
		else:
			return "si"

	def listar(self):
		lista = self.usuarios.listar()
		return self.bson_dumps(lista)

	def obtener(self, nombre_usuario):
		return self.usuarios.obtener(nombre_usuario)

	def obtener_datos_reducidos(self, id_usuario):
		_id_usuario = self.to_ObjectId(id_usuario)
		usuario = self.usuarios.obtener_datos_reducidos(_id_usuario)
		
		rpta = { 
			"usuario" : usuario["usuario"], 
			"tiempo_sesion" : usuario["tiempo_sesion"],
			"ultimo_log" : str(usuario["ultimo_log"]["momento"]),
			"id_estado" : str(usuario["estado"]["_id"])
		}

		if usuario["persona"] != {}:
			rpta["persona"] = {}
			rpta["persona"]["id"] = str(usuario["persona"]["_id"])
			rpta["persona"]["correo"] = str(usuario["persona"]["correo"])
			rpta["persona"]["nombre_completo"] = usuario["persona"]["nombre_completo"]
		else:
			rpta["persona"] = {}

		if usuario["sistema"] != {}:
			rpta["sistema"] = {}
			rpta["sistema"]["id"] = str(usuario["sistema"]["_id"])
			rpta["sistema"]["nombre"] = str(usuario["sistema"]["nombre"])
		else:
			rpta["sistema"] = {}

		return self.bson_dumps(rpta)

	def nombre_repetido(self):
		nombres_repetidos = self.usuarios.nombre_repetido(self.params["_id"], self.params["nombre_usuario"])
		return self.bson_dumps(nombres_repetidos)

	def actualizar_ultimo_log(self, _id, log):
		self.usuarios.actualizar_ultimo_log(_id, log)

	def listar_roles(self, id_usuario):
		rpta = ""
		if id_usuario == "E":
			rol = self.load_controller("rol")
			rpta = rol.listar()
		else:
			rpta = self.usuarios.listar_roles(id_usuario)
		return self.bson_dumps(rpta)

	def asociar_rol(self, id_usuario, id_rol):
		self.usuarios.asociar_rol(id_usuario, id_rol)
		return ""

	def desasociar_rol(self, id_usuario, id_rol):
		self.usuarios.desasociar_rol(id_usuario, id_rol)
		return ""

	def listar_permisos(self, id_usuario):
		rpta = ""
		if id_usuario == "E":
			permiso = self.load_controller("permiso")
			rpta = permiso.listar()
		else:
			rpta = self.usuarios.listar_permisos(id_usuario)
		return self.bson_dumps(rpta)

	def asociar_permiso(self, id_usuario, id_permiso):
		self.usuarios.asociar_permiso(id_usuario, id_permiso)
		return ""

	def desasociar_permiso(self, id_usuario, id_permiso):
		self.usuarios.desasociar_permiso(id_usuario, id_permiso)
		return ""

	def crear(self):
		c = self.load_lib("cipher")

		usuario = self.unquote(self.params["usuario"])
		contrasena = c.encrypt(self.unquote(self.params["contrasena"]))
		_id_estado = self.to_ObjectId(self.unquote(self.params["id_estado"]))
		tiempo = self.unquote(self.params["tiempo"])

		return str(self.usuarios.crear(usuario, contrasena, _id_estado, tiempo))

	def editar(self):
		c = self.load_lib("cipher")

		_id = self.to_ObjectId(self.unquote(self.params["id_usuario"]))
		usuario = self.unquote(self.params["usuario"])
		contrasena = c.encrypt(self.unquote(self.params["contrasena"]))
		_id_estado = self.to_ObjectId(self.unquote(self.params["id_estado"]))
		tiempo = self.unquote(self.params["tiempo"])

		self.usuarios.editar(_id, usuario, contrasena, _id_estado, tiempo)
		return ""

	def asociar_persona(self, id, id_persona, id_sistema):
		_id = self.to_ObjectId(id)
		_id_persona = self.to_ObjectId(id_persona)
		_id_sistema = self.to_ObjectId(id_sistema)
		self.usuarios.asociar_persona(_id, _id_persona, _id_sistema)
		return ""

	def cascada_rol(self, id_rol):
		self.usuarios.cascada_rol(id_rol)
		return ""