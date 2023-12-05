f=open("bela.txt","w")

#f.write("12")
for i in range(100):
    f.write(str(i)+"\n")

f.close()

#open("bela2.txt","w").write("\n".join(range(100)))

open("béla2.txt","w").write("\n".join([str(i) for i in range(100)]))


f=open("bela.txt","r")

lista=[]
for egySor in f:
    lista.append(egySor.strip())

f.close()

print(lista)

f=open("bela.txt","r")
lista=[egySor.strip() for egySor in f.readlines()]

f.close()
print(lista)


f=open("bela.txt","r")
lista2 =map(lambda x: x.strip(), f.readlines())
print(list(lista2))
f.close()

lista=[]
f=open("bela.txt","r")
lista = f.read().strip().split("\n")
print(lista)
f.close()
