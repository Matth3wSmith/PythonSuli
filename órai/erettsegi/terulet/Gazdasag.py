#Gyártó: Kovács Máté

#1. feladat
f=open("terulet.txt","r",encoding="utf-8-sig")
terulet=[]
for sor in f:
	terulet.append(sor.split())

f.close()
print(terulet)

#2. feladat
szelesseg=len(terulet[0][0])*100
hosszusag=len(terulet)*100
teruletha=szelesseg*hosszusag/10000
print("2. feladat: {}m x {}m, területe: {}ha".format(hosszusag,szelesseg,teruletha))

#3.feladat
legelo=0
for sor in terulet:
	for karakter in sor[0]:
		if karakter=="L":
			legelo+=1

legeloSzazalek=legelo*100/teruletha
print("3. feladat: {:.2f}%".format(legeloSzazalek))

#4. feladat
eszakiSzel=0
for i,sor in enumerate(terulet):
	if "L" in sor[0]:
		eszakiSzel+=i*100
		break
print("4. feladat: {}m".format(eszakiSzel))

#5. feladat
legeloHossz=0
for sor in terulet:
	tempHossz=0
	for karakter in sor[0]:
		if karakter=="L":
			tempHossz+=100
		else:
			if tempHossz>legeloHossz:
				legeloHossz=tempHossz
			tempHossz=0
print("5. feladat: {}m".format(legeloHossz))

#6. és 7. feladat
for i,sor in enumerate(terulet):
	for karakter in sor[0]:
		if karakter=="L":
			legeloIndex=sor[0].index("L")
			#Jobbra meddig tart a legelő
			for l in range(len(sor[0])):
				if sor[0][legeloIndex+l]!="L":
					maxLegeloSzel=l
					break
			#Lefele meddig tart a legelő
			for k in range(len(terulet)):
				if terulet[i+k][0][legeloIndex]!="L":
					maxLegeloHossz=k
					break

print(maxLegeloHossz,maxLegeloSzel)
			


