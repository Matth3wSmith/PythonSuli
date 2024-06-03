from feladat2Modul import *

def haromszogBekeres():
    for k in range(3):
        print("{}. adatsor".format(k+1))
        haromszogek.append(haromszog())
    for oldalak in haromszogek:
        print("\ta={} b={} c={}".format(oldalak[0],oldalak[1],oldalak[2]))

def haromszogLehet(haromszogek):
    for i in range(len(haromszogek)):
        legnagyobbOldal=max(haromszogek[i])
        haromszogek[i].remove(legnagyobbOldal)
        if legnagyobbOldal>(haromszogek[i][0]+haromszogek[i][1]):
            print("{}. számsor nem lehet háromszög".format(i+1))
        else:
            print("{}. számsor lehet háromszög".format(i+1))

haromszogek=[]

haromszogBekeres()
haromszogLehet(haromszogek)
