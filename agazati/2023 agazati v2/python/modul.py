import math

def szam():
    osszeg=0
    for i in range(3):
        osszeg+=int(input("{}. szám: ".format(i+1)))
    return osszeg

def keplet(x):
    return (math.sqrt(42*x**3+12)+25*x)/(2*(13-26))*4*(x/6)
