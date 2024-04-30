import string
import random
abc = list(string.ascii_uppercase)

class Telek:
	def __init__(self,sor) -> None:
		vag=sor.strip().split(" ")
		print(vag)
		self.oldal=int(vag[0])
		self.szelesseg=int(vag[1])
		self.szin=vag[2]
		self.hazszam=0

telkek=[]
parosParatlan=[0,-1]
f=open("kerites.txt","r")
for sor in f:
	telkek.append(Telek(sor))
	parosParatlan[telkek[-1].oldal]+=2
	telkek[-1].hazszam=parosParatlan[telkek[-1].oldal]
f.close()

#2. feladat
print("2.feladat")
print("Az eladott telkek száma: {}".format(len(telkek)))

#3. feladat
print("3. feladat")
if telkek[-1].oldal==0:
	print("A páros oldalon adták el az utolsó telket")
else:
	print("A páratlan oldalon adták el az utolsó telket")
print("Az utolsó telek házszáma: {}".format(telkek[-1].hazszam))

#4. feladat
oldalSzerint=[[],[]]
szomszedosSzin=[]
for telek in telkek:
	#oldalSzerint[telek.oldal].append(telek)
	if telek.oldal==0:
		oldalSzerint[0].append(telek)
	else:
		oldalSzerint[1].append(telek)

"""for i in range(1,len(oldalSzerint[1])):
	if oldalSzerint[1][i].szin==oldalSzerint[1][i-1].szin and oldalSzerint[1][i] not in [":","#"]:
		print("A szomszédossal egyezik a kerítés színe: {}".format(oldalSzerint[1][i-1].hazszam)
		break"""

for i,paratlanTelek in enumerate(oldalSzerint[1]):
	if i+1<len(oldalSzerint[1]) and paratlanTelek.szin==oldalSzerint[1][i+1].szin:
		if paratlanTelek.szin==":" or paratlanTelek.szin=="#":
			pass
		else:
			szomszedosSzin.append(paratlanTelek.hazszam)
				

print("4. feladat")
print("A szomszédossal egyezik a kerítés színe: {}".format(szomszedosSzin[0]))

#5. feladat
szomszedokSzine=[]
kertHazszam=int(input("Add meg az eladott telek házszámát: "))
for i,telek in enumerate(telkek):
	if telek.hazszam==kertHazszam:
		print("A kerítés színe / állapota: {}".format(telek.szin))
		if i+1<len(telkek)-1:
			szomszedokSzine.append(telkek[i+1].szin)
		if i>0:
			szomszedokSzine.append(telkek[i-1].szin)
		lehetseges=random.choice(abc)
		while lehetseges in szomszedokSzine:
			lehetseges=random.choice(abc)
		print("Egy lehetséges festési szín: {}".format(lehetseges))


#6. feladat
utcaKep=""
utcaKepHaz=""
f=open("utcakep.txt","w")
for oddHaz in oldalSzerint[1]:
	utcaKep+=oddHaz.szin*oddHaz.szelesseg
	utcaKepHaz+=str(oddHaz.hazszam)+" "*(oddHaz.szelesseg-len(str(oddHaz.hazszam)))
f.write(utcaKep+"\n")
f.write(utcaKepHaz)

f.close()