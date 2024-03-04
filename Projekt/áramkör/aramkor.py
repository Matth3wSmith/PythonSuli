#Áramkör
#Start: 2024.02.16
#Kovács Máté

from tkinter import *
import random
import math
class Jel:
	x = 0
	y = 0
	meret = 100
	szin="black"

	def __init__(self,x,y,meret,canvas):
		self.x=x
		self.y=y
		self.meret=meret
		self.r=self.meret*0.06

		#Bekötési pont
		self.bkp=[[self.x, self.y+self.meret*0.5],[self.x+self.meret, self.y+self.meret*0.5]]

		self.canvas=canvas
		self.rajz()

	def vezetek(self,masik,sajatBKP=1,masikBKP=0):
		#első után a másik, közelebbi pontok
		#	*****
		#	*   *--
		#	***** |
		#         |     *****
		#          -----*   *
		#               *****
		if (sajatBKP==1 and masikBKP==0) and self.bkp[sajatBKP][0] < masik.bkp[masikBKP][0]:
			vonalak=[
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2,	self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2,	masik.bkp[masikBKP][1],
					masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
				],
			]
			self.szin="red"
		#első alatt/felett a másik, közelebbi pontok
		#	*****
		#	*   *--
		#	*****  |
		#      ----
		#     | *****
		#      -*   *
		#       *****
		elif (sajatBKP==1 and masikBKP==0) and self.x < masik.x < self.x+self.meret:
			vonalak=[
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					self.bkp[sajatBKP][0]+self.meret*0.2, self.bkp[sajatBKP][1],
					self.bkp[sajatBKP][0]+self.meret*0.2, (self.bkp[sajatBKP][1]+masik.y)/2,
					masik.bkp[masikBKP][0]-self.meret*0.2, (self.bkp[sajatBKP][1]+masik.y)/2,
					masik.bkp[masikBKP][0]-self.meret*0.2, masik.bkp[masikBKP][1],
					masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
				],
			]
			self.szin="green"
		#első alatt/felett a másik, távolabbi pontok
		#	*****
		#	*   *-----
		#	*****     |
		#             |
		#       ***** |
		#       *   *-
		#       *****
		elif (sajatBKP==1 and masikBKP==1) and self.x < masik.x < self.x+self.meret:
			vonalak=[
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					masik.bkp[masikBKP][0]+self.meret*0.2, self.bkp[sajatBKP][1],
					masik.bkp[masikBKP][0]+self.meret*0.2, masik.bkp[sajatBKP][1],
					masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
				],
			]
			self.szin="blue"
		#első után a másik, távolabbi pontok
		#	*****
		#	*   *-------------
		#	*****             |
		#               ***** |
		#               *   *-
		#               *****
		elif (sajatBKP==1 and masikBKP==1) and self.bkp[sajatBKP][0] < masik.bkp[masikBKP][0]:
			vonalak=[
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.x)/2,					self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.x)/2,					masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2,							masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2,							masik.bkp[masikBKP][1],
					masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
				],
			]
			self.szin="yellow"
		#minden más esetben ferde vonallal összekötés
		else:
			vonalak=[
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					masik.bkp[masikBKP][0], masik.bkp[masikBKP][1],
				],
			]
			self.szin="black"
		for egyvonal in vonalak:
			self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin)

	def rajz(self, vonalak=[],korok=[]):
		self.canvas.create_rectangle(self.x, self.y, self.x+self.meret, self.y+self.meret, fill="grey")

		for egyvonal in vonalak:
			self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin)
		for egykor in korok:
			self.canvas.create_oval(egykor, outline=self.szin, width=self.meret*0.03)


class Elem(Jel):
	def rajz(self):
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.45, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.45, self.y+self.meret*0.2,
				self.x+self.meret*0.45, self.y+self.meret*0.8,
			],
			[
				self.x+self.meret*0.55, self.y+self.meret*0.4,
				self.x+self.meret*0.55, self.y+self.meret*0.6,
			],
			[
				self.x+self.meret*0.55, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		Jel.rajz(self,vonalak)

class Kapcsolo(Jel):
	def rajz(self):
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.333-self.r, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.333+self.r, self.y+self.meret*0.5,
				self.x+self.meret*0.666-self.r, self.y+self.meret*0.3,
			],
			[
				self.x+self.meret*0.666+self.r, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		korok=[
			[
				self.x+self.meret*0.333-self.r, self.y+self.meret*0.5-self.r,
				self.x+self.meret*0.333+self.r, self.y+self.meret*0.5+self.r
			],
			[
				self.x+self.meret*0.666-self.r, self.y+self.meret*0.5-self.r,
				self.x+self.meret*0.666+self.r, self.y+self.meret*0.5+self.r
			]
		]
		Jel.rajz(self,vonalak,korok)

class Lampa(Jel):
	
	def rajz(self):
		self.r=self.meret*0.2
		dx=self.r/math.sqrt(2)
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.5-self.r, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.5-dx, self.y+self.meret*0.5-dx,
				self.x+self.meret*0.5+dx, self.y+self.meret*0.5+dx,
			],
			[
				self.x+self.meret*0.5-dx, self.y+self.meret*0.5+dx,
				self.x+self.meret*0.5+dx, self.y+self.meret*0.5-dx,
			],
			[
				self.x+self.meret*0.5+self.r, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		korok=[
			[
				self.x+self.meret*0.5-self.r, self.y+self.meret*0.5-self.r,
				self.x+self.meret*0.5+self.r, self.y+self.meret*0.5+self.r
			]
		]
		Jel.rajz(self,vonalak,korok)

class Ellenallas(Jel):
	
	def rajz(self):
		
		vonalak=[
			[
				self.x, self.y+self.meret*0.5,
				self.x+self.meret*0.25, self.y+self.meret*0.5,
			],
			[
				self.x+self.meret*0.25, self.y+self.meret*0.4,
				self.x+self.meret*0.25, self.y+self.meret*0.6,
				self.x+self.meret*0.75, self.y+self.meret*0.6,
				self.x+self.meret*0.75, self.y+self.meret*0.4,
				self.x+self.meret*0.25, self.y+self.meret*0.4,
			],
			[
				self.x+self.meret*0.75, self.y+self.meret*0.5,
				self.x+self.meret, self.y+self.meret*0.5,
			]
		]
		
		Jel.rajz(self,vonalak)

#ablak létrehozása
win=Tk()

jatekHatter="lightgray"
jatekSpeed=10

#ablak mérete
win.geometry("1000x600")

win.title("Áramkör")

#canvas létrehozás
canvas=Canvas(win, width=600, height=600, bg=jatekHatter)

#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

lampa1=Lampa(220,220,100,canvas)

kapcs=[]
kapcs.append(Kapcsolo(450,350,100,canvas))
kapcs.append(Kapcsolo(250,350,100,canvas))
kapcs.append(Kapcsolo(450,50,100,canvas))
kapcs.append(Kapcsolo(250,50,100,canvas))
kapcs.append(Kapcsolo(50,50,100,canvas))
kapcs.append(Kapcsolo(50,350,100,canvas))
#ellenallas1=Ellenallas(0,150,100,canvas)

for egyElem in kapcs:
	for masikBKP in [0,1]:
		for sajatBKP in [0,1]:
			lampa1.vezetek(egyElem,sajatBKP=sajatBKP,masikBKP=masikBKP)

win.mainloop()