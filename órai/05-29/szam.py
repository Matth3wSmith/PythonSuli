#Számok bekérése 0 végjelig
#Összegzés külön-külön (pozitiv negativ szamok osszeadasa)
#Melyik van távolabb a nullától
#Első feleében (nagyobb darab), melyik számból volt több (+ v. -)
import math

szam=input("Adj meg potív vagy negatív számokat 0 végjelig: ")
szamok=[]
while szam!="0":
    szamok.append(int(szam))
    szam=input("Adj meg potív vagy negatív számokat 0 végjelig: ")

negativok=[]
pozitivok=[]
for szam in szamok:
    if szam>0:
        pozitivok.append(szam)
    else:
        negativok.append(szam)

pozitivOssz=sum(pozitivok)
negativOssz=sum(negativok)

print("\nA poztív számok összege: {}\nA negatív számok összege: {}".format(pozitivOssz,negativOssz))
if pozitivOssz>abs(negativOssz):
    print("\nA pozitív számok összege van távolabb a nullától")
else:
    print("\nA negatív számok összege van távolabb a nullától")

elsoFelTobb=[0,0]
for szam in szamok[:math.ceil(len(szamok)/2)]:
    if szam>0:
        elsoFelTobb[0]+=1
    else:
        elsoFelTobb[1]+=1

if elsoFelTobb[0]>elsoFelTobb[1]:
    print("\nA lista első felében több negatív szám van.")
else:
    print("\nA lista első felében több negatív szám van.")

#pozitiv negativ osszeszorzása, összegük kiírása, max,min
szorzasok=[]
for pozitiv in pozitivok:
    for negativ in negativok:
        szorzasok.append(pozitiv*negativ)

print("\nAz egy negatív és egy poztív számok párosával való összeszorzásának összege: {}".format(sum(szorzasok)))
print("A legnagyobb szorás: {}\nA legkisebb szorzás: {}".format(max(szorzasok),min(szorzasok)))
