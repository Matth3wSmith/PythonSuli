from radioClassHome import *


f=open("veetel.txt","r")
adatok=[]
for sor in f:
    adatok.append(sor.strip())

print(adatok)
f.close()

for i in range(0,len(adatok),2):
    egyAdat=adatok[i].split()
    kettoAdat=adatok[i+1]
    Uzenet(egyAdat[0],egyAdat[1],kettoAdat)


elsoU=Uzenet.uzenetek[0].sorszam
utolsoU=Uzenet.uzenetek[-1].sorszam


print("2. feladat:")
print("Az első üzenet rögzítője: {}".format(elsoU))
print("Az utolsó üzenet rögzítője: {}".format(utolsoU))

