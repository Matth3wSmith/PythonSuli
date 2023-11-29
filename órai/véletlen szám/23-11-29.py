import random

osztaly=[]
osztalyAtlagok=[]
for i in range(12):
	tanulo=[]
	for a in range(random.randrange(8,13)):
		tanulo.append(random.randrange(1,6))
	osztaly.append(tanulo)
	#átlag összeadás
	osszeg=0
	for b,elem in enumerate(tanulo):
		osszeg+=elem
	atlag=osszeg/len(tanulo)
	osztalyAtlagok.append(atlag)


txt="Osztályátlagok {:.2f}"
for k in osztalyAtlagok:
	print(txt.format(k))

#osztaly=[[tanulo.append(random.randrange(1,6)) for a in range(random.randrange(8,13)), tanulo=[]] for i in range(12)]
