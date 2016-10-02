#!/usr/bin/env python 
import math
def cribadeEratostenes(M):
	H=M[:]
	tam=int(math.sqrt(len(H)))
	if H[0]>0:
		if H[0]==1:
			H.pop(0)
	
		for i in range(tam):
			j=i+1
			while j<len(H):
				if H[j]%H[i]==0:
					H.pop(j)
				j=j+1
		return H
	return M
M=list(range(2,21))
H=cribadeEratostenes(M)
print H
