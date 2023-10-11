lista = []
beker = "."

while beker!="":
    beker = input("Adj meg valamit!")
    if beker!="":
        lista.append(beker)

print(lista)
utolso = lista[-3:]
utolso.sort()

lista.sort()
print(lista)

for e in lista:
    print(e)

for e in lista[-3:]:
    print(e)

print(utolso)
