class Emlos():
	lab=4
	def __init__(self):
		self.suly=0
		
	def beszel(self):
		pass


class Macska(Emlos):
	def __init__(self, nev):
		super().__init__()
		self.nev=nev
		self.suly=1

	def beszel(self):
		print("Miauu")


emlos1=Emlos()
emlos1.beszel()

macska1=Macska("Adolf")
macska1.beszel()
print(macska1.nev)

#MÁSIK MACSKA KÉSZÍTÉSE (1<) egy két függvény meg tulajdonság