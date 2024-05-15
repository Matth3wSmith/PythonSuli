dobasok=[3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]

mezo=0
letraMezo=0
print("2. feladat")
for dobas in dobasok:
    mezo+=dobas
    if mezo%10==0:
        letraMezo+=1
        mezo-=3
    print(mezo, end=" ")
        
print("\n3. feladat")
print("A játék során {} alkalommal lépett létrára.".format(letraMezo))

print("4. feladat")
if mezo>=45:
    print("A játékot bejefezte.")
else:
    print("A játékot abbahagyta.")