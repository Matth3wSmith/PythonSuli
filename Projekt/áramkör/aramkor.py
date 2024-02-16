#Áramkör
#Start: 2024.02.16
#Kovács Máté

from tkinter import *
import random

class elem:
	x = 0
	y = 0
	meret = 100

	def __init__(self,x,y,meret,canvas):
		self.x=x
		self.y=y
		self.meret=meret
		self.canvas=canvas


	def rajz(self):
		self.canvas.create_rectangle(self.x, self.y, self.x+self.meret, self.y+self.meret, fill="blue")

		vonal=[
			[
				self.x,self.y+self.meret*0.5,
				self.x+self.meret*0.45, self.y+self.meret*0.5,
			]
		]
		for egyvonal in vonal:
			self.canvas.create_line()
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

elem1=elem(200,200,100,canvas)
elem1.rajz()

win.mainloop()