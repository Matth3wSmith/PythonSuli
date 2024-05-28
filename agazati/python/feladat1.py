print("1. feladat")
szo=input("Kérek egy szót: ")
szavak=[]
while szo!="":
    szavak.append(szo)
    szo=input("Kérek egy szót: ")

print("A szavak száma: {}".format(len(szavak)))
print("A lista első fele: {}".format("_".join(szavak[:len(szavak)//2])))