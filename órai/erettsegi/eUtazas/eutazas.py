class Utas:
	def __init__(self,megallo,felszallas,azonosito,tipus,erveny) -> None:
		self.megallo=int(megallo)
		self.felszallas=felszallas
		self.azonosito=int(azonosito)
		self.tipus=tipus
		self.ervenyesseg=int(erveny)

#1.feladat
utasok=[]
f=open("utasadat.txt","r")
for sor in f:
	vag=sor.strip().split()
	utasok.append(Utas(vag[0],vag[1],vag[2],vag[3],vag[4]))
f.close()

#2. feladat
print("2. feladat")
print("A buszra {} utas akart felszállni.".format(len(utasok)))

#3. feladat
leszallitas=0
ervenyesek=[]
for utas in utasok:
	felszallDatum=int(utas.felszallas.split("-")[0])
	if (felszallDatum>utas.ervenyesseg and len(str(utas.ervenyesseg))==8) or utas.ervenyesseg==0:
		leszallitas+=1
	else:
		ervenyesek.append(utas)
print("3. feladat")
print("A buszra {} utas nem szálhatott fel.".format(leszallitas))

#4. feladat
megallokDict={}
for utas in utasok:
	if utas.megallo not in megallokDict.keys():
		megallokDict[utas.megallo]=1
	else:
		megallokDict[utas.megallo]+=1

megalloFo=max(megallokDict.values())
megallo=list(megallokDict.keys())[list(megallokDict.values()).index(megalloFo)]
print("4. feladat")
print("A legtöbb utas ({} fő) a {}. megállóban próbált felszáálni.".format(megalloFo,megallo))

#5. feladat
jegyTipusDict={}
for utas in ervenyesek:
	if utas.tipus not in jegyTipusDict.keys():
		jegyTipusDict[utas.tipus]=1
	else:
		jegyTipusDict[utas.tipus]+=1
print(jegyTipusDict)

kedvezmenyes=0
ingyenes=0
for tipus in jegyTipusDict.keys():
	#kedvezményes
	print(tipus)
	if tipus=="TAB" or tipus=="NYB":
		kedvezmenyes+=jegyTipusDict[tipus]
	#ingyenes
	elif tipus=="NYP" or tipus=="RVS" or tipus=="GYK":
		ingyenes+=jegyTipusDict[tipus]

print("5. feladat")
print("Ingyenesen utazók száma: {} fő".format(ingyenes))
print("A kedvezményesen utazók száma: {} fő".format(kedvezmenyes))

#6. feladat
"""Függvény napokszama(e1:egész, h1:egész, n1: egész, e2:egész, h2: egész, n2: egész): egész
	h1 = (h1 + 9) MOD 12
	e1 = e1 - h1 DIV 10
	d1= 365*e1 + e1 DIV 4 - e1 DIV 100 + e1 DIV 400 + (h1*306 + 5) DIV 10 + n1 - 1
	h2 = (h2 + 9) MOD 12
	e2 = e2 - h2 DIV 10
	d2= 365*e2 + e2 DIV 4 - e2 DIV 100 + e2 DIV 400 + (h2*306 + 5) DIV 10 + n2 - 1
	napokszama:= d2-d1"""

def napokszama(e1,h1,n1,e2,h2,n2):
	h1= (h1 + 9)%12
	e1 = e1 - h1 // 10
	d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 // 10
	d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
	napokszama = d2-d1
	return napokszama

#7. feladat
f=open("figyelmeztetes.txt","w")
for utas in ervenyesek:
	if len(str(utas.ervenyesseg))==8:
		datumFelszall=utas.felszallas.split("-")[0]
		datumErveny=str(utas.ervenyesseg)
		napokVissza=napokszama(int(datumFelszall[0:4]),int(datumFelszall[4:6]),int(datumFelszall[6:8]),int(datumErveny[0:4]),int(datumErveny[4:6]),int(datumErveny[6:8]))
		if napokVissza<=3:
			datumForma="-".join([datumErveny[0:4],datumErveny[4:6],datumErveny[6:8]])
			f.write("{} {}\n".format(utas.azonosito,datumForma))
f.close()