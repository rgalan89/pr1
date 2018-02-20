#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#Introducir un fichero y que enumere los archivos .sh

directorio=raw_input('Introduce el fichero a analizar:')

if not os.access(directorio,0):
	print "EL directorio no existe"
	exit()

ficheros=os.listdir(directorio)

for fichero in ficheros:
	if fichero[-3:] == '.sh':
		print fichero


