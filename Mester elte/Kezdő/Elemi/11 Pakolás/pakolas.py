from sys import stdin,stdout

def main():
    ladakSzama=int(stdin.readline())
    ladak=list(map(int,stdin.readline().split()))
    maxlada=ladakSzama
    pakolas=0
    ladaban=maxlada
    while len(ladak)!=0:
        i=ladak.index(maxlada)
        if i+1<len(ladak) and i-1>=0:
            #Ha baloldalt van nagyobb
            if ladak[i-1]>ladak[i+1] and ladak[i-1]<ladaban:
                print("baloldal",ladak[i-1], ladak[i+1])
                ladaban=ladak[i-1]
                ladak.remove(ladaban)
                print(ladak)
            #Ha jobb oldalt nagyobb
            elif ladak[i+1]<ladaban:
                print("jobboldal",ladak[i-1], ladak[i+1])
                ladaban=ladak[i+1]
                ladak.remove(ladaban)
                print(ladak)
            
            else:
                ladak.remove(maxlada)
                maxlada=max(ladak)
                ladaban=maxlada
                pakolas+=1
                print(ladak)


        #csak balra van lada
        elif i+1>=len(ladak) and i-1>=0:
            if ladaban>ladak[i-1]:
                print("baloldal",ladak[i-1])
                ladaban=ladak[i-1]
                ladak.remove(ladaban)
                print(ladak)

            else:
                ladak.remove(maxlada)
                maxlada=max(ladak)
                ladaban=maxlada
                pakolas+=1
                print(ladak)

        #csak jobbra van lada
        elif i-1<0 and i+1<len(ladak):
            if ladaban>ladak[i+1]:
                print("jobboldal", ladak[i+1])
                ladaban=ladak[i+1]
                ladak.remove(ladaban)
                print(ladak)
            else:
                ladak.remove(maxlada)
                maxlada=max(ladak)
                ladaban=maxlada
                pakolas+=1
                print(ladak)

        else:
                ladak.remove(maxlada)
                pakolas+=1
    stdout.write(str(pakolas))
        




    
main()