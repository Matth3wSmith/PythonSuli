from radioClassHome import *


f=open("veetel.txt","r")
adatok=[]
for sor in f:
	adatok.append(sor.strip())


f.close()

#Elmentés classba
for i in range(0,len(adatok),2):
	egyAdat=adatok[i].split()
	kettoAdat=adatok[i+1]
	Uzenet(egyAdat[0],egyAdat[1],kettoAdat)

#2. feladat
elsoU=Uzenet.uzenetek[0].sorszam
utolsoU=Uzenet.uzenetek[-1].sorszam

#3. feladat
farkasok=[]
for adat in Uzenet.uzenetek:
	if adat.farkas()!=False:
		farkasok.append(adat.farkas())
print(farkasok)

#4. feladat
for nap in range(max(Uzenet.napok)):
	Uzenet.napiFelv[nap+1]=0

for uzenet in Uzenet.uzenetek:
	uzenet.felvetelStat()

#5. feladat
helyreallSzoveg=[]
f=open("adaas.txt","w")
for nap in Uzenet.napok:
	napiSzoveg=""
	osszSzoveg=[]
	for uzenet in Uzenet.uzenetek:
		if int(uzenet.nap)==nap:
			osszSzoveg.append(uzenet.szoveg)
	for karakter in range(90):
		szamlalo=0
		for szoveg in osszSzoveg:
			if szoveg[karakter]!="#" and szamlalo!=1:
				napiSzoveg+=szoveg[karakter]
				szamlalo=1
	f.write(str(nap)+"\n")
	f.write(napiSzoveg+"\n")

f.close()
	
print("2. feladat:")
print("Az első üzenet rögzítője: {}".format(elsoU))
print("Az utolsó üzenet rögzítője: {}".format(utolsoU))

print("3. feladat:")
print("{nap}. nap {amator}. rádióamatőr".format(nap=farkasok[0][0],amator=farkasok[0][1]))
print("{nap}. nap {amator}. rádióamatőr".format(nap=farkasok[1][0],amator=farkasok[1][1]))

print("4. feladat")
for i in range(len(Uzenet.napiFelv)):
	print("{nap}. nap: {amator} rádióamatőr".format(nap=i+1,amator=Uzenet.napiFelv[i+1]))

#6. feladat
def szame(szo):
	valasz=True
	for i in range(0,len(szo)):
		if szo[i]<"0" or szo[i]>"9":
			valasz=False
	return valasz

#7. feladat
nap=input("Adja meg a nap sorszámát! ")
amator=input("Adja meg a rádióamatőr sorszámát! ")
egyedek=0
for uzenet in Uzenet.uzenetek:
	if uzenet.nap==nap and uzenet.sorszam==amator:
		elso=szame(uzenet.szoveg[0])
		masodik=szame(uzenet.szoveg[1])
		harmadik=szame(uzenet.szoveg[2])
		negyedik=szame(uzenet.szoveg[3])
		otodik=szame(uzenet.szoveg[4])
		#print(uzenet.nap,uzenet.sorszam)
		#print(uzenet.szoveg)
		#print(elso,masodik,harmadik,negyedik,otodik)
		#Ha két számjegyű az első kettő adat
		if elso == True and masodik == True:
			print(uzenet.szoveg[0:2])
			egyedek+=int(uzenet.szoveg[0:2])
			#Ha két számjegyű a második kettő adat
			if negyedik == True and otodik==True:
				egyedek+=int(uzenet.szoveg[3:5])
			#Ha egy számjegyű
			elif negyedik==True and otodik==False:
				if uzenet.szoveg[4]==" " or uzenet.szoveg[4]=="#":
					egyedek+=int(uzenet.szoveg[3])
		#Ha egy számjegyű
		elif elso==True and masodik==False:
			if uzenet.szoveg[1]=="/":
				egyedek+=int(uzenet.szoveg[0])
			#Ha az előző egyszámjegyű volt akkor a kövi kettő számjegyű-e
			if harmadik==True and negyedik==True:
				egyedek+=int(uzenet.szoveg[2:4])
			#Ha egy számjegyű
			elif harmadik==True and negyedik==False:
				if uzenet.szoveg[3]==" " or uzenet.szoveg[3]=="#" :
					egyedek+=int(uzenet.szoveg[2])
		
		
print("A megfigyelt egyedek száma: {}".format(egyedek))
