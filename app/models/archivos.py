#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/models/extensiones.py

from app.config.model import Model
import pprint

class Archivos(Model):
   # Atributos : id, nombre, descripcion, nombre_genarado, extension_id
	def crear(self):
		'''
		INSERT INTO archivos (nombre, descripcion, nombre_generado, extension_id) VALUES 
		( 
		  'nombre', 'descripcion...adfadfljakldfasdf', 'alkdjfkladsjfkladsjf.png', 
		  (SELECT id FROM extensiones WHERE extension = "jpg")
		) 
		'''