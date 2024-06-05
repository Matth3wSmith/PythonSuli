from sys import stdin, stdout,argv
import time
import numpy as np

def mainPepa():
	#print(argv[1])

	adatok=[]
	adatKell=[]
	f=open(argv[1])
	
	napDb=list(map(int, f.readline().split()))[1]
	for sor in f:
		#print(sor)
		if len(sor.strip())>0:
			adatok.append(list(map(int, sor.split())))
			atlag=sum(adatok[-1])/napDb
			if(max(adatok[-1])-atlag>atlag-min(adatok[-1])):
				adatKell.append(len(adatok))

	f.close()

	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))

	#print(adatKell)
	#n = int(stdin.readline())
	#szamok = list(map(int, stdin.readline().split()))
	#print(szamok)
	#stdout.write(str(osszeg) + '\n' + str(szorzat) + '\n')

#v2
def mainMate2():
	#print(argv[1])
	adatok=[]
	adatKell=[]
	adatHossz=0
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
				adatHossz+=1
				adatok.append(list(map(int, sor.split())))
				atlag=sum(adatok[-1])/napDb
				if(max(adatok[-1])-atlag>atlag-min(adatok[-1])):
					adatKell.append(str(adatHossz))
		f.close()
		

	stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))

#felesleges tárolás kigyomlálva
def mainMate3():
	#print(argv[1])
	adatok=[]
	adatKell=[]
	adatHossz=0
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
			adatHossz+=1
			sor=list(map(int, sor.split()))
			atlag=sum(sor)/napDb
			if(max(sor)-atlag>atlag-min(sor)):
				adatKell.append(adatHossz)
		f.close()
		

	#stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))

#felesleges tárolás kigyomlálva
def mainMate3_1():
	#print(argv[1])
	adatok=[]
	adatKell=[]
	adatHossz=0
	szoveg=""
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
			adatHossz+=1
			sor=list(map(int, sor.split()))
			atlag=sum(sor)/napDb
			if(max(sor)-atlag>atlag-min(sor)):
				adatKell.append(adatHossz)
				szoveg+=str(adatHossz)+" "
		f.close()
		

	#stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))
	#stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))
	stdout.write(szoveg.strip())

#szélsőérték kereső algoritmussal
def mainMate4():
	#print(argv[1])
	adatok=[]
	adatKell=[]
	adatHossz=0
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
			adatHossz+=1
			sor=list(map(int, sor.split()))
			#atlag=sum(sor)/napDb

			biggest = sor[0] 
			smallest = sor[0] 
			osszeg=0

			for index,item in enumerate(sor,start=1):       
				if item > biggest: 
					biggest = item 
				if item < smallest: 
					smallest = item 
				osszeg+=item

			atlag=osszeg/napDb
			if(max(sor)-atlag>atlag-min(sor)):
				adatKell.append(adatHossz)
		f.close()
		

	#stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))

#numpy
def mainMate5():
	adatok=[]
	adatKell=[]
	adatHossz=0
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			adatHossz+=1

			#sor = np.array(list(map(int, sor.split())))
			sor = np.array(sor.split())
			applyall = np.vectorize(int)
			sor = applyall(sor)

			atlag=np.sum(sor)/napDb
			if(np.max(sor)-atlag>atlag-np.min(sor)):
				adatKell.append(adatHossz)
		f.close()
		

	#stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))


tesztFutas=100


#ts = time.time()
#for i in range(tesztFutas):
#	mainPepa()
#tsPepa=time.time()-ts
"""
ts = time.time()
#for i in range(100):
#	mainMate()
tsMate=time.time()-ts

ts = time.time()
for i in range(tesztFutas):
	mainMate2()
tsMate2=time.time()-ts

ts = time.time()
for i in range(tesztFutas):
	mainMate3()
tsMate3=time.time()-ts

ts = time.time()
for i in range(tesztFutas):
	mainMate3_1()
tsMate3_1=time.time()-ts

ts = time.time()
for i in range(tesztFutas):
	mainMate4()
tsMate4=time.time()-ts
"""
ts = time.time()
for i in range(tesztFutas):
	mainMate5()
tsMate5=time.time()-ts

print("\n"*3)
#print("mainPepa: ",tsPepa)
#print("mainMate: ",tsMate)
#print("mainMate2: ",tsMate2)
#print("mainMate3: ",tsMate3)
#print("mainMate3_1: ",tsMate3_1)
#print("mainMate4: ",tsMate4)

print("mainMate5: ",tsMate5)
