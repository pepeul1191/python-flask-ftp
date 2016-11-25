#!/usr/bin/env python
# -*- coding: utf-8 -*-

# index.py

import sys 
import json

from flask import Flask, request
from flask.ext.cors import CORS, cross_origin

from bson.json_util import dumps

from app.config.request import Request
from app.config.bootstrap import Bootstrap

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def index():
	return 'Error : URI vacía'

@app.route('/<path:path>', methods=['GET', 'POST'])
@cross_origin('*')
def catch_all(path):
	rpta = None
	r = Request(path, request.args)

	if r.rpta == None:
		if r.metodo != "":
			b = Bootstrap(r)
			rpta = b.rpta
			return rpta
		else:
			return "Index: No hay metodo"
	else:
		return"Index: No hay metodo"
	

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5001)