f=open("veetel.txt","r")
adatok=[]
for sor in f:
    adatok.append(sor.strip().split())

print(adatok)
f.close()

