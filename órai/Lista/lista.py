lista = ["a", "b", "z", "h", "c", "i", "o"]

print(lista)
print("#"*30)

#Kiiratás for-ral
for elem in lista:
    print(elem)

print("#"*30)

for i in range(len(lista)):
    print(lista[i])

print("#"*30)

#Első három elem
for elem in lista[:3]:
    print(elem)

print("#"*30)

#3. elemtől a végéig
for elem in lista[3:]:
    print(elem)

print("#"*30)

#Utolsó 2 elem
for elem in lista[-2:]:
    print(elem)

print("#"*30)

#Fordított kiiratás
for elem in lista[::-1]:
    print(elem)

lista2 = lista[1:-1]
print(lista2)

