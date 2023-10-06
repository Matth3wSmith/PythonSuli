#Mértékegység átváltó
#Kovács Máté 2023. 10. 06
#Projektfeladat

tipusok = ["Hosszúság", "Terület", "Térfogat", "Tömeg", "Űrmérték", "Űrmérték + térfogat"];

print("#"*35);
#for elem in tipusok:
#    print(elem)

for i,elem in enumerate(tipusok):
    print("\t",str(i+1)+":", elem);

print("\t0: Kilépés");
print("#"*35);

tipusId="";

while tipusId=="" or tipusId not in range(len(tipusok)+1):
    try:
        tipusId = int(input("Válassz!"));
    except:
        print("Nem jó! Válassz a listából!")

