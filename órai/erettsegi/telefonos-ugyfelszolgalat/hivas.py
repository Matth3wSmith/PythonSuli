adatok=[]
f=open("hivas.txt")

for sor in f:
    temp=[]
    tempSor=sor.split(" ")
    for i in range(len(tempSor)):
        temp.append(int(tempSor[i]))
    adatok.append(temp)
    temp.append(temp[3]*60*60+temp[4]*60+temp[5]-temp[0]*60*60+temp[1]*60+temp[2])
f.close()

print(adatok)