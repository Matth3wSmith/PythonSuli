#Gyártó: Kovács Máté

#Termések elmentése classokba
class Termesek():
	termesLista=[]
	
	def __init__(self,nev,dulo,termes,datum):
		self.termesLista.append(self)
		self.nev=nev
		self.dulo=dulo
		self.termes=termes
		self.datum=datum

def repcek():
	mennyiseg = 0
	mazsa = 0
	for termesClass in Termesek.termesLista:
		if termesClass.nev=="repce":
			mennyiseg+=1
			mazsa+=termesClass.termes
	return mennyiseg, mazsa

#Termések beolvasása
f=open("termes.txt","r",encoding="utf-8")

adatok=[]
for sor in f:
	adat=sor.strip().split(":")
	del adat[-1]
	adatok.append(adat)

f.close()
del adatok[0]
#print(adatok)

#Példányosítás
for termes in adatok:
	Termesek(termes[1],termes[2],int(termes[3]),termes[4])

mennyiseg,mazsa=repcek()
print("Ennyi dülőben volt repce: "+str(mennyiseg)+", és ennyi mázsa repce termett: "+str(mazsa))