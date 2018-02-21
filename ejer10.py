#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
#Introducir un directorio y una letra , enumerar archivos con dicha letras.

directorio=raw_input('Introduce el directorio a analizar:')

if not os.access(directorio,0):
	print "EL directorio no existe"
	exit()

letra=raw_input('Introduce la letra:')

ficheros=os.listdir(directorio)

for fichero in ficheros:
	if fichero.count(letra)>0:
		print fichero

