#!/usr/bin/env python
# -*- coding: utf-8 -*-

# app/libs/cipher.py

import base64

class Cipher:
   # Atributos: NA
	def encrypt(self, por_encritar):
		return base64.b64encode(por_encritar)

	def decrypt(self, encriptado):
		return base64.b64decode(encriptado)