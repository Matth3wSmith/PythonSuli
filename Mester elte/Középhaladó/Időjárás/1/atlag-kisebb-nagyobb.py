import random

f=open("be2.txt")

homerseklet=[]
elsoSor=f.readline().strip().split()
telepulesek=elsoSor[0]
napok=elsoSor[1]
for sor in f:
    vag=sor.strip().split()
    for elemI in range(len(vag)):
        vag[elemI]=int(vag[elemI])
    homerseklet.append(vag)
f.close()

kiementT=0
kimenetTelepules=[]
for egyTelepules in homerseklet:
    atlag=0
    for fok in egyTelepules:
        atlag+=fok
    atlag=atlag/len(egyTelepules)
    minKulonbseg=abs(min(egyTelepules)-atlag)
    maxKulonbseg=abs(max(egyTelepules)-atlag)
    if maxKulonbseg>minKulonbseg:
        kiementT+=1
        kimenetTelepules.append(homerseklet.index(egyTelepules)+1)

#print(homerseklet)
print(kiementT,kimenetTelepules)