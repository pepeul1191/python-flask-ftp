#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/controllers/archivo.py

from app.config.controller import Controller
import pprint
import os
from ftplib import FTP_TLS

class Archivo(Controller):
   # Atributos : 
	#def __init__(self):
		#self.usuarios = self.load_model('usuarios')

	def recibir(self):
		#pprint.pprint(self.request.files['file'].__dict__)
		file = self.request.files['file']
		#buffer += open(file, 'rU').read()
		#print buffer
		archivo = self.random_word() + '.jpg'
		file.save(os.path.join('/tmp/', archivo))
		ftps = FTP_TLS()
		ftps.connect('192.168.1.26')
		ftps.sendcmd('USER ftp_user')
		ftps.sendcmd('PASS ftp_user')
		ftps.storlines("STOR " + archivo, open('/tmp/' + archivo, 'r'))
		ftps.retrlines('LIST')
		ftps.quit()
		return 'recibir???'