class Uzenet():
	uzenetek=[]
	napok=[]
	sorszamok=[]
	napiFelv={}
	

	def __init__(self,nap,sorszam,szoveg):
		self.sorszam=sorszam

		if sorszam not in self.sorszamok:
			self.sorszamok.append(sorszam)

		self.nap=nap
		if int(nap) not in self.napok:
			self.napok.append(int(nap))
			self.napok.sort()
		
		self.szoveg=szoveg
		self.uzenetek.append(self)
	
	#2. feladat
	def rogzites(self):
		"""for amator in Uzenet.uzenetek:
			if amator.nap == min(self.napok):
				legkisebb=amator.sorszam"""
	#3. feladat
	def farkas(self):
		if "farkas" in self.szoveg:
			return self.nap,self.sorszam
		else:
			return False

	#4. feladat
	def felvetelStat(self):
		self.napiFelv[int(self.nap)]+=1

		