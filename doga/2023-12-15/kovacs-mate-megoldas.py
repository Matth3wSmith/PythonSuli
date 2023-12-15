adatok=[]
f=open("helsinki.txt")
for sor in f:
    temp=sor.strip().split()
    for i in range(4,len(temp)):
        temp[i]=int(temp[i])
        adatok.append(temp)
f.close()

print(adatok)