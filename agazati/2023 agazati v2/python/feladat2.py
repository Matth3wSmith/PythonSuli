from modul import *

print("1.feladat")
kepletek=[]
for i in range(szam()):
    kepletek.append(keplet(i+100))

atlag=sum(kepletek)/len(kepletek)
print("A lista átlaga: {:.2f}".format(atlag))