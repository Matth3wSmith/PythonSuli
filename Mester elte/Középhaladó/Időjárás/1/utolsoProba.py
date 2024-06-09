from sys import stdin, stdout,argv

def main2():
	adatKell=[]
	adatHossz=0
	napDb=list(map(int, input().split()))[1]

	for sor in stdin:
		adatHossz+=1
		sor=list(map(int, sor.split()))
		atlag=sum(sor)/napDb
		if(max(sor)-atlag>atlag-min(sor)):
			adatKell.append(adatHossz)
	
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))


def main3():
	adatKell=[]
	adatHossz=0
	elsoSor=input()
	varosDb=list(map(int, elsoSor.split()))[0]
	napDb=list(map(int, elsoSor.split()))[1]

	for adatHossz in range(1,varosDb+1):
		sor=list(map(int, input().split()))
		atlag=sum(sor)/napDb
		if(max(sor)-atlag>atlag-min(sor)):
			adatKell.append(adatHossz)
	
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))



def main4():
	adatKell=[]
	adatHossz=0
	elsoSor=input()
	varosDb=list(map(int, elsoSor.split()))[0]
	napDb=list(map(int, elsoSor.split()))[1]

	
	while True:
		try:
			sor=list(map(int, input().split()))
		except:
			break
		atlag=sum(sor)/napDb
		if(max(sor)-atlag>atlag-min(sor)):
			adatKell.append(adatHossz)
	
	stdout.write(str(len(adatKell)) + " " + " ".join(list(map(str, adatKell))))


main2()