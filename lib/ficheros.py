# -*- coding: utf-8 -*-

import os
import sys

#Comprobar si existe un directorio y si existe crearlo.
def crea_dir(directorio):
	if os.access(directorio,0):
		return 1

	else: 
		os.mkdir(directorio)
		return 0


#Indicar directorio ,comprobar si son directorios o archivos y comprobar su tamaño.
def lista(directorio):
	if not  os.access(directorio,0):
		print 'Directorio inexistente'
		exit()
	lista=os.listdir(directorio)
	for fichero in lista:
		f1=directorio+'/'+fichero
		if os.path.isfile(f1):
			print fichero + '--->'+str(os.path.getsize(f1))

	
def lista_tam(directorio,tam):
	if not os.access(directorio,0):
		print 'Directorio inexistente'
		exit()
	if tam[-1].upper() not in ('K','M','G'):
		print 'Solo permite K,M,G,'
		exit()
	if tam[-1]=='K':
		t=t*1024
	if tam[-1]=='M':
		t=t*1024*1024
	else:
		t=t*1024*1024*1024
	lista=os.listdir(directorio)
	print t
	for fichero in lista:
		f1=directorio+'/'+fichero
		if os.path.isfile(f1):
			if os.path.getsize(f1)>t:
				print fichero + '--->' +str(os.path.getsize(f1))
	

#Unico fichero y que lo pinte.

def cat(fichero):
	if not os.access(fichero,0):
		print 'FIchero no existe'
		exit()
	if not os.path.isfile(fichero):
		print "No es un fichero"
		exit()

	f=open(fichero,'r')	
	contenido=f.read()
	print contenido
	f.close()

#UN grep, indicarle un fichero y un texto y que filtre por el.


def grep(fichero):

	if not os.access(fichero,0):
                print 'FIchero no existe'
                exit()
        if not os.path.isfile(fichero):
                print "No es un fichero"
                exit()
	f=open(fichero,'r')
	while True:
		linea=f.readline()
		if not linea:
			break
		if linea.count(texto)>0:
			print linea[:-1]
	
def cp(fichero,destino):
	if not os.access(fichero,0):
                print 'FIchero no existe'
                exit()
        if not os.path.isfile(fichero):
                print "No es un fichero"
                exit()
	if os.access(destino,0):
                print 'FIchero ya existe'
                exit()
        if os.path.isfile(destino):
                print "Es un archivo"
                exit()
	f1=open(fichero,'r')
	f2=open(destino,'w')
	lineas=f1.readlines()
	for linea in lineas:
		f2.write(linea)
	f1.close()
	f2.close()


def ftp
	from ftplib import ftp
	ftp=FTP()
	ftp.connect('192.168.1.54',23, -999)
	ftp.login('oracle','oracle')
#

		


