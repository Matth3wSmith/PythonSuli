#Készítő: Kovács Máté
import math
print("Gyártó: Kovács Máté")
print("Add meg a telek 'a' és 'b' oldalának hosszát!")

print(" "*14+"-"*25)
[[print(" "*14+"|"+" "*23+"|")] for i in range(3)]
print("-"*15+" "*9+"-"*15)
[[print("|"+" "*23+"|  b") if i==1 else print("|"+" "*23+"|")] for i in range(3)]
print("-"*25)
print(" "*12+"a"+" "*12)

a = int(input("Az 'a' oldal hossza (m):"))
b = int(input("A 'b' oldal hossza (m):"))
terulet = 2*a*b
print("A telek területe négyzetméterben: "+str(terulet))
