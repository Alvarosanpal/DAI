#!/usr/bin/env python
import random
intentos=10
encontrado=0
num=random.randint(1,100)
while intentos>0 and encontrado==0:
	numero=input("Introduce un numero del 1 al 100")
	if numero==num:
		print "Enhorabuena lo has adivinado!!"
		encontrado=1
	elif numero<num:
		print "El numero es mayor" 
	else:
		print "El numero es menor"
	intentos=intentos-1	
