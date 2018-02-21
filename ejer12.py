#!/usr/bin/env python
# -*- coding: utf-8 -*-

def saludar(saludo)
	print saludo

def iniciales(nombre,ape1,ape2):
	iniciales=nombre+[0]+'.'+ape1[0]+'.'+ape2[0]+'.' 
	return "Tus iniciales son:"+iniciales.upper()

def iniciales1(nombre,ape1,ape2):
	iniciales=nombre[0]+'.'+ape2
	for ape in apellidos:
		iniciales=iniciales+'.'+ape1[0]+'.'+ape2[0]+'.'
	return iniciales.upper()


