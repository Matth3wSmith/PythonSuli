
f=open("dolgozok.txt","r")
f.read()
adatok=[]
for sor in f:
    print(sor.strip(";"))


print(adatok)