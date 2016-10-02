#!/usr/bin/env python
import random
from timeit import timeit
def burbuja (M):
	H=M[:]
	tam=len(M)-1
	aux=0
	while tam>0:
		for j in range(tam):
			if H[j]>H[j+1]:
				aux=H[j]
				H[j]=H[j+1]
				H[j+1]=aux
		tam=tam-1
	return H
		
M=[1,2,3,4,5,6,7,8,9,10]
for i in range(10): M[i]=random.randint(1,100)
H=burbuja(M)
print M
print "Metodo Burbuja ",H
M.sort()
print "Metodo sort ",M



