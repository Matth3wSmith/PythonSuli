import random
import math

def veletlen(mettol,meddig,lepes=1):
	darab = math.ceil((meddig-mettol)/lepes)
	eltolas = mettol

	szam = math.floor(random.random()*darab)*lepes+eltolas
	return szam

print(veletlen(10,100))

#100 veletelen 1-20
szamok=[]
for i in range(100):
	szamok.append(veletlen(1,20))

print(szamok)

#


lista=[[veletlen(160,200) for a in range(veletlen(10,21))] for i in range(veletlen(10,21))]

[print(i,":",elem) for i,elem in enumerate(lista)]