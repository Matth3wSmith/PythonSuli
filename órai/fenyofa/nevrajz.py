import transzformaciok
from tkinter import *

#ablak létrehozása
win=Tk()

#ablak mérete
win.geometry("1000x1000")

#canvas létrehozás
canvas=Canvas(win, width=600, height=300)
canvas.configure(bg="lightgray")
#canvas akkora amekkora az ablak
canvas.pack(fill = BOTH, expand = 1)

fenyo2=[200,0,
        0,100,
        150,100,
        0,200,
        150,200,
        0,300,
        150,300,
        150,400,
        250,400,
        250,300,
        400,300,
        250,200,
        400,200,
        250,100,
        400,100,
        200,0]

fenyo2Masolat=transzformaciok.eltolas(fenyo2,100,100)
#canvas.create_line(fenyo2Masolat,width=5,fill="green")

mate=[[0,0,
   0,100,
   100,100,
   100,500,
   0,500,
   0,600,
   300,600,
   300,500,
   200,500,
   200,100,
   400,300,
   600,100,
   600,500,
   500,500,
   500,600,
   800,600,
   800,500,
   700,500,
   700,100,
   800,100,
   800,0,
   500,0,
   400,200,
   300,0,
   0,0],

   [0,0,
   0,100,
   100,100,
   100,500,
   0,500,
   0,600,
   300,600,
   300,500,
   200,500,
   200,100,
   400,300,
   600,100,
   600,500,
   500,500,
   500,600,
   800,600,
   800,500,
   700,500,
   700,100,
   800,100,
   800,0,
   500,0,
   400,200,
   300,0,
   0,0]]

mate2=[]
for e in mate:
        e=transzformaciok.nagyit(e,0.4)
        e=transzformaciok.eltolas(e, 100, 100)
        e=transzformaciok.forgat(e, 45)
        mate2.append(e)
print(mate2)
for e in mate2:
        canvas.create_line(e,width=5,fill="black")
win.mainloop()