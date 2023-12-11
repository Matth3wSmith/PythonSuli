adatok=[]

f=open("cb.txt")

for sor in f:
    adatok.append(sor)

f.close()

print(adatok)