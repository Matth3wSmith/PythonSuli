#Szerző: Kovács Máté
#Dátum: 2023.12.12
#10.B

print("Gyártó: Kovács Máté, 2023.12.12")
print("Járda betonozása")
hossz=int(input("Add meg a járda hossszát méterben!"))
szelesseg=int(input("Add meg a járda szélességét méterben!"))
melyseg=0.1
beton=hossz*szelesseg*melyseg
print("Ennyi köbméter betonra van szükség a "+str(hossz)+" méter hosszú és "+str(szelesseg)+" méter széles járda lebetonozására: "+str(beton)+" m3")