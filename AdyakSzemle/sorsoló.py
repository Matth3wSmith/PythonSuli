import random
import math

class Tanulo():
	tanulok=[]

	def __init__(self, nev, cikkSzam):
		self.nev=nev
		self.cikkSzam=cikkSzam
		self.tanulok.append(self)
		 
	def sorsol():
		sorsolt=[]
		for a in range(2):
			sorsolt.append(random.choice(nevek))
		print(sorsolt)

class RegiTanulo():
	regiTanulok=[]
	def __init__(self,nev,cikkSzam):
		self.nev=nev
		self.cikkSzam=cikkSzam
		self.regiTanulok.append(self)
class UjTanulo():
	ujTanulok=[]
	def	__init__(self, nev, cikkSzam):
		self.nev=nev
		self.cikkSzam=cikkSzam
		self.ujTanulok.append(self)

#Neveket tartalmazo txt beolvasása és mentése
f=open("ember.txt","r",encoding="utf-8")
nevek = []
for elem in f:
	nevek.append(elem.strip().split(":"))
f.close()

for nev in nevek:
	Tanulo(nev[0],nev[1])

#Régi nevek beolvasása
f=open("sorsolt.txt","r",encoding="utf-8")

regiNevek=[]
for elem in f:
	regiNevek.append(elem.strip().split(":"))

f.close()

hetSzamlalo=0
#print("Régi nevek ",regiNevek)
for regiNev in range(len(regiNevek)):
	if regiNev < 2:
		#print(regiNevek[regiNev])
		RegiTanulo(regiNevek[regiNev][0],int(regiNevek[regiNev][1]))
	else:
		#print(regiNevek[regiNev])
		hetSzamlalo=int(regiNevek[regiNev][0])
print("Régi soroltak ",RegiTanulo.regiTanulok[0].nev,RegiTanulo.regiTanulok[1].nev)

#Új sorsolása és mentése
sorsoltak=[]
for a in range(2):
	egySorsolt=random.choice(nevek)
	sorsoltak.append(egySorsolt)
	if egySorsolt==sorsoltak[a]:
		sorsoltak[a]=random.choice(nevek)

print(sorsoltak)

for sorsolt in sorsoltak:
	UjTanulo(sorsolt[0],int(sorsolt[1]))

#Hányszor lehetnek
egyTag=math.ceil(104/len(nevek))

print(Tanulo.tanulok)
#Ellenzőrzés hogy előző héten volt-e és hogy hányszor volt összesen
regi0=RegiTanulo.regiTanulok[0].nev
regi1=RegiTanulo.regiTanulok[1].nev
uj0=UjTanulo.ujTanulok[0].nev
uj1=UjTanulo.ujTanulok[1].nev
if (regi0==(uj0 or uj1)) or (regi1==(uj0 or uj1)):
	pass

"""

#Új nevek sorsolása
sorsolt=[]
for a in range(2):
	sorsolt.append(random.choice(nevek))

print(sorsolt)

#Régi nevek beolvasása
f=open("sorsolt.txt","r",encoding="utf-8")

het=[]
for elem in f:
	het.append(elem.strip().split(":"))

f.close()

for nev in het:
	nev[-1]=int(nev[-1])

#Hányszor voltak
egyTag=math.ceil(104/len(nevek))

print("Eredeti új",sorsolt)
print("Eredeti régi",het)

#Ellenzőrzés hogy előző héten volt-e és hogy hányszor volt összesen
for ujNevIndex in range(len(sorsolt)):
	for regiNev in het:
		while sorsolt[ujNevIndex]==regiNev or sorsolt[ujNevIndex][1]==egyTag or sorsolt[0]==het[0] or sorsolt[0]==het[1] or sorsolt[1]==het[0] or sorsolt[0]==sorsolt[1]:
			print(sorsolt[0][0])
			print("Ezzel a névvel végez műveletet:", sorsolt[ujNevIndex])
			while sorsolt[ujNevIndex]==regiNev:
				sorsolt[ujNevIndex]=random.choice(nevek)
				print("Egyezik a régi hetivel, az új amit sorsolt:",sorsolt[ujNevIndex])
			while int(sorsolt[ujNevIndex][1])>=egyTag:
				uj=random.choice(nevek)
				sorsolt[ujNevIndex]=uj
				print("Már elég cikket írt, az új amit sorsolt:",sorsolt[ujNevIndex])
			while sorsolt[0]==sorsolt[1]:
				sorsolt[1]=random.choice(nevek)
print("változtatott új",sorsolt)
print("Eredeti régi",het)

#Új sorsoltak beírása az ember.txtbe
f=open("ember.txt","w",encoding="utf-8")
for i in range(len(sorsolt)):
	index=nevek.index(sorsolt[i])
	sorsolt[i][1]+=1
for nevSor in nevek:
	f.write(nevSor[0]+":"+str(nevSor[1])+"\n")
f.close()

#Új sorsolt beírása sorsolt.txtbe
f=open("sorsolt.txt","w",encoding="utf-8")

for i in range(len(sorsolt)):
	f.write(sorsolt[i][0]+":"+str(sorsolt[i][1])+"\n")


het[2]=het[2][0]+1

#Ha vége az évnek nullázzon mindent
if het[2]==51:
	het[2]=0
	f2=open("ember.txt","w",encoding="utf-8")
	for nevSor in nevek:
		nevSor[1]=0
		f2.write(nevSor[0]+":"+str(nevSor[1])+"\n")
	f2.close()

f.write(str(het[2]))
"""

f.close()