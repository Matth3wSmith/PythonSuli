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
print("\n3. feladat: {:.2f}%".format(legeloSzazalek))

#4. feladat
eszakiSzel=0
for i,sor in enumerate(terulet):
	if "L" in sor[0]:
		eszakiSzel+=i*100
		break
print("4. feladat: {}m".format(eszakiSzel))


