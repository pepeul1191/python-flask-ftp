# app/controllers/rol.py

from app.config.controller import Controller

class Rol(Controller):
   # Atributos: _id, nombre, llave
   	def __init__(self):
		self.roles = self.load_model('roles')

	def listar (self):
		lista = self.roles.listar()
		return self.bson_dumps(lista)

	def crear(self):
		temp_id = self.params["temp_id"]
		rol = self.unquote(self.params["rol"])
		
		object_id = self.roles.crear(rol)
		rpta = {'temporal' : temp_id, 'nuevo_id' : str(object_id)}
		return self.json_dumps(rpta)

	def editar(self):
		_id = self.to_ObjectId(self.params["_id"])
		rol = self.unquote(self.params["rol"])
		
		self.roles.editar( _id, rol)
		self.roles.editar_roles_usuario(self.params["_id"])
		return ""

	def eliminar(self, id):
		_id = self.to_ObjectId(id)
		self.roles.eliminar(_id)
		return ""

	def listar_permisos(self, id_rol):
		lista = self.roles.listar_permisos(id_rol)
		return self.bson_dumps(lista) 

	def asociar_permiso(self, id_rol, id_permiso):
		self.roles.asociar_permiso(id_rol, id_permiso)
		return ""

	def desasociar_permiso(self, id_rol, id_permiso):
		self.roles.desasociar_permiso(id_rol, id_permiso)
		return ""