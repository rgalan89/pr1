#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Pedir el nombre y apellido y poner las iniciales separada de punto.
import sys

print sys.argv[1]
print sys.argv[2]
print sys.argv[3]

if len(sys.argv) !=4:
	print"Los argumentos son Nombre y apellidos"
	exit()

iniciales= sys.argv[1][0]+ '.'+ sys.argv[2][0]+ '.' + sys.argv[3][0] 
print "Tus iniciales son" +iniciales.upper()
