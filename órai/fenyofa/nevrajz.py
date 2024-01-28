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

   ]
a=[[0,400,
   180,400,
   250,250,
   350,250,
   420,400,
   600,400,
   400,0,
   200,0,
   0,400],

   [250,200,
    340,200,
    370,50,
    280,50,
    250,200]]

t=[0,0,
   0,50,
   175,50,
   175,300,
   225,300,
   225,50,
   400,50,
   400,0,
   0,0]

e=[0,0,
   0,500,
   400,500,
   400,400,
   100,400,
   100,300,
   400,300,
   400,200,
   100,200,
   100,100,
   400,100,
   400,0,
   0,0
   ]

hatter="#ffffff"
betuszinek=["red", hatter, "blue"]

mate2=[]                                                                                                                                                                                                        
#for e in mate:
        #e=transzformaciok.nagyit(e,0.4)
        #e=transzformaciok.eltolas(e, 100, 100)
        #e=transzformaciok.forgat(e, 45)
        #mate2.append(e)

#mate2=transzformaciok.masol(mate)
#mate2=transzformaciok.nagyit(mate2,0.4)
#mate2=transzformaciok.eltolas(mate2,100,100)

mate=transzformaciok.nagyit(mate,0.4)
mate=transzformaciok.eltolas(mate,100,100)
canvas.create_line(mate,width=5,fill="black")

a=transzformaciok.nagyit(a,0.6)
a=transzformaciok.eltolas(a,450,100)
canvas.create_line(a,width=5,fill="black")

t=transzformaciok.nagyit(t,0.8)
t=transzformaciok.eltolas(t,750,100)
canvas.create_line(t,width=5,fill="black")

e=transzformaciok.nagyit(e,0.5)
e=transzformaciok.eltolas(e,1100,100)
canvas.create_line(e,width=5,fill="black")

#while True:
        #canvas.delete("all")
        #ate2=transzformaciok.forgat(mate2,0.009)
        #for i,e in enumerate(mate2):
                #canvas.create_polygon(e,width=betuszinek[i],fill="blue")
        #win.update_idletasks()
        #win.update()
win.mainloop()