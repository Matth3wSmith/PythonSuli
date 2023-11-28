#Nyári nap hőmérséklete, 5 különböző városban, óránként, + napszak kiírása
import random
import math

def veletlen(mettol,meddig,lepes=1):
	darab = math.ceil((meddig-mettol)/lepes)
	eltolas = mettol

	szam = math.floor(random.random()*darab)*lepes+eltolas
	return szam

nap=[]

for a in range(5):
	belso=[]
	for i in range(1,25):
		if i<=8:
			belso.append(veletlen(15,23))
		if 8<i<19:
			if 11<=i<=14:
				belso.append(veletlen(29,33))
			else:
				belso.append(veletlen(23,29))
		if i>=19:
			belso.append(veletlen(23,17))
	nap.append(belso)

print("Budapest:",nap[0])
print("Szombathely",nap[1])
print("Tata",nap[2])
print("Szeged",nap[3])
print("Székesfehérvár",nap[4])