from sys import stdin, stdout,argv
import time
def main():
	return argv[1]


#print(argv[1])
adatok=[]
adatKell=[]
adatHossz=0
with open(main(),"r") as f:
	#napDb=list(map(int, f.readline().split()))[1]
	next(f)
	napDb=1000

	for sor in f:
		#print(sor)
			adatHossz+=1
			adatok.append(list(map(int, sor.split())))
			atlag=sum(adatok[-1])/napDb
			if(max(adatok[-1])-atlag>atlag-min(adatok[-1])):
				adatKell.append(str(adatHossz))
	f.close()
	

stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))
