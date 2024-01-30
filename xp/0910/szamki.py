#Gyártó: Kovács Máté

def szamki():
	szam=input("Adj meg egy egész számot!")
	hossz=len(szam)
	szamlista=[]
	ezredes=[]
	keszSzam=""
	if hossz>4:
		for egySzam in szam:
			szamlista.append(egySzam)
		#print(szamlista)
		end=hossz-(hossz%3)
		#print("end:"+str(end))
		if hossz%3==1:
			ezredes.append(list(szamlista[0]))
			for i in range(1,end,3):
				ezredes.append(szamlista[i:i+3])
		if hossz%3==2:
			ezredes.append(list(szamlista[0]))
			for i in range(2,end,3):
				ezredes.append(szamlista[i:i+3])
		if hossz%3==0:
			for i in range(0,end,3):
				ezredes.append(szamlista[i:i+3])
		#print(ezredes)
		k=0
		for elem in ezredes:
			for szam in elem:
				keszSzam+=szam
			k+=1
			if len(ezredes)==k:
				break
			keszSzam+="."
	else:
		keszSzam=szam
	return keszSzam


print("A megadott szám ezres tagolással: "+str(szamki()))

