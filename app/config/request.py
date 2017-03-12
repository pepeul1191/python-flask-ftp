# app/config/request.py

class Request:
   # Atributos: controlador, metodo, argumento
	def __init__(self, path, params, request):
		self.rpta = None
		self.request = request

		if len(params) == 0:
			self.params = False
		else:
			self.params = params
		
		array_url = path.split('/')
		self.controlador = array_url.pop(0)

		try:
			self.metodo = array_url.pop(0)	 
		except IndexError:
			self.rpta = "IndexError : No hay metodo"

		try:
			self.argumento = array_url
		except IndexError:
			self.argumento  = ""

	def to_string (self):
		print "controlador : " + self.controlador + ", metodo : " + self.metodo + " , argumento(s) : " + self.argumento 