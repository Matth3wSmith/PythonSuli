from sys import stdin,stdout

evek={
    "zold":[4,5],
    "piros":[6,7],
    "sarga":[8,9],
    "feher":[0,1],
    "fekete":[2,3]
}

def main():
    ev=input()
    for evSzin in evek:
        if int(ev[-1]) in evek[evSzin]:
            stdout.write(evSzin)
            
main()