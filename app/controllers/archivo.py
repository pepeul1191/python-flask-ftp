#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/archivo.py

from app.config.controller import Controller
import pprint
import os
from ftplib import FTP_TLS

class Archivo(Controller):
   # Atributos : id, nombre, descripcion, nombre_genarado, extension_id
	def recibir(self):
		file = self.request.files['file']
		nombre = self.params['nombre']
		descripcion = self.params['descripcion']
		extension = file.filename.split('.')
		extension = extension[len(extension) -1]
		archivo = self.generar_nombre_no_repetido(extension)

		file.save(os.path.join('/tmp/', archivo))
		ftps = FTP_TLS()
		ftps.connect('192.168.1.26')
		ftps.sendcmd('USER ftp_user')
		ftps.sendcmd('PASS ftp_user')
		ftps.storbinary("STOR " + archivo, open('/tmp/' + archivo, 'rb'))
		id_generado = self.registrar_en_db(nombre, descripcion, archivo, extension)
		#ftps.retrlines('LIST')
		ftps.quit()
		
		return id_generado

	def generar_nombre_no_repetido(self, extension):
		ftps = FTP_TLS()
		ftps.connect('192.168.1.26')
		ftps.sendcmd('USER ftp_user')
		ftps.sendcmd('PASS ftp_user')
		
		existe = False
		nombre_generado = ''
		while (existe == False):
			files = []
			nombre_generado = self.random_word() + '.' + extension
			#print nombre_generado
			try:
			    files = ftps.nlst()
			    if nombre_generado not in files:
			    	existe = True
			except ftplib.error_perm, resp:
			    if str(resp) == "550 No files found":
			        print "No files in this directory"
			    else:
			        raise
		ftps.quit()

		return nombre_generado

	def registrar_en_db(self, nombre, descripcion, nombre_generado, extension):
		archivos = self.load_model('archivos')
		archivos.crear(nombre, descripcion, nombre_generado, extension)
		return archivos.last_id