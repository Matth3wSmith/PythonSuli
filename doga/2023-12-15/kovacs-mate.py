adatok=[]
f=open("helsinki.txt")

for sor in f:
    adatok.append(sor.split())
f.close()

for elem in adatok:
    elem[0]=int(elem[0])
    elem[1]=int(elem[1])

print(adatok)