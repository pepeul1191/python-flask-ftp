#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/roles.py

from app.config.model import Model

class Roles(Model):
   # Atributos: _id, nombre, llave

	def listar(self):
		return list(self.db.roles.find())

	def crear(self, rol):
		documento = {"rol" : rol, "permisos" : []}
		return self.db.roles.insert(documento)

	def editar(self,  _id, rol):
		documento = {"rol" : rol}
		self.db.roles.update( {'_id': _id }, documento)

	def eliminar(self, _id):
		self.db.roles.remove( {'_id': _id })

	def listar_permisos(self, id_rol):
		return self.db.eval("listar_permisos('" + id_rol + "')")

	def asociar_permiso(self, id_rol, id_permiso):
		self.db.eval("asociar_permiso('" + id_rol + "', '" + id_permiso + "')")

	def desasociar_permiso(self, id_rol, id_permiso):
		self.db.eval("desasociar_permiso('" + id_rol + "', '" + id_permiso + "')")

	def editar_roles_usuario(self, id):
		self.db.eval("editar_roles_usuario('" + id + ')")