#!/usr/bin/env pyton
# -*- coding: utf-8 -*-

#Calcular edad
edad=input("Introduce tu año de nacimiento:")
edad=2018-edad
print 'Tu edad es:' +str(edad)
if edad >3 and edad <18:
	print 'Jovencito'
elif edad >=18 and edad <=30:
	print 'Joven'
elif edad >30 and edad <45:
	print 'Maduro'
else:
	print 'Eres un viejuno'


