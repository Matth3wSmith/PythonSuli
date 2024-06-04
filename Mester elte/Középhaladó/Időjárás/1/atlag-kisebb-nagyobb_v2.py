from sys import stdin, stdout,argv
import time
def main():
	#print(argv[1])
	adatok=[]
	adatKell=[]
	adatHossz=0
	with open(argv[1],"r") as f:
		napDb=list(map(int, f.readline().split()))[1]

		for sor in f:
			#print(sor)
				adatHossz+=1
				adatok.append(list(map(int, sor.split())))
				atlag=sum(adatok[-1])/napDb
				if(max(adatok[-1])-atlag>atlag-min(adatok[-1])):
					adatKell.append(str(adatHossz))
		f.close()
		

	stdout.write(str(len(adatKell)) + " " + " ".join(adatKell))

kezdoIdo=time.time()
main()
vegIdo=time.time()
print("\n",vegIdo-kezdoIdo)
