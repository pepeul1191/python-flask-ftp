# app/controllers/permiso.py

from app.config.controller import Controller

class Permiso(Controller):
   # Atributos: _id, nombre, llave
   	def __init__(self):
		self.permisos = self.load_model('permisos')

	def listar (self):
		lista = self.permisos.listar()
		return self.bson_dumps(lista)

	def crear(self):
		temp_id = self.params["temp_id"]
		nombre = self.params["nombre"]
		llave = self.params["llave"]

		object_id = self.permisos.crear(nombre, llave)
		rpta = {'temporal' : temp_id, 'nuevo_id' : str(object_id)}
		return self.json_dumps(rpta)

	def editar(self):
		_id = self.params["_id"]
		nombre = self.params["nombre"]
		llave = self.params["llave"]
		
		_id = self.to_ObjectId(_id)
		self.permisos.editar( _id, nombre, llave)
		return ""

	def eliminar(self, _id):
		_id = self.to_ObjectId(_id)
		self.permisos.eliminar(_id)
		return ""