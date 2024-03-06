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

		if sajatBKP==1 and masikBKP==0 and self.bkp[sajatBKP][0] < masik.bkp[masikBKP][0]:
			vonalak=[
			
				[
					self.bkp[sajatBKP][0],self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2,self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.bkp[masikBKP][0])/2,masik.bkp[masikBKP][1],
					masik.bkp[masikBKP][0],masik.bkp[masikBKP][1]
				]
			]
		elif (sajatBKP==1 and masikBKP==1) and self.bkp[sajatBKP][0] < masik.bkp[masikBKP][0]:
			vonalak=[
			
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.x)/2, self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.x)/2, masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2, masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2, masik.bkp[masikBKP][1],
					masik.x+masik.meret,masik.bkp[masikBKP][1]
				]
			]
		elif (sajatBKP==1 and masikBKP==1) and self.x<masik.x<self.x+self.meret:
			vonalak=[
				[
					self.bkp[sajatBKP][0], self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.x)/2, self.bkp[sajatBKP][1],
					(self.bkp[sajatBKP][0]+masik.x)/2, masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2, masik.y+masik.meret*1.2,
					masik.x+masik.meret*1.2, masik.bkp[masikBKP][1],
					masik.x+masik.meret,masik.bkp[masikBKP][1]
				]
			]
		else:
			vonalak=[
				[
					self.bkp[sajatBKP][0],self.bkp[sajatBKP][1],
					masik.bkp[masikBKP][0],masik.bkp[masikBKP][1]
				]
			]
		
			
		for egyvonal in vonalak:
			self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin)

	def rajz(self, vonalak=[],korok=[]):
		
		self.canvas.create_rectangle(self.x, self.y, self.x+self.meret, self.y+self.meret, fill="grey", tags="A")

		for egyvonal in vonalak:
			self.canvas.create_line(egyvonal, width=self.meret*0.03, fill=self.szin, tags="A")
		for egykor in korok:
			self.canvas.create_oval(egykor, outline=self.szin, width=self.meret*0.03, tags="A")


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
canvas.pack(side=LEFT)

#Választó felület
frame1=Frame()
lampa=Button(master=frame1,text="Lámpa")
kapcsolo=Button(master=frame1,text="Kapcsoló")
elem=Button(master=frame1,text="Elem")
ellenallas=Button(master=frame1,text="Ellenállás")

frame1.pack(side=RIGHT)
lampa.pack(pady=10,padx=20)
kapcsolo.pack(pady=10,padx=20)
elem.pack(pady=10,padx=20)
ellenallas.pack(pady=10)


alkatreszek=[]
def lampaSpawn(event):
	print(event)
	alkatreszek.append(Lampa(0,0,100,canvas))
def kapcsoloSpawn(event):
	print(event)
	alkatreszek.append(Kapcsolo(0,0,100,canvas))
def elemSpawn(event):
	print(event)
	alkatreszek.append(Elem(0,0,100,canvas))
def ellenallasSpawn(event):
	print(event)
	alkatreszek.append(Ellenallas(0,0,100,canvas))



def motion(event,kivElem=0,objX=0,objY=0):
	print(event)
	x, y = event.x, event.y
	print('{}, {}'.format(x, y))
	
	for alkatresz in alkatreszek:
		#Megegyezik-e a kattintás koordinátái és az alkatrész koordinátái
		if alkatresz.x<=event.x<alkatresz.x+alkatresz.meret and alkatresz.y<event.y<alkatresz.y+alkatresz.meret:
			print("Felismerve")
			alkatresz.x+=1
			alkatresz.y+=1
			tavX=event.x-objX
			tavY=event.y-objY
			B=canvas.gettags("A")
			print(B)
			canvas.move(B,1,1)
			
			#canvas.bind("<ButtonRelease-1>",kiiras)

def mozgatas(event):
	#Létrehozott alkatrészek vizsgálata
	kivalasztottElem=0
	objX=0
	objY=0
	for alkatresz in alkatreszek:
		#Megegyezik-e a kattintás koordinátái és az alkatrész koordinátái
		if alkatresz.x<=event.x<alkatresz.x+alkatresz.meret and alkatresz.y<event.y<alkatresz.y+alkatresz.meret:
			print("Felismerve")
			kivalasztottElem=alkatresz
			objX=alkatresz.x
			objY=alkatresz.y
			#win.bind('<Motion>', motion)
			canvas.bind("<ButtonRelease-1>",motion)
	return objX,objY,kivalasztottElem

			

	#tavX=event.x-objX
	#tavY=event.y-objY

def kiiras(event):
	print(event)
canvas.bind("<Button>",mozgatas)

lampa.bind("<Button-1>",lampaSpawn)

kapcsolo.bind("<Button-1>",kapcsoloSpawn)

elem.bind("<Button-1>",elemSpawn)

ellenallas.bind("<Button-1>",ellenallasSpawn)
		  
#elem1=Elem(100,100,100,canvas)
#elem1.rajz()
#kapcsolo1=Kapcsolo(200,100,100,canvas)

#lampa1=Lampa(400,50,100,canvas)

ellenallas1=Ellenallas(500,150,100,canvas)

#lampa1.vezetek(ellenallas1)
#lampa1.vezetek(ellenallas1,masikBKP=1)
win.mainloop()