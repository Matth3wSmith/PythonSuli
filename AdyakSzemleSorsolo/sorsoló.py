import random
import math

def szamAtalakit(lista):
	for i in lista:
		i[1]=int(i[1])

#Neveket tartalmazo txt beolvasása és mentése
f=open("ember.txt","r",encoding="utf-8")
nevek = []
for elem in f:
	nevek.append(elem.strip().split(":"))
f.close()

szamAtalakit(nevek)

print("Összes név ",nevek)
print("*"*50)

#Régi nevek beolvasása
f=open("sorsolt.txt","r",encoding="utf-8")

regiNevek=[]
for elem in f:
	regiNevek.append(elem.strip().split(":"))

f.close()
print(regiNevek)
for i in range(len(regiNevek)):
	if i<2:
		regiNevek[i][1]=int(regiNevek[i][1])
	else:
		regiNevek[2]=int(regiNevek[2][0])

#print("Régi nevek ",regiNevek)
#print("*"*50)

hetSzamlalo=0

#Új sorsolása és mentése
sorsoltak=[]
for a in range(2):
	egySorsolt=random.choice(nevek)
	sorsoltak.append(egySorsolt)

while sorsoltak[0]==sorsoltak[1]:
	sorsoltak[1]=random.choice(nevek)
#print("Sorsolt nevek ",sorsoltak)
#print("*"*50)

#Hányszor lehet valaki
egyTag=math.ceil(104/len(nevek))

#Ellenzőrzés hogy előző héten volt-e és hogy hányszor volt összesen
for ujNev in sorsoltak:
	for regiNev in regiNevek:
		while ujNev==regiNev or ujNev[1]==egyTag:
			#print(sorsoltak)
			#print("Ezzel a névvel végez műveletet:", ujNev)
			while ujNev==regiNev:
				#print("##",ujNev)
				#print("##",sorsoltak)
				index=sorsoltak.index(ujNev)
				ujNev=random.choice(nevek)
				#print("Egyezik a régi hetivel, az új amit sorsolt:",ujNev)
				sorsoltak[index]=ujNev
			while int(ujNev[1])>=egyTag:
				#print("##",ujNev)
				#print("##",sorsoltak)
				index=sorsoltak.index(ujNev)
				ujNev=random.choice(nevek)
				sorsoltak[index]=ujNev
				#print("Már elég cikket írt, az új amit sorsolt:",ujNev)
			while sorsoltak[0]==sorsoltak[1]:
				sorsoltak[1]=random.choice(nevek)
		while sorsoltak[1]==regiNevek[0]:
			sorsoltak[1]=random.choice(nevek)
		while sorsoltak[0]==regiNevek[0]:
			sorsoltak[0]=random.choice(nevek)
#print("változtatott új",sorsoltak)
#print("Eredeti régi",regiNevek)


#Új sorsoltak beírása az ember.txtbe
f=open("ember.txt","w",encoding="utf-8")
for nev in sorsoltak:
	nev[1]+=1
for nevSor in nevek:
	f.write(nevSor[0]+":"+str(nevSor[1])+"\n")
f.close()

#Új sorsolt beírása sorsolt.txtbe
f=open("sorsolt.txt","w",encoding="utf-8")

for i in sorsoltak:
	f.write(i[0]+":"+str(i[1])+"\n")

#Hét megnövelése
regiNevek[2]+=1

#Ha vége az évnek nullázzon mindent
if regiNevek[2]==51:
	regiNevek[2]=0
	f2=open("ember.txt","w",encoding="utf-8")
	for nevSor in nevek:
		nevSor[1]=0
		f2.write(nevSor[0]+":"+str(nevSor[1])+"\n")
	f2.close()

f.write(str(regiNevek[2]))

f.close()