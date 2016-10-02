#!/usr/bin/env python
import random
def comprobarllaves(H):
	total=0
	i=0
	tam=len(H)
	if tam%2==0:
		while total>-1 and i<tam:
			if H[i]=='[':
				total=total+1
			else:
				total=total-1
			i=i+1
		if total==0:
			return True
		else :
			return False
	else:
		return False
		
tam=random.randint(1,10)
M=list()
for i in range(tam):
	M.append(random.choice("[]"))
cadena=""
for i in range (tam):
	cadena=cadena+ M[i]
print cadena
print comprobarllaves(cadena)
